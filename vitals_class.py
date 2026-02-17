class VitalSigns:
    def __init__(self, heart_rate, systolic, diastolic, temp, o2_sat):
        self.heart_rate = heart_rate
        self.systolic = systolic
        self.diastolic = diastolic
        self.temp = temp
        self.o2_sat = o2_sat
    
    def assess_heart_rate(self):
        if self.heart_rate < 60:
             heart_rate_dx = "Bradycardia"
        elif self.heart_rate > 100:
             heart_rate_dx = "Tachycardia"
        else:
             heart_rate_dx= "Normal"
        return heart_rate_dx
    
    def assess_blood_pressure(self):
         if self.systolic < 90 or self.diastolic < 60:
             blood_pressure_dx = "Hypotensive"
         elif self.systolic > 140 or self.diastolic > 90:
             blood_pressure_dx = "Hypertensive"
         else:
             blood_pressure_dx = "Normal BP"
         return blood_pressure_dx

    def assess_temperature(self):
        if self.temp < 97.0:
            temperature_dx = "Hypothermia"
        elif self.temp > 100.3:
            temperature_dx = "Fever"
        elif self.temp >= 99.1:
            temperature_dx = "Low-grade fever"
        else:
            temperature_dx = "Normal"    
        return temperature_dx

    def assess_oxygen(self):
        if self.o2_sat < 92:
            oxygen_sat_dx = "Critical - supplement oxygen"
        elif self.o2_sat >= 95:
            oxygen_sat_dx = "Normal"
        else:
            oxygen_sat_dx = "Low - monitor closely"
        return oxygen_sat_dx

    def get_summary(self):
        vitals_summary = {
            "heart_rate": self.assess_heart_rate(),
            "blood_pressure": self.assess_blood_pressure(),
            "temperature": self.assess_temperature(),
            "oxygen": self.assess_oxygen()
        }
        return vitals_summary

if __name__ == "__main__":
    patient1 = VitalSigns(54, 120, 92, 99, 93)

    print("---Patient Vitals Sumamry---")
    print()
    print(patient1.get_summary())