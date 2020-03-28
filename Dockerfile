FROM python:3.7-slim
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
