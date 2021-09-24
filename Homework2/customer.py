"""
This file contains the functions for a customer to execute.
Functions will be called by the main.py file.
functions: placeOrder(), checkOrder(), placeRandomOrder()
"""

import re
import random


# prompt for order through comma separated list
# parse through menu items and store in list
# input:    menuList -  menu with available items
#           orderInput - the comma separated string of items the customer wants to order
def placeOrder(menuList, orderInput):
    orderInput1 = orderInput.lower()
    # split the order into a list on the commas
    orderItems = re.split(', |,', orderInput1)
    checkOrder(menuList, orderItems)


# check that each item exists on the menu and that there is some in stock
# if in stock, reduce the amount available by one
# if not in stock, display error message
# prompt user if they want to order again - yes or no
# input:    menuList -  menu with available items
# output:   the status of the order
def checkOrder(menuList, orderedItems):
    inValidMenuItems = []
    # parse through every item in orderedItems
    for orderedItem in orderedItems:
        # flag for a valid item
        validItem = False
        # parse through the categories in menu
        for category in menuList:
            # parse through the items in category
            for items in menuList[category]:
                # if the orderedItem exists in the category items and is available, reduce quantity by one
                if orderedItem in items:
                    for item in items:
                        if item.__eq__(orderedItem):
                            if items[item] > 0:
                                validItem = True
                                items[item] = int(items[item]) - 1
        # if item was not found in menu, add to invalid items list
        if not validItem:
            inValidMenuItems.append(orderedItem)

    # if there are invalid items ordered, let customer know
    if len(inValidMenuItems) > 0:
        print("I'm sorry. We do not have: ")
        print(*inValidMenuItems, sep=", ")
        # prompt them to order again
        # they can either order again or leave restaurant
        orderAgain = input("Would you like to order again? (Y/N)").lower()
        if orderAgain.__eq__('y'):
            orderInput = input(
                "What would you like for your dinner? (Please separate items by a comma. Ex: Flan, Pinot Noir, Salad, Beef)")
            placeOrder(menuList, orderInput)
        elif orderAgain.__eq__('n'):
            print("I am sorry we couldn't help you. Come back again soon.")
    else:
        print("Your order has been placed.")


# generate random order with one item from each category as long as it is in stock
# reduce the amount available by one
# print the randomly generated order
# input:    menuList -  menu with available items
# output:   print the random order chosen for the customer
def placeRandomOrder(menuList):
    selectedItemInCat = ""
    randomOrder = ""
    # parse through each category in the menu and select an item as long as it is available
    for category in menuList:
        options = []
        for items in menuList[category]:
            for item in items:
                # check if item is available and add to the options list
                if items[item] > 0:
                    options.append(item)
            # if there are available items in that category, choose a random one
            if len(options) > 0:
                selectedItemInCat = random.choice(list(options))
            # reduce quantity by one
            if items[selectedItemInCat] > 0:
                items[selectedItemInCat] -= 1
        randomOrder += selectedItemInCat + '\n'
    # tell customer their random order
    print("Your order will be:")
    print(randomOrder)
