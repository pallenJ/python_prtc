import time
from collections import Counter
from pprint import pprint
from selenium import webdriver


driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/color')
driver.implicitly_wait(300)


# print(len(btns))
btns = driver.find_elements_by_xpath('//*[@id="grid"]/div')


def analysis():

    btns_rgba = [btn.value_of_css_property('background-color') for btn in btns]
    # 백그라운드 컬러 추출
    #pprint(btns_rgba)

    result = Counter(btns_rgba)
    pprint(result)

    #값이 1인것 탐색
    for key, value in result.items():
        if value == 1:
            answer = key
            break
        else:
            answer = None
            print("정답을 찾을 수 없습니다.")

    # 정답클릭
    # 1. btns_rgba에서 인덱스값을 구함
    # 2. 해당 값으로 btns에 접근
    if answer :
        index = btns_rgba.index(answer)# indexOf와 같은 역할.
        btns[index].click();

## main
start = time.time()
while time.time() - start <=60:
    analysis()

