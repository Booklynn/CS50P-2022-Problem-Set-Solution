def main():
    s = input()
    emoji = convert(s)
    print(emoji)

def convert(s):
    if ":)" or ":(" in s:
        s = s.replace(":)", "🙂")
        emoji = s.replace(":(", "🙁")
        return emoji

main()