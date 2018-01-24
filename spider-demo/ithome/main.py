        from urllib import request
from bs4 import BeautifulSoup
import requests
import os
import threading

class Spider():
    def __fetch_content(self,url):
        req = request.Request(url)        
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')
        r = request.urlopen(req)
        htmls =r.read()              
        return htmls
    def __get_titles(self,htmls):
        soup =BeautifulSoup(htmls,'html.parser',from_encoding='utf-8')      
        soup_item =soup.select('ul.ulcl li .block h2 ')        
        return_list= []        
        for item in soup_item:            
            title = item.select('a')[0]
            date =item.select('span.state')[0].string  
            return_list.append ({
                'href':title['href'],
                'title':title.string,
                'date':date
            })           
        return return_list    
    def __get_content(self):
        pass
    def __get_commonts(self):
        '''
        获取评论区
        https://dyn.ithome.com/comment/344038
        '''
        pass    
    def __print_title(self,titles):
        pass
        
    def main(self):
        domain ="https://www.ithome.com/"
        htmls = self.__fetch_content(domain +'ithome/getajaxdata.aspx?page=1&type=indexpage')
        titles=self.__get_titles(htmls)
        print(titles)

spider = Spider()
spider.main()  