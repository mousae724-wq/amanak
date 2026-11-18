import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# --- بيانات تجريبية بنفس أرقامك ---
STATS = {
    "score": 94,
    "total": 12847,
    "safe_pct": 79.5,
    "suspicious_pct": 15.1,
    "high_risk_pct": 5.4,
    "safe_count": 10213,
    "suspicious_count": 1940,
    "high_risk_count": 694,
}

REPORTS = [
    {"id": "R-12847", "type": "رابط مشبوه", "risk": "عالي", "score": 12, "time": "منذ 2 دقيقة", "status": "محظور"},
    {"id": "R-12846", "type": "رسالة احتيال", "risk": "متوسط", "score": 58, "time": "منذ 9 دقائق", "status": "قيد المراجعة"},
    {"id": "R-12845", "type": "تحويل بنكي", "risk": "آمن", "score": 94, "time": "منذ 18 دقيقة", "status": "تم"},
    {"id": "R-12844", "type": "رابط مشبوه", "risk": "عالي", "score": 21, "time": "منذ 31 دقيقة", "status": "محظور"},
    {"id": "R-12843", "type": "بريد إلكتروني", "risk": "آمن", "score": 91, "time": "منذ 44 دقيقة", "status": "تم"},
]

HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>أمانك | لوحة حماية الاحتيال</title>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'IBM Plex Sans Arabic',system-ui,sans-serif;background:#F2F3F5;color:#111827}
.top{background:#0F1F33;color:#fff;padding:14px 0;border-bottom:1px solid #1E3350}
.wrap{max-width:1120px;margin:auto;padding:0 20px}
.top-in{display:flex;justify-content:space-between;align-items:center}
.logo{display:flex;gap:12px;align-items:center}
.mark{width:38px;height:38px;background:#fff;color:#0F1F33;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:19px;border-radius:8px}
.logo b{font-size:19px}.logo span{display:block;font-size:12px;color:#9AA8BC;font-weight:400}
.user{text-align:left;font-size:13px}.user b{font-size:14px}.user small{color:#9AA8BC}
.main{padding:22px 0 40px}
.head{display:flex;justify-content:space-between;align-items:end;margin-bottom:18px}
.head h1{font-size:26px}.head p{color:#5B6B7F;font-size:14px;margin-top:4px}
.badge{background:#fff;border:1px solid #DCE1E7;padding:6px 12px;border-radius:999px;font-size:13px;color:#2F3E52}
.grid{display:grid;grid-template-columns:1.15fr 2fr;gap:16px;margin-bottom:16px}
.card{background:#fff;border:1px solid #E2E6EB;border-radius:12px;padding:20px}
.score-box{text-align:center}
.score-num{font-size:56px;font-weight:700;line-height:1}.score-label{color:#5B6B7F;font-size:14px;margin-top:6px}
.bar{height:8px;background:#EEF1F4;border-radius:99px;overflow:hidden;margin:16px 0 10px}
.bar i{display:block;height:100%;background:#0F766E;width:94%}
.legend{display:flex;justify-content:space-between;font-size:13px;color:#5B6B7F}
.kpis{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.kpi{border:1px solid #E2E6EB;border-radius:10px;padding:16px}
.kpi small{color:#5B6B7F}.kpi b{font-size:24px;display:block;margin:6px 0 2px}.kpi span{font-size:13px}
.kpi.safe b{color:#0F766E}.kpi.warn b{color:#B45309}.kpi.danger b{color:#B91C1C}
.table-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}
.table-head h3{font-size:16px}.table-head a{font-size:13px;color:#0F3A5F;text-decoration:none}
table{width:100%;border-collapse:collapse;font-size:14px}
th{text-align:right;color:#5B6B7F;font-weight:500;padding:10px 8px;border-bottom:1px solid #E2E6EB}
td{padding:13px 8px;border-bottom:1px solid #F0F2F4}
.pill{padding:4px 10px;border-radius:99px;font-size:12px;font-weight:600}
.pill.high{background:#FEF2F2;color:#B91C1C}.pill.mid{background:#FFFBEB;color:#92400E}.pill.safe{background:#ECFDF5;color:#065F46}
.status{color:#5B6B7F;font-size:13px}
.footer{margin-top:16px;display:flex;gap:10px;flex-wrap:wrap}
.footer a{background:#fff;border:1px solid #DCE1E7;padding:8px 14px;border-radius:8px;font-size:13px;color:#111827;text-decoration:none}
@media(max-width:760px){.grid{grid-template-columns:1fr}.kpis{grid-template-columns:1fr}.head{flex-direction:column;align-items:start;gap:10px}.top-in{flex-direction:row}}
</style>
</head>
<body>
<div class="top"><div class="wrap top-in">
<div class="logo"><div class="mark">أ</div><div><b>أمانك</b><span>AMANAK • نظام حماية الاحتيال</span></div></div>
<div class="user"><b>موسى مسؤول الآن</b><br><small>آخر تحديث: الآن • القاهرة</small></div>
</div></div>
<div class="wrap main">
<div class="head"><div><h1>نظرة عامة على الحماية</h1><p>متابعة عمليات الفحص والتهديدات في الوقت الفعلي</p></div><div class="badge">● النظام يعمل بشكل طبيعي</div></div>
<div class="grid">
<div class="card score-box"><div class="score-num">94<span style="font-size:22px;color:#5B6B7F"> / 100</span></div><div class="score-label">درجة حماية الذكاء الاصطناعي</div><div class="bar"><i></i></div><div class="legend"><span>ممتاز</span><span>آخر 24 ساعة</span></div><p style="font-size:13px;color:#5B6B7F;margin-top:14px;text-align:right;line-height:1.7">النظام مستقر. تم حظر 694 عملية عالية الخطورة خلال آخر 24 ساعة.</p></div>
<div class="card"><div style="display:flex;justify-content:space-between"><div><small style="color:#5B6B7F">إجمالي عمليات الفحص</small><b style="font-size:32px;display:block;margin-top:4px">12,847</b></div><span style="font-size:13px;color:#0F766E;background:#ECFDF5;padding:6px 10px;border-radius:99px;height:fit-content">▲ 12.4% عن أمس</span></div>
<div class="kpis" style="margin-top:16px">
<div class="kpi safe"><small>آمن</small><b>79.5%</b><span>10,213 عملية</span></div>
<div class="kpi warn"><small>مشبوه</small><b>15.1%</b><span>1,940 عملية</span></div>
<div class="kpi danger"><small>عالي الخطورة</small><b>5.4%</b><span>694 عملية</span></div>
</div></div>
</div>
<div class="card"><div class="table-head"><h3>أحدث التقارير</h3><a href="/api/reports">عرض كل التقارير ←</a></div>
<table><tr><th>المعرف</th><th>النوع</th><th>الخطر</th><th>الدرجة</th><th>الوقت</th><th>الحالة</th></tr>
{% for r in reports %}
<tr><td><b>{{r.id}}</b></td><td>{{r.type}}</td><td><span class="pill {{'high' if r.risk=='عالي' else 'mid' if r.risk=='متوسط' else 'safe'}}">{{r.risk}}</span></td><td>{{r.score}}</td><td class="status">{{r.time}}</td><td>{{r.status}}</td></tr>
{% endfor %}
</table></div>
<div class="footer"><a href="/api/reports">/api/reports</a><a href="/api/stats">/api/stats</a><a href="/health">/health</a></div>
</div></body></html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, reports=REPORTS)

@app.route("/api/stats")
def stats():
    return jsonify(STATS)

@app.route("/api/reports")
def reports():
    return jsonify(REPORTS)

@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "amanak"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)