import os
import requests
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

def explain_with_model(term: str, language: str = "en") -> str:
    if language == "tr":
        api_url = "https://api-inference.huggingface.co/models/ahmetfurkandemr/turkish-ai-term-explainer"
        prompt = f"Yapay zeka terimini açıkla: {term}"
    else:
        api_url = "https://api-inference.huggingface.co/models/declare-lab/flan-alpaca-base"
        prompt = f"Explain the AI term '{term}' in simple English."

    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    data = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.7,
            "top_p": 0.9,
            "do_sample": True
        }
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and "generated_text" in result[0]:
                return result[0]["generated_text"]
            else:
                return "Model çalıştı ama açıklama alınamadı."
        else:
            return f"Model çağrısı başarısız oldu. Kod: {response.status_code}"
    except Exception as e:
        return f"Hata oluştu: {str(e)}"