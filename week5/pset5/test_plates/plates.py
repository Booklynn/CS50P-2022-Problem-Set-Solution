def main():
    is_valid(plate)

def is_valid(s):
    len_s = len(s)

    if not s[:2].isalpha() or len(s) < 2 or len(s) > 6:
        return False

    for c in s[2:]:
        if c == '.' or c.isspace() or c == '!' or c == '0' and s[s.index(c) - 1].isalpha():
            return False

    for c in s[len_s - 2:1:-1]:
        if c.isdigit() and s[-1].isalpha():
            return False

    for c in s[len_s - 3::-1]:
        if c.isdigit() and s[-2].isalpha() and s[-1].isdigit():
            return False

    return True


if __name__ == "__main__":
    main()