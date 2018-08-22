********进程之间的数据共享********（了解）

展望未来，基于消息传递的并发编程是大势所趋

即便是使用线程，推荐做法也是将程序设计为大量独立的线程集合，通过消息队列交换数据。

这样极大地减少了对使用锁定和其他同步手段的需求，还可以扩展到分布式系统中。

但进程间应该尽量避免通信，即便需要通信，也应该选择进程安全的工具来避免加锁带来的问题。

以后尝试使用数据库来解决现在进程之间的数据共享问题。


Manager模块介绍

进程间数据是独立的，可以借助于队列或管道实现通信，二者都是基于消息传递的
虽然进程间数据独立，但可以通过Manager实现数据共享，事实上Manager的功能远不止于此

A manager object returned by Manager() controls a server process which holds 
Python objects and allows other processes to manipulate them using proxies.

A manager returned by Manager() will support types list, dict, Namespace, Lock, 
RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value and 
Array.



from multiprocessing import Manager, Process, Lock


def work(num0, num1, lock):
    lock.acquire()  # 不加锁而操作共享的数据，肯定会出现数据错乱
    num0[1] -= 1
    num1['name'] = 'Tom'
    lock.release()
    print('子进程中的num0值是', num0)
    print('子进程中的num0值是', num1)


if __name__ == '__main__':
    lock = Lock()
    m = Manager()
    num0 = m.list([1, 6, 3, 4])  # `dict`, `list` and `Namespace`
    num1 = m.dict({'name': 'Jack'})
    p = Process(target=work, args=(num0, num1, lock))
    p.start()
    p.join()
    print('主进程中的num0值是', num0)
    print('主进程中的num1值是', num1)

=================================================================

from multiprocessing import Manager, Process, Lock


def work(d, lock):
    with lock:  # 不加锁而操作共享的数据,肯定会出现数据错乱
        d['count'] -= 1


if __name__ == '__main__':
    lock = Lock()
    with Manager() as m:
        dic = m.dict({'count': 100})
        p_l = []
        for i in range(100):
            p = Process(target=work, args=(dic, lock))
            p_l.append(p)
            p.start()
        for p in p_l:
            p.join()
        print(dic)

===================================================================

Value模块数据贡献的例子


from multiprocessing import Process,Value,Lock
import time


def get_money(num,l):# 取钱
    l.acquire()# 拿走钥匙，锁上门，不允许其他人进屋
    for i in range(100):
        num.value -= 1
        print(num.value)
        time.sleep(0.01)
    l.release()# 还钥匙，打开门，允许其他人进屋

def put_money(num,l):# 存钱
    l.acquire()
    for i in range(100):
        num.value += 1
        print(num.value)
        time.sleep(0.01)
    l.release()

if __name__ == '__main__':
    num = Value('i',100)
    l = Lock()
    p = Process(target=get_money,args=(num,l))
    p.start()
    p1 = Process(target=put_money, args=(num,l))
    p1.start()
    p.join()
    p1.join()
    print(num.value)