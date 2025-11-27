FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8081
EXPOSE 8081

CMD ["uvicorn", "app:application", "--host", "0.0.0.0", "--port", "8081"]
