patient_record = {
    "name": "Jason Roland",
    "age": 43,
    "room_number": 210
}

patient_record["heart_rate"] = int(input("Enter patient's heart rate: "))
patient_record["systolic_bp"] = int(input("Enter patient's systolic blood pressure: "))
patient_record["diastolic_bp"] = int(input("Enter patient's diastolic blood pressure: "))
patient_record["patient_temp"] = float(input("Enter patient's temperature: "))

print("--- Patient Record ---")
for key, value in patient_record.items():
    print(f"{key}: {value}")