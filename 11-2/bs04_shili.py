import requests
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/warandpeace.html'
response = requests.get(url).text

soup = BeautifulSoup(response,'lxml')
alltext = soup.findAll(id='text')
print(alltext[0].get_text())