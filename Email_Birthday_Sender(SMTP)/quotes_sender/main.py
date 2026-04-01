import random
import smtplib
import  datetime as dt

my_email = "12639@holbertonstudents.com"
password =  "kzxi qxkq diok cxkz"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="aismayilzada19980@ada.edu.az", msg=f"Subject:Motivation \n\n { quote}")



