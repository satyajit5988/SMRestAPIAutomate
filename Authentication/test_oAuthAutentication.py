import requests
import json
import jsonpath


def test_oauth_auth():

    TOKEN_URL = "http://thetestingworldapi.com/Token"
    data = {'grant_type':'password','username':'admin','password':'abc'}
    response = requests.post(TOKEN_URL, data=data)
    print(response.text)

    token_value = jsonpath.jsonpath(response.json(),'access_token')
    auth = {'Authorization': 'Bearer '+token_value[0]}

    API_URL="http://thetestingworldapi.com/api/StDetails/10692997"
    response = requests.get(API_URL, headers=auth)
    print(response.text)