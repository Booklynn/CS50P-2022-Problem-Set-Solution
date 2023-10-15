import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if youtube_link := re.search(r'src="(https?://(?:www\.)?youtube\.com.+?)"', s):
        if youtube_link:
            youtube_short_link = re.sub(r"^https?://(?:www\.)?youtube\.com/", "https://youtu.be/", youtube_link.group(1))
            return youtube_short_link.replace("embed/", "")


if __name__ == "__main__":
    main()
