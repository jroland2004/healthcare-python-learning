patients = []

while True:

    name = input("Enter patient's full name (or 'done' to finish): ")
    if name == 'done':
        break

    heart_rate = int(input("Enter patient's heart rate: "))
    temp = float(input("Enter patient's temperature: "))

    patient = {
        "name": name,
        "heart_rate": heart_rate,
        "temperature": temp
    }

    patients.append(patient)

print("--- Patient Summary ---")
print(f"Total number of patinets in queue: {len(patients)}")

for patient in patients:  
    if patient["heart_rate"] < 60:
        hr_flag = ("**Bradycardia**")
    elif patient["heart_rate"] > 100:
        hr_flag = ("**Tachycardia**")
    else:
        hr_flag = ("")
    if patient["temperature"] > 100.4:
        temp_flag = ("**Fever**")
    else:
        temp_flag = ("")
    print(f"Patient: {patient['name']}")
    print(f"HR: {patient['heart_rate']} {hr_flag}")
    print(f"Temp: {patient['temperature']} {temp_flag}")
    print("")

   


 