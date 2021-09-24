"""
    menuList() function creates a dictionary of the different menu categories with the key as the category
    and the value as another dictionary with the key being the food and the value being
    the quantity of that food:
    Assign a random value of the item based on the given ranges:
        Entrees (1-6): chicken, beef, vegetarian
        Sides (5-10): soup, salad
        Wines (2-5): merlot, chardonnay, pinot noir, rose
        Desserts (1-3): flan, creme brulee, chocolate moose, cheesecake
"""

import random


# output: returns dictionary of menu items with the random number generated
def menuList():
    return {
        'entrees': [
            {
                'chicken': random.randint(1, 6),
                'beef': random.randint(1, 6),
                'vegetarian': random.randint(1, 6)
            }
        ],
        'sides': [
            {
                'soup': random.randint(5, 10),
                'salad': random.randint(5, 10)
            }
        ],
        'wines': [
            {
                'merlot': random.randint(2, 5),
                'chardonnay': random.randint(2, 5),
                'pinot noir': random.randint(2, 5),
                'rose': random.randint(2, 5)
            }
        ],
        'desserts': [
            {
                'flan': random.randint(1, 3),
                'creme brulee': random.randint(1, 3),
                'chocolate mouse': random.randint(1, 3),
                'cheesecake': random.randint(1, 3)
            }
        ]
    }
