patients = []

with open('patient_list.txt', 'r') as file:
   for line in file: 
    each_line = line.split(", ")
   
    name = each_line[0]
    age = each_line[1]
    diagnosis = each_line[2]
    patient = { 
    "name": name,
    "age": age,
    "diagnosis": diagnosis
    }
    patients.append(patient)
   

   print(f"Total Patients: {len(patients)}")
   print()
   for patient in patients:
    print(f"{patient['name']} - {patient['diagnosis']}")
       
       