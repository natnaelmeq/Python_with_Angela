import smtplib
import datetime as dt
import random

import random

my_email = "natnael@gmail.com"
password = "1234566"  # we have to use app password because of security not allowed to use normal password

now = dt.datetime.now()

weekday = now.weekday(0)
print(weekday)
# #0= monday,1=Tuesday,2 wedensday....
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # this helps to secure the message
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="amen@gmail.com",
                            msg=f"Subject:Monday Motivation\n\nt{quote}")
