# @Time    : 2019/07/01 7:55AM
# @Author  : HGzhao
# @File    : parser_storage.py

from bs4 import BeautifulSoup
import pandas as pd
import requests

# 请求弹幕数据
url = 'http://comment.bilibili.com/99768393.xml'
html = requests.get(url).content

# 解析弹幕数据
html_data = str(html, 'utf-8')
bs4 = BeautifulSoup(html_data, 'lxml')
results = bs4.find_all('d')
comments = [comment.text for comment in results]
comments_dict = {'comments': comments}

# 将弹幕数据保存在本地
br = pd.DataFrame(comments_dict)
br.to_csv('barrage.csv', encoding='utf-8')
