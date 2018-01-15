from urllib import request
from bs4 import BeautifulSoup
class Spider():
    #这个正则写的很棒棒
    # 爬虫库 beautifulSoup ,Scrapy
    url ='https://cl.giit.us/thread0806.php?fid=16&search=&page=1'
    root_pattern ='<div class="video-info">([\s\S]*?)</div>'
    name_pattern ='</i>([\s\S]*?)</span>'
    number_pattern ='<span class="video-number">([\s\S]*?)</span>'
    def __fetch_content(self):
        req = request.Request(Spider.url)        
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')
        r = request.urlopen(req)
        htmls =r.read()              
        return htmls
    def __soup(self,htmls):
        soup =BeautifulSoup(self.__fetch_content(),'html.parser',from_encoding='utf-8')
        print(soup.select('#ajaxtable tr.tr3 td.tal h3 a'))
        print(1)
    def go(self):
        htmls= self.__fetch_content()
        self.__soup(htmls)

spider = Spider()
spider.go()    
