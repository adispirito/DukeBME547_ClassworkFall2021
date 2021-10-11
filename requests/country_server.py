import requests

server_name = "http://vcm-7631.vm.duke.edu:5000/compare/"
r = requests.get(server_name+"countries")
print(r.test)

request_json = {"one": "Afganistan", "two": "Albania"}
r = requests.post(server_name+"countries", json = request_json)

if r.status_code != 200:
    print(r.text)
else:
    print(r.json())
# countries = {"one": "Spain", "two": "Sweden"}
# r = requests.post(server_name, json=countries)
# print(r.json())
