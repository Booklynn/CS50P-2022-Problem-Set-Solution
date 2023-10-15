import random

def main():
    score = 10
    level = get_level()

    for _ in range(score):
        X, Y = generate_integer(level)
        answer = X + Y

        for re_try in range(3):
            question = input(f"{X} + {Y} = ")
            if question != str(answer):
                print("EEE")
                if re_try == 2:
                    score -= 1
                    print(f"{X} + {Y} = {answer}")
            elif question == str(answer):
                break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            selected_level = int(input("Level: ").strip())
            if int(selected_level) in [1, 2, 3]:
                return selected_level

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        X = (random.randint(0, 9))
        Y = (random.randint(0, 9))
    elif level == 2:
        X = (random.randint(10, 99))
        Y = (random.randint(10, 99))
    elif level == 3:
        X = (random.randint(100, 999))
        Y = (random.randint(100, 999))

    return X, Y


if __name__ == "__main__":
    main()