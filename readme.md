# 🧠 AI Code Generator

Bu proje, OpenAI API'sini kullanarak doğal dil girdilerinden Python kodu üreten basit bir web uygulamasıdır. Flask ile geliştirilmiş ve Docker ile konteynerleştirilmiştir.

---

## 🚀 Özellikler

- Kullanıcıdan gelen istemlere göre GPT-3.5 modelinden Python kodu üretir.
- Gelen yanıtları başlık ve kod olarak ayırır.
- Flask web arayüzü sunar.
- Docker ortamında kolayca çalıştırılabilir.

---

## ▶️ Local Ortamda Terminal Üzerinden Çalıştırma

Projeyi localde çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1.Depoyu klonlayın:

git clone https://github.com/Yhyyzci/AiCase.git

2.Sanal ortam oluşturun (opsiyonel ama önerilir):

python -m venv venv


3.Sanal ortamı etkinleştirin:


macOS/Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate

4.Gerekli paketleri yükleyin:

pip install flask openai

5.app.py dosyasını açın ve kendi OpenAI API anahtarınızı şu satıra yazın:

openai.api_key = "YOUR_API_KEY"


6.Uygulamayı başlatın:

python app.py

7.Tarayıcınızdan şu adrese gidin:

http://localhost:5001

🐳 Docker ile Çalıştırma

1.Docker imajını oluşturun:
docker build -t ai-code-generator .

2.Konteyneri çalıştırın (API anahtarınızı burada verin):
docker run -p 5001:5001 -e OPENAI_API_KEY=your-api-key-here ai-code-generator


🌐 Kullanım
Web arayüzüne gidin (http://localhost:5000)

Girdi kutusuna bir istem yazın (örnek: "iki sayıyı toplayan bir Python fonksiyonu yaz").

"Gönder" tuşuna basın.

Başlık ve üretilen Python kodunu görüntüleyin.
