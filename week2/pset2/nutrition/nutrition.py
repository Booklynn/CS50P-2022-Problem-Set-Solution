fruits = {
    'Apple': 130,
    'Avocado': 50,
    'Banana': 110,
    'Cantaloupe': 50,
    'Grapefruit': 69,
    'Honeydew Melon': 50,
    'Kiwifruit': 90,
    'Lemon': 15,
    'Lime': 80,
    'Nectarine': 60,
    'Orange': 80,
    'Peach': 60,
    'Pear': 100,
    'Pineapple': 50,
    'Plums': 70,
    'Strawberries': 50,
    'Sweet Cherries': 100,
    'Tangerine': 50,
    'Watermelon': 80
}

item = input('Item: ').title()

for fruit in fruits:
    if item == fruit:
        print('Calories:', fruits[item])