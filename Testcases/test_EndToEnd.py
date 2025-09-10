import json
import jsonpath
import requests


def test_Add_New_User():
    API_URL="https://thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Users/User/PycharmProjects/SMRestAPIAutomate/TestData/addUserDetails.json", "r")
    request_json = json.loads(file.read())
    response = requests.post(API_URL, request_json)
    user_id = jsonpath.jsonpath(response.json(), 'id')
    print("Response 1 ------------------")
    print(user_id[0])

    TECH_API_URL="https://thetestingworldapi.com/api/technicalskills"
    file = open("C:/Users/User/PycharmProjects/SMRestAPIAutomate/TestData/addtechnicalDetails.json", "r")
    request_json = json.loads(file.read())
    request_json['id'] = user_id[0]
    request_json['st_id'] = user_id[0]
    response = requests.post(TECH_API_URL, request_json)
    print("Response 2 ------------------")
    print(response.text)

    ADDRESS_API_URL="https://thetestingworldapi.com/api/addresses"
    file = open("C:/Users/User/PycharmProjects/SMRestAPIAutomate/TestData/addAddress.json", "r")
    request_json = json.loads(file.read())
    request_json['stId'] = user_id[0]
    response = requests.post(ADDRESS_API_URL, request_json)
    print("Response 3 ------------------")
    print(response.text)

    FINAL_API_URL = "https://thetestingworldapi.com/api/FinalStudentDetails/" + str(user_id[0])
    response = requests.get(FINAL_API_URL)
    print("Response 4 ------------------")
    print(response.text)