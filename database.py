def create_patient_entry(patient_name, patient_id, patient_age):
    new_patient = [patient_name, patient_id, patient_age, []]
    return new_patient


def output(data):
    for patient in data:
        print(patient)
        print("Name: {}, id: {}, age: {}"
              .format(patient[0], patient[1], patient[2]))


def id_match(data, id):
    for patient in data:
        if patient[1] == id:
            return patient
    return False


def add_test_results(data, id, test, value):
    patient = id_match(data, id)
    patient[3].append((test, value))


def main():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 30))
    db.append(create_patient_entry("Bob Boyles", 2, 34))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    add_test_results(db, 3, "HDL", 100)
    print(id_match(db, 3))

    room_list = ["Room 1", "Room 2", "Room 3"]

    for i, patient in enumerate(db):
        print("Name = {}, Room = {}".format(patient[0], room_list[i]))

    for patient, room in zip(db, room_list):
        print("Name = {}, Room = {}".format(patient[0], room))


if __name__ == "__main__":
    main()
