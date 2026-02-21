class Bed:
    def __init__(self, bed_number):
        self.bed_number = bed_number
        self.patient = None

    def is_empty(self):
        return self.patient is None
    
    def assign_patient(self, patient):
        self.patient = patient

    def discharge(self):
        self.patient = None

class Patient:
    def __init__(self, name, age, diagnosis):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis

    def describe(self):
        return f"{self.name}, {self.age}, {self.diagnosis}"

class Ward:
    def __init__(self, name, beds):
        self.name = name
        self.beds = []
        for i in range(beds):
            bed = Bed(i + 1)
            self.beds.append(bed)

    def admit_patient(self, patient):
        for bed in self.beds:
            if bed.is_empty():
                bed.assign_patient(patient)
                return bed.bed_number
        return "No beds available."

    def discharge_patient(self, bed_number):
        for bed in self.beds:
            if bed.bed_number == bed_number:
                bed.discharge()
                return

    def get_census(self):
        count = 0
        for bed in self.beds:
            if not bed.is_empty():
                count += 1
        return count
        
    def print_status(self):
        print(f"Ward: {self.name}")
        for bed in self.beds:
            if bed.is_empty():
                print(f"Bed Number: {bed.bed_number} : Available")
            else:
                print(f"Bed Number: {bed.bed_number} : Occupied - {bed.patient.describe()}")


ward = Ward("Cardiac Unit", 3)
patient1 = Patient("Jason Roland", 43, "MI")
patient2 = Patient("Brooke Roland", 45, "AFiib")

ward.admit_patient(patient1)
ward.admit_patient(patient2)
ward.print_status()
print(f"Census: {ward.get_census()}")
