import random

while True:
    try:
        lvl = int(input("Level: "))
        if lvl >= 1:
            n = random.randint(1, lvl)
            break
    except:
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if guess >= 1:
            if guess > n:
                print("Too large!")
            elif guess < n:
                print("Too small!")
            else:
                print("Just right!")
                break
    except:
        pass
