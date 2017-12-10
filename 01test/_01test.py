
print("你好")
##基本语法
#打印
age = 1


# 变量
a='abc'
b =a
a='xyz'
print(b)

# 常量
#除法
print(10/3)
print(10//3) #//地板除
print(10%3) #求余数 
#字符串格式化
# 占位符 	替换内容
# %d 	整数
# %f 	浮点数
# %s 	字符串
# %x 	十六进制整数
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))


# if
if age >=18:
    print('1')
else :
    print("2")


#list
classmates = ['Michael', 'Bob', 'Tracy',2]
print(classmates)
#list 基本
#len(list) 长度
#list[i]  可以为复数
#append
#insert(i,item)
#pop(i) 删除  默认为最后一个

#tuple 数组

#for
#range() 生成一个整数序列
names =  list(range(10))
for name in names:
    print(name)


# while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#dict
