
def add_end(L=[]):
    L.append('END')
    return L

print( add_end([1,2,3]))

print( add_end())
print( add_end())
# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


#*args是可变参数，args接收的是一个tuple；

#**kw是关键字参数，kw接收的是一个dict。

person('Adam', 45, gender='M', job='Engineer')

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)


#list切片函数
L = list(range(100))
print(L)
print(L[:10]) #前10 
print(L[1:10]) # 索引91 取到索引101 但不包括101
print(L[-10:]) # 后10



