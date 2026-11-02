# 1. İçinde Python 3.12 kurulu küçük bir Linux ile başla
FROM python:3.12-slim

# 2. Container içinde /app klasöründe çalış
WORKDIR /app

# 3. Önce SADECE requirements.txt'yi kopyala (önbellek için)
COPY requirements.txt .

# 4. Paketleri kur
RUN pip install --no-cache-dir -r requirements.txt

# 5. Sonra projenin geri kalanını kopyala
COPY . .

# 6. Uygulama 5000 portunu kullanıyor (not)
EXPOSE 5000

# 7. Container açılınca bu komut çalışsın
CMD ["python", "app.py"]
