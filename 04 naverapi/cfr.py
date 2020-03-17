import json
import os
import sys
from pprint import pprint

import requests
client_id = "zIZX9IwtySmzedLu9yHD"
client_secret = "rlgId2Wc15"
#url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

files = {'image': open('test.jpg', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }

response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code

if(rescode==200):
    # print (response.text)
    data = json.loads(response.text) # JSON 파싱
    pprint(data) # 속성은 https://developers.naver.com/docs/clova/api/CFR/API_Guide.md#%EC%9D%91%EB%8B%B5-2 참조
else:
    print("Error Code:" + rescode)
