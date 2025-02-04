def patient_and_doc(hospital_data):
    print("Patient Names and Their Doctors:")
for key, values in hospital_data.items():
    print(f"{values['name']} is treated by {values['doctor_name']}")

print("\n")

def medications(hospital_data):
    print("Medications prescribed to each patient:")
for key, values in hospital_data.items():
    print(f"Medications prescribed to {values['name']}:")
    for k, v in values['medications'].items():
        print(f" {k}: {v['dose']} {v['frequency']}")
    print()

