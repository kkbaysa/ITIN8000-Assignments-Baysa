""" The project should simulate the operation of a restaurant.
When I run main.py it should start by randomly generating a quantity
for each of the menu items in the restaurant.
These quantities will have to go down when customers order the menu items.
Each customer order can contain an Entree, Side, Wine, and a Dessert.
This work has been done by Kaitlyn Baysa during Fall 2021 in ITIN8000
"""

import menu as m
import waiter as w
import customer as c
import manager as ma

# store menu items from the menuList() in menu.py
menuList = m.menuList()
restaurantOpen = True

# loop that allows system to continuously run an take input
while True:
    # flag for valid Role initialized to false - will be flagged as true with a valid role
    role = False

    # Prompt user for a valid role
    # if role is invalid, prompt until it is valid
    while not role:
        # Store role
        roleInput = input(
            "\nEnter your role (Enter \"W\" for Waiter, \"C\" for Customer, and \"M\" for Manager): ").lower()
        actionValid = False
        # if role is waiter, prompt for an action: 1 - read menu; 2 - read section of menu
        if roleInput.__eq__("w"):
            # set role flag to true
            role = True
            print("1: Read Menu\n2: What are the (entrees/wines/sides/desserts)")
            # prompt for waiter action
            while not actionValid:
                actionInput = input("Enter the number of the action: ")
                # if 1 print menu items
                if actionInput.__eq__('1'):
                    actionValid = True
                    # call readMenu() from waiter.py which prints the entire menu with quantities
                    w.readMenu(menuList)
                # else if 2 prompt user for menu category that they want (Entrees/Wines/Sides/Desserts)
                elif actionInput.__eq__('2'):
                    actionValid = True
                    # flag for valid category search set to false
                    validCategory = False
                    # continue to ask for the category until a valid one is entered
                    while not validCategory:
                        # prompt user for category to read from menu
                        categoryInput = input(
                            "Enter the name of the category that you want to see (entrees, sides, wines, desserts): ")
                        # validate that the category is valid
                        if categoryInput in menuList:
                            # set flag to true
                            validCategory = True
                            # call readMenuCategory() from waiter.py
                            w.readMenuCategory(menuList, categoryInput)
                        else:
                            print("\nInvalid category.")

        # else if role is customer, prompt for an action: 1 - order items; 2 - random order
        elif roleInput.__eq__("c"):
            role = True
            print("1: Order Items\n2: Random Order")
            while not actionValid:
                actionInput = input("Enter the number of the action: ")
                # if 1, have customer place order through comma separated list
                if actionInput.__eq__('1'):
                    actionValid = True
                    if restaurantOpen:
                        orderInput = input("What would you like for your dinner? (Please separate items by a comma. Ex: Flan, Pinot Noir, Salad, Beef)")
                        actionValid = True
                        c.placeOrder(menuList, orderInput)
                    else:
                        print("Sorry you can't order right now while the restaurant is closed.")
                # if 2 generate random order with one item from each category as long as it is in stock
                elif actionInput.__eq__('2'):
                    actionValid = True
                    if restaurantOpen:
                        c.placeRandomOrder(menuList)
                    else:
                        print("Sorry you can't order right now while the restaurant is closed.")

        # else if role is manager, prompt for an action: 1 - open; 2 - close
        elif roleInput.__eq__("m"):
            role = True
            print("1: Open Restaurant\n2: Close Restaurant")
            while not actionValid:
                actionInput = input("Enter the number of the action: ")
        # if 1, restart the most outer loop to generate new menu and print new menu of foods and quantities
                if actionInput.__eq__('1'):
                    actionValid = True
                    restaurantOpen = True
                    ma.openRestaurant()
        # if 2, print list of remaining food at the end of the night in list and set all values to zero
                if actionInput.__eq__('2'):
                    actionValid = True
                    restaurantOpen = False
                    ma.closeRestaurant(menuList)
