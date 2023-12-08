import os
import smtplib

EMAIL_ADDRESS = "amazon.pricecheck.py@gmail.com"
EMAIL_PASSWORD = "uxfg sfbf dypv vbnk"

import smtplib
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Your item has dropped price!'
    body = 'your item has dropped price of '

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'zyan2@babson.edu', msg)