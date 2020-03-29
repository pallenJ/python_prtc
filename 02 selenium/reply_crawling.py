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
time.sleep(3)
driver.quit()
