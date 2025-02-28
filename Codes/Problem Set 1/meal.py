# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

# Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

# If up for a challenge, optionally add support for 12-hour times, allowing the user to input times in these formats too:

#   #:## a.m. and ##:## a.m.
#   #:## p.m. and ##:## p.m.

import re

def main():
    
    time = input("What time is it? ")
    
    time = convert(time)

# For Time between 7:00 and 8:00
    if time >= 7 and time <= 8:
        print("breakfast time")

# For Time between 12:00 and 13:00
    elif time >= 12 and time <=13:
        print("lunch time")

# For Time between 18:00 and 19:00
    elif time >= 18 and time <=19:
        print("dinner time")

    else:
        return 0



def convert(time):
    

# For 12 hour clock, based on multiple delimiter ":" & " "
    if "a.m." in time or "p.m." in time:
        hours, minutes, post = re.split(r"[: ]", time)
        if post == "p.m.":
            hours = int(hours) + 12
            
# For 24 hours, based on single delimiter
    else:
        hours, minutes = time.split(":")

    new_minutes = float(minutes) / 60

    new_time = float(hours) + new_minutes

    return new_time


if __name__ == "__main__":
    main()