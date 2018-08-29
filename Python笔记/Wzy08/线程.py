*********线程和python********


******理论知识******

****全局解释器锁（GIL）****

Python代码的执行由Python虚拟机（也叫解释器主循环）来控制。Python在设计之初就考虑到要在主循环中，
同时只有一个线程在执行。虽然Python解释器中可以“运行”多个线程，但在任意时刻只有一个线程在解释器中运行。
对Python虚拟机的访问由全局解释器锁（GIL）来控制，正式这个锁能保证同一个时刻只有一个线程在运行。

在多线程环境中，Python虚拟机 按以下方式执行：

a、设置GIL
b、切换到一个线程去运行
c、运行指定数量的字节码指令或者线程主动让出控制（可以调用time.sleep(0)）
d、把线程设置为睡眠状态
e、解锁GIL
d、再次重复以上所有步骤

在调用外部代码（如 C/C++扩展函数）的时候，GIL将会被锁定，直到这个函数结束为止（由于在这期间,
没有Python的字节码被运行，所以不会做线程切换）编写扩展的程序U员可以主动解锁GIL。 


****Python线程模块的选择****

Python提供了几个用于多线程编程的模块，包括thread、threading和Queue等。thread和threading
模块允许程序员创建和管理线程。thread模块提供了基本的线程和锁的支持，threading提供了更高级别、
功能更强的线程管理的功能。Queue模块允许用户创建一个可以用于多个线程之间共享数据的队列数据结构。
避免使用thread模块，因为更高级别的threading模块更为先进，对线程的支持更为完善，而且使用thread
模块里的属性有可能会与threading出现冲突；其次低级别的thread模块的同步原语很少(实际上只有一个)，
而threading模块则有很多；再者，thread模块中当主线程结束时，所有的线程都会被强制结束掉，没有警
告也不会有正常的清除工作，至少threading模块能确保重要的子线程退出后进程才退出。 

thread模块不支持守护线程，当主线程退出时，所有的子线程不论它们是否还在工作，都会被强行退出。
threading模块支持守护线程，守护线程一般是一个等待客户请求的服务器，如果没有客户提出请求它就
在那等着，如果设定一个线程为守护线程，就表示这个线程是不重要的，在进程退出的时候，不用等待这
个线程退出

********threading模块*********

multiprocessing模块完全模仿了threading模块的接口，二者在使用层面，有很大的相似性。

*****线程的创建Threading.Thread类****

**线程的创建**

方式1：
from threading import Thread
import time


def func(name):
    time.sleep(2)
    print('My name is %s' % name)


t = Thread(target=func, args=('Tom',))
t.start()
print('There is 主线程')

方式2：
from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(2)
        print('My name is %s' % self.name)


t = MyThread('Tom')
t.start()
print('There is 主线程')


**多线程与多进程**

*pid比较

from threading import Thread
from multiprocessing import Process
import os


def work():
    print('hello', os.getpid())


if __name__ == '__main__':
    # part1:在主进程下开启多个线程,每个线程都跟主进程的pid一样
    t1 = Thread(target=work)
    t2 = Thread(target=work)
    t1.start()
    t2.start()
    print('主线程/主进程pid', os.getpid())

    # part2:开多个进程,每个进程都有不同的pid
    p1 = Process(target=work)
    p2 = Process(target=work)
    p1.start()
    p2.start()
    print('主线程/主进程pid', os.getpid())

*开启效率的较量

from multiprocessing import Process
from threading import Thread


def work():
    print('hello')


if __name__ == '__main__':
    # 在主进程下开启线程
    t = Thread(target=work)
    t.start()
    print('主线程/主进程')
    '''
    打印结果:
    hello
    主线程/主进程
    '''

    # 在主进程下开启子进程
    t = Process(target=work)
    t.start()
    print('主线程/主进程')
    '''
    打印结果:
    主线程/主进程
    hello
    '''

*内存数据的共享问题

from threading import Thread
from multiprocessing import Process
import os


def work():
    global n
    n = 0


if __name__ == '__main__':
    # n=100
    # p=Process(target=work)
    # p.start()
    # p.join()
    # print('主',n) #毫无疑问子进程p已经将自己的全局的n改成了0,但改的仅仅是它自己的,查看父进程的n仍然为100

    n = 1
    t = Thread(target=work)
    t.start()
    t.join()
    print('主', n)  # 查看结果为0,因为同一进程内的线程之间共享进程内的数据

**Thread类的其他方法**

Thread实例对象的方法
  # isAlive(): 返回线程是否活动的。
  # getName(): 返回线程名。
  # setName(): 设置线程名。

