import os
import smtplib
from email.mime.text import MIMEText

EMAIL_ID = os.environ["EMAIL_ID"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]

msg = MIMEText("""
Congratulations Gajendran!

Your Germany AI Job Agent is working successfully.

The next step is to connect it with LinkedIn, Indeed and StepStone to fetch real jobs.
""")

msg["Subject"] = "Germany AI Job Agent - Test Email"
msg["From"] = EMAIL_ID
msg["To"] = EMAIL_ID

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(EMAIL_ID, EMAIL_PASSWORD)
    server.send_message(msg)

print("Test email sent successfully!")
