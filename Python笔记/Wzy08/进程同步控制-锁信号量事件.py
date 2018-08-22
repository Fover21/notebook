********进程同步控制********


****锁--multiprocessing.Lock****

通过学习，我么实现了程序的异步，让多个任务可以同时在几个进程中处理，他们之间的运行没有顺序，一旦
开启不受我们控制。尽管并发编程让我们能更加充分的利用IO资源，但是也给我们带来了新的问题

当多个进程使用同一份数据资源的时候，就会引发数据安全或顺序混乱问题。


**多进程抢占资源

import os
import time
import random
from multiprocessing import Process


def work(n):
    print('%s: %s is running' % (n, os.getpid()))
    time.sleep(random.random())
    print('%s:%s is done' % (n, os.getpid()))


if __name__ == '__main__':
    for i in range(3):
        p = Process(target=work, args=(i,))
        p.start()

**使用锁维护执行顺序
由并发变成了串行，牺牲了运行效率，但避免了竞争

import time
import random
import os
from multiprocessing import Process,Lock


def work(n, l):
    l.acquire()
    print('%s: %s is running' % (n, os.getpid()))
    time.sleep(random.random())
    print('%s:%s is done' % (n, os.getpid()))
    l.release()

if __name__ == '__main__':
    l = Lock()
    for i in range(3):
        p = Process(target=work, args=(i,l))
        p.start()

上面这种情况虽然使用加锁的形式实现了顺序的执行，但是程序又重新变成串行了，这样确实会浪费了时间，却保证了数据的安全。

接下来，我们以模拟抢票为例，来看看数据安全的重要性。

from multiprocessing import Lock, Process
import time


def show(i):  # 产看余票信息
    with open('余票') as f:
        temp = f.read()
    print('第%s个人查到还有余票%s' % (i, temp))


def buy(i, l):  # 买票
    l.acquire()
    with open('余票') as f:
        temp = int(f.read())
    time.sleep(0.1)
    if temp > 0:
        temp -= 1
        print('\033[31m 第%s个人买到了票\033[0m' % i)
    else:
        print('\033[32m第%s个人没有买到票\033[0m' % i)
    time.sleep(0.1)
    with open('余票', 'w') as f:
        f.write(str(temp))
    l.release()


if __name__ == '__main__':

    l = Lock()

    for i in range(10):  # 多用户查看票数
        p = Process(target=show, args=(i + 1,))
        p.start()

    for i in range(10):  # 模拟并发多个用户抢票
        p = Process(target=buy, args=(i + 1, l))
        p.start()


#加锁可以保证多个进程修改同一块数据时，同一时间只能有一个任务可以进行修改，
#即串行的修改，没错，速度是慢了，但牺牲了速度却保证了数据安全。
虽然可以用文件共享数据实现进程间通信，但问题是：
1.效率低（共享数据基于文件，而文件是硬盘上的数据）
2.需要自己加锁处理

#因此我们最好找寻一种解决方案能够兼顾：
1、效率高（多个进程共享一块内存的数据）
2、帮我们处理好锁问题。这就是mutiprocessing模块为我们提供的基于消息的IPC通信机制：队列和管道。
队列和管道都是将数据存放于内存中
队列又是基于（管道+锁）实现的，可以让我们从复杂的锁问题中解脱出来，
我们应该尽量避免使用共享数据，尽可能使用消息传递和队列，避免处理复杂的同步和锁问题，
而且在进程数目增多时，往往可以获得更好的可获展性。



****信号量****

介绍：
互斥锁同时只允许一个线程更改数据，而信号量Semaphore是同时允许一定数量的线程更改数据 。
假设商场里有4个迷你唱吧，所以同时可以进去4个人，如果来了第五个人就要在外面等待，等到有人出来才能再进去玩。
实现：
信号量同步基于内部计数器，每调用一次acquire()，计数器减1；每调用一次release()，计数器加1.当计数器为0时，
acquire()调用被阻塞。这是迪科斯彻（Dijkstra）信号量概念P()和V()的Python实现。信号量同步机制适用于访问
像服务器这样的有限资源。

信号量与进程池的概念很像，但是要区分开，信号量涉及到加锁的概念

from multiprocessing import Process, Semaphore
import time, random


def work(sem, user):
    sem.acquire()
    print('%s 占到一个房间' % user)
    time.sleep(random.random())  # 模拟在房间中待的时间
    sem.release()


if __name__ == '__main__':
    sem = Semaphore(4)
    p_ls = []
    for i in range(10):
        p = Process(target=work, args=(sem, 'user %s' % i,))
        p.start()
        p_ls.append(p)

    [i.join() for i in p_ls]
    print('>>>>>>>>>>>>>>>>>>>')


****事件****


python线程的事件用于主线程控制其他线程的执行，事件主要提供了三个方法 set、wait、clear。

事件处理的机制：is_set() 方法的值，默认为False
那么当程序执行 event.wait 方法时就会阻塞，
如果is_set()值为True，那么event.wait 方法执行时便不再阻塞。

clear()方法：将is_set()的值设置为False
set()方法：将is_set()的值设置为True



红绿灯实例：

from multiprocessing import Process, Event
import time
import random


# 亮灯和车行驶是异步的
# 亮灯的进程先开启
# is_set()刚开始默认为False
# 先开始l绿灯亮，这个时候car的进程开启，is_set()为True，可以过车

def light(e):
    while 1:
        if e.is_set():
            e.clear()
            print('\033[31m红灯亮了\033[0m')
        else:
            e.set()
            print('\033[32m绿灯亮了\033[0m')
        time.sleep(2)


def cars(i, e):
    if not e.is_set():
        print('第%s辆车在等待' % i)
        e.wait()
    print('第%s辆车过去了' % i)


if __name__ == '__main__':

    e = Event()
    tr = Process(target=light, args=(e,))  # 创建一个进程控制红绿灯
    tr.start()

    for i in range(50):  # 创建50个进程代表50辆车
        car = Process(target=cars, args=(i + 1, e))
        car.start()
        time.sleep(random.random())

























