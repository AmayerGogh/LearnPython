from django.shortcuts import render
from django.http import *
#from django.template import RequestContext,loader
from .models import *
# Create your views here.
def index(request):
    #retrun HttpResponse('hello')
    #去这里加载模板
    #方式一
    # temp=loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())
    #方式二 (推荐)
    #return render(request,'booktest/index.html')

    bookList =BookInfo.objects.all()
    context ={'list':bookList}
    return render(request,'booktest/index.html',context)

def detail(request,id):
    book = BookInfo.objects.get(pk=id)
    heroList =book.heroinfo_set.all()
    context={'list':heroList}
    return render(request,'booktest/detail.html',context)