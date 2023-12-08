import smtplib
from config import password
from webscraping import download_page, parse_html


def sending_email(userinput_email,percent_off):
    EMAIL_ADDRESS = "amazon.pricecheck.py@gmail.com"
    EMAIL_PASSWORD = password
    import smtplib
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'Your item has dropped in price!'
        body = f'Your item has dropped in price.\n It is currently on a discount of {percent_off}.'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, userinput_email, msg)





    