#BeautifulSoup的基本选择器和css选择器

from bs4 import BeautifulSoup

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

soup = BeautifulSoup(html_doc,'lxml')
#soup解析库自带的方法

#print(soup.title)
#<title>The Dormouse's story</title>

#print(soup.title.name)
#title

#print(soup.title.string)
#The Dormouse's story

#print(soup.title.parent.name)
#head

# print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>

#print(soup.p['class'])
#['title']

#print(soup.a)
#<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

#print(soup.find_all('a'))
#[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

#print(soup.find(id="link3"))
#<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# for link in soup.find_all('a'):
# 	print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie

# print(soup.get_text())
# The Dormouse's story

# The Dormouse's story
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
# ...

#body的所有字节点
#print(soup.body.contents)

#所有的后代节点
# for child in soup.descendants:
# 	print(child)

#CSS选择器
#print(soup.select('title'))
#[<title>The Dormouse's story</title>]

#print(soup.select('a'))
#[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

#print(soup.head.next_element)
#head的下一个子节点：<title>The Dormouse's story</title>

# print(soup.select('b'))
#选择《b》标签的 [<b>The Dormouse's story</b>]

#选择属性为sister的标签
#print(soup.select('.sister'))
#[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

#选择id为link的标签
# print(soup.select('#link1'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

#选择p标签里面id是link1的标签
# print(soup.select('p #link1'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

#选择head标签下面的title标签
# print(soup.select('head > title'))
# [<title>The Dormouse's story</title>]

#选取a标签中class=“sister”的标签
# print(soup.select('a[class="sister"]'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

#选择a标签中href=“”的标签
# print(soup.select('a[href="http://example.com/elsie"]'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

#选择p标签中a标签为href=“”
# print(soup.select('p a[href="http://example.com/elsie"]'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
