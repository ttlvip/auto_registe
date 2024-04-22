import html
import os
import json
import requests

domain = os.getenv('DOMAIN', 'localhost')
port = os.environ.get('PORT', '8096')
api_key = os.environ.get('API_KEY')
copy_user_id = os.environ.get('COPY_USER_ID')
isSSL = os.environ.get('IS_SSL', 'N')


def add_user(username, password):
    prefix = 'https://' if isSSL.lower() == 'y' else 'http://'
    url = prefix + domain + ':' + port + '/emby/Users/New?api_key=' + api_key
    new_user_params = json.dumps({
        'Name': username,
        'CopyFromUserId': copy_user_id,
        'UserCopyOptions': ['UserConfiguration', 'UserPolicy']
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request('POST', url, headers=headers, data=new_user_params)
    # 创建成功后设置密码
    if response.status_code == 200:
        data = response.json()
        user_id = data.get('Id')
        url = prefix + domain + ':' + port + '/emby/Users/' + user_id + '/Password?api_key=' + api_key
        new_password_params = json.dumps({
            'Id': user_id,
            'NewPw': password,
            'ResetPassword': False
        })
        response = requests.request('POST', url, headers=headers, data=new_password_params)
        if response.status_code == 204:
            return '注册成功! 请使用填写的用户名密码登录.'
        else:
            # 如果密码设置失败就删掉创建的用户
            url = prefix + domain + ':' + port + '/emby/Users/' + user_id + 'Delete?api_key=' + api_key
            requests.request('POST', url, headers=headers)
            return '密码设置失败, 请联系管理员'
    else:
        return html.unescape(response.text)
