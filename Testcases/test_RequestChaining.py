import json
import jsonpath
import requests


def test_add_new_student():
    global user_id
    API_URL="https://thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Users/User/PycharmProjects/SM - RestAPIAutomate/TestData/addUserDetails.json", "r")
    json_input = json.loads(file.read())
    response = requests.post(API_URL, json_input)
    user_id = jsonpath.jsonpath(response.json(), 'id')
    print("Response 1 ------------------")
    print(user_id[0])

def test_get_new_student():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/" + str(user_id[0])
    response = requests.get(API_URL )
    print("Response 2 ------------------")
    print(response.text)