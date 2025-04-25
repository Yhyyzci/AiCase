FROM python:3.10

# Uygulama dizinine geç
WORKDIR /app

# Dosyaları kopyala
COPY . .


RUN pip install --no-cache-dir flask openai==0.28

# Portunu aç
EXPOSE 5001

# Uygulamayı başlat
CMD ["python3", "app.py"]
