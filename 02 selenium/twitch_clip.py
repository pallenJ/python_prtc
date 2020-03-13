import re
import time
from urllib.request import urlretrieve

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
        if d_type == 'title':
            vid_title = span.text
        elif d_type == 'date':
            vid_date = span.text
    except:
        pass


# 정규식으로 특수문자 처리
vid_date = re.sub('[^0-9a-zA-Zㄱ-힗]','',vid_date)
vid_title = re.sub('[^0-9a-zA-Zㄱ-힗]','',vid_title)

print(vid_title,vid_date)

urlretrieve(vid_url, vid_title+'_'+vid_date+'.mp4')

driver.close()
