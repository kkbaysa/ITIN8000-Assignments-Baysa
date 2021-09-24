import os
import waiter as w


# Open: Restarts the main.py file and generates a new random amount of foods
def openRestaurant():
    print("Restaurant is now open.")
    os.system("python main.py")


# Lists the remaining food at the end of the night and then sets all of the values to zero
def closeRestaurant(menuList):
    for category in menuList:
        for items in menuList[category]:
            for item in items:
                items[item] = 0
    w.readMenu(menuList)
    print("The restaurant is now closed.")
