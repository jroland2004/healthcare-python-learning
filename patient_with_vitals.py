from vitals_class import VitalSigns

class Patient:
    def __init__(self, name, age, vitals):
        self.name = name
        self.age = age
        self.vitals = vitals

    def birthday(self):
        self.age += 1

    def update_vitals(self, new_vitals):
        self.vitals = new_vitals

    def get_report(self):
        report = f"Patient: {self.name}, {self.age} years old\n"
        report += "Vitals Assessment:\n"
        report += f"  Heart Rate: {self.vitals.assess_heart_rate()}\n"
        report += f"  Blood Pressure: {self.vitals.assess_blood_pressure()}\n"
        report += f"  Temperature: {self.vitals.assess_temperature()}\n"
        report += f"  Oxygen: {self.vitals.assess_oxygen()}"
        return report


vitals = VitalSigns(45, 125, 82, 98, 92)
patient = Patient("Jason Roland", 45, vitals)

vitals2 = VitalSigns(88, 145, 92, 99.1, 95)
patient.update_vitals(vitals2)
print(patient.get_report())