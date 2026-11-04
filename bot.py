# Mochi durum botu: grupta butona basılınca "🕌 Sena namaza kalktı" gibi mesaj atar.
# Flask'tan ayrı, kendi container'ında çalışır: python bot.py
import json
import os
import time
import urllib.request

# Butonlar: anahtar → (buton yazısı, gruba gidecek mesaj)
DURUMLAR = {
    "masada": ("🪑 Masaya oturdum", "🪑 {isim} masaya oturdu"),
    "namaz": ("🕌 Namaza kalktım", "🕌 {isim} namaza kalktı"),
    "mola": ("☕ Moladayım", "☕ {isim} molada"),
    "kalkti": ("🚶 Masadan kalktım", "🚶 {isim} masadan kalktı"),
    "bitti": ("🌙 Ders bitti, free day", "🌙 {isim} için ders bitti, bugün free day!"),
    "sitem": ("😤 Sena'ya sitem et", "😤 {isim} diyor ki: Sena, Allah belanı vermesin, ne uğraştırdın bizi! 😂"),
}


# "1489831325:Sena,111:Sudenas" yazısını {1489831325: "Sena", 111: "Sudenas"} yapar
def kullanicilari_oku(metin):
    kullanicilar = {}
    for parca in metin.split(","):
        if ":" in parca:
            kimlik, isim = parca.split(":", 1)
            kullanicilar[int(kimlik.strip())] = isim.strip()
    return kullanicilar


# Butona basan kişi listedeyse gruba gidecek mesajı döndürür, değilse None
def durum_mesaji(kullanici_id, durum, kullanicilar):
    isim = kullanicilar.get(kullanici_id)
    if isim is None or durum not in DURUMLAR:
        return None
    return DURUMLAR[durum][1].format(isim=isim)


# Grupta görünecek buton listesi
def klavye():
    return {"inline_keyboard": [
        [{"text": buton, "callback_data": anahtar}]
        for anahtar, (buton, _) in DURUMLAR.items()
    ]}


# Telegram'a istek atar
def telegram(token, metod, **parametreler):
    parametreler = {k: v for k, v in parametreler.items() if v is not None}
    istek = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/{metod}",
        data=json.dumps(parametreler).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(istek, timeout=40) as cevap:
        return json.load(cevap)


# Gelen tek bir olayı (buton tıklaması ya da /panel komutu) işler
def isle(token, chat_id, kullanicilar, olay):
    # Biri butona bastı
    if "callback_query" in olay:
        tiklama = olay["callback_query"]
        kullanici_id = tiklama["from"]["id"]
        metin = durum_mesaji(kullanici_id, tiklama.get("data"), kullanicilar)

        if metin is None:
            print(f"İzinsiz tıklama: {kullanici_id}", flush=True)
            telegram(token, "answerCallbackQuery", callback_query_id=tiklama["id"],
                     text=f"Bu butonları kullanma iznin yok. Telegram ID'n: {kullanici_id}",
                     show_alert=True)
            return

        telegram(token, "sendMessage", chat_id=chat_id, text=metin)
        telegram(token, "answerCallbackQuery", callback_query_id=tiklama["id"], text="✓ gönderildi")
        print(metin, flush=True)

    # Listedeki biri /panel yazdı: butonları gruba gönder
    elif "message" in olay:
        mesaj = olay["message"]
        if mesaj.get("text", "").startswith("/panel") and mesaj["from"]["id"] in kullanicilar:
            telegram(token, "sendMessage", chat_id=mesaj["chat"]["id"],
                     text="🍡 Ne yapıyorsun? Butona bas 👇", reply_markup=klavye())


def main():
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    kullanicilar = kullanicilari_oku(os.environ.get("TELEGRAM_KULLANICILAR", ""))
    print(f"Mochi botu başladı. İzinli kişiler: {list(kullanicilar.values())}", flush=True)

    sira = None  # hangi olaydan devam edeceğimiz
    while True:
        try:
            # 30 saniyeye kadar yeni olay bekler (long polling)
            olaylar = telegram(token, "getUpdates", offset=sira, timeout=30,
                               allowed_updates=["message", "callback_query"])["result"]
        except Exception as hata:
            print(f"Telegram'a ulaşılamadı: {hata}", flush=True)
            time.sleep(5)
            continue

        for olay in olaylar:
            sira = olay["update_id"] + 1
            try:
                isle(token, chat_id, kullanicilar, olay)
            except Exception as hata:
                print(f"Olay işlenemedi: {hata}", flush=True)


if __name__ == "__main__":
    main()
