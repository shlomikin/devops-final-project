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

status = "Passed" if final_grade >= 60 else "Failed"

logging.info("Calculation completed")

html = f"""
<html>
<head><title>Grade Report</title></head>
<body>
<h2>Student Report</h2>
<p>Name: {args.name}</p>
<p>Original Grade: {args.grade}</p>
<p>Bonus Applied: {bonus}</p>
<p>Final Grade: {final_grade}</p>
<p>Status: {status}</p>
<p>Exam Date: {args.exam_date}</p>
</body>
</html>
"""

with open("output/report.html", "w") as f:
    f.write(html)

print("Report generated successfully")
