"""
This file contains the functions for a manager to execute.
Functions will be called by the main.py file.
functions: openRestaurant(), closeRestaurant()
"""

import os
import waiter as w


# Open: Restarts the main.py file and generates a new random amount of foods
# output: notify that the restaurant is open
def openRestaurant():
    print("Restaurant is now open.")
    os.system("python main.py")


# Lists the remaining food at the end of the night and then sets all of the values to zero
# input: menu with items and quantities
# output: notify that the restaurant is closed
def closeRestaurant(menuList):
    # parse through every item in each category and set the quantity to 0
    for category in menuList:
        for items in menuList[category]:
            for item in items:
                items[item] = 0
    w.readMenu(menuList)
    print("The restaurant is now closed.")
