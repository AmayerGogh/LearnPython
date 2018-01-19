class HtmlOurputer(object):
    def __init__(self):
        self.datas =[]

    def collect_data(self,data):
        if data is None:
            return 
        self.datas.append(data)

    def output_html(self):
        with open('test.html', 'w',encoding='utf-8') as fout:              
            fout.write("<html><head><meta charset='utf-8'></head>")
            fout.write("<body>")            
            for item in self.datas:
                fout.write('<a href="%s">%s</a>' % (item['url'], item['title']))
                fout.write('<p>%s</p>' % item['summary'])
                fout.write('\r\n')
            fout.write("</body></html>")
       

