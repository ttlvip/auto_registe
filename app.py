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
    resp_message = add_user(username, password)
    if resp_message.startswith('注册成功'):
        code = 200
    else:
        code = 500
    resp_json = {
        'code': code,
        'message': resp_message
    }
    return jsonify(resp_json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5080)
