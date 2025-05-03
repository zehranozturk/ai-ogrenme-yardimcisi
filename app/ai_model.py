import os
import requests
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

def explain_with_model(term: str) -> str:
    api_url = "https://api-inference.huggingface.co/models/declare-lab/flan-alpaca-base"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    prompt = f"Explain the AI term '{term}' in simple English."
    data = {"inputs": prompt}

    try:
        response = requests.post(api_url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            return result[0].get("generated_text", "Açıklama üretilemedi.")
        else:
            return f"Model çağrısı başarısız oldu. Kod: {response.status_code}"
    except Exception as e:
        return f"Hata oluştu: {str(e)}"