class Medication:
    def __init__(self, name, dose, unit):
        self.name = name
        self.dose = dose
        self.unit = unit

    def describe(self):
        return f"{self.name}, {self.dose}, {self.unit}"

class MedicationList:
    def __init__(self, patient_name):
        self.patient_name = patient_name
        self.medications = []
    
    def add_medication(self, medication):
        self.medications.append(medication)

    def remove_medications(self, med_name):
        for medication in self.medications:
            if medication.name == med_name:
                self.medications.remove(medication)
                return

    def count(self):
        return len(self.medications)

    def print_all(self):
        print(f"Patient Name: {self.patient_name}")
        for medication in self.medications:
            print(f"{medication.name}, {medication.dose}, {medication.unit}")

med1 = Medication("Lisinopril", 10, "mg")
med2 = Medication("Metformin", 500, "mg")

med_list = MedicationList("Jason Roland")
med_list.add_medication(med1)
med_list.add_medication(med2)
med_list.print_all()
print(f"Total Medications: {med_list.count()}")

med_list.remove_medications("Lisinopril")
med_list.print_all()
print(f"Total Medication: {med_list.count()}")

