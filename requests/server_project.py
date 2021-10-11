import requests

server_name = "http://vcm-21170.vm.duke.edu:5000/"
request_json = {
   "name": "Anthony DiSpirito",
   "net_id": "ad424",
   "e-mail": "anthony.dispirito@duke.edu"
}
r = requests.post(server_name+"student", json = request_json)

r = requests.get(server_name + "list")
if r.status_code != 200:
    print(r.text)
else:
    print(r.json())

request_json = {
   "a": 1,
   "b": 2
}
r = requests.post(server_name+"sum", json = request_json)
if r.status_code != 200:
    print(r.text)
else:
    print(r.json())


############### BLOOD MATCH ##################
server_name = "http://vcm-7631.vm.duke.edu:5002/"
patient_name = "ad424"
r = requests.get(server_name + f"get_patients/{patient_name}")
if r.status_code != 200:
    print(r.text)
else:
    print(r.json())

blood_types = []
for _,v in r.json().items():
    r = requests.get(server_name + f"get_blood_type/{v}")
    blood_types.append(r.text)

answer = "No"
request_json = {"Name": patient_name, "Match": answer}
r = requests.post(server_name+"match_check", json = request_json)
print(r.text) # is "Correct"
