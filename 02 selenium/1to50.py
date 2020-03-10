from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/1to50')
driver.implicitly_wait(300)

num =1

def clickBtn():
    # 1 to 50 게임의 각각의 버튼 가져옴
    global num
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

    for btn in btns:
        if btn.text == str(num): # 문자열로 형변환후 비교
            btn.click()
            num+=1
            return

## main code
while num<=50:
    clickBtn()
