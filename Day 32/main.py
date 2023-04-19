# import smtplib
#
# myEmail = "maarcusreniero@gmail.com"
# MY_PASSWORD = "G_maarcus@170603"
# FRIEND_MAIL_ID = "albionhubert.jl@gmail.com"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=myEmail, password=MY_PASSWORD)  # logging in
#
#     connection.sendmail(from_addr=myEmail,
#                         to_addrs=FRIEND_MAIL_ID,
#                         msg="Subject:Hi\n\nThis is the body of the email")  # sends the mail
#
# # connection.close() not necessary to use this
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

print(year, month, day_of_week)

dob = dt.datetime(year=2003, month=6, day=17)
print(dob)