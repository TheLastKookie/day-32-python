import os
import random
import smtplib
import pandas as pd
from datetime import datetime
# Automated Birthday Wisher
# Make sure to update the birthdays.csv file with your friends and family's birthdays as shown by the test input
# Also make sure to change the letter templates to end with your name
# Fill in your email and password
MY_EMAIL = ""
MY_PASSWORD = ""

today = (datetime.now().month, datetime.now().day)

birthday_df = pd.read_csv("birthdays.csv")
birthday_data = birthday_df.to_dict(orient="records")
for birthday in birthday_data:
    if (birthday["month"], birthday["day"]) == today:
        name = birthday["name"]
        template_letter = random.choice(os.listdir("./letter_templates"))
        with open("./letter_templates/" + template_letter) as starting_letter:
            contents = starting_letter.read()
            contents = contents.replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday["email"],
                msg=f"Subject:Happy Birthday!!\n\n{contents}"
            )
