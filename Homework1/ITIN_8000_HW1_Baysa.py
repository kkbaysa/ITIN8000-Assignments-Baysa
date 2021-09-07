# This is my program for Homework 1 of ITIN 8000
# The program is meant to take today's date and construct the parts of the date to print out
# "Hello. Today's Date is [Month Name] [Day Number][th/nd/st/rd] of [Year].
# The product of the month and day is [Month Number * Day], which is an [Odd/Even] number.
# If you counted the days this month so far you would have
# [Loop to count up to the current day of the month with each number on a new line] days.”
# This work was done by Kaitlyn Baysa in Fall 2021.

from datetime import datetime

# Get today's date
today = datetime.now()
# Assign the month number to variable
month_number = today.month
# Assign the month name to variable
month_name = today.strftime("%B")
# Assign the day number to a variable
day_number = today.day
# Assign the year number to a variable
year_number = today.year

# Validate day to add correct suffix
# If the day is equal to 1, 21, or 31 define suffix variable as "st"
if day_number == (1 or 21 or 31):
    suffix = "st"
# If the day is equal to 2, or 22 define suffix variable as "nd"
elif day_number == (2 or 22):
    suffix = "nd"
# If the day is equal to 3, 23 define suffix variable as "rd"
elif day_number == (3 or 23):
    suffix = "rd"
# If it is any other day define suffix variable as "th"
else:
    suffix = "th"

# Determine product of day and month
# Assign product as "even" or "odd"
# If the product of day number and month number modulus of 2 is zero (it is even) and define day_type as "even"
if day_number * month_number % 2 == 0:
    day_type = "even"
# Else define product_type as "odd"
else:
    day_type = "odd"

# print the statement "Hello. Today's date is..." with variables
# include a new line
print("“Hello. Today's date is", month_name, str(day_number) + suffix, " of ", year_number, "\b."
      " The product of the month and day is " + str(month_number * day_number) + ", which is an " + day_type + " number.\n")

# create list of days with range
numDays = list(range(1, day_number+1))
# print the statement "If you counted..." with the list of days
print("If you counted the days this month so far you would have", numDays, "day(s).")
