# coding:utf-8
from timeit import Timer
li =[1,2]
li2 =[23,5]


def test1():
    li=[]
    for i in range(10000):
        li.append(i)
# 最慢
def test2():
    li =[]
    for i in range(10000):
        li += [i]
def test3():
    li =[i for  i in range (10000) ]
def test4():
    li =list(range(10000))    
def test5():
    li =[]
    for i in range(10000):
        li.extend([i])


timer1= Timer("test1()","from __main__ import test1")
print(timer1.timeit(10),'秒')

timer2= Timer("test2()","from __main__ import test2")
print(timer2.timeit(10),'秒')

timer3= Timer("test3()","from __main__ import test3")
print(timer3.timeit(10),'秒')

timer4= Timer("test4()","from __main__ import test4")
print(timer4.timeit(10),'秒')

timer5= Timer("test5()","from __main__ import test5")
print(timer5.timeit(10),'秒')

# 0.4525510287863113 秒
# 3.6852624102993583 秒
# 0.2072015041791877 秒
# 0.003794111368376818 秒
# 0.725194180337291 秒
