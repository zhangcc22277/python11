#beautifulSoup中的主要参数的使用

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(html_doc,"lxml")

#text参数
#print(soup.find_all(text="Elsie"))
#['Elsie']
#print(soup.find_all(text=['Elsie','Lacie','Tillie']))
#['Elsie', 'Lacie', 'Tillie']
# print(soup.find_all(text=re.compile('Dormouse')))
#["The Dormouse's story", "The Dormouse's story"]

#limit参数-----a标签中的两个a标签
# print(soup.find_all('a',limit=2))
#[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

#t=recusive参数
# print(soup.html.find_all('title'))
# [<title>The Dormouse's story</title>]
# print(soup.html.find_all('title',recersive=False))
# [<title>The Dormouse's story</title>]

#tag对象


#NavigableString对象
#print(soup.p.string)
#The Dormouse's story
#print(type(soup.p.string))

#BeautifulSoup对象

