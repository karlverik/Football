import requests
from lxml import etree
#//*[@id="page-wrapper"]/div[3]/div/div/div/div/div[2]/table[1]/tbody/tr[2]/td[1]/text()
#//*[@id="mw-content-text"]/div/table[1]/tbody/tr[1]/td[1]/a
url = 'http://www.chezaiyi.cn/lifeculture/121244.html'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
res = requests.get(url,headers=headers).content.decode('utf-8')
tree = etree.HTML(res)
nation_asia = tree.xpath('//*[@id="page-wrapper"]/div[3]/div/div/div/div/div[2]/table[1]/tr/td[1]/text()')
nation_africa = tree.xpath('//*[@id="page-wrapper"]/div[3]/div/div/div/div/div[2]/table[2]/tr/td[1]/text()')
nation_north = tree.xpath('//*[@id="page-wrapper"]/div[3]/div/div/div/div/div[2]/table[3]/tr/td[1]/text()')
nation_south = tree.xpath('//*[@id="page-wrapper"]/div[3]/div/div/div/div/div[2]/table[4]/tr/td[1]/text()')
nation_ofc = tree.xpath('//*[@id="page-wrapper"]/div[3]/div/div/div/div/div[2]/table[5]/tr/td[1]/text()')
nation_europe = tree.xpath('//*[@id="page-wrapper"]/div[3]/div/div/div/div/div[2]/table[6]/tr/td[1]/text()')
print(nation_africa)
print(nation_asia)
print(nation_europe)
print(nation_north)
print(nation_south)
print(nation_ofc)