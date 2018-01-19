# ss
import time,threading

def musicing(music):
    print('music playing...')
    for i in range(0,len(music)):
        print('第',str(i+1),"首歌是:",str(music[i]))
        print(time.strftime('%Y%H%M%S',time.localtime()))
        time.sleep(3)
        print("play next...")

def codding(line):
    print("我在打码") 
    j = 0
    while j <= line:
        print("我准备写入第" + str(j + 1) +"行代码")
        j = j + 1
        # 当前时间为
        print(time.strftime('%Y%H%M%S', time.localtime()))
        # 假设每写一行代码的时间为1秒
        time.sleep(1)
        print("写下一行代码...")

def default(music,number):
    # 开始听歌
    musicing(music)    
    # 开始打码
    codding(number)
def with_thread(music,number):
    threads =[]
    th1 =threading.Thread(target=musicing,args=(music,))
    threads.append(th1)
    th2 =threading.Thread(target=codding,args=(number,))
    threads.append(th2)
    for item in threads:
        item.setDaemon(True)
        item.start()

if __name__ =='__main__':
    # 设定我要听的歌为
    music = ["music1","music2","music3"]
    # 设定我要打码的行数
    line = 5

    start =time.time()
    #default(music,line) #常规的方式
    with_thread(music,line)
    end = time.time()
    print("完成的时间为：" + str(end - start))