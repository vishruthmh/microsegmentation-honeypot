FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
VOLUME ["/logs"]
CMD ["python", "honeypot.py", "--host=0.0.0.0", "--port=8080"]
