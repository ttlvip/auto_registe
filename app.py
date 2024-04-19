import html
import json
import requests
from flask import Flask, render_template, request, jsonify
from requests import JSONDecodeError

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    # 从表单获取数据
    data = request.get_json()  # 获取POST请求的JSON数据
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    # todo 添加代码将数据保存到数据库
    url = "http://nas.biupiaa.top:8096/emby/Users/New?api_key=4ba3d6690162400ea8ae536f3468928c"
    payload = json.dumps({
        "Name": username
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        resp_json = response.json()
        name = resp_json.get("Name")
        server_id = resp_json.get("ServerId")
        server_name = resp_json.get("ServerName")
        user_id = resp_json.get("Id")
        # 返回一个成功消息
        return jsonify(
            {"status": "success", "message": f"Registration successful for username: {name}, server_id: {server_id}, server_name: {server_name}, id: {user_id}"})
    else:
        resp_text = response.text
        resp_text = html.unescape(resp_text)
        return jsonify(
            {"status": "fail", "message": f"{resp_text}"})


if __name__ == '__main__':
    app.run(debug=True)