threading模块提供的一些方法：
  # threading.currentThread(): 返回当前的线程变量。
  # threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
  # threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

from threading import Thread
import threading
from multiprocessing import Process
import os


def work():
    import time
    time.sleep(3)
    print(threading.current_thread().getName())


if __name__ == '__main__':
    # 在主进程下开启线程
    t = Thread(target=work)
    t.start()

    print(threading.current_thread().getName())
    print(threading.current_thread())  # 主线程
    print(threading.enumerate())  # 连同主线程在内有两个运行的线程
    print(threading.active_count())
    print('主线程/主进程')


join方法

from threading import Thread
import time


def sayhi(name):
    time.sleep(2)
    print('%s say hello' % name)


if __name__ == '__main__':
    t = Thread(target=sayhi, args=('egon',))
    t.start()
    t.join()
    print('主线程')
    print(t.is_alive())



**守护线程**

无论是进程还是线程，都遵循：守护xx会等待主xx运行完毕后被销毁。需要强调的是：运行完毕并非终止运行

#1.对主进程来说，运行完毕指的是主进程代码运行完毕
#2.对主线程来说，运行完毕指的是主线程所在的进程内所有非守护线程统统运行完毕，主线程才算运行完毕


#1 主进程在其代码结束后就已经算运行完毕了（守护进程在此时就被回收）,然后主进程会一直等非守护的
#子进程都运行完毕后回收子进程的资源(否则会产生僵尸进程)，才会结束，
#2 主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收）。因为主线程的结束意味
#着进程的结束，进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束。

from threading import Thread
import time


def work():
    time.sleep(5)
    print('in work')


def work1():
    time.sleep(2)
    print('in work1')


f = Thread(target=work)
f1 = Thread(target=work1)
f.daemon = True
f.start()
f1.start()

****锁****

**锁与GIL**
**同步锁**

*多个线程抢占资源的情况

from threading import Thread, Lock
import time


def work(R):
    global n
    #R.acquire()
    temp = n
    time.sleep(0.1)
    n = temp - 1
    #R.release()

if __name__ == '__main__':
    #R = Lock()
    n = 100
    l = []
    for i in range(10):
        p = Thread(target=work,args=(R,))
        l.append(p)
        p.start()
    for p in l:
        p.join()

    print(n)




import threading
R=threading.Lock()
R.acquire()
'''
对公共数据的操作
'''
R.release()


*互斥锁与join的区别

#不加锁:并发执行,速度快,数据不安全
from threading import current_thread,Thread,Lock
import os,time
def task():
    global n
    print('%s is running' %current_thread().getName())
    temp=n
    time.sleep(0.5)
    n=temp-1


if __name__ == '__main__':
    n=100
    lock=Lock()
    threads=[]
    start_time=time.time()
    for i in range(100):
        t=Thread(target=task)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    stop_time=time.time()
    print('主:%s n:%s' %(stop_time-start_time,n))


# 不加锁:未加锁部分并发执行,加锁部分串行执行,速度慢,数据安全
from threading import current_thread, Thread, Lock
import os, time


def task():
    # 未加锁的代码并发运行
    time.sleep(3)
    print('%s start to run' % current_thread().getName())
    global n
    # 加锁的代码串行运行
    lock.acquire()
    temp = n
    time.sleep(0.5)
    n = temp - 1
    lock.release()


if __name__ == '__main__':
    n = 100
    lock = Lock()
    threads = []
    start_time = time.time()
    for i in range(10):
        t = Thread(target=task)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    stop_time = time.time()
    print('主:%s n:%s' % (stop_time - start_time, n))

既然加锁会让运行变成串行,那么我在start之后立即使用join,就不用加锁了啊,也是串行的效果啊
#没错:在start之后立刻使用jion,肯定会将10个任务的执行变成串行,毫无疑问,最终n的结果也肯定是90,是安全的,但问题是
#start后立即join:任务内的所有代码都是串行执行的,而加锁,只是加锁的部分即修改共享数据的部分是串行的
#单从保证数据安全方面,二者都可以实现,但很明显是加锁的效率更高.

from threading import current_thread,Thread,Lock
import os,time
def task():
    time.sleep(3)
    print('%s start to run' %current_thread().getName())
    global n
    temp=n
    time.sleep(0.5)
    n=temp-1


if __name__ == '__main__':
    n=100
    lock=Lock()
    start_time=time.time()
    for i in range(100):
        t=Thread(target=task)
        t.start()
        t.join()
    stop_time=time.time()
    print('主:%s n:%s' %(stop_time-start_time,n))

 #耗时是多么的恐怖

**死锁与递归锁**

进程也有死锁与递归锁

