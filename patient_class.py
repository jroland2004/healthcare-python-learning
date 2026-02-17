class Patient:
    def __init__(self, name, age, diagnosis):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis

    def describe(self):
        return f"{self.name} is {self.age} years old, diagnosed with {self.diagnosis}"

    def is_adult(self):
        return self.age >= 18 
            
        

patient_male = Patient("John", 45, "hypertention")
patient_female = Patient("Sara", 17, "COPD")

print(patient_male.describe())
print(patient_male.is_adult())
print()
print(patient_female.describe())
print(patient_female.is_adult())
