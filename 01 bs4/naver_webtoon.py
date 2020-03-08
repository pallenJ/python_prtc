from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://comic.naver.com/webtoon/weekday.nhn');
soup = bs(html.text,'html.parser')
data1_list = soup.findAll('div', {'class': 'col_inner'})#모든 요일에 대해서

week_title_list = [];
week_title_list2 = [t.text for t in data1_list];

for data1 in data1_list :
    data2 = data1.findAll('a', {'class': 'title'})
    title_list = [t.text for t in data2]
    week_title_list.append(title_list);

pprint(week_title_list)
html.close();