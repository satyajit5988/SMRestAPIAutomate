import json
import jsonpath
import requests

url = "https://reqres.in/api/users/7"
response = requests.post(url)

file = open("/TestData/userdata.json", "r")
json_input = file.read()
request_json = json.loads(json_input)

print(request_json)

js_response = requests.put(url,request_json)

print(js_response.status_code)
assert js_response.status_code == 401

# response_json = json.loads(js_response.text)
# updated = jsonpath.jsonpath(response_json, 'updatedAt')
# print(updated[0])