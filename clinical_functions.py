

def convert_to_kg(weight_in_lbs):
    weight_kg = weight_in_lbs/2.2
    return weight_kg

def convert_to_m(height_in_in):
    height_m = height_in_in * 0.0254
    return height_m

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        bmi_flag = "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        bmi_flag = "Normal"  
    elif bmi >= 25 and bmi <= 29.9:
        bmi_flag = "Overweight"
    else:
        bmi_flag = "Obese"
    return bmi_flag


patient_weight = float(input("Enter patient's weight in pounds: "))
patient_height = float(input("Enter patient's height in inches: "))

weight_kg = convert_to_kg(patient_weight)
height_m = convert_to_m(patient_height)
bmi = calculate_bmi(weight_kg, height_m)
bmi_class = classify_bmi(bmi)


print(f"Patient's BMI is {bmi:.1f}. Patient's BMI classification is {bmi_class}")
