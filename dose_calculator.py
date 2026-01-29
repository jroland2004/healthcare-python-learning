weight_pounds = float(input("What is the patient's weight in pounds? "))
dose_by_weight = float(input("How many milligrams are ordered per kilogram? "))
medication_concentration = float(input("What is concentration available? Provide the number of milligrams availble in each milliliter. "))

#Converts punds to kilograms
pounds_to_kilo = (weight_pounds / 2.2)
dose_per_kg = (pounds_to_kilo * dose_by_weight)
dose_volume = (dose_per_kg / medication_concentration)

print(f"Based on the weight and medication concentration, your total dose is {dose_per_kg:.1f}mg and your total volume to administer is {dose_volume:.1f}mL")