所谓死锁： 是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，
若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等
待的进程称为死锁进程，如下就是死锁

from threading import Lock as Lock
import time
mutexA=Lock()
mutexA.acquire()
mutexA.acquire()
print(123)
mutexA.release()
mutexA.release()

解决方法，递归锁，在Python中为了支持在同一线程中多次请求同一资源，python提供了可重入锁RLock。

这个RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可
以被多次require。直到一个线程所有的acquire都被release，其他的线程才能获得资源。上面的例子
如果使用RLock代替Lock，则不会发生死锁


*递归锁RLock

from threading import RLock as Lock
import time
mutexA=Lock()
mutexA.acquire()
mutexA.acquire()
print(123)
mutexA.release()
mutexA.release()


######典型问题******科学家吃面问题

# import time
# from threading import Thread, Lock
#
# noodle_lock = Lock()
# fork_lock = Lock()
#
#
# def eat1(name):
#     noodle_lock.acquire()
#     print('%s 抢到了面条' % name)
#     fork_lock.acquire()
#     print('%s 抢到了叉子' % name)
#     print('%s 吃面' % name)
#     fork_lock.release()
#     noodle_lock.release()
#
#
# def eat2(name):
#     fork_lock.acquire()
#     print('%s 抢到了叉子' % name)
#     time.sleep(1)
#     noodle_lock.acquire()
#     print('%s 抢到了面条' % name)
#     print('%s 吃面' % name)
#     noodle_lock.release()
#     fork_lock.release()


import time
from threading import Thread, RLock

fork_lock = noodle_lock = RLock()


def eat1(name):
    noodle_lock.acquire()
    print('%s 抢到了面条' % name)
    fork_lock.acquire()
    print('%s 抢到了叉子' % name)
    print('%s 吃面' % name)
    fork_lock.release()
    noodle_lock.release()


def eat2(name):
    fork_lock.acquire()
    print('%s 抢到了叉子' % name)
    time.sleep(1)
    noodle_lock.acquire()
    print('%s 抢到了面条' % name)
    print('%s 吃面' % name)
    noodle_lock.release()
    fork_lock.release()


for name in ['Jake', 'Tom', 'Wzy']:
    t1 = Thread(target=eat1, args=(name,))
    t2 = Thread(target=eat2, args=(name,))
    t1.start()
    t2.start()



****信号量****

同进程的一样

Semaphore管理一个内置的计数器，
每当调用acquire()时内置计数器-1；
调用release() 时内置计数器+1；
计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()。

实例：(同时只有5个线程可以获得semaphore,即可以限制最大连接数为5)：

from threading import Thread, Semaphore
import threading
import time


def func():
    sm.acquire()
    print('%s get sm' % threading.current_thread().getName())
    time.sleep(3)
    sm.release()


if __name__ == '__main__':
    sm = Semaphore(5)
    for i in range(23):
        t = Thread(target=func)
        t.start()



****事件****

同进程的一样

线程的一个关键特性是每个线程都是独立运行且状态不可预测。如果程序中的其 他线程需要通过判断某个
线程的状态来确定自己下一步的操作,这时线程同步问题就会变得非常棘手。为了解决这些问题,我们需要
使用threading库中的Event对象。 对象包含一个可由线程设置的信号标志,它允许线程等待某些事件的
发生。在 初始情况下,Event对象中的信号标志被设置为假。如果有线程等待一个Event对象, 而这个
Event对象的标志为假,那么这个线程将会被一直阻塞直至该标志为真。一个线程如果将一个Event对象的
信号标志设置为真,它将唤醒所有等待这个Event对象的线程。如果一个线程等待一个已经被设置为真的
Event对象,那么它将忽略这个事件, 继续执行

event.is_set()：返回event的状态值；
event.wait()：如果 event.isSet()==False将阻塞线程；
event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
event.clear()：恢复event的状态值为False。


例如，有多个工作线程尝试链接MySQL，我们想要在链接前确保MySQL服务正常才让那些工作线程去连接
MySQL服务器，如果连接不成功，都会去尝试重新连接。那么我们就可以采用threading.Event机制来
协调各个工作线程的连接操作


import threading
import time, random
from threading import Thread, Event


def conn_mysql():
    count = 1
    while not event.is_set():
        if count > 3:
            raise TimeoutError('链接超时')
        print('<%s>第%s次尝试链接' % (threading.current_thread().getName(), count))
        event.wait(0.5)
        count += 1
    print('<%s>链接成功' % threading.current_thread().getName())


def check_mysql():
    print('\033[45m[%s]正在检查mysql\033[0m' % threading.current_thread().getName())
    time.sleep(random.randint(1, 3))
    event.set()


