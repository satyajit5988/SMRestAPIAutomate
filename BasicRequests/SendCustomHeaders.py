import requests

headerData = {'T1':'first_header','T2':'second_headers'}

response = requests.get("https://httpbin.org/get", headers=headerData)
print(response.text)