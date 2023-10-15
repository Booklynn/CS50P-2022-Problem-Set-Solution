import sys

len_argv = len(sys.argv)

if len_argv < 2:
    print("Too few command-line arguments")
    sys.exit(1)

if len_argv > 2:
     print("Too many command-line arguments")
     sys.exit(1)

if not sys.argv[1].endswith(".py"):
    print("Not a Python file")
    sys.exit(1)

line_count = 0

try:
    with open(sys.argv[1]) as my_file:
        for line in my_file:
            line = line.lstrip()
            if line.startswith("#") or not line:
                continue
            line_count += 1
    print(line_count)
    sys.exit(0)

except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)