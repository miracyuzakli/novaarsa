# Base image
FROM python:3.11

# Çalışma dizini ayarlama
WORKDIR /usr/src/app

# Bağımlılıkları yükleme
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyalama
COPY . .

# Gunicorn'u çalıştırın
CMD ["python" "manage.py" "runserver" "0.0.0.0:8000"]