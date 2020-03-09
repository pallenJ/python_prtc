from bs4 import BeautifulSoup as bs
from pprint import pprint
from urllib.request import urlretrieve
import requests, re , os
# re는 정규식을 가능케함
# os는 시스템 명령어를 실행하게 해줌

try:
    if not (os.path.isdir('image')):
        os.makedirs(os.path.join('image'))
except OSError as e:
    print("폴더 생성실패")
    exit()
#웹페이지를 열고 소스코드를 읽어옴
html = requests.get('https://comic.naver.com/webtoon/weekday.nhn');
soup = bs(html.text,'html.parser')
html.close()

#모든 요일에 대해서 요일별 웹툰영역 추출
data1_list = soup.findAll('div', {'class': 'col_inner'})
li_list = []
for data1 in data1_list:
    #제목과 썸네일 추출
    li_list.extend(data1.findAll('li')) #extend로 하나씩 다 추가
#pprint(li_list);

for li in li_list :
    img = li.find('img')
    title = img['title']
    title = re.sub('[^0-9a-zA-Zㄱ-힗]','',title) # 정규식으로 특수문자 제외
    img_src = img['src']
    print(title,img_src)
    urlretrieve(img_src,'./image/'+title+'.jpg') #주소, 파일경로 + 파일명+확장자