if __name__ == '__main__':
    event = Event()
    conn1 = Thread(target=conn_mysql)
    conn2 = Thread(target=conn_mysql)
    check = Thread(target=check_mysql)

    conn1.start()
    conn2.start()
    check.start()



****条件****

使得线程等待，只有满足某条件时，才释放n个线程

Python提供的Condition对象提供了对复杂线程同步问题的支持。Condition被称为条件变量，除了提供
与Lock类似的acquire和release方法外，还提供了wait和notify方法。线程首先acquire一个条件变量，
然后判断一些条件。如果条件不满足则wait；如果条件满足，进行一些处理改变条件后，通过notify方法通
知其他线程，其他处于wait状态的线程接到通知后会重新判断条件。不断的重复这一过程，从而解决复杂的
同步问题。

import threading


def run(n):
    con.acquire()
    con.wait()
    print("run the thread: %s" % n)
    con.release()


if __name__ == '__main__':

    con = threading.Condition()
    for i in range(10):
        t = threading.Thread(target=run, args=(i,))
        t.start()

    while True:
        inp = input('>>>')
        if inp == 'q':
            break
        con.acquire()
        con.notify(int(inp))
        con.release()
        print('****')


****定时器****

定时器，指定n秒后执行某个操作


from threading import Timer
 
def hello():
    print("hello, world")
 
t = Timer(1, hello)
t.start()  # after 1 seconds, "hello, world" will be printed


****线程队列****

queue队列 ：使用import queue，用法与进程Queue一样

queue is especially useful in threaded programming when information must be 
exchanged safely between multiple threads.

class queue.Queue(maxsize=0) #first in first out 先进先出

import queue

q=queue.Queue()
q.put('first')
q.put('second')
q.put('third')

print(q.get())
print(q.get())
print(q.get())
'''
结果(先进先出):
first
second
third
'''

class queue.LifoQueue(maxsize=0) #last in fisrt out 先进后出

import queue

q=queue.LifoQueue()
q.put('first')
q.put('second')
q.put('third')

print(q.get())
print(q.get())
print(q.get())
'''
结果(后进先出):
third
second
first
'''

class queue.PriorityQueue(maxsize=0) #存储数据时可设置优先级的队列

import queue

q=queue.PriorityQueue()
#put进入一个元组,元组的第一个元素是优先级(通常是数字,也可以是非数字之间的比较),数字越小优先级越高
q.put((20,'a'))
q.put((10,'b'))
q.put((30,'c'))

print(q.get())
print(q.get())
print(q.get())
'''
结果(数字越小优先级越高,优先级高的优先出队):
(10, 'b')
(20, 'a')
(30, 'c')
'''


更多方法


Constructor for a priority queue. maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite.

The lowest valued entries are retrieved first (the lowest valued entry is the one returned by sorted(list(entries))[0]). A typical pattern for entries is a tuple in the form: (priority_number, data).

exception queue.Empty
Exception raised when non-blocking get() (or get_nowait()) is called on a Queue object which is empty.

exception queue.Full
Exception raised when non-blocking put() (or put_nowait()) is called on a Queue object which is full.

Queue.qsize()
Queue.empty() #return True if empty  
Queue.full() # return True if full 
Queue.put(item, block=True, timeout=None)
Put item into the queue. If optional args block is true and timeout is None (the default), block if necessary until a free slot is available. If timeout is a positive number, it blocks at most timeout seconds and raises the Full exception if no free slot was available within that time. Otherwise (block is false), put an item on the queue if a free slot is immediately available, else raise the Full exception (timeout is ignored in that case).

Queue.put_nowait(item)
Equivalent to put(item, False).

Queue.get(block=True, timeout=None)
Remove and return an item from the queue. If optional args block is true and timeout is None (the default), block if necessary until an item is available. If timeout is a positive number, it blocks at most timeout seconds and raises the Empty exception if no item was available within that time. Otherwise (block is false), return an item if one is immediately available, else raise the Empty exception (timeout is ignored in that case).

Queue.get_nowait()
Equivalent to get(False).

Two methods are offered to support tracking whether enqueued tasks have been fully processed by daemon consumer threads.

Queue.task_done()
Indicate that a formerly enqueued task is complete. Used by queue consumer threads. For each get() used to fetch a task, a subsequent call to task_done() tells the queue that the processing on the task is complete.

If a join() is currently blocking, it will resume when all items have been processed (meaning that a task_done() call was received for every item that had been put() into the queue).

Raises a ValueError if called more times than there were items placed in the queue.

Queue.join() block直到queue被消费完毕


*********Python标准模块--concurrent.futures*********







































