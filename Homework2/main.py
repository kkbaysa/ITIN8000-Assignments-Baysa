""" The project should simulate the operation of a restaurant.
When I run main.py it should start by randomly generating a quantity
for each of the menu items in the restaurant.
These quantities will have to go down when customers order the menu items.
Each customer order can contain an Entree, Side, Wine, and a Dessert.
This work has been done by Kaitlyn Baysa during Fall 2021 in ITIN8000
"""

### In menu.py ###
# menuList() function creates a dictionary of the different menu categories with the key as the category
# and the value as another dictionary with the key being the food and the value being
# the quantity of that food:
# Assign a random value of the item based on the given ranges
# Entrees (1-6): chicken, beef, vegetarian
# Sides (5-10): soup, salad
# Wines (2-5): merlot, chardonnay, pinot noir, rose
# Desserts (1-3): flan, creme brulee, chocolate moose, cheesecake
# create flag for the role that will stay false until it is valid

### In main.py ###
# loop that allows system to continuously run an take input

# store menu items from the menuList() in menu.py

#flag for valid Role initialized to false - will be flagged as true with a valid role

# Prompt user for a valid role
# if role is invalid, prompt until it is valid
# Store role

# if role is waiter, prompt for an action: 1 - read menu; 2 - read section of menu
    # if 1 print menu items
    # else if 2 prompt user for menu category that they want (Entrees/Wines/Sides/Desserts)
        # check if that category exists
        # if category exists, print menu category with items and quantities
        # else print error message and prompt user to reenter the category of the menu that they want read

# else if role is customer, prompt for an action: 1 - order items; 2 - random order
    # if 1, prompt for order through comma separated list
        # parse through menu items and store in list
        # check that each item exists on the menu and that there is some in stock
        # if in stock, reduce the amount available by one
        # if not in stock, display error message
    # if 2 generate random order with one item from each category as long as it is in stock
        # reduce the amount available by one
        # print the randomly generated order

# else if role is manager, prompt for an action: 1 - open; 2 - close
    # if 1, restart the most outer loop to generate new menu
        # print new menu of foods and quantities
    # if 2, print list of remaining food at the end of the night in list and set all values to zero
