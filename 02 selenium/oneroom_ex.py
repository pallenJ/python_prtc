import time
from pprint import pprint

from selenium import webdriver

url = "https://new.land.naver.com/rooms?ms=37.4968699,126.9461784,15&a=OR&b=B1:B2&e=RETAIL&aa=SMALLSPCRENT&ad=true"

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(1)
driver.minimize_window()
driver.get(url)

# 크롤링
#onerooms = driver.find_elements_by_class_name('item_inner')
oneroomList = []
onerooms = driver.find_elements_by_css_selector('div.item_inner')


for oneroom in onerooms :
    try:
        title    = oneroom.find_element_by_css_selector('div.item_title').text
        roomType = oneroom.find_element_by_css_selector('strong.type').text
        payType  = oneroom.find_element_by_css_selector('span.type').text
        price    = oneroom.find_element_by_css_selector('span.price').text
        spec     = oneroom.find_element_by_css_selector('span.spec').text
        oneroomList.append((roomType))
        print(title,'|',roomType,'/',payType,'/',price,spec)
    except :
        pass

time.sleep(3)
driver.quit()
