input_text = input('Input: ')

for char in input_text:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        continue
    print(char, end='')

print()