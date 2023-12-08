import smtplib
from config import password

# from webscraping import download_page, parse_html


def sending_email(userinput_email, percent_off, discounted_price, original_price):
    EMAIL_ADDRESS = "amazon.pricecheck.py@gmail.com"
    EMAIL_PASSWORD = password
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = "Your item has dropped in price!"
        body = f"Dear Amazon Price Check User: \n This is Amazon Price Check. \n We are excited to inform you the price of your item has dropped to {discounted_price} from {original_price}.\n It is currently on a discount of {percent_off}."

        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(EMAIL_ADDRESS, userinput_email, msg)
