from django.contrib import admin
from .models import *

#在添加一个表的同时 关联3个英雄
class HeroInfoInline(admin.TabularInline): #可以换成 StackedInline 
    model=HeroInfo
    extra =3




class BookInfoAdmin(admin.ModelAdmin):
    '''
    
    '''
    #控制显示的字段
    list_display=['id','btitle','bpub_date']
    #过滤
    list_filter=['btitle']
    #
    search_fields=['btitle']
    list_per_page=1

    fieldsets=[
        ('基础',{'fields':['btitle']}),
        ('继续编辑',{'fields':['bpub_date']})

    ]
    # 关联表 添加一个book的同时 关联3个英雄
    inlines =[HeroInfoInline]

# Register your models here.
# 注册这些类
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)