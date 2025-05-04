# 🩺 AI-Based Healthcare Assistance System

This project is an **AI-powered web application** that provides instant medical insights such as disease diagnosis, drug information, and disease-related data using natural language input. It integrates a **React.js** frontend with a **FastAPI** backend, and utilizes the **OpenRouter API** for AI-generated medical responses.

## 🌐 Features

- 🔍 **Symptom-Based Disease Diagnosis**  
  Input symptoms (e.g., *cold, cough, fever*) and receive possible medical conditions with causes, severity levels, and treatment suggestions.

- 💊 **Drug Information Lookup**  
  Search any drug (e.g., *Paracetamol, Metformin*) to get its use, dosage, side effects, precautions, and alternatives.

- 🧬 **Disease Insights**  
  Enter a disease name (e.g., *Diabetes*) to obtain a comprehensive overview: symptoms, causes, medications, lifestyle advice, and prevention.

---

## 🛠️ Technologies Used

| Component      | Technology       |
|----------------|------------------|
| Frontend       | React.js         |
| Backend        | FastAPI          |
| AI Model       | OpenRouter API (GPT-4 Turbo or Claude-3) |
| Styling        | CSS              |
| Deployment     | Localhost / Future: Render / Vercel / Railway |

---

## 🚀 Installation & Setup

### Prerequisites
- Node.js
- Python 3.8+
- Virtualenv (optional but recommended)

### 1. Backend (FastAPI)

```bash
# Clone the repository
git clone https://github.com/your-username/healthcare-ai-assistant.git
cd healthcare-ai-assistant/backend

# Create virtual environment and activate it
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up .env
echo "OPENROUTER_API_KEY=your_api_key_here" > .env

# Run the server
uvicorn main:app --reload

### 2. Frontend (React)
bash
Copy
Edit
cd ../frontend
npm install
npm start
