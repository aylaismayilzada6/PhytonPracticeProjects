import smtplib

my_email = "12639@holbertonstudents.com"
password =  "kzxi qxkq diok cxkz"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="elza9mail@gmail.com", msg="Subject: Hello \n\n Zdorova bratva")
