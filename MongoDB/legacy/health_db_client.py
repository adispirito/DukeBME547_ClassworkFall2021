import requests

patient1 = {"name": "Ann Ables", "id": 201, "blood_type": "A+"}
r = requests.post("http://127.0.0.1:5000/new_patient", json=patient1)
print(r.status_code)
print(r.text)

test1 = {"id": 201, "test_name": "hdl", "test_result": 120}
r = requests.post("http://127.0.0.1:5000/add_tests", json=test1)
print(r.status_code)
print(r.text)
