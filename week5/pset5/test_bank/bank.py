def main():
    greeting = input("Greeting: ")
    print(value(greeting))

def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting[0] == ('h'):
        return 20
    return 100

if __name__ == "__main__":
    main()