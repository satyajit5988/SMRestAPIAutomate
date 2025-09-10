import json
import jsonpath
import requests

url = "https://reqres.in/api/users"
response = requests.post(url)

file = open("/TestData/userdata.json", "r")
json_input = file.read()
request_json = json.loads(json_input)

print(request_json)

js_response = requests.post(url,request_json)

print(js_response.status_code)
assert js_response.status_code == 401

# response_json = json.loads(js_response.text)
# id = jsonpath.jsonpath(response_json, 'id')
# print(id[0])