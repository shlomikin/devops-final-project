import argparse
import datetime
import logging
import os
import sys

os.makedirs("output", exist_ok=True)

logging.basicConfig(
    filename="output/log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

parser = argparse.ArgumentParser()

parser.add_argument("--name", required=True)
parser.add_argument("--grade", type=int, required=True)
parser.add_argument("--bonus", required=True)
parser.add_argument("--exam_date", required=True)

args = parser.parse_args()

if args.grade < 0 or args.grade > 100:
    logging.error("Grade must be between 0 and 100")
    sys.exit("Grade must be between 0 and 100")

try:
    datetime.datetime.strptime(args.exam_date, "%Y-%m-%d")
except ValueError:
    logging.error("Date must be YYYY-MM-DD")
    sys.exit("Date must be YYYY-MM-DD")

bonus = args.bonus.lower() == "true"

final_grade = args.grade
if bonus:
    final_grade += 5
    if final_grade > 100:
        final_grade = 100

status = "PASSED 🎉" if final_grade >= 60 else "FAILED ❌"
status_color = "#00ff88" if final_grade >= 60 else "#ff4d4d"
grade_color = "#4facfe" if final_grade >= 60 else "#ff6a6a"

logging.info("Calculation completed")

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Student Grade Report</title>
<style>
body {{
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #4facfe, #00f2fe);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}}

.card {{
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 40px;
    width: 450px;
    color: white;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    animation: fadeIn 1s ease-in-out;
}}

@keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(20px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

h1 {{
    text-align: center;
    margin-bottom: 20px;
}}

.grade {{
    font-size: 60px;
    font-weight: bold;
    text-align: center;
    color: {grade_color};
    margin: 10px 0;
}}

.status {{
    text-align: center;
    font-weight: bold;
    font-size: 18px;
    padding: 8px;
    border-radius: 20px;
    background-color: rgba(0,0,0,0.3);
    color: {status_color};
}}

.info {{
    margin-top: 25px;
}}

.info p {{
    margin: 8px 0;
    font-size: 16px;
}}

.footer {{
    margin-top: 25px;
    text-align: center;
    font-size: 13px;
    opacity: 0.8;
}}
</style>
</head>
<body>
<div class="card">
<h1>📊 Student Report</h1>

<div class="grade">{final_grade}</div>
<div class="status">{status}</div>

<div class="info">
<p><strong>Name:</strong> {args.name}</p>
<p><strong>Original Grade:</strong> {args.grade}</p>
<p><strong>Bonus Applied:</strong> {bonus}</p>
<p><strong>Exam Date:</strong> {args.exam_date}</p>
<p><strong>Generated:</strong> {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
</div>

<div class="footer">
Generated automatically by Jenkins Pipeline 🚀
</div>
</div>
</body>
</html>
"""

with open("output/report.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Report generated successfully")
