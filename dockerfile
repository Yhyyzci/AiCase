FROM python:3.10

WORKDIR /app
COPY . .
RUN pip install flask openai
EXPOSE 5000
CMD ["python", "app.py"]
