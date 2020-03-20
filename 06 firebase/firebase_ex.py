import firebase_admin
from firebase_admin import credentials, db

# 파이어베이스 DB 인증 및 앱 초기화
cred = credentials.Certificate("mykey.json") # 만든 새 프로젝트에서 가져온 인증키
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://semicircle-16117.firebaseio.com/' # dbURL
})

ref = db.reference() # db 위치 지정
ref.update({'준모':'호래이'}) # 해당변수가 없을경우 생성

ref = db.reference('연습/파이썬') # 경로가 없으면 생성
ref.update({'파이썬 레시피 웹 활용':'complete'})
ref.update({'파이썬 괴식 레시피':'proceeding'})

ref = db.reference()
ref.update({'수강자' : ['구독자A','구독자B','구독자C','구독자D']}) # list 는 인덱스:요소 로 자리잡음
