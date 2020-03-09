from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://comic.naver.com/webtoon/weekday.nhn');
soup = bs(html.text,'html.parser')
html.close()
data1_list = soup.findAll('div', {'class': 'col_inner'})#모든 요일에 대해서

li_list = []
for data1 in data1_list:
    #제목과 썸네일 추출
    li_list.extend(data1.findAll('li')) #extend로 하나씩 다 추가
pprint(li_list);
