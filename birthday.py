# Created by Daniel Sanchez
# August 24, 2020
# Reads through .txt file and emails specified user if it is somebody's birthday

#Imports datetime package to check the current date
import datetime

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

print(today)

