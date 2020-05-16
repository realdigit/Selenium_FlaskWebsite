from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>主页</h1>
              <a href="/login">登录</a>'''

@app.route('/login', methods=['GET'])
def signin_form():
    return '''<form action="/loginstatus" method="post">
              <p>用户名: <input name="username"></p>
              <p>密码  : <input name="password" type="password"></p>
              <p><button type="submit">登录</button></p>
              </form>'''

@app.route('/loginstatus', methods=['POST'])
def signin():
    if request.form['username']=='username1' and request.form['password']=='password1':
        return '''<h3>Hello, <a id="user" href="/dashboard">username1</a>!</h3>
        <a href="/logout">登出</a>     
        '''
    return '<h3>用户名或密码错误！</h3>'

if __name__ == '__main__':
    app.run(port=5001, debug=False)