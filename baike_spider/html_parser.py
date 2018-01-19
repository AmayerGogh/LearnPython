import re
import urllib.parse
from bs4 import BeautifulSoup

class HtmlParser(object):
    def __get_new_urls(self,page_url,soup):
        new_urls =set()
        links =soup.find_all('a',href=re.compile(r'/item/'))
        for item in links:
            new_url=item['href']
            new_full_url=urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    def __get_new_data(self,page_url,soup):
        res_data ={}
        res_data['url'] =page_url
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title']=title_node.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node= soup.find('div',class_='lemma-summary')
        if summary_node is None:
            res_data['summary'] =''
            return res_data
        res_data['summary'] =summary_node.get_text()
        return res_data
    def parser(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup =BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls =self.__get_new_urls(page_url,soup)
        new_data =self.__get_new_data(page_url,soup)
        return new_urls,new_data