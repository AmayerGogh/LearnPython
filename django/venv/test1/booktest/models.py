from django.db import models

# Create your models here.
# 要继承这个 才能被认定为数据库model
class BookInfo(models.Model):
    #只能用规定的数据类型
    btitle =models.CharField(max_length=20)
    bpub_date =models.DateTimeField()
    #后台默认模板显示这个
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname =models.CharField(max_length=10)
    hgender=models.BooleanField()
    hcontent =models.CharField(max_length=1000)
    hbook =models.ForeignKey(BookInfo) #接book表
    def __str__(self):
        return self.hname

