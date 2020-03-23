import os
import time
import zipfile
from pprint import pprint
from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm

keyword = input('수집할 키워드를 입력하세요 :')

# 웹 접속 - 네이버 이미지 접속

print('접속중')
driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(30)

url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}'.format(keyword)
driver.get(url)

#페이지 스크롤

body = driver.find_element_by_css_selector('body') #body태그부분 가져옴
for i in range(3):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)# 아이피차단을 막기위한것

# 이미지 링크수집

imgs = driver.find_elements_by_css_selector('img._img')# 태그명.클래스명

rs = []

for img in tqdm(imgs):  # 이미지 다운로드 확인을 위한것
    if 'http' in img.get_attribute('src'):
        rs.append(img.get_attribute('src'))

driver.close()

print('수집완료')
if not os.path.isdir('./{}'.format(keyword)):
    print('폴더생성')
    os.mkdir('./{}'.format(keyword))

for idx, link in tqdm(enumerate(rs)) :
    start = link.rfind('.')
    end   = link.rfind('&')
    #print(link[start:end])
    filetype = link[start:end] #파일타입 저장
    urlretrieve(link,'./{}/{}{}{}'.format(keyword,keyword,idx,filetype))

print('다운로드 완료')

