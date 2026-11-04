from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)
app.json.ensure_ascii = False


# Tatlı mesajlar listesi. Bunları kendi mesajlarınla değiştir!
FORTUNES = [
    
    "Haydi bakalım, gelecekteki sen bugünkü emeğine teşekkür edecek. 🌱",
    "Biraz dur ve Rabbine yönel. Kalbinin de dinlenmeye ihtiyacı var. 🤍",
    "Bugün mükemmel olmak zorunda değilsin, sadece biraz ilerlemen yeterli.",
    "Kendine biraz nazik davran. Her gün aynı güçte olmak zorunda değilsin.",
    "Haydi, beş dakika bile olsa başla. Motivasyon bazen başladıktan sonra gelir!",
    "Namazını erteleme, belki de ihtiyacın olan huzur tam da orada.",
    "Bir sayfa bile ilerlemektir. Küçük adımlar da seni hedefine götürür.",
    "Kötü bir gün, kötü bir hayat demek değildir.",
    "Dünya için koştururken ruhunu da ihmal etme.",
    "Hadi çalışkan arı, bugün de biraz bal yapalım! 🐝",
    "Her öğrendiğin bilgi, kendine açtığın yeni bir kapı.",
    "Dinlenmek tembellik değil, kendine bakmanın bir parçasıdır.",
    "Duanı et, gayretini göster ve gerisini Allah'a bırak.",
    "Telefonu bırak, hayallerine biraz zaman ayır. 📚",
    "Kendini başkalarının yolculuğuyla kıyaslama. Senin zamanın sana ait.",
    "Bir bardak su iç, masanı toparla ve yeniden başla.",
    "Yeni bir gün, yeni bir ihtimal. Bismillah!",
    "Kalbin yorulduğunda secdeyi hatırla.",
    "Bugün kendin için yaptığın küçücük bir şey bile kıymetli.",
    "Hayallerin biraz emek, biraz sabır ve bolca istikrar bekliyor.",
    "Hadi bakalım, ertelediğin o küçük işi aradan çıkaralım!",
    "Allah gönlüne ferahlık, zihnine açıklık, işlerine kolaylık versin.",
    "Sen yalnızca başardıklarından ibaret değilsin. Olduğun hâlinle de değerlisin.",
    "Biraz ders, biraz dua, biraz hareket, bolca huzur! 🌷",
    "Kendine verdiğin sözleri tutmanın en güzel zamanı: ŞİMDİ!",
    "Her şeyi bugün çözmek zorunda değilsin. Biraz nefes al.",
    "Namaz, günün telaşında ruhuna verdiğin güzel bir mola olsun.",
    "Yavaş ilerliyor olabilirsin ama yerinde saymıyorsun.",
    "Bugün kendinin daha iyi bir versiyonuna küçük bir iyilik yap.",
    "Psst! Sen sandığından çok daha fazlasını başarabilirsin. 🧸",
    "Kahveni al, güzel bir niyet et ve gününe başla.",
    "Disiplin, kendine verdiğin değerin günlük bir yansımasıdır.",
    "Her şeyi kontrol etmek zorunda değilsin. Tevekkül etmeyi de hatırla.",
    "Bugünkü 25 dakikan, yarınki özgüvenin olabilir.",
    "Kendine de en sevdiğin insana davrandığın gibi davran.",
    "Haydi, biraz hareket et! Bedeninin de ilgine ihtiyacı var.",
    "Bir seccade, biraz dua ve Rabbine açılan bir kalp...",
    "Mükemmel zamanı bekleme, güzel şeyler küçük başlangıçlarla olur.",
    "Bugün de vazgeçme. Kendine verdiğin emek boşa gitmeyecek.",
    "Bugün yeni bir sayfa, ona güzel şeyler yaz. ☀️",
    "Sen bir proje değilsin. Sürekli geliştirilmek zorunda değilsin. Bazen sadece yaşa.",
    "Biraz çalış, biraz dinlen, kendine biraz da sevgi ver.",
    "Kendine inan. Henüz yolun başındasın.",
    "Rabbine yönelmek için mükemmel olmayı bekleme. Olduğun hâlinle dua et.",
    "Bugün de kendin için güzel bir şey yapmayı ihmal etme.",
    "Hedeflerin seni korkutmasın, onları küçük parçalara böl.",
    "İçindeki umudu küçümseme. En güzel başlangıçlar bazen sessiz olur.",
    "Haydi, gelecekteki kendine güzel bir anı bırak!",
    "Bir mola ver, nefes al ve yeniden dene. Her şey adım adım.",
    "Bugün kalbine huzur, hayatına bereket gelsin. 🤍",
    "Küçük adımlar, büyük değişimlerin başlangıcıdır.",
    "Başlamak için hazır hissetmene gerek yok. Sadece başla.",
    "Allah emeğine bereket, kalbine huzur versin.",
    "Kendini ihmal etmeden, kendin için ilerle. 🌸"

]


# Ana sayfa: templates/index.html dosyasını gösterir
@app.route("/")
def index():
    return render_template("index.html")


# Sağlık kontrolü: "uygulama yaşıyor mu?"
@app.route("/health")
def health():
    return jsonify(status="bozuk")


# Rastgele fal: listeden bir mesaj seçip JSON olarak döndürür
@app.route("/api/fortune")
def fortune():
    secilen = random.choice(FORTUNES)
    return jsonify(fortune=secilen)


# Sadece "python app.py" ile çalıştırınca sunucuyu başlatır
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
