# This project is an alarm clock that allows the user to enter the number
# of hours they would like to sleep for. The script will then take the
# current time, add the hours and at the right time, a song will randomly
# be selected to open on a browser and play at the correct time.

# How to get current time: http://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/
# How to pause execution momentarily: http://pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/

import random, webbrowser, datetime, time
from datetime import datetime, timedelta

url1 = "https://www.youtube.com/watch?v=y6Sxv-sUYtM"
url2 = "https://www.youtube.com/watch?v=pRpeEdMmmQ0"
url3 = "https://www.youtube.com/watch?v=OPf0YbXqDm0"
url4 = "https://www.youtube.com/watch?v=09R8_2nJtjg"

Time = time.strftime("%H:%M:%S")

print("")
print ("Currently it is:", Time)
minutes_of_sleep = int(input("Enter the number of minutes you would like to sleep for:"))
hours_of_sleep = int(input("Enter the number of hours you would like to sleep for:"))
print("")

Alarm = (datetime.now() + timedelta(hours=hours_of_sleep) + timedelta(minutes=minutes_of_sleep)).strftime('%H:%M:%S')
print("You will be woken up at:", Alarm)
yes_no = str(input("Would you like to set this alarm? [Y/N]")).lower()
print("")

while yes_no == "y" or yes_no == "yes":

    while Time != Alarm:
        print("It is currently:", time.strftime("%H:%M:%S"))
        Time = time.strftime("%H:%M:%S")
        time.sleep(1)
        if Time == Alarm:
            print("")
            print("Time to wake up!")
            url = random.choice([url1, url2, url3, url4])
            webbrowser.open(url)
            break

# The motivation behind this quick script was to help all you out there who
# have trouble waking up on time for things.
# Funny story: I slept 1.25hrs into my 3rd exam in 1st year, 1st semester.
# It wasn't a complete shipwreck because I slept into Linear Algebra which
# I was apparently good at because my mark only went up after that exam.
# Shout out to my TA, David Abou Chacra, and housemate, Bhavya Shah @bhavyata9
