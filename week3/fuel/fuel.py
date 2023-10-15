while True:
    fuel = input("Fraction: ")
    try:
       num, denom = fuel.split("/")
       if (int(num) / int(denom)) <= 1:
           break
    except (ValueError, ZeroDivisionError):
        pass

if ((int(num) / int(denom)) * 100) <= 1:
    print("E")
elif ((int(num) / int(denom)) * 100) >= 99:
    print("F")
else:
    print(f"{round((int(num) / int(denom)) * 100)}%")