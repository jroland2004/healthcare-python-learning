

def iv_drip_rate(volume_ml, time_hours):
    drip_rate = (volume_ml * 20) / (time_hours * 60)
    return int(drip_rate)

def weight_based_dose(weight_kg, dose_per_kg):
    wt_dose = weight_kg * dose_per_kg
    return wt_dose

def mcg_to_mg(mcg):
    milligrams_fm_mcg = mcg / 1000
    return milligrams_fm_mcg

def mg_to_mcg(mg):
    micrograms_fm_milli = mg * 1000
    return  micrograms_fm_milli

def mean_arterial_pressure(systolic, diastolic):
    MAP_BP = (systolic + (2 * diastolic)) / 3
    return round(MAP_BP, 1)

def creatinine_clearance(age, weight_kg, creatinine, is_female=False):
    creatinine_clearance_est = ((140 - age) * weight_kg) / (72 * creatinine)
    if is_female:
        return round(creatinine_clearance_est * 0.85, 1)
    else:
        return round(creatinine_clearance_est, 1)