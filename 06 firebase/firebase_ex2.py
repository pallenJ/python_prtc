import firebase_admin
from firebase_admin import credentials, db

# 파이어베이스 DB 인증 및 앱 초기화
cred = credentials.Certificate("mykey.json") # 만든 새 프로젝트에서 가져온 인증키
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://semicircle-16117.firebaseio.com/' # dbURL
})

# 데이터베이스 레퍼런스 생성후 데이터 읽기
ref = db.reference('없는경로') #이당시의 데이터가 확인된다
print(ref.get()) # 특정 값이 가져와지거나 None

ref = db.reference('준모')
print(ref.get())

ref = db.reference(('수강자'))
print(ref.get())

ref = db.reference(('연습'))
print(ref.get())
