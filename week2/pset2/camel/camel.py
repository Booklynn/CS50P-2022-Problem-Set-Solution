text = input('camelCase: ')

for char in text:
    if char.isupper():
        print('_' + char.lower(), end="")
    else:
        print(char, end="")

print()