from clinical_calc import (
    iv_drip_rate,
    weight_based_dose,
    mcg_to_mg,
    mg_to_mcg,
    mean_arterial_pressure,
    creatinine_clearance
)

# Test IV drip rate: 1000mL over 8 hours
print(f"IV drip rate: {iv_drip_rate(1000, 8)} drops/min")

# Test weight-based dose: 70kg patient, 15mg/kg
print(f"Weight-based dose: {weight_based_dose(70, 15)} mg")

# Test conversions
print(f"500 mcg = {mcg_to_mg(500)} mg")
print(f"2.5 mg = {mg_to_mcg(2.5)} mcg")

# Test MAP: 120/80
print(f"MAP for 120/80: {mean_arterial_pressure(120, 80)} mmHg")

# Test creatinine clearance: 65yo male, 70kg, creatinine 1.2
print(f"CrCl (male): {creatinine_clearance(65, 70, 1.2)} mL/min")

# Test creatinine clearance: 65yo female, 70kg, creatinine 1.2
print(f"CrCl (female): {creatinine_clearance(65, 70, 1.2, is_female=True)} mL/min")