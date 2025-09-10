import requests
import jsonpath
import pytest
from TestData.testDataUsersCSV import student_data_list
from TestData.testUpdateUsersCSV import update_data_list


# Parametrize the test using the student data
# @pytest.mark.parametrize("student_data", student_data_list)
# def test_add_new_student(student_data):
#     global user_id
#     API_URL = "https://thetestingworldapi.com/api/studentsDetails"
#     response = requests.post(API_URL, json=student_data)
#     print(response.text)
#     # print(response.status_code)
#     user_id = jsonpath.jsonpath(response.json(), 'id')
#     # print(user_id[0])

@pytest.fixture(params=student_data_list)
def test_add_new_student(request):
    global user_id
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    response = requests.post(API_URL, json=request.param)
    user_id = jsonpath.jsonpath(response.json(), 'id')
    # print(user_id[0])

# @pytest.mark.parametrize("update_data", update_data_list)
# def test_update_new_student(update_data):
#     API_URL="https://thetestingworldapi.com/api/studentsDetails/" + str(user_id[0])
#     response = requests.put(API_URL, json={**update_data, "id": user_id[0]})
#     print(response.text)

def test_get_new_student(test_add_new_student):
    API_URL="https://thetestingworldapi.com/api/studentsDetails/" + str(user_id[0])
    response = requests.get(API_URL )
    print(response.status_code)

def test_delete_new_student(test_add_new_student):
    API_URL="https://thetestingworldapi.com/api/studentsDetails/" + str(user_id[0])
    response = requests.delete(API_URL)
    print(response.status_code)
