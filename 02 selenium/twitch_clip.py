import time

from selenium import webdriver


driver = webdriver.Chrome('chromedriver')
driver.get('https://www.twitch.tv/soorte214/clip/AgileGracefulCheesecakePeteZarollTie')

time.sleep(3)

# video tag 확인

url_element = driver.find_element_by_tag_name('video') # 가져올 태그명
vid_url = url_element.get_attribute('src') # 가져올 속성명 
print(vid_url)

