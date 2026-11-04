from bot import DURUMLAR, durum_mesaji, klavye, kullanicilari_oku

KULLANICILAR = {1489831325: "Sena", 111: "Sudenas"}


# Test 1: Secret'taki yazı doğru okunuyor mu?
def test_kullanicilari_oku():
    sonuc = kullanicilari_oku("1489831325:Sena, 111:Sudenas,222:Zeynep Selin")
    assert sonuc == {1489831325: "Sena", 111: "Sudenas", 222: "Zeynep Selin"}


# Test 2: Listedeki kişi butona basınca doğru mesaj hazırlanıyor mu?
def test_izinli_kisi():
    assert durum_mesaji(1489831325, "namaz", KULLANICILAR) == "🕌 Sena namaza kalktı"


# Test 3: Listede olmayan biri mesaj gönderemez
def test_izinsiz_kisi():
    assert durum_mesaji(999, "mola", KULLANICILAR) is None


# Test 4: Olmayan bir buton mesaj üretmez
def test_bilinmeyen_durum():
    assert durum_mesaji(1489831325, "uyku", KULLANICILAR) is None


# Test 5: Her durum için bir buton var mı?
def test_klavye():
    butonlar = [satir[0]["callback_data"] for satir in klavye()["inline_keyboard"]]
    assert butonlar == list(DURUMLAR)
