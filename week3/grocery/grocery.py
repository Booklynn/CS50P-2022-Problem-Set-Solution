items = {}

while True:
    try:
        user_item = input().upper()
        items[user_item] = items.get(user_item, 0) + 1

    except EOFError:
        break

for item in sorted(items.keys()):
    print(items[item], item)