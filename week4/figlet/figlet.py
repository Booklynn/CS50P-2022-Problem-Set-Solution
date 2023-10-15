from pyfiglet import Figlet
import sys

figlet = Figlet()

if len(sys.argv) != 3:
    print("Invalid usage")
    sys.exit(1)

elif sys.argv[1] != "-f":
    print("Invalid usage")
    sys.exit(1)

elif not sys.argv[2] in figlet.getFonts():
    print("Invalid usage")
    sys.exit(1)

user_input = input().strip()

figlet.setFont(font=sys.argv[2])

print(figlet.renderText(user_input))