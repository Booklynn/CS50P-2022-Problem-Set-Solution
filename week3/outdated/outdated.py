months =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        user_date = input("Date: ")
        if user_date[5].isdigit():
            month, day, year = user_date.strip().split("/")

            if int(month) >= 13 or int(month) <= 0 or int(day) >= 32 or int(day) <= 0:
                raise Exception()

        else:
            month, day, year = user_date.strip().split(" ")
            month = months.index(month) + 1
            day = day[:-1]
            if int(month) >= 13 or int(month) <= 0 or int(day) >= 32 or int(day) <= 0:
                raise Exception()

        print(f"{year}-{int(month):02}-{int(day):02}")
        break

    except:
        pass
