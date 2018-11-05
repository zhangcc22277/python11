#BesutifulSoup解析在线网页实例

import urllib
from bs4 import BeautifulSoup

url = urllib.request.urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup=BeautifulSoup(url.read(),'lxml')

namelist = soup.findAll('span',{'class':'green'})
for name in namelist:
	print(name.get_text)