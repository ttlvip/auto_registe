import os
import json
import requests

domain = os.environ.get('DOMAIN')
port = os.environ.get('PORT')
api_key = os.environ.get('API_KEY')
copy_user_id = os.environ.get('COPY_USER_ID')


def add_user(username, password):
    url = 'http://' + domain + ':' + port + '/emby/Users/New?api_key=' + api_key
    payload = json.dumps({
        "Name": username,
        "CopyFromUserId": copy_user_id
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response
