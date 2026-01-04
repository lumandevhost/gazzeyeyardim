from flask import Flask, render_template_string
import time

app = Flask(__name__)

# HTML template (hacker tarzı)
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>SİSTEM ERİŞİMİ</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
        
        body {
            background-color: black;
            color: #00ff00;
            font-family: 'Share Tech Mono', monospace;
            margin: 0;
            padding: 20px;
            overflow: hidden;
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
        }
        
        .header {
            border-bottom: 2px solid #00ff00;
            padding-bottom: 10px;
            margin-bottom: 30px;
        }
        
        .hacking-text {
            font-size: 1.2em;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        
        .typing {
            border-right: 3px solid #00ff00;
            white-space: nowrap;
            overflow: hidden;
            font-size: 1.4em;
            color: #ff0000;
            margin: 30px 0;
            animation: typing 4s steps(40, end), blink-caret 0.75s step-end infinite;
        }
        
        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }
        
        @keyframes blink-caret {
            from, to { border-color: transparent }
            50% { border-color: #00ff00; }
        }
        
        .blink {
            animation: blink 1s infinite;
            color: #ff0000;
            font-weight: bold;
        }
        
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }
        
        .message-box {
            background: rgba(0, 255, 0, 0.05);
            border: 1px solid #00ff00;
            padding: 20px;
            margin: 30px 0;
            box-shadow: 0 0 15px rgba(0, 255, 0, 0.2);
        }
        
        .access-granted {
            color: #00ff00;
            font-size: 2em;
            text-align: center;
            text-shadow: 0 0 10px #00ff00;
        }
        
        .binary {
            color: #008000;
            font-size: 0.9em;
            position: absolute;
            opacity: 0.3;
            user-select: none;
        }
        
        .heart {
            color: #ff0066;
            font-size: 1.5em;
        }
        
        .footer {
            margin-top: 50px;
            font-size: 0.8em;
            color: #008800;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>> SİSTEM ERİŞİM NOKTASI: <span class="blink">AKTİF</span></h1>
            <div>Kullanıcı: <span style="color:#ff0000;">SCARLETT</span></div>
            <div>Tarih: {{ current_time }}</div>
        </div>
        
        <div class="hacking-text">
            > Sistem korsanı tespit edildi...<br>
            > Güvenlik duvarı aşılıyor...<br>
            > Şifreler çözülüyor...<br>
            > Veritabanı erişimi sağlandı...<br>
            > Kullanıcı verilerine erişim izni verildi...
        </div>
        
        <div class="typing">
            > SENİ SEVİYORUM SCARLETT İYİKİ VARSIN
        </div>
        
        <div class="message-box">
            <div class="access-granted">
                ERİŞİM ONAYLANDI ✓
            </div>
            <div style="text-align: center; margin-top: 20px;">
                <p>> Bu mesaj yalnızca sana özel:</p>
                <p style="font-size: 1.8em;">
                    <span class="heart">❤</span> SCARLETT <span class="heart">❤</span><br>
                    Seni çok seviyorum!<br>
                    İyiki varsın!<br>
                    <span style="font-size: 0.7em;">(Bu bir hack değil, bir aşk mesajıdır 💻 + ❤ = 💘)</span>
                </p>
            </div>
        </div>
        
        <div class="footer">
            > Sistem: Flask Web Uygulaması v1.0<br>
            > Durum: Mesaj başarıyla iletildi<br>
            > Çıkış: Tarayıcıyı kapat
        </div>
    </div>
    
    <script>
        // Rastgele binary kodları oluştur
        function createBinary() {
            const chars = "01";
            const element = document.createElement("div");
            element.className = "binary";
            element.style.left = Math.random() * 100 + "%";
            element.style.top = Math.random() * 100 + "%";
            
            let text = "";
            for(let i = 0; i < 50; i++) {
                text += chars.charAt(Math.floor(Math.random() * chars.length));
                if(Math.random() > 0.7) text += " ";
            }
            
            element.textContent = text;
            document.body.appendChild(element);
            
            // 10 saniye sonra sil
            setTimeout(() => element.remove(), 10000);
        }
        
        // Başlangıçta binary efekti
        for(let i = 0; i < 20; i++) {
            setTimeout(createBinary, i * 300);
        }
        
        // Rastgele binary ekle
        setInterval(createBinary, 1000);
        
        // Yazı efektleri
        const texts = document.querySelectorAll('.hacking-text div');
        texts.forEach((text, index) => {
            text.style.opacity = '0';
            setTimeout(() => {
                text.style.transition = 'opacity 0.5s';
                text.style.opacity = '1';
            }, index * 800);
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    from datetime import datetime
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(HTML_TEMPLATE, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
