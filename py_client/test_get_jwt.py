import requests
from getpass import getpass


auth_end_point='http://127.0.0.1:8000/api/token/'
username=input('what is your username?\n')
password=getpass('what is your password?\n')
auth_response=requests.post(auth_end_point, json={'username':username,'password':password})

# print(auth_response.json())
access_token=''
headers=''
refresh_token=''
if auth_response.status_code==200:
    access_token=auth_response.json()['access']
    headers={'Authorization' : f'Bearer {access_token}'}
    refresh_token=auth_response.json()['refresh']