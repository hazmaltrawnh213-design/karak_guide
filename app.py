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
        </head>
        <body style="text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #eef2f3; padding: 20px; direction: rtl;">
            
            <div style="background: linear-gradient(135deg, #1e3c72, #2a5298); color: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 30px;">
                <h1 style="margin: 0; font-size: 32px;">🏰 دليل الكرك السياحي الاحترافي 🏰</h1>
                <p style="margin: 10px 0 0 0; font-size: 18px; opacity: 0.9;">تصميم وتطوير المطور: حازم الطراونه</p>
            </div>

            <div style="max-width: 900px; margin: 0 auto; padding-bottom: 40px;">
                
                <div style="background: white; border-right: 6px solid #e67e22; border-radius: 8px; padding: 20px; margin-bottom: 20px; text-align: right; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                    <h2 style="color: #e67e22; margin-top: 0;">🌟 اماكن مشهورة</h2>
                    <div style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
                        <div style="flex: 1; min-width: 250px;">
                            <h3 style="color: #2c3e50; margin-bottom: 5px;">🏰 قلعة الكرك التاريخية</h3>
                            <p style="color: #555; line-height: 1.6;">من أكبر وأهم القلاع التاريخية في الأردن، تمتاز بأبراجها وإطلالتها الساحرة وممراتها الأثرية العريقة التّي تشهد على حضارات متعاقبة.</p>
                            <a href="https://maps.google.com/?q=Karak+Castle" target="_blank" style="display: inline-block; background-color: #e67e22; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; font-weight: bold; font-size: 14px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">📍 موقع قلعة الكرك على خرائط جوجل</a>
                        </div>
                        <div style="flex: 1; text-align: center;">
                            <img src="{img_karak}" alt="قلعة الكرك" style="width: 100%; max-width: 350px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                        </div>
                    </div>
                </div>

                <div style="background: white; border-right: 6px solid #9b59b6; border-radius: 8px; padding: 20px; margin-bottom: 20px; text-align: right; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                    <h2 style="color: #9b59b6; margin-top: 0;">🍽️ مطاعم وأكل شعبي</h2>
                    <div style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
                        <div style="flex: 1; min-width: 250px;">
                            <h3 style="color: #2c3e50; margin-bottom: 5px;">😋 مطعم عادل الحلبي</h3>
                            <p style="color: #555; line-height: 1.6;">من أقدم وأعرق المطاعم الشعبية في الكرك، يقدم الوجبات والمأكولات التراثية السريعة التي يفضلها أهل المدينة وزوارها منذ عقود.</p>
                            <a href="https://maps.google.com/?q=Adel+Halabi+Restaurant+Karak" target="_blank" style="display: inline-block; background-color: #9b59b6; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; font-weight: bold; font-size: 14px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">📍 موقع مطعم عادل الحلبي على خرائط جوجل</a>
                        </div>
                        <div style="flex: 1; text-align: center;">
                            <img src="{img_halabi}" alt="مطعم عادل الحلبي" style="width: 100%; max-width: 350px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                        </div>
                    </div>
                </div>

            </div>
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

