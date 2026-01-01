FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY quantum_avatar/ ./quantum_avatar/

EXPOSE 5000

CMD ["python", "quantum_avatar/ui/app.py"]