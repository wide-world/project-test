import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from flask import Flask, render_template

app = Flask(__name__)

# Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('./mykey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kisfestival-a86f4-default-rtdb.firebaseio.com/'
})

ref = db.reference().child('member')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/vote/<string:code>')
def vote(code):
    return render_template('vote.html', employ_num=code)


@app.route('/complete')
def complete():
    return render_template('complete.html')


@app.route('/<string:mem_id>')
def member_id(mem_id):
    mem_data = ref.child(mem_id).get()
    return mem_data


@app.route('/data')
def data():
    member_data = ref.get()
    return member_data


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # app.run(port=5000, debug=True)
