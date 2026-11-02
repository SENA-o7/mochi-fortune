from app import app, FORTUNES


# Test 1: /health çalışıyor mu?
def test_health():
    client = app.test_client()           # sahte tarayıcı oluştur
    response = client.get("/health")     # /health adresine git
    assert response.status_code == 200   # 200 (her şey yolunda) dönmeli
    veri = response.get_json()           # JSON'u Python sözlüğüne çevir
    assert veri["status"] == "ok"        # içinde status: ok olmalı


# Test 2: /api/fortune listeden bir mesaj veriyor mu?
def test_fortune():
    client = app.test_client()
    response = client.get("/api/fortune")
    assert response.status_code == 200
    veri = response.get_json()
    assert veri["fortune"] in FORTUNES   # mesaj listenin İÇİNDE mi?


# Test 3: Ana sayfa açılıyor mu?
def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
