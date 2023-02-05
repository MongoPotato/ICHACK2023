import requests
import json

dev_id = "ichack-octopulps-dev-lSKPE263GO"
api_key = "c01aacd7f227a9054f7c5ce2ab8e8e1e317947d1f5df2c7607778dc51d3ff92d"
signing_secret = "c1dfefa32b646695bf6980ddb9bca043a20b1a2e40c303a2"



def request_session(public_key):

    params = {
        'reference_id' : public_key
    }
    headers = {
        
        'dev-id' : dev_id,
        'X-API-Key' : api_key
    }

    response = requests.post('https://api.tryterra.co/v2/auth/generateWidgetSession',headers=headers,params=params,json=[])

    if response.status_code == 200 or response.status_code == 201 :
        response_dict = response.json()
        print(response_dict)
    else:
        print("Request failed with status code:", response.status_code, response.json())

#Fetch All subscriptions :


def request_session_google(public_key):

    params = {
        "resource": "GOOGLE",
        "reference_id": public_key}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        'dev-id': dev_id,
        "x-api-key": api_key
    }
    response = requests.post("https://api.tryterra.co/v2/auth/authenticateUser",headers=headers,params=params)

    if response.status_code == 200 or response.status_code == 201 :
        response_dict = response.json()
        #print(response_dict)
        return response            
    else:
        print("Request failed with status code:", response.status_code, response.json())
        return response




def remove_user(user_id):
    headers = {
        'dev-id': dev_id,
        'x-api-key': api_key,
        'accept' : 'application/json' 
    }
    response = requests.delete("https://api.tryterra.co/v2/auth/deauthenticateUser?user_id={}".format(user_id),headers=headers).json()
    print(response)

def clear_users():

    headers = {
        'accept' : 'applocation/json',
        'dev-id' : dev_id,
        'X-API-Key' : api_key
    }


    response = requests.get("https://api.tryterra.co/v2/subscriptions",headers=headers,json=[]).json()
    for user in response["users"] :
        user_id = user["user_id"]
        headers = {
            'dev-id': dev_id,
            'x-api-key': api_key,
            'accept' : 'application/json' 
        }
        response = requests.delete("https://api.tryterra.co/v2/auth/deauthenticateUser?user_id={}".format(user_id),headers=headers).json()
#remove_user('52682458-f6aa-4d98-9ca7-bf623de385c9')
#remove_user('c023c427-9603-4a8c-9c1c-f02afe85f9d6')


#clear_users()

def print_users() :

    headers = {
        'accept' : 'applocation/json',
        'dev-id' : dev_id,
        'X-API-Key' : api_key
    }


    response = requests.get("https://api.tryterra.co/v2/subscriptions",headers=headers,json=[]).json()
    for user in response["users"] :
        print(user)



#https://widget.tryterra.co/session/0b625869-adfa-4dcc-987b-9ffc868cce26


def get_activity(user_id,start_date='2023-02-04',end_date='2023-02-04'):


    headers = {
        'dev-id': dev_id,
        'X-API-Key': api_key
    }




    params = {
        'to_webhook': 'false',
        'user_id': user_id,
        'start_date': start_date,
        'end_date': end_date
    }
    response = requests.get('https://api.tryterra.co/v2/daily', headers=headers, params=params)



    if response.status_code == 200 :
        response_dict = response.json()
        return response_dict
    else:
        print("Request failed with status code:", response.status_code,response.json())
        return None


def get_steps(user_id):
    resp = get_activity(user_id)
    return resp["data"][0]["distance_data"]["steps"]



request_session_google('Hector')
"""

request_session()
print_users()

headers = {
    'accept' : 'applocation/json',
    'dev-id' : dev_id,
    'X-API-Key' : api_key
}

response = requests.get("https://api.tryterra.co/v2/subscriptions",headers=headers,json=[]).json()
for user in response["users"] :
    dico = get_activity(user['user_id'])
    print(dico)
"""

#clear_users()
#request_session_google('Hector')
#clear_users()
#print_users()
#print(get_steps("ddede8b9-85f7-4a0c-833b-5f7b9f0a5328"))
