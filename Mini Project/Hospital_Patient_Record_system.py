patients = []

while True:
    print("\n" + "=" * 40)
    print("Hospital Patient Record System")
    print("=" * 40)
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        patient_id = input("Patient ID: ")
        name = input("Patient Name: ")
        age = int(input("Age: "))
        disease = input("Disease: ")

        patient = {
            "id": patient_id,
            "name": name,
            "age": age,
            "disease": disease
        }

        patients.append(patient)

        print("Patient added successfully.")

    elif choice == 2:
        if len(patients) == 0:
            print("No patient records found.")
        else:
            print("\nPatient Records")
            print("-" * 40)
            for patient in patients:
                print("ID:", patient["id"])
                print("Name:", patient["name"])
                print("Age:", patient["age"])
                print("Disease:", patient["disease"])
                print("-" * 40)

    elif choice == 3:
        search_id = input("Enter Patient ID: ")
        found = False

        for patient in patients:
            if patient["id"] == search_id:
                print("\nPatient Found")
                print("ID:", patient["id"])
                print("Name:", patient["name"])
                print("Age:", patient["age"])
                print("Disease:", patient["disease"])
                found = True
                break

        if not found:
            print("Patient not found.")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid Choice.")