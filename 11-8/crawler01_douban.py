from bs4 import BeautifulSoup
import requests
# import urllib

url = 'https://book.douban.com/'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36'
}
response = requests.get(url=url,headers=headers).text
soup=BeautifulSoup(response,'lxml')
book_all = soup.find_all('p')

# book = book_all.find_all('span')
for t in book_all:
	print(t.get_text())
# book_title=book_all.find_all('a')
# title = book_all.find('a')
# for title in book_all:
# 	print(title.)
# book_title=book_all.find_all('a')
# print(book_title.get_text())