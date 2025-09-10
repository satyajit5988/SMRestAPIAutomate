import jsonpath
import requests
import json
import pytest

url = "https://reqres.in/api/users?page=2"

@pytest.mark.sanity
def test_GetUser():
    response = requests.get(url)

    json_response = json.loads(response.text)
    print(json_response)

    pages = jsonpath.jsonpath(json_response, 'total_pages')

    for i in range(0,3):
        firstname = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
        print(firstname[0])
    print(pages[0])

    print(response.status_code)
    assert response.status_code == 200

    print(response.headers)
    print(response.headers.get('Date'))
    print(response.headers.get('Server'))

    print(response.cookies)
    print(response.encoding)
    print(response.elapsed)

    print(response.content)