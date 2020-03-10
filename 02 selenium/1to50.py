import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')
driver.get('https://www.youtube.com/')

time.sleep(3)

# 검색어창 부분
# XPATH : selenium 에서 특정한 요소를 가리키는 경로 지정법
# //*[@id="search"]는 유튜브 검색창을 XPATH로 계산된 경로
search = driver.find_element_by_xpath('//*[@id="search"]')

# search 변수에 저장된 곳에 값 전송
search.send_keys('무다무다')
time.sleep(1)

#엔터나 방향키등 특수키는 Keys.원하는 키 로 가능. 엔터의 경우 아래와 같음
search.send_keys(Keys.ENTER)
