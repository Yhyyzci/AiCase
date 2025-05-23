from flask import Flask, request, render_template_string
import openai
import re

app = Flask(__name__)

# OpenAI API anahtarını buraya yaz
openai.api_key = "Kendi Key'in buraya yaz" 

# AI'dan gelen yanıtı işleyen fonksiyon
def parse_response(reply):
    code_match = re.search(r"```python(.*?)```", reply, re.DOTALL)
    title_match = re.search(r"Baslik:\s*(.*)", reply)
    return {
        "code": code_match.group(1).strip() if code_match else "",
        "title": title_match.group(1).strip() if title_match else ""
    }

# Ana sayfa
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen bir Python kod üretici asistansin"},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response['choices'][0]['message']['content']
        parsed = parse_response(reply)
        result = parsed

    return render_template_string("""
        <form method="post">
            <textarea name="prompt" rows="5" cols="50" placeholder="İstemi buraya yaz..."></textarea><br>
            <input type="submit" value="Gönder">
        </form>
        {% if result %}
            <h2>{{ result.title }}</h2>
            <pre>{{ result.code }}</pre>
        {% endif %}
    """, result=result)

# Uygulamayı başlat (Docker çalışması için host ekledik)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
