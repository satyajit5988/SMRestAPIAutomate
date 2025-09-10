import json
import jsonpath
import requests
import pytest

url = "https://reqres.in/api/users"

@pytest.fixture()
def start_exec():
    global file
    file = open("C:/Users/User/PycharmProjects/SM - RestAPIAutomate/TestData/userdata.json", "r")

@pytest.mark.smoke
def test_create_new_user(start_exec):
    # Read input JSN file
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)

    # Make POST request with JSON Input
    js_response = requests.post(url,request_json)

    # Validate response code
    print(js_response.status_code)
    assert js_response.status_code == 401

    # Fetch response headers
    print(js_response.headers.get("Content-Length"))

    # Parse response
    # response_json = json.loads(js_response.text)
    # id = jsonpath.jsonpath(response_json, 'id')
    # print(id[0])

@pytest.mark.smoke
def test_create_other_user(start_exec):
    # Read input JSN file
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)

    # Make POST request with JSON Input
    js_response = requests.post(url,request_json)

    # Validate response code
    print(js_response.status_code)
    assert js_response.status_code == 401

    # Fetch response headers
    print(js_response.headers.get("Content-Length"))

    # Parse response
    # response_json = json.loads(js_response.text)
    # id = jsonpath.jsonpath(response_json, 'id')
    # print(id[0])