

name = input("Enter patient's name: ")
      
while True:
    
    try:
        age = int(input("Enter patient's age: "))
        break
    except ValueError:
        print("Invalid age. Please enter a number.")
while True:
    try:
        temp = float(input("Enter patient's temperature: "))
        break
    except ValueError:
        print("Invalid temperature. Please enter a number.")

print("--Patient Summary--")
print()
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Temperature: {temp}")
