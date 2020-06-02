from flask import Flask, request, jsonify,session
from werkzeug.utils import redirect
app=Flask(__name__)
app.secret_key='yzuo'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/welcome/<username>')
def welcome_username(username):
    return 'welcome %s' %username

@app.route('/number/<int:number>')
def my_number(number):
    return 'mynumber %s' %(number+number)

@app.route('/baidu')
def baidu():
    return redirect('http://www.baidu.com')

@app.route('/test/myfirst',methods=['POST'])
def first_post():
    my_json=request.get_json()
    print(my_json)
    get_name=my_json.get('name')
    get_age=my_json.get('age')
    get_age+=10
    return jsonify(name=get_name,age=get_age)

@app.route('/test/login',methods=['POST'])
def login():
    get_data=request.get_json()
    username=get_data.get('username')
    password=get_data.get('password')
    if not all([username,password]):
        return jsonify(msg='参数不完整')
    if username=='yzuo' and password=='yzuo':
        session['username']=username
        return jsonify(msg='登录成功')
    else:
        return jsonify(msg='账号或密码错误')

@app.route('/session',methods=['GET'])
def check_session():
    username=session.get('username')
    if username is not None:
        return jsonify(username=username)
    else:
        return jsonify(msg='未登录')

@app.route('/test/logout',methods=['GET'])
def logout():
    session.clear()
    return jsonify(msg='成功退出登录')

app.run()