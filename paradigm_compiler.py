# used to create csv for all judges paradigms

import pdfplumber
import pandas as pd

lines = []

with pdfplumber.open("26_DTOC2.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        cropped = (
            page.crop((42, 230, 442, 792)) if i == 0
            else page.crop((42, 0, 442, 792))
        )
        text = cropped.extract_text()
        if text:
            lines.extend(text.split("\n"))
lines = [line.strip() for line in lines if "Last changed on" not in line]

judges = pd.read_csv("Tabroom-judgelist (2).csv")["First"].dropna().tolist()
judge_paradigms = {}

current_judge = None
for line in lines:
    match = next((j for j in judges if j in line), None)
    if match:
        current_judge = match
        judge_paradigms[current_judge] = []
    else:
        if current_judge:
            judge_paradigms[current_judge].append(line)

for judge in judge_paradigms:
    judge_paradigms[judge] = "\n".join(judge_paradigms[judge])

pd.DataFrame(
    judge_paradigms.items(),
    columns=["judge", "paradigm"]
).to_csv("judge_paradigms.csv", index=False)
