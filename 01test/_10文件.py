#读取文件
#f = open('c:/temp/3434.txt', 'r')
#print(f.read())
#f.close()
#with open('c:/temp/3434.txt', 'r',encoding='gbk') as f:
#    for line in f.readlines():
#        print(line.strip()) # 把末尾的'\n'删掉

## 二进制
#with open('c:/temp/3434.txt', 'rb') as f:
#    print(f.read())
#写
#with open('c:/temp/34342.txt', 'w') as f:
#    f.write('你好, world1!')
##追加
#with open('c:/temp/3434威威2.txt', 'a') as f:
#    f.write('你好, world1!')



# import os
# print(os.name)
# #print(os.uname())
# print(os.environ)

#操作流
# from io import StringIO
# f = StringIO()
# f.write("hello")
# print(f.getvalue())
# f.write(' world')
# print(f.getvalue())
# #读取
# f =StringIO('hello \n nihao \n ni \n hao')
# while True:
#     s =f.readline()
#     if s =='':
#         break
#     print(s.strip())
    

#test
with open('01test3434威威2.txt', 'a') as f:
   f.write('你好, world1!\r\n') 
print(1)      