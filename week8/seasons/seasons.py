from datetime import date
import inflect
import sys


def main():
    print(convert(input("Date of Birth: ")))


def convert(date_of_birth):
    try:
        parsed_date_of_birth = date.fromisoformat(date_of_birth)
        difference = date.today() - parsed_date_of_birth
        minutes = difference.days * 24 * 60

        p = inflect.engine()
        return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"

    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
