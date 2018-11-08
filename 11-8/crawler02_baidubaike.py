

from bs4 import BeautifulSoup
import requests
import re
import random

base_url = 'https://baike.baidu.com'
his=['/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB']
url = base_url + his[-1]

html = requests.get(url).text
soup=BeautifulSoup(html,'lxml')
# print(soup.find('h1').get_text(),'		url:',his[-1])
print(html)