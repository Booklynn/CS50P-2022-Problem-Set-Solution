import sys
import csv

len_argv = len(sys.argv)

if len_argv < 3:
    print("Too few command-line arguments")
    sys.exit(1)

if len_argv > 3:
     print("Too many command-line arguments")
     sys.exit(1)

if not sys.argv[1].endswith(".csv"):
    print("Not a CSV file")
    sys.exit(1)

try:
    data_to_write = []
    with open(sys.argv[1]) as existing_file:
        csv_reader = csv.DictReader(existing_file)
        for row in csv_reader:
                last, first = row['name'].split(', ', 1)
                house = row['house']
                data_to_write.append({'first': first, 'last': last, 'house': house})

        fieldnames = ['first', 'last', 'house']
        with open(sys.argv[2], mode='w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(data_to_write)

    sys.exit(0)


except FileNotFoundError:
    print(f"Could not read {sys.argv[1]}")
    sys.exit(1)