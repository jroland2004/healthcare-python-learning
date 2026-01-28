weight_pounds = float(input("How much do you weight in pounds? "))
height_inches = float(input("How tall are you in inches? "))
pounds_to_kilo = weight_pounds * 0.453592
inches_to_meters = height_inches * 0.0254
bmi = pounds_to_kilo/ (inches_to_meters ** 2)

print(f"If your weight is {weight_pounds} pounds and your height is {height_inches} inches, your BMI is {bmi:.1f}")