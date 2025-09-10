import json
import jsonpath
import openpyxl
import requests
from DataDriven import Library


def test_Add_Multiple_Users():
    API_URL="https://thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Users/User/PycharmProjects/SM - RestAPIAutomate/TestData/addMultipleUserDetails.json", "r")
    request_json = json.loads(file.read())

    obj = Library.Common("C:/Users/User/PycharmProjects/SM - RestAPIAutomate/TestData/userMultipleData.xlsx","Sheet1")
    col = obj.fetch_column_count()
    keyList = obj.fetch_key_names()
    row = obj.fetch_row_count()

    for i in range(2,row+1):
        updated_response_json = obj.update_request_with_data(i,request_json,keyList)

        response = requests.post(API_URL, updated_response_json)

        print(response.text)
        print(response.status_code)
        assert response.status_code == 201