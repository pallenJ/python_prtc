import time
import pandas as pd

from selenium import webdriver

def get_replys(url,imp_time=5,delaytime = 0.1):


    # 웹드라이버
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(imp_time)
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

    # 댓글 추출
    contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
    contents = [content.text for content in contents]
    print('댓글 추출 완료')
    # 작성자

    nicks = driver.find_elements_by_css_selector('span.u_cbox_nick')
    nicks = [nick.text for nick in nicks]
    print('닉네임 추출 완료')

    # 날짜
    dates = driver.find_elements_by_css_selector('span.u_cbox_date')
    dates = [date.text for date in dates]
    print('날짜 추출 완료')

    # 취합

    replys = list(zip(nicks,dates,contents))
    # for reply in replys:
    #     print(reply)

    driver.quit()
    return replys;

if __name__ == '__main__':
    url = 'https://news.naver.com/main/read.nhn?m_view=1&includeAllCount=true&mode=LSD&mid=shm&sid1=102&oid=055&aid=0000803363'
    reply_data = get_replys(url)
    
    col = ['작성자','날짜','내용']
    data_frame = pd.DataFrame(reply_data,columns=col)
    data_frame.to_excel('news.xlsx', sheet_name="코로나 뉴스 테스트", startrow=0,header=True)
