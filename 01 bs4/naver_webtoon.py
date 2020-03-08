from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://comic.naver.com/webtoon/weekday.nhn');
soup = bs(html.text,'html.parser')
data1 = soup.findAll('div',{'class':'col_inner'})[6]
data2 = data1.findAll('a',{'class':'title'})

title_list = []
for t in data2 :
    title_list.append(t.text);

pprint(title_list)
html.close();