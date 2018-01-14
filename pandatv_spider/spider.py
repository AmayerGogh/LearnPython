# ```
# 爬取的熊猫tv
# ```
from urllib import request
import re

class Spider():
    #这个正则写的很棒棒
    # 爬虫库 beautifulSoup ,Scrapy
    url ='https://www.panda.tv/cate/lol1'
    root_pattern ='<div class="video-info">([\s\S]*?)</div>'
    name_pattern ='</i>([\s\S]*?)</span>'
    number_pattern ='<span class="video-number">([\s\S]*?)</span>'
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls =r.read().decode('utf-8')
        #print(htmls)
        return htmls
 
    def __analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        anchors=[]
        for item in root_html:
            #print(item)
            name =re.findall(Spider.name_pattern,item)
            number =re.findall(Spider.number_pattern,item)
            anchor={'name':name,'number':number}            
            anchors.append(anchor)
        return anchors

    def __refine(self,anchors):
        l = lambda anchor:{
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
            }
        return map(l,anchors)

    def __sort(self,anchors):
        return sorted(anchors,key =self.__sort_seed,reverse=True)

    def __sort_seed(self,anchor):
        str_an = anchor['number']
        number =float(re.findall('\d*',str_an)[0])
        if '万' in str_an:
            number *=10000
        return number

    def __show(self,anchors):
        # for anchor in anchors:
        #     print(anchor['name']+'-----' +anchor['number'])
        for rank in range(0,len(anchors)):
            print('rank '  +str(rank +1)
            + ':' +anchors[rank]['name']
            + '   '+ anchors[rank]['number']
            )

    def go(self): #入口
        htmls = self.__fetch_content()
        anchors= self.__analysis(htmls)
        anchors =list(self.__refine(anchors))
        anchors =self.__sort(anchors)
        self.__show(anchors)
        


spider = Spider()
spider.go()        