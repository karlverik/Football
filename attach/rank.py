import requests
from lxml import etree
import xlrd

def rank_1():
    yearlist = [2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010]
    url = 'http://liansai.500.com/paiming/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    for year in yearlist:
        data = {'c': 'paiming',
                'm': 'main',
                'lselect': str(year) + '-1'}
        res = requests.post(url, headers=headers,data=data).text
        tree = etree.HTML(res)
        rk = tree.xpath('//*[@class="pm_data"]/tr/td[1]/text()')
        name = tree.xpath('//*[@class="pm_data"]/tr/td[2]/text()')
        dict_1 = {}

def nation():
    dict = {}
    file = xlrd.open_workbook('football_rank.xls')
    nation = file.sheet_names()
    for i in nation:
        c = i.split('_')
        dict[c[1]] = c[0]
    return(dict)


dict = {}
def rank_2():
    yearlist = [2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011]
    location = [1,2,3,4,5,6]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    for loc in location:
        data = {'sex': '0',
                'season': '2018',
                'month': '1'}
        url = 'http://zq.win007.com/cn/paiming.html?location=%s'%(loc)
        res = requests.post(url, headers=headers, data=data).text
        tree = etree.HTML(res)
        #rk = tree.xpath('//*[@id="div_Table1"]/tr/td[1]/text()')
        name = tree.xpath('//*[@id="div_Table1"]/tr/td[2]/a/text()')
        list_1 = []
        nation_list = nation()
        for i in name:
            i = i.rstrip(' ')
            if i in nation_list.keys():
                c = str(nation_list[i]) +'_'+i
                list_1.append(c)
        print(list_1)
        dict[loc] = list_1


rank_2()
asa = dict[1]
eup = dict[2]
afc = dict[3]
sa = dict[4]
ofc = dict[5]
na = dict[6]
print(asa)
print(eup)
print(afc)
print(sa)
print(ofc)
print(na)





