from functools import reduce
def f(x):
    return x*x

r=map(f,range(10))
print(r)
print(list(r))

li =[]
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

def add(x,y):
    return x+y
re= reduce(add,range(10))
print(re)

def fn(x,y):
    return x*10 +y

print (reduce(fn,range(10)))

#demo 整数转换
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))
print(str2int("123123111"))

#filter

#py闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f4, f5, f6 = count2()

print(f4())
print(f5())
print(f6())


#装饰器

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-03-25')
ff=now
ff()
print(ff.__name__)

#偏函数   ，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
def int2(x,base =2):
    return int(x,base)
int2('1000000')

