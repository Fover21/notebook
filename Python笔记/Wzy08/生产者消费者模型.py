********生产者消费者模型********


在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。该模式通过平衡生产线程和消费
线程的工作能力来提高程序的整体处理数据的速度。

为什么要使用生产者和消费者模式

在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，如果
生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产
数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这
个问题于是引入了生产者和消费者模式。

什么是生产者消费者模式

生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不
直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给
阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平
衡了生产者和消费者的处理能力。

基于队列实现生产者消费者模型


JoinableQueue([maxsize]) 
创建可连接的共享进程队列。这就像是一个Queue对象，但队列允许项目的使用者通知生产者项目已
经被成功处理。通知进程是使用共享的信号和条件变量来实现的。

****方法介绍

JoinableQueue的实例p除了与Queue对象相同的方法之外，还具有以下方法：

q.task_done()
使用者使用此方法发出信号，表示q.get()返回的项目已经被处理。如果调用此方法的次数大于从队列
中删除的项目数量，将引发ValueError异常。

q.join()
生产者将使用此方法进行阻塞，直到队列中所有项目均被处理。阻塞将持续到尾队列中的每个项目均调用
q.task_done()方法为止。


建立永远运行的进程，使用和处理队列上的项目。生产者将项目放入队列，并等待它们被处理。



实现方法一（通用）

from multiprocessing import Process, JoinableQueue


def consumer(q, name):
    while 1:
        info = q.get()
        print("%s吃了" % name + info)
        q.task_done()


def producer(q, name):
    for i in range(10):
        info = '%s生产了%s号包子' % (name, i)
        q.put(info)
    q.join()


if __name__ == '__main__':
    q = JoinableQueue(10)
    pro = Process(target=producer, args=(q, 'Tom',))
    con = Process(target=consumer, args=(q, 'Jake'))
    con1 = Process(target=consumer, args=(q, 'Jason'))
    con.daemon = True  # 有几个消费者就有几个守护进程
    con1.daemon = True
    con1.start()
    con.start()
    pro.start()
    pro.join()


实现方法二（比较野）

from multiprocessing import Process, Queue
import time

def consumer(q, name):
    while 1:
        info = q.get()
        if info:
            print("%s吃了" % name + info)
        else:
            break

def producer(q, name):
    for i in range(10):
        time.sleep(0.1)
        info = '%s生产了%s号包子' % (name, i)
        q.put(info)



if __name__ == '__main__':
    q = Queue(10)
    pro = Process(target=producer, args=(q, 'Tom',))
    con = Process(target=consumer, args=(q, 'Jake'))
    con1 = Process(target=consumer, args=(q, 'Jason'))
    pro.start()
    con1.start()
    con.start()
    pro.join()
    q.put(None)#有几个消费者就要put几个None
    q.put(None)

实现方法三（比较野）

from multiprocessing import Process, Queue
import time

def consumer(q, name):
    while 1:
        info = q.get()
        if info:
            print("%s吃了" % name + info)
        else:
            break


def producer(q, name):
    for i in range(10):
        time.sleep(0.1)
        info = '%s生产了%s号包子' % (name, i)
        q.put(info)
    q.put(None) #有几个消费者就要put几个Nne
    q.put(None)


if __name__ == '__main__':
    q = Queue(10)

    pro = Process(target=producer, args=(q, 'Tom',))
    Process(target=producer, args=(q, 'Tom1',)).start()
    Process(target=producer, args=(q, 'Tom2',)).start()
    con = Process(target=consumer, args=(q, 'Jake'))
    con1 = Process(target=consumer, args=(q, 'Jason'))
    con1.start()
    pro.start()
    con.start()