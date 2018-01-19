# coding:utf8  
# """
# 爬取百度百科 1000个页面
# 视频地址https://www.imooc.com/video/10689
# github https://github.com/zision/Learn-PythonCrawler
# """
import url_manager ,html_outputer,html_downloader,html_parser

class SpiderMain(object):
    def __init__(self):
        self.urls =url_manager.UrlManager() #url管理器
        self.downloader =html_downloader.HtmlDownloader() #下载器
        self.parser =html_parser.HtmlParser() #解析器
        self.outputer=html_outputer.HtmlOurputer() #输入器

    def craw(self,root_url):
        count =1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d :%s' % (count,new_url) )
                html_cont =self.downloader.download(new_url)
                new_urls,new_data=self.parser.parser(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if  count >=100:
                    break
                count +=1
            except Exception as e:
                print(str(e))    
            self.outputer.output_html()
        print(root_url)
        pass

if __name__ =='__main__':
    root_url ='https://baike.baidu.com/item/Python/407313?fr=aladdin'
    obj_spider =SpiderMain()
    obj_spider.craw(root_url)
'''
爬虫思路
url管理器加入url
if url管理器有url
  获取url
  内容 = 下载器(url)
  更多的url,解析出来的数据  = 解析器(url,内容)
  url管理器 加入更多的url
  处理器    加入解析出来的数据
'''  
