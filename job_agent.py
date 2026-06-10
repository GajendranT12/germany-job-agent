import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

KEYWORDS = [
    "Data QA Engineer",
    "ETL Testing",
    "Data Warehouse Testing",
    "Azure Databricks",
    "Big Data Testing"
]

PROFILE = {
    "experience": "10+ years",
    "visa_sponsorship": True,
    "language": "English",
    "relocation": "Germany"
}

def search_jobs():
    print("Integrate LinkedIn, StepStone, Indeed APIs or Playwright scraping here.")
    return []

def score_job(job):
    score = 0
    skills = ["SQL", "Databricks", "ETL", "PySpark"]
    for skill in skills:
        if skill.lower() in job.get("description", "").lower():
            score += 25
    return score

def send_email(jobs):
    body = "\n".join(
        f"{j['title']} | {j['company']} | Score: {j['score']}"
        for j in jobs
    )

    msg = MIMEText(body)
    msg["Subject"] = "Germany Data QA Job Digest"
    msg["From"] = "YOUR_EMAIL"
    msg["To"] = "YOUR_EMAIL"

    print("Configure SMTP settings before enabling email.")

if __name__ == "__main__":
    jobs = search_jobs()
    ranked = []
    for job in jobs:
        job["score"] = score_job(job)
        ranked.append(job)

    ranked = sorted(ranked, key=lambda x: x["score"], reverse=True)
    send_email(ranked[:20])
