from django.db import models
#自定义管理器对象
class BookInfoManage(models.Manager):
    def get_queryset(self):
        return super(BookInfoManage,self).get_queryset().filter(
    isDelete=False)
    #对象方法
    def create(self,btitle):
        b =BookInfo()
        b.btitle =btitle
        return b

class BookInfo(models.Model)    :
    btitle =models.CharField(max_length=10)
    isDelete=models.BooleanField(default= False)
    class Meta:
        db_table ='bookinfo'
    books=models.Manager()    
    books2=BookInfoManage()
    #创建一个类方法
    @classmethod
    def create(cls,btitle):
        b =BookInfo()
        b.btitle =btitle
        return b