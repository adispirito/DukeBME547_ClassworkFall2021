from flask import Flask, request, jsonify

app = Flask(__name__)
db = []


@app.route("/", methods=["GET"])
def status():
    return "Server is on"


@app.route("/new_patient", methods=["POST"])
def new_patient():
    in_data = request.get_json()
    error_string, status_code = validate_new_patient_input(in_data)
    if error_string is not True:
        return error_string, status_code
    new_patient = add_database_entry(in_data["name"],
                                     in_data["id"],
                                     in_data["blood_type"])
    return f"Added patient {new_patient}"


def validate_new_patient_input(in_data):
    if type(in_data) is not dict:
        return "The input was not a dictionary.", 400
    expected_keys = {"name": str, "id": int, "blood_type": str}
    for key, v in expected_keys.items():
        if key not in in_data:
            return f"The key {key} is missing from input", 400
        if type(in_data[key]) is not expected_keys[key]:
            return f"The key {key} has the wrong data type", 400
    return True, 200


def add_database_entry(patient_name, id_no, blood_type):
    new_patient = {"name": patient_name,
                   "id": id_no,
                   "blood_type": blood_type,
                   "tests": []}
    db.append(new_patient)
    return new_patient

def add_tests(in_tests):
    q_id = in_tests["id"]
    for patient in db:
        id = patient["id"]
        if id == q_id:
            patient["tests"].append((in_tests["test_name"],
                                     in_tests["test_result"]))


@app.route("/add_tests", methods=["POST"])
def add_tests_app():
    in_tests = request.get_json()
    add_tests(in_tests)
    print(db)
    return in_tests, 200


if __name__ == "__main__":
    app.run()
