from datetime import datetime 
import pandas
import random
import smtplib

myEmail = "imran05081991@gmail.com"
myPass = "123@123@321"

today = (datetime.now().month,datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
  birthday_person = birthday_dict[today]
  file_path = f"letters_template/letters_{random.randint(1,4)}.txt"
  with open(file_path) as letter_file:
    content = letter_file.read()
    content = content.replace("[NAME]", birthday_person["name"])

  with smtplib.SMTP("smtp.gmail.com", 573) as connection:
    connection.starttls()
    connection.login(myEmail, myPass)
    connection.sendmail(
      from_addr=myEmail,
      to_addrs=birthday_person["email"],
      msg=f"Subject:Happy Birthday {birthday_person['name']}\n\n{content}"
    )
