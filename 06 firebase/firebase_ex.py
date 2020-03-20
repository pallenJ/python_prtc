import firebase_admin
from firebase_admin import credentials, db

# 파이어베이스 DB 인증 및 앱 초기화
cred = credentials.Certificate("mykey.json") # 만든 새 프로젝트에서 가져온 인증키
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://semicircle-16117.firebaseio.com/' # dbURL
})

ref = db.reference() # db 위치 지정
ref.update({'준모':'호래이'}) # 해당변수가 없을경우 생성
