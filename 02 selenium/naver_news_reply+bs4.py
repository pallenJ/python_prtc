import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime

def get_replys(url,imp_time=5,delaytime = 0.1):


    # 웹드라이버
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(imp_time) # implicitely time은 기다려 주는 시간
    driver.get(url)

    # 댓글 더보기 계속 클릭
    while True:
        try:
            moreShow = driver.find_element_by_css_selector('a.u_cbox_btn_more')
            moreShow.click()
            time.sleep(delaytime)
        except:
            break
    print('더보기 끝')

    html = driver.page_source
   #print(html)

    soup = BeautifulSoup(html,'lxml') # html.parser보다 빠르고 좋음 --pip3 install bs4 lxml
    # 댓글 추출
    contents = soup.select('span.u_cbox_contents')
    contents = [content.text for content in contents]
    print('댓글 추출 완료')

    # 작성자
    nicks = soup.select('span.u_cbox_nick')
    nicks = [nick.text for nick in nicks]
    print('닉네임 추출 완료')

    # 날짜
    dates = soup.select('span.u_cbox_date')
    dates = [date.text for date in dates]
    print('날짜 추출 완료')

    # 취합

    replys = list(zip(nicks,dates,contents))
    # for reply in replys:
    #     print(reply)

    driver.quit()
    return replys;

if __name__ == '__main__':
    start = datetime.now()
    url = 'https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=023&aid=0003518785&date=20200328&type=1&rankingSeq=1&rankingSectionId=100&m_view=1&includeAllCount=true&m_url=%2Fcomment%2Fall.nhn%3FserviceId%3Dnews%26gno%3Dnews023%2C0003518785%26sort%3Dlikability'
    #url = 'https://news.naver.com/main/read.nhn?m_view=1&includeAllCount=true&mode=LSD&mid=sec&sid1=104&oid=421&aid=0004065481'
    reply_data = get_replys(url,5,0.1)

    col = ['작성자','날짜','내용']
    data_frame = pd.DataFrame(reply_data,columns=col)
    data_frame.to_excel('news.xlsx', sheet_name="판빙빙 뉴스 테스트", startrow=0,header=True)
    end = datetime.now()
    print(end-start)

## 웹 자동화는 셀레니움이 좋음. 그러나 동적페이지의 경우 html 추출까지는 셀레니움 분석엔 bs를 쓰는게 난이도와 속도의 균형에 좋음.