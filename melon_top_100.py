import requests as req
from bs4 import BeautifulSoup as bs

user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

res = req.get('https://www.melon.com/chart/index.htm', headers = user_agent)
soup = bs(res.text, 'lxml')

title = soup.select('div.ellipsis.rank01 > span > a')

singer = soup.select('span.checkEllipsis')

singer_list = []# 순수한 가수 이름 정보
title_list = []#순수한 노래 제목 정보

for i in range(len(singer)):
    singer_list.append(singer[i].text)
    title_list.append(title[i].text)

import pandas as pd
dic = {'가수':singer_list,'노래제목':title_list}
melon = pd.DataFrame(dic)

melon.to_csv('melon_top_100.csv',encoding = 'euc-kr')
