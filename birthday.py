# Created by Daniel Sanchez
# August 24, 2020
# Reads through .txt file and emails specified user if it is somebody's birthday

#Imports datetime package to check the current date
import datetime
#Imports smtplib and ssl packages for sending emails
import smtplib, ssl

#Gets the current day and month
complete_time = datetime.datetime.now()
current_day = str(complete_time.day)
current_month = str(complete_time.month)

#Ensures the day and month are properly formatted
if len(current_day) == 1:
    current_day = '0' + current_day
if len(current_month) == 1:
    current_month = '0' + current_month
today = current_month + current_day

#Reads from file
FILE_NAME = "testBirthdays.txt"
readFile = open(FILE_NAME, 'r')
lines = readFile.readlines()

#Checks if there is a birthday today
birthdays = []
for i in lines:
    if i[:4] == today:
        birthdays.append(i)

#Stores today's birthdays in arrays
birthyear = []
names = []
for i in birthdays:
    data = i.split("\t")
    birthyear.append(int(data[1]))
    names.append(data[2][:len(data[2]) - 1])

#Gets ages of people with a birthday
age = []
for i in birthyear:
    age.append(int(complete_time.year) - i)

#Sends email to specified user with birthday information
port = 465
smtp_server = "smtp.gmail.com"
sender_email        #ADD YOUR THE SENDER EMAIL ADDRESS
reciever_email      #ADD THE RECIEVER EMAIL ADDRESS
password = ""       #ADD THE PASSWORD TO YOUR EMAIL

context = ssl.create_default_context()

message = """\
        Subject: Birthday Today!!!
        """

for i in range(len(names)):
    message = "\n" + message + names[i] + " is " + str(age[i]) + " today! \n"

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, message)


