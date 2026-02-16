patients = []

while True:
    name = input("Enter patient's name: ")
    if name == "done":
        break
    age = int(input("Enter patient's age: "))
    diagnosis = input("Enter patient's diagnosis: ")

    with open("patient_log.txt", "a") as file:
        file.write(f"{name}, {age}, {diagnosis}\n")

with open("patient_log.txt", "r") as file:
    for line in file:
        content = line.strip()

        name, age, diagnosis = content.split(", ")
        patient = {
            "name": name,
            "age": age,
            "diagnosis": diagnosis
        }
        patients.append(patient)

print("---Patient Summary--")
print()        
for patient in patients:
    print(f"Patient Name: {patient["name"]}")
    print(f"Patient Age: {patient["age"]}")
    print(f"Patient Diagnosis: {patient["diagnosis"]}")
    print()