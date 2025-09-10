import requests

param = {'name':'letslearn','role':'NGO'}

response = requests.get("https://httpbin.org/get", params=param)
print(response.text)