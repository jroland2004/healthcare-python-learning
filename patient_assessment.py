from clinical_functions import convert_to_kg, convert_to_m, calculate_bmi, classify_bmi
from vitals_functions import get_vitals_summary

patient_name = input("Enter patient's name: ")
patient_weight = float(input("Enter patient's weight in pounds: "))
patient_height = float(input("Enter patient's height in inches: "))
hr = int(input("Enter the patient's heart rate: "))
systolic = int(input("Enter the patient's systolic blood pressure: "))
diastolic = int(input("Enter the patient's diastolic bloos pressure: "))
temp = float(input("Enter patient's temperature: "))
o2_sat = int(input("Enter the patient's oxygen saturation: "))

weight_kg = convert_to_kg(patient_weight)
height_m = convert_to_m(patient_height)
bmi = calculate_bmi(weight_kg, height_m)
bmi_class = classify_bmi(bmi)

vitals = get_vitals_summary(hr, systolic, diastolic, temp, o2_sat)

print("---Patinet Summary---")
print(f"Patinet Name: {patient_name}")
print("BMI:")
print(f"Patient's BMI is {bmi:.1f}. Patient's BMI classification is {bmi_class}")
print("Vitals:")
for vital, result in vitals.items():
    print(f" {vital}: {result}")