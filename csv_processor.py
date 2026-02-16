import csv
from vitals_functions import get_vitals_summary

patients = []

with open("patients.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        patient = {
            "name": row["name"], 
            "age": int(row["age"]),
            "heart_rate": int(row["heart_rate"]), 
            "systolic": int(row["systolic"]), 
            "diastolic": int(row["diastolic"]), 
            "temp": float(row["temp"]), 
            "o2_sat": float(row["o2_sat"])
        }
        assessment = get_vitals_summary(int(row["heart_rate"]), int(row["systolic"]), int(row["diastolic"]), float(row["temp"]), float(row["o2_sat"]))
        patient["hr_assessment"] = assessment["heart_rate"]
        patient["bp_assessment"] = assessment["blood_pressure"]
        patient["temp_assessment"] = assessment["temperature"]
        patient["o2_assessment"] = assessment["oxygen"]
        patients.append(patient)
        
print("--Patient Assessment Summary---")
print()
for patient in patients:
    print(f"Patient Name: {patient['name']}")
    print(f"Patient Age: {patient['age']}")
    print(f"Patient Heart Rate: {patient['heart_rate']} **{patient['hr_assessment']}**")
    print(f"Patient Blood Pressure: {patient['systolic']}/{patient['diastolic']} **{patient['bp_assessment']}**")
    print(f"Patient Temperature: {patient['temp']} **{patient['temp_assessment']}**")
    print(f"Patient Oxygen: {patient['o2_sat']} **{patient['o2_assessment']}**")
    print()