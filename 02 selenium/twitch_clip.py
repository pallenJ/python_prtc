import time

from selenium import webdriver


driver = webdriver.Chrome('chromedriver')
driver.get('https://www.twitch.tv/soorte214/clip/AgileGracefulCheesecakePeteZarollTie')

time.sleep(3)

# video tag 확인

url_element = driver.find_element_by_tag_name('video') # 가져올 태그명
vid_url = url_element.get_attribute('src') # 가져올 속성명 

title_element1 = driver.find_element_by_class_name('tw-flex')
title_element2 = driver.find_elements_by_tag_name('span')
vid_title, vid_date = None,None

for span in title_element2:
    try:
        d_type = span.get_attribute('data-test-selector')
        print(span.text)
        if d_type == 'title':
            vid_title = span.text
        elif d_type == 'date':
            vid_date = span.text
    except:
        pass

print(vid_title,vid_date)
