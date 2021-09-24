import re
import random


# prompt for order through comma separated list
# parse through menu items and store in list
def placeOrder(menuList, orderInput):
    orderInput1 = orderInput.lower()
    orderItems = re.split(', |,', orderInput1)
    checkOrder(menuList, orderItems)


# check that each item exists on the menu and that there is some in stock
# if in stock, reduce the amount available by one
# if not in stock, display error message
# prompt user if they want to order again - yes or no
def checkOrder(menuList, orderedItems):
    for orderedItem in orderedItems:
        for category in menuList:
            for items in menuList[category]:
                if orderedItem in items:
                    # print("This exists!")
                    for item in items:
                        if item.__eq__(orderedItem):
                            if items[item] > 0:
                                items[item] = int(items[item]) - 1
                            else:
                                print(item, 'not available.')
                                orderAgain = input("Would you like to order again? (Y/N)").lower()
                                if orderAgain.__eq__('y'):
                                    orderInput = input(
                                        "What would you like for your dinner? (Please separate items by a comma. Ex: Flan, Pinot Noir, Salad, Beef)")
                                    placeOrder(menuList, orderInput)
                                elif orderAgain.__eq__('n'):
                                    print("I am sorry we couldn't help you. Come back again soon.")


# generate random order with one item from each category as long as it is in stock
# reduce the amount available by one
# print the randomly generated order
def placeRandomOrder(menuList):
    randomOrder = ""
    for category in menuList:
        options = []
        for items in menuList[category]:
            for item in items:
                if items[item] > 0:
                    options.append(item)
            if len(options) > 0:
                selectedItemInCat = random.choice(list(options))
            if items[selectedItemInCat] > 0:
                items[selectedItemInCat] -= 1
        randomOrder += selectedItemInCat + '\n'
    print("Your order will be:")
    print(randomOrder)
