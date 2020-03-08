from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨');
# pprint(html.text)
soup = bs(html.text,'html.parser')
# pprint(soup)

data1 = soup.find('div',{'class':'detail_box'})#같은게 여러개 있을경우 첫번째 탐색할걸 반환
# pprint(data1)

data2 = data1.findAll('dd');
# pprint(data2)

find_dust = data2[0].find('span',{'class':'num'})
pprint(find_dust.text) # text 부분만 가져올때 .text

