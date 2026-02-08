
def assess_heart_rate(hr):
    if hr < 60:
        heart_rate_dx = "Bradycardia"
    elif hr > 100:
        heart_rate_dx = "Tachycardia"
    else:
        heart_rate_dx= "Normal"
    return heart_rate_dx

def assess_blood_pressure(systolic, diastolic):
    if systolic < 90 or diastolic < 60:
        blood_pressure_dx = "Hypotensive"
    elif systolic > 140 or diastolic > 90:
        blood_pressure_dx = "Hypertensive"
    else:
        blood_pressure_dx = "Normal BP"
    return blood_pressure_dx

def assess_temperature(temp):
    if temp < 97.0:
       temperature_dx = "Hypothermia"
    elif temp > 100.3:
       temperature_dx = "Fever"
    elif temp >= 99.1:
       temperature_dx = "Low-grade fever"
    else:
       temperature_dx = "Normal"    
    return temperature_dx

def assess_oxygen(o2_sat):
    if o2_sat < 92:
      oxygen_sat_dx = "Critical - supplement oxygen"
    elif o2_sat >= 95:
      oxygen_sat_dx = "Normal"
    else:
      oxygen_sat_dx = "Low - monitor closely"
    return oxygen_sat_dx

def get_vitals_summary(hr, systolic, diastolic, temp, o2_sat):
    vitals_summary = {
        "heart_rate": assess_heart_rate(hr),
        "blood_pressure": assess_blood_pressure(systolic, diastolic),
        "temperature": assess_temperature(temp),
        "oxygen": assess_oxygen(o2_sat)
    }
    return vitals_summary


hr = int(input("Enter the patient's heart rate: "))
systolic = int(input("Enter the patient's systolic blood pressure: "))
diastolic = int(input("Enter the patient's diastolic bloos pressure: "))
temp = float(input("Enter patient's temperature: "))
o2_sat = int(input("Enter the patient's oxygen saturation: "))

patient_vital_summary = get_vitals_summary(hr, systolic, diastolic, temp, o2_sat)


print("---Patient's Vital Summary---")
for vital, result in patient_vital_summary.items():
    print(f" {vital}: {result}")