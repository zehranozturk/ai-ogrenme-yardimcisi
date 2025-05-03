# Yapay Zeka Kavram Açıklayıcı

## Amaç
Yeni nesil öğrenme konseptine uygun olarak, kullanıcıdan alınan bir kavramı Hugging Face üzerindeki `flan-t5-small` modeli ile açıklayan basit bir FastAPI uygulamasıdır.

## Kurulum
1. Sanal ortam oluştur:
    python3 -m venv venv
    source venv/bin/activate

2. Gerekli paketleri yükle:
    pip install -r requirements.txt

3. .env dosyası oluştur ve içine API tokenını ekle:
    HF_TOKEN=hf_...

4. Uygulamayı başlat:
    uvicorn app.main:app --reload

## Kullanım
Tarayıcıdan `http://127.0.0.1:8000` adresine gidin ve bir kavram girin.
