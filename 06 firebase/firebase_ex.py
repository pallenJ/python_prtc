import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("mykey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://semicircle-16117.firebaseio.com/'
})