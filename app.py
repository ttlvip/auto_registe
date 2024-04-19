import html
from flask import Flask, render_template, request, jsonify
from emby.add_user import add_user

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
    response = add_user(username, password)
    if response.status_code == 200:
        resp_json = response.json()
        name = resp_json.get("Name")
        server_id = resp_json.get("ServerId")
        server_name = resp_json.get("ServerName")
        user_id = resp_json.get("Id")
        # 返回一个成功消息
        return jsonify(
            {"status": "success",
             "message": f"Registration successful for username: {name}, server_id: {server_id}, server_name: "
                        f"{server_name}, id: {user_id}"})
    else:
        resp_text = response.text
        resp_text = html.unescape(resp_text)
        return jsonify(
            {"status": "fail", "message": f"{resp_text}"})


if __name__ == '__main__':
    app.run(debug=True)
