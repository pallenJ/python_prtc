import time
from pprint import pprint

from selenium import webdriver

url = "https://land.naver.com/article/divisionInfo.nhn?rletTypeCd=A01&tradeTypeCd=&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1171000000"

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(1)
#driver.minimize_window()

#페이지이동
driver.get(url)

## 정지버튼 누르기
driver.find_element_by_css_selector('a.btn_stop_on').click()

##몇명인지 확인

num = driver.find_element_by_css_selector('span.pagenum').text
num = int(num.split('/')[-1])
print('중개사수 : ',num)

time.sleep(5)
driver.quit()

