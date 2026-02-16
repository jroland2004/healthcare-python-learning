import json
import csv
from vitals_functions import get_vitals_summary

patients = []

with open("patients.csv", "r") as file:
     reader = csv.DictReader(file)
     for row in reader:
        patient = {
            "name": row["name"], 
            "age": int(row["age"]),
            "vitals": {
                "heart_rate": int(row["heart_rate"]), 
                "systolic": int(row["systolic"]), 
                "diastolic": int(row["diastolic"]), 
                "temp": float(row["temp"]), 
                "o2_sat": float(row["o2_sat"])
         }
        }
        assessment = get_vitals_summary(
            patient["vitals"]["heart_rate"],
            patient["vitals"]["systolic"],
            patient["vitals"]["diastolic"],
            patient["vitals"]["temp"],
            patient["vitals"]["o2_sat"],
            
        )
        patient['assessments'] = assessment
        patients.append(patient)

with open("patient_records.json", "w")as file:
    json.dump(patients, file, indent=2)

with open("patient_records.json", "r") as file:
    data = json.load(file)
    print("--Patient Assessment Summary---")
    print()
    for patient in data:
        print(f"Patient Name: {patient['name']}")
        print(f"Patient Age: {patient['age']}")
        print(f"Patient Heart Rate: {patient['vitals']['heart_rate']} **{patient['assessments']['heart_rate']}**")
        print(f"Patient Blood Pressure: {patient['vitals']['systolic']}/{patient['vitals']['diastolic']} **{patient['assessments']['blood_pressure']}**")
        print(f"Patient Temperature: {patient['vitals']['temp']} **{patient['assessments']['temperature']}**")
        print(f"Patient Oxygen: {patient['vitals']['o2_sat']} **{patient['assessments']['oxygen']}**")
        print()