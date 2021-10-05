"""
Homework 3 part 1 will create a python script that collects input from a user.
The user's information will be stores in a UserName.txt file.
The user's age will be stores in a binary file DaysOld.txt.
It will then read those files back.
This assignment was completed by Kaitlyn Baysa during Fall2021 - ITIN8000
"""

from datetime import datetime, date
import csv

# Ask for the users first and last name, favorite color, and date of birth
fName = str(input('Enter your first name: '))
lName = str(input('Enter your last name: '))
favColor = str(input('Enter your favorite color: '))
dobValid = False
dob = ''
# validate date format as MM/DD/YYYY
while not dobValid:
    dobInput = str(input('Enter your date of birth (MM/DD/YYYY): '))
    try:
        dob = datetime.strptime(dobInput, '%m/%d/%Y')
        dobValid = True
    except ValueError:
        dobValid = False
        print("Incorrect data format - should be MM/DD/YYYY")

# Calculate how many days old the user is
# Write the user's age in days to a binary file named DaysOld.txt
dob = date(dob.year, dob.month, dob.day)
today = date(date.today().year, date.today().month, date.today().day)
daysOld = int((today - dob).days)
with open("DaysOld.txt", "wb") as fileOut:
    fileContent = bytes(daysOld)
    fileOut.write(fileContent)
    fileOut.close()

# Write the user's name in the format last name, first name and favorite color in UserName.txt
with open("UserName.txt", "wt") as fileOut:
    fileContent = "Last Name: " + lName + "\nFirst Name: " + fName + "\nFavorite Color: " + favColor
    fileOut.write(fileContent)
    fileOut.close()

# Add the user to a CSV file named UserData.csv in the order Last Name, First Name, Favorite Color, Days Old
with open("UserData.csv", "at") as csvOut:
    entry = [lName, fName, favColor, str(daysOld)]
    csvWriter = csv.writer(csvOut)
    csvWriter.writerow(entry)
    csvOut.close()

# read back UserName.txt
print("\n--- Reading UserName.txt --- ")
with open("UserName.txt", "rt") as fileIn:
    lines = fileIn.readlines()
    for line in lines:
        print(line.replace("\n", ""))
fileIn.close()

# read back DaysOld.txt
print("\n--- Reading DaysOld.txt ---")
with open("DaysOld.txt", "rb") as fileIn:
    print(len(fileIn.read()))
fileIn.close()

# read back UserData.csv
print("\n--- Reading UserData.csv ---")
with open("UserData.csv", "rt") as fileIn:
    data = fileIn.readlines()
    for line in data:
        print(line.replace("\n", ""))
fileIn.close()
