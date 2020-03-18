import json
import os
import sys
import urllib.request
from pprint import pprint

client_id = "zIZX9IwtySmzedLu9yHD"
client_secret = "rlgId2Wc15"
encText = urllib.parse.quote("라면 먹고싶다")# 번역할 내용이 들어감
data = "source=ko&target=en&text=" + encText # 언어 구성은 https://developers.naver.com/docs/papago/papago-nmt-api-reference.md참고
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    res = json.loads(response_body.decode('utf-8'))
    pprint(res['message']['result']['translatedText'])
else:
    print("Error Code:" + rescode)