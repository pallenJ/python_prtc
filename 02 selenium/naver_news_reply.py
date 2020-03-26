import time

from selenium import webdriver

url = 'https://news.naver.com/main/read.nhn?m_view=1&includeAllCount=true&mode=LSD&mid=shm&sid1=102&oid=055&aid=0000803363'

# 웹드라이버
driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(5)
driver.get(url)

# 댓글 더보기 계속 클릭
while True:
    try:
        moreShow = driver.find_element_by_css_selector('a.u_cbox_btn_more')
        moreShow.click()
        time.sleep(1)
    except:
        break
print('끝')
