x, y, z, = input("Expression: ").split(" ")

if y != "+" and y != "-" and y != "*" and y != "/":
    print("Please use expression: +, -, *, or /")
    exit()

print(float(eval(x + y + z)))