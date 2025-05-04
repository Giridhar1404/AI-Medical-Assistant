from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise RuntimeError("❌ OPENROUTER_API_KEY is missing! Check your .env file.")

# FastAPI app setup
app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust based on frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body models
class SymptomInput(BaseModel):
    symptoms: str

class DrugInput(BaseModel):
    drug_name: str

class DiseaseInput(BaseModel):
    disease_name: str

# OpenRouter API function
def ai_generate(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "gpt-4-turbo",  # Use Claude-3 for medical accuracy if needed
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500,  # Increase for more detailed responses
        "temperature": 0.7  # Balanced creativity
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response_json = response.json()
        return response_json["choices"][0]["message"]["content"].strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API Endpoints
@app.post("/diagnose")
def diagnose_disease(input_data: SymptomInput):
    """Takes symptoms as input and returns possible diseases with summarized explanations."""
    prompt = f"""
    Given the symptoms: {input_data.symptoms}, provide a **detailed medical diagnosis**.
    Include:
    - Possible diseases
    - Causes
    - Symptoms explanation
    - Severity levels
    - Treatment options
    - Prevention tips
    Format it clearly in 20 lines.
    """
    response_text = ai_generate(prompt)
    return {"possible_diseases": response_text}

@app.post("/drug-info")
def get_drug_info(input_data: DrugInput):
    """Fetches drug information, including usage, dosage, and alternatives in a summarized format."""
    prompt = f"""
    Provide detailed information about the drug **{input_data.drug_name}**:
    - Purpose and medical use
    - Dosage recommendations
    - Side effects
    - Alternative medications
    - Precautions and warnings
    - Drug interactions
    Format it clearly in 20 lines.
    """
    response_text = ai_generate(prompt)
    return {"drug_info": response_text}

@app.post("/disease-info")
def get_disease_info(input_data: DiseaseInput):
    """Fetches detailed disease information with a structured and summarized format."""
    prompt = f"""
    Provide a **comprehensive guide** on **{input_data.disease_name}** including:
    - Overview
    - Symptoms & Stages
    - Causes
    - Diagnosis methods
    - Medications
    - Treatment options
    - Lifestyle & diet recommendations
    - Prevention measures
    Format it clearly in 20 lines.
    """
    response_text = ai_generate(prompt)
    return {"disease_info": response_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
