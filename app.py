import os
from flask import Flask
from pyngrok import ngrok

app = Flask(__name__)

def find_image(base_name):
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    if os.path.exists(static_dir):
        for file in os.listdir(static_dir):
            if file.lower().startswith(base_name.lower()):
                return f"/static/{file}"
    return "https://images.unsplash.com/photo-1585551691229-4176181db38f?w=400"

@app.route('/')
def home():
    img_karak = find_image('karak')
    img_halabi = find_image('halabi')

    html_content = f"""
    <html>
        <head>
            <title>دليل الكرك السياحي</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{
                    text-align: center; 
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                    background-color: #f4f7f6; 
                    padding: 15px; 
                    direction: rtl;
                    margin: 0;
                }}
                .hero-section {{
                    background: linear-gradient(rgba(30, 60, 114, 0.85), rgba(42, 82, 152, 0.85)), 
                                url('https://images.unsplash.com/photo-1541432901042-2d8bd64b4a9b?q=80&w=1200') no-repeat center center;
                    background-size: cover;
                    color: white; 
                    padding: 40px 20px; 
                    border-radius: 15px; 
                    box-shadow: 0 4px 15px rgba(0,0,0,0.15); 
                    margin-bottom: 25px;
                }}
                .tabs-container {{
                    display: flex;
                    justify-content: center;
                    gap: 10px;
                    margin-bottom: 25px;
                }}
                .tab-button {{
                    background-color: #ffffff;
                    color: #2c3e50;
                    border: 2px solid #2a5298;
                    padding: 12px 25px;
                    font-size: 16px;
                    font-weight: bold;
                    border-radius: 30px;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
                }}
                .tab-button.active {{
                    background-color: #2a5298;
                    color: white;
                }}
                .content-section {{
                    display: none;
                    max-width: 700px; 
                    margin: 0 auto;
                }}
                .content-section.active {{
                    display: block;
                }}
                .card {{
                    background: white; 
                    border-radius: 12px; 
                    padding: 20px; 
                    margin-bottom: 20px; 
                    text-align: right; 
                    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
                }}
                .card-img {{
                    width: 100%; 
                    max-height: 380px; 
                    object-fit: cover;
                    border-radius: 10px; 
                    margin-bottom: 15px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                }}
                .btn {{
                    display: block; 
                    text-align: center;
                    color: white; 
                    padding: 12px; 
                    border-radius: 8px; 
                    text-decoration: none; 
                    font-weight: bold; 
                    font-size: 15px; 
                    margin-top: 15px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
            </style>
        </head>
        <body>
            
            <div class="hero-section">
                <h1 style="margin: 0; font-size: 30px;">🏰 أهلاً بك في دليل الكرك السياحي 🏰</h1>
                <p style="margin: 10px 0 0 0; font-size: 16px; opacity: 0.95;">اكتشف التاريخ والأصالة العريقة برعاية المطور حازم الطراونه</p>
            </div>

            <div class="tabs-container">
                <button class="tab-button active" onclick="switchTab('places', this)">🏛️ الأماكن السياحية</button>
                <button class="tab-button" onclick="switchTab('restaurants', this)">🍽️ المطاعم والشعبي</button>
            </div>

            <div id="places" class="content-section active">
                <div class="card" style="border-top: 6px solid #e67e22;">
                    <img src="{img_karak}" alt="قلعة الكرك" class="card-img">
                    <h2 style="color: #e67e22; margin-top: 5px;">🏰 قلعة الكرك التاريخية</h2>
                    <p style="color: #444; line-height: 1.7; font-size: 16px;">من أكبر وأهم القلاع التاريخية في الأردن، تمتاز بأبراجها وإطلالتها الساحرة وممراتها الأثرية العريقة التّي تشهد على حضارات متعاقبة.</p>
                    <a href="https://maps.google.com/?q=Karak+Castle" target="_blank" class="btn" style="background-color: #e67e22;">📍 موقع قلعة الكرك على خرائط جوجل</a>
                </div>
            </div>

            <div id="restaurants" class="content-section">
                <div class="card" style="border-top: 6px solid #9b59b6;">
                    <img src="{img_halabi}" alt="مطعم عادل الحلبي" class="card-img">
                    <h2 style="color: #9b59b6; margin-top: 5px;">😋 مطعم عادل الحلبي</h2>
                    <p style="color: #444; line-height: 1.7; font-size: 16px;">من أقدم وأعرق المطاعم الشعبية في الكرك، يقدم الوجبات والمأكولات التراثية السريعة التي يفضلها أهل المدينة وزوارها منذ عقود.</p>
                    <a href="https://maps.google.com/?q=Adel+Al+Halabi+Restaurant+Karak" target="_blank" class="btn" style="background-color: #9b59b6;">📍 موقع مطعم عادل الحلبي على خرائط جوجل</a>
                </div>
            </div>

            <script>
                function switchTab(tabId, button) {{
                    // إخفاء كل الأقسام
                    document.querySelectorAll('.content-section').forEach(section => {{
                        section.classList.remove('active');
                    }});
                    // إزالة اللون الأزرق من كل الأزرار
                    document.querySelectorAll('.tab-button').forEach(btn => {{
                        btn.classList.remove('active');
                    }});
                    
                    // إظهار القسم المطلوب وتفعيل الزر تابعه
                    document.getElementById(tabId).classList.add('active');
                    button.classList.add('active');
                }}
            </script>
        </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    try:
        ngrok.set_auth_token("3FpseieYk5LvPm7Q2YuREANL9iZ_6cGw5xgeg4dCa3thof2FA")
        public_url = ngrok.connect(5000)
        print("\n" + "="*50)
        print(f"🔗🔗 الرابط العالمي الجديد للموبايل: {public_url.public_url}")
        print("="*50 + "\n")
    except Exception as e:
        print(f"Ngrok error: {e}")
        
    app.run(host='0.0.0.0', port=5000)

