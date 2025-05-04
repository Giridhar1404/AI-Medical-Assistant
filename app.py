import google.generativeai as genai

genai.configure(api_key="your-actual-api-key")
print(genai.list_models())  # This will list supported models
