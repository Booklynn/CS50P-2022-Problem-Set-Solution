import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    if matches := re.search(r"^([1-9]|1[0-2])(?::([0-59]{2}))?\s+(AM|PM)\s+to\s+([1-9]|1[0-2])(?::([0-59]{2}))?\s+(AM|PM)$", s, re.IGNORECASE):

        form_hour = int(matches.group(1))
        form_min = matches.group(2)
        form_am_pm = matches.group(3).upper()

        to_hour = int(matches.group(4))
        to_min = matches.group(5)
        to_am_pm = matches.group(6).upper()

        if form_am_pm == "AM" and to_am_pm == "AM":
            if form_hour > to_hour:
                raise ValueError("Invalid input format")
        elif form_am_pm == "PM" and to_am_pm == "PM":
            if form_hour > to_hour:
                raise ValueError("Invalid input format")

        if form_hour == 12 and form_am_pm == "AM":
            form_hour = form_hour - 12
        if form_min is None:
            form_min = "00"
        if form_hour >= 1 and form_hour <= 11 and form_am_pm == "PM":
            form_hour = form_hour + 12

        if to_hour == 12 and to_am_pm == "AM":
            to_hour = to_hour - 12
        if to_min is None:
            to_min = "00"
        if to_hour >= 1 and to_hour <= 11 and to_am_pm == "PM":
            to_hour = to_hour + 12

        return f"{form_hour:02}:{form_min} to {to_hour:02}:{to_min}"

    raise ValueError("Invalid input format")


if __name__ == "__main__":
    main()
