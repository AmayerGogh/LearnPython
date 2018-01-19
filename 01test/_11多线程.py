import time,threading

#新线程执行的代码
def loop():
    print('线程 %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('线程 %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('线程 %s ended.' % threading.current_thread().name)


print('主线程 %s is running...' % threading.current_thread().name)
threads  =[]
for item in range(10):
    t = threading.Thread(target=loop, name='LoopThread'+ str(item+1))
    t.start()    
    threads.append(t)
for item in threads:
    item.join()    

#t2 = threading.Thread(target=loop, name='LoopThread2')

# t2.start()
# t.join()
# t2.join()
print('主线程 %s ended.' % threading.current_thread().name)