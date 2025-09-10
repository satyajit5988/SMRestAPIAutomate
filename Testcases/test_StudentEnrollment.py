import json
import jsonpath
import requests


def test_AddNewUser():
    API_URL="https://thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Users/User/PycharmProjects/SM - RestAPIAutomate/TestData/addUserDetails.json", "r")
    json_input = json.loads(file.read())
    response = requests.post(API_URL, json_input)
    print(response.text)


def test_UpdateNewUser():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/10692976"
    file = open("C:/Users/User/PycharmProjects/SM - RestAPIAutomate/TestData/addUserDetails.json", "r")
    json_input = json.loads(file.read())
    response = requests.put(API_URL, json_input)
    print(response.text)


def test_GetNewUser():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/10692976"
    response = requests.get(API_URL)
    json_response = json.loads(response.text)
    print(json_response)
    # json_response = response.json()
    user_id = jsonpath.jsonpath(json_response,'data.id')
    assert user_id[0] == 10692976

def test_DeleteNewUser():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/10692976"
    response = requests.delete(API_URL)
    json_response = json.loads(response.text)
    print(json_response)
