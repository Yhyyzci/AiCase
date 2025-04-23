FROM python:3.10

# Uygulama dizinine geç
WORKDIR /app

# Dosyaları kopyala
COPY . .

# Gereken paketleri yükle
RUN pip install --no-cache-dir flask openai

# Uygulama portunu aç
EXPOSE 5000

# Uygulamayı başlat
CMD ["python3", "app.py"]
