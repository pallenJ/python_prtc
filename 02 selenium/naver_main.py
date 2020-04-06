from pprint import pprint

from selenium import webdriver

url = "https://www.naver.com/"

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(1)
driver.minimize_window()
driver.get(url)

themeCast = driver.find_elements_by_css_selector('ul.themecast_list > li.tl_default')

for tl_default in themeCast:
    pprint(tl_default.text)