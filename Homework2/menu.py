import random



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
                'chocolate moose': random.randint(1, 3),
                'cheesecake': random.randint(1, 3)
            }
        ]
    }
