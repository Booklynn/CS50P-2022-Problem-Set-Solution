def main():
    input_text = input('Input: ')
    print(shorten(input_text))


def shorten(input_text):
    str_without_vowels = ''

    for char in input_text:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            continue
        str_without_vowels += char

    return str_without_vowels


if __name__ == "__main__":
    main()