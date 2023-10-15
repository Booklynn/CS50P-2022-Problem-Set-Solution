import inflect

p = inflect.engine()

lyrics = "Adieu, adieu, to"
list = []

while True:
    try:
        name = input("Name: ").title()
        list.append(name)
        mylist = p.join((list))

    except EOFError:
        break

print(f"{lyrics} {mylist}")
