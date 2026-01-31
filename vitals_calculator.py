
heart_rate = int(input("Enter the patient's heart rate: "))
systolic_bp = int(input("Enter the patient's systolic blood pressure: "))
diastolic_bp = int(input("Enter the patient's diastolic bloos pressure: "))
oxygen_sat = int(input("Enter the patient's oxygen saturation: "))
patient_temp = float(input("Enter patient's temperature: "))



if heart_rate < 60:
    heart_rate_dx = "Bradycardia"
elif heart_rate > 100:
    heart_rate_dx = "Tachycardia"
else:
    heart_rate_dx = "Normal"

if systolic_bp < 90 or diastolic_bp < 60:
   blood_pressure_dx = "Hypotensive"
elif systolic_bp > 140 or diastolic_bp > 90:
    blood_pressure_dx = "Hypertensive"
else:
    blood_pressure_dx = "Normal BP"

if oxygen_sat < 92:
   oxygen_sat_dx = "Critical - supplement oxygen"
elif oxygen_sat >= 95:
    oxygen_sat_dx = "Normal"
else:
    oxygen_sat_dx = "Low - monitor closely"

if patient_temp < 97.0:
   temperature_dx = "Hypothermia"
elif patient_temp > 100.3:
    temperature_dx = "Fever"
elif patient_temp >= 99.1:
    temperature_dx = "Low-grade fever"
else:
    temperature_dx = "Normal"


print(f"--- Vital Signs Summary ---\nHeart Rate: {heart_rate_dx}\nBlood Pressure: {blood_pressure_dx}\nO2 Saturation: {oxygen_sat_dx}\nTemperature: {temperature_dx}")


