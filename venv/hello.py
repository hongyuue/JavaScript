 # -*- coding: utf-8 -*-
from flask import Flask
#使用了 Flask这个构造函数来创建一个 Flask 的 实例app. Flask的参数是
#程序的名称
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)
