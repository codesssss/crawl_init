import threading
import time
#多线程加法
exitFlag ,sum,count,result=0,0,0,1000000

class myThread_a (threading.Thread):
    def __init__(self, threadID: object, name: object, counter: object) -> object:
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        global sum,count,result
        print ("开始线程：" + self.name)
        while count<=result:
            threadLock_b.acquire()
            sum += count
            count+=1
            print("在打印的是：",self.name)
            print("计数为", count, "  ", "总数为", sum)
            time.sleep(0.0001)
            threadLock_a.release()

class myThread_b (threading.Thread):
    def __init__(self, threadID: object, name: object, counter: object) -> object:
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        global sum,count,result
        print ("开始线程：" + self.name)
        threadLock_a.acquire()
        while count<=result:
            threadLock_a.acquire()
            sum += count
            count+=1
            print("在打印的是：",self.name)
            print("计数为", count, "  ", "总数为", sum)
            time.sleep(0.0001)
            threadLock_b.release()



threadLock_a= threading.Lock()
threadLock_b= threading.Lock()
# 创建新线程
thread1 = myThread_a(1, "Thread-1", 1)
thread2 = myThread_b(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

