import smtplib
import datetime
import random

MY_EMAIL = "maarcusreniero@gmail.com"
MY_PASSWORD = "G_maarcus@170603"
FRIEND_MAIL_ID = "lazar.gis@gmail.com"


def chooseQuote():
    with open("quotes.txt") as quote:
        all_quotes = quote.readlines()
        quote = random.choice(all_quotes)
        return quote


def sendEmail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)

        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=FRIEND_MAIL_ID,
                            msg=f"Subject: Monday Motivation{chooseQuote()}")


now = datetime.datetime.now()
day = now.weekday()
if day == 0:
    sendEmail()
