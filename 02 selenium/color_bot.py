import time
from collections import Counter
from pprint import pprint
from selenium import webdriver


driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/color')
driver.implicitly_wait(300)


# print(len(btns))
btns = driver.find_elements_by_xpath('//*[@id="grid"]/div')




## main

# main을 클래스 값으로 가지는게 답인 현 사이트의 경우만 가능
start = time.time()
while time.time() - start <=60:
    try:
        btn = driver.find_element_by_class_name('main')
        btn.click()
    except:
        pass

