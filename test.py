import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
import codecs
import threading

def download_img(imageurl,image_dir,imageName ="xxx.jpg"):
    rsp =requests.get(imageurl,stream =True)
    image =rsp.content
    path=image_dir +imageName +'.jpg'
    with open(path,'wb') as file:
        file.write(image)

# download_img('http://python.jobbole.com/wp-content/themes/jobboleblogv3/_assets/img/jobbole-logo.png','c:/temp/')
# print(1)
def crawler(s,i,url,header,image_dir,txtfile):
    postData={'start':i}
    res =s.post(url,data=postData,header =header)
    soup =BeautifulSoup(res.content,'html.parser')
    table =soup.find_all('table',{'width':'100%'})
    sz =len(table)
    print(sz)


def main():
    url = "http://book.douban.com/top250?"
    txtfile = codecs.open("top2501.txt",'w','utf-8')
    header = { "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36",
           "Referer": "http://book.douban.com/"
           }
    image_dir = "C:/code/temp/"
    s =requests.Session()
    s.get(url,header)
    crawler(s,1,url,header,image_dir,txtfile)
    


if __name__ =='__main__':
    #main()        
    l =range(100)
    sl= l[5:]
    print(sl)
    for item in sl:
        print(item)
