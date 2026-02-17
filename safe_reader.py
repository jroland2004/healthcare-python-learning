import csv

while True:
    file_name = input("Enter the name of the file to open: ")
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        break
    except FileNotFoundError:
        print("That is not a valid file name.")