import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('./mykey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kisfestival-a86f4-default-rtdb.firebaseio.com/'
})

ref = db.reference()

ref = db.reference('member/')
js = [
    {
        'id': '113226',
        'name': '윤세연',
        'security': 971224,
        'sex': 1
    },
    {
        'id': '113223',
        'name': '백종성',
        'security': 970719,
        'sex': 1
    },
    {
        'id': '113225',
        'name': '양준식',
        'security': 960420,
        'sex': 1
    },
    {
        'id': '113245',
        'name': '박한규',
        'security': 971016,
        'sex': 1
    }
]
for i in range(len(js)):
    ref.update({js[i]['id']: js[i]})

