import pprint

from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/color')
driver.implicitly_wait(300)

btns = driver.find_elements_by_xpath('//*[@id="grid"]/div')
# print(len(btns))

# 백그라운드 컬러 추출
btns_rgba = [btn.value_of_css_property('background-color') for btn in btns]
pprint(btns_rgba)