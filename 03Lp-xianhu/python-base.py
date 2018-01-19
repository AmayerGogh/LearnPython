# _*_ coding: utf-8 _*_
'''
学习python基本
源地址 https://github.com/xianhu/LearnPython/blob/master/python_base.py
?? :疑问
'''
class Teacher(object):
    def sayHello(self):
        print("你好")
teacher =Teacher()
isTrue =True
# dir_teacher =dir(teacher) # 简单的列出对象obj所包含的方法名称，返回一个字符串列表
# for item in dir_teacher:  
#     print(item)

# print(help(teacher.sayHello)) # 查询obj.func的具体介绍和用法

#-- 测试类型的三种方法，推荐第三种
# if type(teacher) ==type(Teacher):
#     print("true")
# else:
#     print("none")    
# if type(teacher) == Teacher:
#     print("true")    
# if isinstance(teacher, Teacher):
#     print("true")


#print(1 if isTrue else 2) # 三元表达式(有点奇葩)

# import decimal
# from decimal import Decimal
# result =Decimal('0.01') +Decimal('0.02')
# print(result)

#set
# s = set([3,5,9,10]) # 创建一个数值集合，返回{3, 5, 9, 10}
# t = set("Hello")  # 创建一个唯一字符的集合返回{}
# s.update([2,3,4,5,6,7]) #无则加,有则不变
# print(s)
# s.discard(2) #直接删除
# print(s)
# s.add('x')
# if 3 in s:
#     s.remove(3)
# print(s)
# print({x**2 for x in [1,2,3,4]}) # 集合解析，结果：{16, 1, 4, 9} ??
# print({x for x in 'spam'}) # 集合解析，结果：{'a', 'p', 's', 'm'}

#frozenset
# a = set([1, 2, 3])
# b = set([])
# b.add(a)                     # error: set是不可哈希类型
# b.add(frozenset(a)) # ok，将set变为frozenset，可哈希

#str
# print("s\np\ta\x00m" )
# print(r's\np\ta\x00m') # Raw字符串，不会进行转义，抑制转义
# print(b"Spadfsddm") # Python3中的字节字符串 ??
# print("""
# Spadfsddm
# sdfsdf
# sfd
# sdf
# """) # 多行str
# print("123213"\
#     "123213"\
#      "123123") # 多行str
# print(bin(1))

#str
#print([[1, 2], 'string', {}] )

#-- 文档字符串:出现在Module的开端以及其中函数或类的开端 使用三重引号字符串
# """
# module document
# """
# def func():
#     """
#     function document
#     """
#     print()
# class Employee(object):
#     """
#     class document
#     """
#     print()
# print(func.__doc__)     # 输出函数文档字符串
# print(Employee.__doc__) # 输出类的文档字符串

# #-- 嵌套函数举例:工厂函数
# def maker(N):
#     def action(X):
#         return X ** N
#     return action
# f = maker(2)                       # pass 2 to N
# print(f(3)) # 9, pass 3 to X


#-- 函数注解: 编写在def头部行 主要用于说明参数范围、参数类型、返回值类型等
# def func(a:'spam', b:(1, 10), c:float) -> int :
#     print(a, b, c)
# func.__annotations__               # {'c':<class 'float'>, 'b':(1, 10), 'a':'spam', 'return':<class 'int'>}
# # 编写注解的同时 还是可以使用函数默认值 并且注解的位置位于=号的前边
# def func(a:'spam'='a', b:(1, 10)=2, c:float=3) -> int :
#     print(a, b, c)

# #类
# print(teacher.__class__)
# print(teacher.__class__.__name__)
# print(teacher.__dict__)


#-- 类方法是对象:无绑定类方法对象 / 绑定实例方法对象
# class Spam(object):
#     def doit(self, message):
#         print(message)
#     def selfless(message):
#         print(message)
# obj = Spam()
# x = obj.doit                        # 类的绑定方法对象 实例 + 函数
# x('hello world')
# x = Spam.doit                       # 类的无绑定方法对象 类名 + 函数
# x(obj, 'hello world')
# x = Spam.selfless                   # 类的无绑定方法函数 在3.0之前无效
# x('hello world')

