import sys
from tabulate import tabulate
import csv


len_argv = len(sys.argv)

if len_argv < 2:
    print("Too few command-line arguments")
    sys.exit(1)

if len_argv > 2:
     print("Too many command-line arguments")
     sys.exit(1)

if not sys.argv[1].endswith(".csv"):
    print("Not a CSV file")
    sys.exit(1)
    
try:
    with open(sys.argv[1]) as csv_file:
        reader = csv.reader(csv_file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))

    sys.exit(0)

except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)