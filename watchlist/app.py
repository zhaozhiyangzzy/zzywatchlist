from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello():
    print('zhello')
    return 'hello'

@app.route('/user/<name>')
def user_page(name):
    return 'User:%s' % name
@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    return 'Test page'
@app.route('/home')
def hello():
    return 'welcome to my watchlist'
