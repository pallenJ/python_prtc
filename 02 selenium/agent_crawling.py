import time
from pprint import pprint
from selenium import webdriver

import pandas as pd

url = "https://land.naver.com/article/divisionInfo.nhn?rletTypeCd=A01&tradeTypeCd=&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1171000000"

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(1)
#driver.minimize_window()

#페이지이동
driver.get(url)

## 정지버튼 누르기
driver.find_element_by_css_selector('a.btn_stop_on').click()

##몇명인지 확인

num = driver.find_element_by_css_selector('span.pagenum').text
num = int(num.split('/')[-1])
print('중개사수 : ',num)

print('[정보 추출]')
rs =[]
# 중개사들 프로필 저장영역
for i in range(num):
    p_count = 0
    while True :
        if p_count>3 :
            break
        try:
            profile = driver.find_element_by_css_selector('div.bx_com') # 프로필 영역
            # 뉴스댓글과 달리 정보의 개수가 다 다를 수 있어서 딕셔너리 사용
            data = {}

            # 업체명과 대표명, 가능언어
            data['company'] = profile.find_element_by_css_selector('h5.t_mem').text #업체명
            area1 = profile.find_element_by_css_selector('ul.lst_mem > li:nth-child(1)').text
            data['name'] = area1.split('|')[0][len('대표 '):] #대표명
            if '가능' in area1:
                data['lang'] = area1.split('|')[1][:-3] #대표|가능한 외국어
            area2 = profile.find_element_by_css_selector('ul.lst_mem > li:nth-child(2)').text
            phones = area2[3:].split(' / ')
            for index , phone in enumerate(phones):
                data['phone{}'.format(index+1)] = phone
            print(data)
            rs.append(data)
            break
        except:
            p_count+=1
    # 맨 마지막 사람인지 확인
    count = 0
    flag = False
    while True:
        if count>3:
            break
        try:
            p_num = driver.find_element_by_css_selector('span.pagenum').text
            p_num = int(p_num.split('/')[0])
            print('현재 탐색번호: ',p_num)
            if num==p_num: # 탐색번호와 마지막 번호가 같으면 멈춤
                flag = True
            break
        except:
            count+=1
            print('error',count)
    if flag:
        break
    # 다음 프로필로 넘기기
    count = 0;
    while True:
        ## 서버가 느린경우도 있으므로 다음버튼을 누르고 딜레이를 발생시켜 기다림
        try :
            driver.find_element_by_css_selector('a.btn_next_on').click()
            #time.sleep(.5)
            break
        except:
            count+=1
            if(count>3):
                break

# 엑셀저장

print('엑셀저장')
excel_name = '부동산 중개사'
data_frame = pd.DataFrame(rs)
data_frame.to_excel('./{}.xlsx'.format(excel_name),sheet_name=excel_name,startrow=0,header=True)

time.sleep(5)
driver.quit()

