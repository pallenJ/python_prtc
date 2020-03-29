from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

url = "https://news.naver.com/main/read.nhn?oid=031&aid=0000531767&m_view=1"

#driver 연결

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(1)
driver.maximize_window()

print("[접속하기]")
driver.get(url)

## 더보기 버튼 누르기
#
attemp = 0 # 더보기 탐색횟수

while True:
    try:
        driver.find_element_by_css_selector('span.u_cbox_box_more').click()
        attemp = 0
    except:
        attemp +=1
        if attemp>5:
            break # 더이상 더보기가 없을때 나옴

## 댓글 요소 찾기
print('[댓글 요소 찾기]')
replys = driver.find_elements_by_css_selector('ul.u_cbox_list > li.u_cbox_comment')

# nick : span.u_cbox_nick
# content : span.u_cbox_contents
## 작성자와 댓글 내용 추출(작성자 , 댓글 내용

results = []
del_msg = 0
for reply in replys:
    try:
        author = reply.find_element_by_css_selector('span.u_cbox_nick').text
        content = reply.find_element_by_css_selector('span.u_cbox_contents').text
        results.append((author, content))
    except:
        del_msg+=1 #삭제된 댓글일시 발생하는 예외처리
print('삭제된 댓글:',del_msg)
#pprint(results)

## 엑셀파일 만들기

print('[엑셀로 저장]')
col = ['작성자','내용']
data_frame = pd.DataFrame(results,columns=col)
data_frame.to_excel('excelTest.xlsx',sheet_name='수집시트이름',startrow=0,header=True)

# 닫음
time.sleep(3)
driver.quit()
