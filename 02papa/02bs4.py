from bs4 import BeautifulSoup
import re
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
soup =BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
print('获取所有的链接')
links =soup.find_all('a')
for item in links:
    print(item.name,item['href'],item.get_text())

print('获取所有的lacie链接')    
linknode =soup.find_all('a',href='http://example.com/lacie')
for item in linknode:
    print(item.name,item['href'],item.get_text())

print('正则匹配')    
linknode =soup.find_all('a',href= re.compile(r'ill'))
for item in linknode:
    print(item.name,item['href'],item.get_text())
 
print('获取P')
pnode=soup.find_all('p',class_='title')
for link in pnode :
    print (link.name,link.get_text())    