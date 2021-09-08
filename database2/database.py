def create_database_entry(patient_name, id_no, age):
    new_patient = [patient_name, id_no, age, []]
    return new_patient

def print_database(db):
    for elem in db:
        print(db)
        print(f"Name = {db[0]}")

def print_age_over(db, age_thres = 32):
    for entry in db:
        age = entry[2]
        if age > age_thres:
            name = entry[0]
            print(name)

def print_database_enum(db):
    locations = ["Room 1", "Room 4", "ER", "Post-OP"]
    for i, elem in enumerate(db):
        print(f"{i} - {elem} - {locations[i]}")

def print_database_zip(db):
    locations = ["Room 1", "Room 4", "ER", "Post-OP"]
    for (i, elem), location in zip(enumerate(db), locations):
        print(f"{i} - {elem} - {location}")

def get_patient(db, id_no):
    for entry in db:
        if entry[1] == id_no:
            return entry

def main():
    db = []
    x = create_database_entry("Ann Ables", 1, 30)
    db.append(x)
    x = create_database_entry("Bob Boyles", 2, 31)
    db.append(x)
    x = create_database_entry("Chris Chou", 3, 33)
    db.append(x)
    x = create_database_entry("David Dinkins", 4, 34)
    db.append(x)
    # print(db)

    # y = db[1]
    # print(y)

    # y = db[-1]
    # print(y)

    # bobsname = db[1][0]
    # print(bobsname)

    # print_database(db)

    # print_age_over(db, 32)

    # found_patient = get_patient(db, 3)
    # print(found_patient)

    # print_database_zip(db)

    patient_id_tested = 24
    test_done = ("HDL", 65)
    patient = get_patient(db, patient_id_tested)
    patient[3].append(test)
    print_database_zip(db)

if __name__ == "__main__":
    main()
