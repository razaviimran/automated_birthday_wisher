from datetime import datetime
import pandas
import random
import smtplib

myEmail = "youremailhere"
myPass = "yourpasswordhere"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letters_templates/letter_{random.randint(1, 2)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(myEmail, myPass)
        connection.sendmail(
            from_addr=myEmail,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!!!\n\n{contents}"
        )
