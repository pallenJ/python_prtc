from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://news.naver.com/main/read.nhn?oid=031&aid=0000531767&m_view=1"

#driver 연결

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

print("[접속하기]")
driver.get(url)

## 댓글 요소 찾기
print('[댓글 요소 찾기]')
replys = driver.find_elements_by_css_selector('ul.u_cbox_list > li.u_cbox_comment')

# nick : span.u_cbox_nick
# content : span.u_cbox_contents
## 작성자와 댓글 내용 추출(작성자 , 댓글 내용

result = []
del_msg = 0
for reply in replys:
    try:
        author = reply.find_element_by_css_selector('span.u_cbox_nick').text
        content = reply.find_element_by_css_selector('span.u_cbox_contents').text
        result.append((author,content))
    except:
        del_msg+=1 #삭제된 댓글일시 발생하는 예외처리
print('삭제된 댓글:',del_msg)
pprint(result)
# 닫음
time.sleep(3)
driver.quit()
