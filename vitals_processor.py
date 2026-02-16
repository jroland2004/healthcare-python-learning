from vitals_functions import get_vitals_summary

patients = []

with open('vitals_log.txt', 'r') as file:
    for line in file:
        content = line.strip()
        name, heart_rate, systolic, diastolic, temp, o2_sat = content.split(", ")
        patient = {
            "name": name, 
            "heart_rate": int(heart_rate), 
            "systolic": int(systolic), 
            "diastolic": int(diastolic), 
            "temp": float(temp), 
            "o2_sat": float(o2_sat)
        }
        assessment = get_vitals_summary(int(heart_rate), int(systolic), int(diastolic), float(temp), float(o2_sat))
        patient["hr_assessment"] = assessment["heart_rate"]
        patient["bp_assessment"] = assessment["blood_pressure"]
        patient["temp_assessment"] = assessment["temperature"]
        patient["o2_assessment"] = assessment["oxygen"]
        
        patients.append(patient)



print(f"Total Number of Patient: {len(patients)}")
print()
print()
for patient in patients:
    print(f"--Patient Name: {patient['name']}")
    print(f"Heart Rate: {patient['heart_rate']} - {patient['hr_assessment']}")
    print(f"Blood Pressure: {patient['systolic']}/{patient['diastolic']} - {patient["bp_assessment"]}")
    print(f"Temperature: {patient['temp']} - {patient["temp_assessment"]}")
    print(f"Oxygen Saturation: {patient['o2_sat']} - {patient["o2_assessment"]}")
    print()