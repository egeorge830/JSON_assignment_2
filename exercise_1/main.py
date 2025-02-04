def patient_and_doc(hospital_data):
    print("Patient Names and Their Doctors:")
for key, values in hospital_data.items():
    print(f"{values['name']} is treated by {values['doctor_name']}")

print("\n")

def medications(hospital_data, patient_name):
    print(f"Medications prescribed to {patient_name}:")
for key, values in hospital_data.items():
    if values["name"] == patient_name:
        for k, v in values["medications"].items():
            print(f" {k}: {v["dose"]} {v["frequency"]}")
        return

medications(hospital_data, "Jenny Joseph")

print("\n")

def unique_con(hospital_data):

    unique_conditions = set()

    print("All unique conditions across all patients:")

    for x in hospital_data.values():
        for y in x["medical_condition"]:
            unique_conditions.add(y)

    for y in unique_conditions:
        print(y)

unique_con(hospital_data)

    print("\n")

def doctor_assigned(hospital_data, patient_name):
    for j in hospital_data.values():
        if j["name"] == patient_name:
            print(f'{j["doctor_name"]} is the doctor treating {j["name"]}')
            return
doctor_assigned(hospital_data, "Peter George")


