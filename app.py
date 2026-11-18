# AMANAK - أمانك | Backend Python - Musa
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

@app.route('/api/dashboard/summary')
def dashboard_summary():
    return jsonify({
        "user": "Musa",
        "brand": "AMANAK - أمانك",
        "total_scans": 12847,
        "safe": 10219, "safe_percent": 79.5,
        "suspicious": 1942, "suspicious_percent": 15.1,
        "high_risk": 686, "high_risk_percent": 5.4,
        "ai_protection_score": 94
    })

@app.route('/api/scans')
def scans():
    return jsonify([
        {"id": 842913, "link": "cheapgoods.app/promo/9941", "risk": "High Risk", "status": "Blocked"},
        {"id": 842912, "link": "sale-off.co/deal", "risk": "Suspicious", "status": "Reviewed"},
        {"id": 842910, "link": "storename.sa/product", "risk": "Safe", "status": "Approved"},
    ])

@app.route('/api/reports')
def reports():
    return jsonify([
        {"id": 1, "title": "متوسط خطر الاحتيال انخفض لـ 22%"},
        {"id": 2, "title": "تم حظر 320 رابط ضار تلقائيا"},
        {"id": 3, "title": "ثقة العملاء ارتفعت +14%"},
    ])

@app.route('/')
def home():
    return render_template_string("""
    <html dir="rtl"><head><meta charset="utf-8"><title>AMANAK</title>
    <style>body{background:#070714;color:#fff;font-family:sans-serif;padding:20px}
    .card{background:#14142b;border:1px solid #a855f7;border-radius:20px;padding:20px}
    h1{font-size:50px;background:linear-gradient(90deg,#00e5c7,#a855f7);-webkit-background-clip:text;-webkit-text-fill-color:transparent}</style></head>
    <body><h2>AMANAK - أمانك</h2><p>Musa - Security Admin</p>
    <div class="card"><small>AI PROTECTION SCORE</small><h1>94/100</h1>
    <p>Total: 12,847 | Safe 79.5% | Suspicious 15.1% | High Risk 5.4%</p></div>
    <p>APIs: <a href="/api/dashboard/summary" style="color:#00e5c7">/api/dashboard/summary</a> | <a href="/api/scans" style="color:#00e5c7">/api/scans</a> | <a href="/api/reports" style="color:#00e5c7">/api/reports</a></p>
    </body></html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
