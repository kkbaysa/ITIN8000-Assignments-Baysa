# prints the entire menu with quantities
# inputs:   menuListInput - menuList to read in
# outputs:  print the entire menu with the items and quantities
def readMenu(menuList):
    print('I will read the list of menu items.\n')
    for category in menuList:
        print("For our", category, "we have: ")
        for items in menuList[category]:
            for item in items:
                print(item, ':', items[item], 'available')
        print('')


# check if that category exists
# if category exists, print menu category with items and quantities
# else print error message and prompt user to reenter the category of the menu that they want read
# inputs:   menuListInput - menuList to read in
#           categoryInput - category to search for in menuListInput
# outputs:  print the category of the menu with the items and quantities
def readMenuCategory(menuListInput, categoryInput):
    categorySearch = categoryInput.lower()
    if categorySearch in menuListInput:
        for category in menuListInput:
            if categorySearch.__eq__(category):
                print("For our", category, "we have: ")
                for items in menuListInput[category]:
                    for item in items:
                        print(item, ':', items[item], 'available')
        print('')
    else:
        print("I'm sorry. That category does not exist. Try again.")
