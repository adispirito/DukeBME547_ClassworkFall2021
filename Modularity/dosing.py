
"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""


def find_dose_amount():
    display_menu()
    diagnosis = get_diagnosis()
    display_patient_weight_instruct()
    weight_input = get_weight()
    weight, units = parse_weight_input(weight_input)
    if units == "lb":
        weight = convert_lb_to_kg(weight)
    dosage_mg_per_kg = get_dosage(diagnosis)
    dosage_mg_first_day = calc_dosage(weight, dosage_mg_per_kg)
    display_dosage(weight, dosage_mg_first_day)

def display_menu():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")

def get_diagnosis():
    diagnosis = input("Enter a number: ")
    diagnosis = int(diagnosis)
    return diagnosis

def display_patient_weight_instruct():
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")

def get_weight():
    weight_input = input("Enter weight: ")
    return weight_input

def parse_weight_input(weight_input):
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    return weight, units

def convert_lb_to_kg(weight):
    weight = weight / 2.205
    return weight

def get_dosage(diagnosis):
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis-1]
    return dosage_mg_per_kg

def calc_dosage(weight, dosage_mg_per_kg):
    dosage_mg_first_day = weight * dosage_mg_per_kg
    return dosage_mg_first_day

def display_dosage(weight, dosage_mg_first_day):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first day"
          .format(dosage_mg_first_day))


if __name__ == '__main__':
    find_dose_amount()
