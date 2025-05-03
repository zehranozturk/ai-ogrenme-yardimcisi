# Yapay Zeka Kavram Açıklayıcı 🌐🤖

Bu proje, yapay zeka (AI) ile ilgili terimlerin basit bir dille açıklanmasını sağlayan web tabanlı bir yardımcı araçtır. Kullanıcı, istediği kavramı girerek Hugging Face API üzerinden çalışan bir modelden İngilizce veya Türkçe açıklama alabilir.

## 🚀 Özellikler

- ✅ FastAPI destekli hızlı backend  
- ✅ HTML/CSS ile responsive kullanıcı arayüzü  
- ✅ Hugging Face üzerinden çalışan Flan-T5 modeli entegrasyonu  
- ✅ Türkçe ve İngilizce dil seçenekleri  
- ✅ Gerçek zamanlı açıklama üretimi  

## ⚙️ Kurulum

```bash
git clone https://github.com/zehranozturk/ai-ogrenme-yardimcisi.git
cd ai-ogrenme-yardimcisi
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
🔗 Tarayıcıdan aç: http://127.0.0.1:8000
