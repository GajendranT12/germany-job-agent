import os
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

EMAIL_ID = os.environ["EMAIL_ID"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]

KEYWORDS = [
    "Data QA Engineer",
    "ETL Testing",
    "Data Warehouse Testing",
    "Big Data Testing",
    "Azure Databricks"
]

YOUR_SKILLS = [
    "sql",
    "etl",
    "databricks",
    "pyspark",
    "spark",
    "data warehouse",
    "azure"
]


def search_indeed():
    jobs = []

    for keyword in KEYWORDS:
        query = keyword.replace(" ", "+")

        url = (
            f"https://de.indeed.com/jobs?"
            f"q={query}&l=Germany"
        )

        headers = {
            "User-Agent": (
                "Mozilla/5.0"
            )
        }

        response = requests.get(url, headers=headers)
        print(f"Searching for keyword: {keyword}")
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        cards = soup.select("div.job_seen_beacon")

        for card in cards[:5]:
            title_elem = card.select_one("h2")

            if not title_elem:
                continue

            title = title_elem.get_text(strip=True)

            jobs.append({
                "title": title,
                "company": "Indeed Germany",
                "description": title,
                "url": url
            })

    return jobs


def score_job(job):
    score = 0

    description = job["description"].lower()

    for skill in YOUR_SKILLS:
        if skill in description:
            score += 10

    return score


def send_email(jobs):
    if not jobs:
        body = "No matching jobs found today."
    else:
        body = ""

        for idx, job in enumerate(jobs, 1):
            body += (
                f"{idx}. {job['title']}\n"
                f"Company: {job['company']}\n"
                f"Score: {job['score']}\n"
                f"Link: {job['url']}\n\n"
            )

    msg = MIMEText(body)

    msg["Subject"] = "Germany Data QA Jobs"
    msg["From"] = EMAIL_ID
    msg["To"] = EMAIL_ID

    with smtplib.SMTP(
        "smtp.gmail.com",
        587
    ) as server:

        server.starttls()

        server.login(
            EMAIL_ID,
            EMAIL_PASSWORD
        )

        server.send_message(msg)


jobs = search_indeed()

print(f"Total jobs found: {len(jobs)}")

for job in jobs:
    job["score"] = score_job(job)

jobs.sort(
    key=lambda x: x["score"],
    reverse=True
)

send_email(jobs[:10])

print("Email sent successfully!")
