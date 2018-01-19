from urllib import request
from bs4 import BeautifulSoup
import requests
import os

class Spider():
    #这个正则写的很棒棒
    # 爬虫库 beautifulSoup ,Scrapy
   
    root_pattern ='<div class="video-info">([\s\S]*?)</div>'
    name_pattern ='</i>([\s\S]*?)</span>'
    number_pattern ='<span class="video-number">([\s\S]*?)</span>'
    def __fetch_content(self,url):
        req = request.Request(url)        
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')
        r = request.urlopen(req)
        htmls =r.read()              
        return htmls
    def __fetch_content_requests(self, url):
        '''
        Get the response of the page and then return
        :param url : url
        :return: content
        '''
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
        }
        content = requests.get(url, headers=header)
        content.encoding = 'gbk'
        return content.text
    def download_img(self,imageurl,image_dir,imageName ="xxx"):
        if not os.path.exists(image_dir):
            os.mkdir(image_dir)
        path=image_dir +imageName +'.jpg'
        print('downning... ' +imageurl)              
        try:
            rsp =requests.get(imageurl,stream =True)
            image =rsp.content              
            with open(path,'wb') as file:
                file.write(image) 
            print('ok 位置'+path ) 
        except Exception as e:
            print('错误:', e)        
    def __get_titles(self,htmls):
        soup =BeautifulSoup(htmls,'html.parser',from_encoding='utf-8')
        titles=soup.select('#ajaxtable tr.tr3 td.tal h3 a')
        titles =titles[9:]
        src= []        
        for title in titles:
             src.append(title['href'])
        return src    
    def __get_images(self,src):
        domain='https://cl.giit.us/'
        htmls= self.__fetch_content_requests(domain+src)        
        soup = BeautifulSoup(htmls, "html.parser")
        imgaes= soup.select("input[type='image']")
        srcs= []
        for item in imgaes:        
             srcs.append(item['src'])            
        return srcs
        
        
    def go(self):
        print('开始')
        url ='https://cl.giit.us/thread0806.php?fid=16&search=&page=1'
        htmls= self.__fetch_content(url)
        titles = self.__get_titles(htmls)
        i_out =1
        for src in titles:
            print("title 为"+src)
            images_src_list = self.__get_images(src)
            i=1
            for img_src in images_src_list:
                path ='c:/code/temp/%s/' % str(i_out)
                self.download_img(img_src,path,str(i))                
                i+=1
            i_out+=1    

#spider = Spider()
#spider.go()    