# Gunakan base image Python versi 3.12 yang ringan
FROM python:3.12-slim

# Tentukan working directory di dalam container
WORKDIR /app

# Copy seluruh file project ke container
COPY . /app

# Install dependencies dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Ekspos port Flask (5000)
EXPOSE 5000

# Jalankan aplikasi Flask (OOP)
CMD ["python", "flask_app/app.py"]
