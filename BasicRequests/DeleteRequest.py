import json
import requests

url = "https://reqres.in/api/users/2"
response = requests.delete(url)

json_response = json.loads(response.text)
print(json_response)