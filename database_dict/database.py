class Patient:

    def __init__(self, name, id_no, age, tests):
        self.name = name
        self.id_no = id_no
        self.age = age
        self.tests = tests

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def id_no(self):
        return self._id_no
    @id_no.setter
    def id_no(self, value):
        self._id_no = value

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value

    @property
    def tests(self):
        return self._tests
    @tests.setter
    def tests(self, value):
        self._tests = value

    def __repr__(self):
        return f"{self._id_no}: {self._name}"

# def classwork():
#     new_patient = Patient("Ann Ables",
#                           120,
#                           36,
#                           [])
#     new_patient.name = "Bob"


def create_database_entry(patient_name, id_no, age, tests = []):
    # new_patient = {'patient_name': patient_name,
    #                'id_no': id_no,
    #                'age': age,
    #                'tests': []}
    new_patient = Patient(patient_name, id_no, age, tests)
    return new_patient

def print_database(db):
    for elem in db:
        # print(db)
        # print(f"Name = {db['patient_name']}")
        print(f"Name = {db.patient_name}")

def print_age_over(db, age_thres = 32):
    for entry in db:
        age = entry['age']
        if age > age_thres:
            name = entry['patient_name']
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
    patient = db[id_no]
    # for entry in db:
    #     # print(entry)
    #     if entry['id_no'] == id_no:
    #         return entry
    return patient

def main():
    db = {}
    x = create_database_entry("Ann Ables", 1, 30)
    # db.append(x)
    db[x.id_no] = x
    x = create_database_entry("Bob Boyles", 2, 31)
    # db.append(x)
    db[x.id_no] = x
    x = create_database_entry("Chris Chou", 3, 33)
    # db.append(x)
    db[x.id_no] = x
    x = create_database_entry("David Dinkins", 4, 34)
    # db.append(x)
    db[x.id_no] = x
    print(db)

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

    patient_id_tested = 4
    test_done = ("HDL", 65)
    patient = get_patient(db, patient_id_tested)
    # print(patient)
    # patient['tests'].append(test_done)
    # print(db)
    patient.tests.append(test_done)
    print(db)

    # print_database_zip(db)

if __name__ == "__main__":
    main()
