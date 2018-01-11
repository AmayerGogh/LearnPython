from collections import Iterable
import os
#list切片函数
L = list(range(100))
print(L)
print(L[:10]) #前10 
print(L[1:10]) # 索引91 取到索引101 但不包括101
print(L[-10:]) # 后10
print(L[:10:2]) #前10个数 每两个取1个
#用来判断是否可以for
_list ="abcdefghijklmnopqrstuvwxyz"
canIterable = isinstance(_list,Iterable)

if(canIterable):
    print(canIterable)
    for item in _list:
        print(item)

#内置元素对
for i, item in enumerate(['A', 'B', 'C']):
    print(i, item)
#这也可以,厉害了   
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


#列表生成式    
_list2 =[x * x for x in range(1, 11) if x % 2 == 0]
print(_list2)

#ext 
_list3 = [d for d in os.listdir('.')]
print(_list3)

#列表生成器 generator
_g1 =(d for  d in range(10))
print(_g1)
print(next(_g1))
print(next(_g1))
print(next(_g1))
print(next(_g1))
for item in _g1:
    print(item)