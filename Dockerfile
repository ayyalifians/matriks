# Gunakan Python versi ringan
FROM python:3.12-slim

# Set direktori kerja
WORKDIR /app

# Salin semua file ke dalam container
COPY . /app

# Install dependensi
RUN pip install flask

# Buka port 5000
EXPOSE 5000

# Jalankan aplikasi Flask
CMD ["python", "flask_app/app.py"]
