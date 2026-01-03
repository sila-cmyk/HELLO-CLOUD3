from flask import Flask, render_template_string, request

app = Flask(__name__)
application = app

# Verileri veritabanı yerine bu listede tutacağız
ziyaretci_listesi = []

HTML = """
<!doctype html>
<html>
<head>
    <title>Buluttan Selam!</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; background: #eef2f3; }
        h1 { color: #333; }
        form { margin: 20px auto; }
        input { padding: 10px; font-size: 16px; }
        button { padding: 10px 15px; background: #4CAF50; color: white; border: none; border-radius: 6px; cursor: pointer; }
        ul { list-style: none; padding: 0; }
        li { background: white; margin: 5px auto; width: 200px; padding: 8px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Buluttan Selam!</h1>
    <p>Adını yaz, selamını bırak </p>
    <form method="POST">
        <input type="text" name="isim" placeholder="Adını yaz" required>
        <button type="submit">Gönder</button>
    </form>
    <h3>Ziyaretçiler:</h3>
    <ul>
        {% for ad in isimler %}
            <li>{{ ad }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        isim = request.form.get("isim")
        if isim:
            # İsmi listenin en başına ekle
            ziyaretci_listesi.insert(0, isim)
            # Sadece son 10 ismi tutalım
            if len(ziyaretci_listesi) > 10:
                ziyaretci_listesi.pop()

    return render_template_string(HTML, isimler=ziyaretci_listesi)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
