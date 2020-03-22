import os
import time
from pprint import pprint
from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

keyword = '마마무'

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
    time.sleep(1)


# 이미지 링크수집

imgs = driver.find_elements_by_css_selector('img._img')# 태그명.클래스명

rs = []

for img in imgs:
    if 'http' in img.get_attribute('src'):
        rs.append(img.get_attribute('src'))

driver.close()

print('수집완료')
if not os.path.isdir('./{}'.format(keyword)):
    os.mkdir('./{}'.format(keyword))

for idx, link in enumerate(rs) :
    start = link.rfind('.')
    end   = link.rfind('&')
    #print(link[start:end])
    filetype = link[start:end] #파일타입 저장
    urlretrieve(link,'./{}/{}{}{}'.format(keyword,keyword,idx,filetype))