#-- 获取对象信息: 属性和方法
# dir(teacher)                              # 使用dir函数
# hasattr(teacher, 'x')                     # 测试是否有x属性或方法 即a.x是否已经存在
# setattr(teacher, 'y', 19)                 # 设置属性或方法 等同于a.y = 19
# getattr(teacher, 'z', 0)                  # 获取属性或方法 如果属性不存在 则返回默认值0
# #这里有个小技巧，setattr可以设置一个不能访问到的属性，即只能用getattr获取
# setattr(teacher, "can't touch", 100)      # 这里的属性名带有空格，不能直接访问
# getattr(teacher, "can't touch", 0)        # 但是可以用getattr获取

#-- 为类动态绑定属性或方法: MethodType方法
# 一般创建了一个class的实例后, 可以给该实例绑定任何属性和方法, 这就是动态语言的灵活性
# class Student(object):
#     pass
# s = Student()
# s.name = 'Michael'                  # 动态给实例绑定一个属性
# def set_age(self, age):             # 定义一个函数作为实例方法
#     self.age = age
# from types import MethodType
# s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法 类的其他实例不受此影响
# s.set_age(25)                       # 调用实例方法
# Student.set_age = MethodType(set_age, Student) # 为类绑定一个方法 类的所有实例都拥有该方法

#-- 类的继承和子类的初始化
    # 1.子类定义了__init__方法时，若未显示调用基类__init__方法，python不会帮你调用。
    # 2.子类未定义__init__方法时，python会自动帮你调用首个基类的__init__方法，注意是首个。
    # 3.子类显示调用基类的初始化函数：
# class FooParent(object):
#     def __init__(self, a):
#         self.parent = 'I\'m the Parent.'
#         print('Parent:a=' + str(a))
#     def bar(self, message):
#         print(message + ' from Parent')
# class FooChild(FooParent):
#     def __init__(self, a):
#         #FooParent.__init__(self, a)
#         print('Child:a=' + str(a))
#     # def bar(self, message):
#     #     #FooParent.bar(self, message)
#     #     print(message + ' from Child')
# fooChild = FooChild(10)
# fooChild.bar('HelloWorld') #并不会输出父类的

# #-- #实例方法 / 静态方法 / 类方法
# class Methods(object):
#     def imeth(self,x):
#         print(self,x)
#     def smeth(x):
#         print(x)
#     def cmeth(xxx,x):
#         print(xxx,x)
#     #imeth=classmethod(imeth) 不能这样
#     smeth = staticmethod(smeth) # 调用内置函数，也可以使用@staticmethod
#     cmeth = classmethod(cmeth)  # 调用内置函数，也可以使用@classmethod
# obj =Methods()     
# obj.imeth(1)          #<__main__.Methods object at 0x000002ACBDE5A080> 1
# Methods.imeth(obj, 2) #<__main__.Methods object at 0x000002ACBDE5A080> 2
# Methods.smeth(3)      # 3 静态方法
# obj.smeth(4)          # 4 静态方法也可以实例调用
# Methods.cmeth(5)      # <class '__main__.Methods'> 5
# obj.cmeth(6)          # <class '__main__.Methods'> 6
# #Methods.imeth(7)      #异常

#-- 函数装饰器:是它后边的函数的运行时的声明 由@符号以及后边紧跟的"元函数"(metafunction)组成
# @staticmethod
# def smeth(x): print(x)
# # 等同于:
# def smeth(x): print(x)
# smeth = staticmethod(smeth)
# # 同理
# @classmethod
# def cmeth(cls, x): print(x)
# # 等同于
# def cmeth(cls, x): print(x)
# cmeth = classmethod(cmeth)