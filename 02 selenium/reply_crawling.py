from pprint import pprint
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from PIL import Image
from io import BytesIO # 댓글 캡쳐를 위해 함께 필요

def capture_replys(keyword,url,excel_name = None):
    #keyword = '손해배상'
    ##keyword = '공주'
    
    #url = "https://news.naver.com/main/read.nhn?oid=031&aid=0000531767&m_view=1"
    ##url = "https://news.naver.com/main/ranking/read.nhn?oid=449&aid=0000189238&m_view=1"

    url +='&m_view=1'

    #driver 연결
    
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(1)
    driver.maximize_window()
    
    print("[접속하기]")
    driver.get(url)
    
    ## 더보기 버튼 누르기
    #
    attemp = 0 # 더보기 탐색횟수
    
    while True:
        try:
            driver.find_element_by_css_selector('span.u_cbox_box_more').click()
            attemp = 0
        except:
            attemp +=1
            if attemp>5:
                break # 더이상 더보기가 없을때 나옴
    
    ## 댓글 요소 찾기
    print('[댓글 요소 찾기]')
    replys = driver.find_elements_by_css_selector('ul.u_cbox_list > li.u_cbox_comment')
    
    # nick : span.u_cbox_nick
    # content : span.u_cbox_contents
    ## 작성자와 댓글 내용 추출(작성자 , 댓글 내용
    
    results = []
    keyword_result = [] # index, author, content
    del_msg = 0
    for index,reply in enumerate(replys):
        try:
            print("find ", index)
            author = reply.find_element_by_css_selector('span.u_cbox_nick').text
            content = reply.find_element_by_css_selector('span.u_cbox_contents').text
            results.append((author, content))
    
            #키워드가 있나 확인
            if keyword in content:
                keyword_result.append((index,author,content))
        except:
            del_msg+=1 #삭제된 댓글일시 발생하는 예외처리
    print('삭제된 댓글:',del_msg)
    #pprint(results)
    
    ## 폴더생성
    folder_name = keyword
    if not os.path.isdir('./{}'.format(folder_name)):
        os.mkdir('./{}'.format(folder_name))
    
    ## 상단바 삭제
    print('[상단바 메뉴 숨기기]')
    header = driver.find_element_by_css_selector('#header')
    driver.execute_script("arguments[0].style.display='none'",header)
    
    ## 캡쳐하기 - 1.셀레니움을 이용한 방법
    # for index, k in enumerate(keyword_result):
    #     replys[k[0]].screenshot('./{0}/{0}{1}.png'.format(keyword,index))
    
    ## 캡쳐하기 - 2.자바스크립트를 이용한 방법
    print('캡쳐')
    for index, k in enumerate(keyword_result):
        # 화면캡쳐 -> 필요한 요소에 대한 좌표값을 구함
        ## 캡쳐 -> 잘라내기 -> 파일로 저장
        driver.execute_script('arguments[0].scrollIntoView(true);',replys[k[0]])
    
        # 현재화면 캡쳐
        img = driver.get_screenshot_as_png() # 바이너리 형태로 저장
    
        ## 요소좌표 추출 후 현재화면 캐벼사진에서 잘라내어 저장
        location =replys[k[0]].location_once_scrolled_into_view #현재 화면에서 해당요소가 어딨는지 dic형태 반환
        size = replys[k[0]].size
    
        left = location['x']
        top  = location['y']
        right = left + size['width']
        bottom = top + size['height']
        box = (left, top, right, bottom)
    
        if location:
            im = Image.open(BytesIO(img)) #Image.open에 바이트형태를 바로 넣으려면 ByteIO필요
            im = im.crop(box)
            im.save('./{0}/{0}{1}.png'.format(keyword,index))
    
    
    ## 엑셀파일 만들기
    
    print('[엑셀로 저장]')
    if excel_name:
        col = ['작성자','내용']
        data_frame = pd.DataFrame(results,columns=col)
        data_frame.to_excel('{}.xlsx'.format(excel_name),sheet_name='수집시트이름',startrow=0,header=True)

    # 닫음
    time.sleep(3)
    driver.quit()

if __name__ == '__main__':
    capture_replys(keyword='공주', url='https://news.naver.com/main/ranking/read.nhn?oid=449&aid=0000189238',excel_name='test')
