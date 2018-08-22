********进程间通信-队列和管道********

****进程间通信-队列和管道

IPC（Inter-Process Communication）

****队列

**概念介绍

创建贡献的进程队列，Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。

Queue([maxsize]) 创建共享的进程队列。
参数 ：maxsize是队列中允许的最大项数。如果省略此参数，则无大小限制。
底层队列使用管道和锁定实现。

*********方法介绍：

Queue([maxsize]) 
创建共享的进程队列。maxsize是队列中允许的最大项数。如果省略此参数，则无大小限制。底层队列使
道和锁定实现。另外，还需要运行支持线程以便队列中的数据传输到底层管道中。 
Queue的实例q具有以下方法：

q.get( [ block [ ,timeout ] ] ) 
返回q中的一个项目。如果q为空，此方法将阻塞，直到队列中有项目可用为止。block用于控制阻塞行为
默认为True. 如果设置为False，将引发Queue.Empty异常（定义在Queue模块中）。timeout是可选
超时时间，用在阻塞模式中。如果在制定的时间间隔内没有项目变为可用，将引发Queue.Empty异常。

q.get_nowait( ) 
同q.get(False)方法。

q.put(item [, block [,timeout ] ] ) 
将item放入队列。如果队列已满，此方法将阻塞至有空间可用为止。block控制阻塞行为，默认为True。
如果设置为False，将引发Queue.Empty异常（定义在Queue库模块中）。timeout指定在阻塞模式中等
待可用空间的时间长短。超时后将引发Queue.Full异常。

q.qsize() 
返回队列中目前项目的正确数量。此函数的结果并不可靠，因为在返回结果和在稍后程序中使用结果之间，
队列中可能添加或删除了项目。在某些系统上，此方法可能引发NotImplementedError异常。


q.empty() 
如果调用此方法时 q为空，返回True。如果其他进程或线程正在往队列中添加项目，结果是不可靠的。
也就是说，在返回和使用结果之间，队列中可能已经加入新的项目。

q.full() 
如果q已满，返回为True. 由于线程的存在，结果也可能是不可靠的（参考q.empty（）方法）。。

**********其他方法：

q.close() 
关闭队列，防止队列中加入更多数据。调用此方法时，后台线程将继续写入那些已入队列但尚未写入的数
据，但将在此方法完成时马上关闭。如果q被垃圾收集，将自动调用此方法。关闭队列不会在队列使用者
中生成任何类型的数据结束信号或异常。例如，如果某个使用者正被阻塞在get（）操作上，关闭生产者
中的队列不会导致get（）方法返回错误。

q.cancel_join_thread() 
不会再进程退出时自动连接后台线程。这可以防止join_thread()方法阻塞。

q.join_thread() 
连接队列的后台线程。此方法用于在调用q.close()方法后，等待所有队列项被消耗。默认情况下，此方
由不是q的原始创建者的所有进程调用。调用q.cancel_join_thread()方法可以禁止这种行为。




例子：

**单看队列用法

'''

multiprocessing模块支持进程间通信的两种主要形式：管道和队列
都是基于消息传递实现的

'''

from multiprocessing import Queue

q = Queue(3)

# put, get, put_nowait, get_nowait, full, empty

q.put(1)
q.put(2)
q.put(3)
# q.put(4) #如果队列已经满了，程序就会停在这里，等待数据被别人取走，再将数据放入队列
# 如果队列中的数据一致不被取走，程序就会永远停在这里

try:
    q.put_nowait(4)  # 可以使用put_nowait()，如果队列满了就不会阻塞，但是会因为队列满了而报错

except:  # 因此我们可以用一个try语句来处理这个错误。这样程序不会一直阻塞下曲，但是会丢掉这个消息
    print('队列已满')

# 因此，我们再放入数据之前，可以看一下队列的状态，如果已经满了，就不继续put了

print(q.full())  # 满了

print(q.get())
print(q.get())
print(q.get())

# print(q.get())  #同put方法一样，如果队列已经空了，那么继续取就会出现阻塞

try:
    q.get_nowait()  # 可以使用get_nowait()，如果队列满了不会阻塞，但是会因为没取到值而报错
except:  # 因此我们可以用一个try语句来处理这个错误。这样程序就不会一致阻塞下去
    print('空了')

print(q.empty())  # 空了

**Queue实现进程间的通信

from multiprocessing import Queue, Process


def func(q):
    q.put('hello')  # 调用主函数中p进程传递过来的进程参数 put函数为向队列中添加一条数据。


if __name__ == '__main__':
    q = Queue()  # 创建一个Queue对象
    p = Process(target=func, args=(q,))  # 创建一个进程
    p.start()
    print(q.get())
    p.join()

**批量生产数据放入对列再批量获取

import os
from multiprocessing import Queue, Process


def inputQ(queue):
    info = str(os.getpid()) + '(put):'
    queue.put(info)


def outputQ(queue):
    info = queue.get()
    print('%s%s\033[32m%s\033[0m' % (str(os.getpid()), '(get):', info))


if __name__ == '__main__':
    record1 = []
    record2 = []

    queue = Queue(3)

    # 输入进程
    for i in range(10):
        p = Process(target=inputQ, args=(queue,))
        p.start()
        record1.append(p)

    # 输出进程
    for i in range(10):
        p = Process(target=outputQ, args=(queue,))
        p.start()
        record2.append(p)

    [p.join() for p in record1]
    [p.join() for p in record2]



********管道********

****介绍

#创建管道的类：
Pipe([duplex]):在进程之间创建一条管道，并返回元组（conn1,conn2）,其中conn1，conn2表示
道两端的连接对象，强调一点：必须在产生Process对象之前产生管道

#参数介绍：
dumplex:默认管道是全双工的，如果将duplex射成False，conn1只能用于接收，conn2只能用于发送。

#主要方法：
conn1.recv():接收conn2.send(obj)发送的对象。如果没有消息可接收，recv方法会一直阻塞。
如果连接的另外一端已经关闭，那么recv方法会抛出EOFError。
conn1.send(obj):通过连接发送对象。obj是与序列化兼容的任意对象

#其他方法：
conn1.close():关闭连接。如果conn1被垃圾回收，将自动调用此方法
conn1.fileno():返回连接使用的整数文件描述符
conn1.poll([timeout]):如果连接上的数据可用，返回True。timeout指定等待的最长时限。如果省略
此参数，方法将立即返回结果。如果将timeout射成None，操作将无限期地等待数据到达。
 
conn1.recv_bytes([maxlength]):接收c.send_bytes()方法发送的一条完整的字节消息。maxlength
指定要接收的最大字节数。如果进入的消息，超过了这个最大值，将引发IOError异常，并且在连接上无法进
行进一步读取。如果连接的另外一端已经关闭，再也不存在任何数据，将引发EOFError异常。
conn.send_bytes(buffer [, offset [, size]])：通过连接发送字节数据缓冲区，buffer是支持缓冲
区接口的任意对象，offset是缓冲区中的字节偏移量，而size是要发送字节数。结果数据以单条消息的形式发
出，然后调用c.recv_bytes()函数进行接收    
 
conn1.recv_bytes_into(buffer [, offset]):接收一条完整的字节消息，并把它保存在buffer对象中，
该对象支持可写入的缓冲区接口（即bytearray对象或类似的对象）。offset指定缓冲区中放置消息处的字节
位移。返回值是收到的字节数。如果消息长度大于可用的缓冲区空间，将引发BufferTooShort异常。

****Pipe初使用

from multiprocessing import Process, Pipe


def f(conn):
    conn.send("Hello The_Third_Wave")
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()


注意：
应该特别注意管道端点的正确管理问题。如果是生产者或消费者中都没有使用管道的某个端点，就应将
它关闭。这也说明了为何在生产者中关闭了管道的输出端，在消费者中关闭管道的输入端。如果忘记执
行这些步骤，程序可能在消费者中的recv（）操作上挂起。管道是由操作系统进行引用计数的，必须在
所有进程中关闭管道后才能生成EOFError异常。因此，在生产者中关闭管道不会有任何效果，除非消费
也关闭了相同的管道端点。


**引发EOFError

from multiprocessing import Pipe, Process


def func(con):
    con1, con2 = con
    con1.close()  # 子进程使用con2和父进程通信，所以
    while 1:
        try:
            print(con2.recv())  # 当主进程的con1发数据时，子进程要死循环的去接收。
        except EOFError:  # 如果主进程的con1发完数据并关闭con1，子进程的con2继续接收时，就会报错，使用try的方式，获取错误
            con2.close()  # 获取到错误，就是指子进程已经把管道中所有数据都接收完了，所以用这种方式去关闭管道
            break


if __name__ == '__main__':
    con1, con2 = Pipe()
    p = Process(target=func, args=((con1, con2),))
    p.start()
    con2.close()  # 在父进程中，使用con1去和子进程通信，所以不需要con2，就提前关闭
    for i in range(10):  # 生产数据
        con1.send(i)  # 给子进程的con2发送数据
    con1.close()  # 生产完数据，关闭父进程这一端的管道

**多个消费者之间的竞争问题带来的数据不安全问题

from multiprocessing import Process, Pipe, Lock


def consumer(p, name, lock):
    produce, consume = p
    produce.close()
    while True:
        lock.acquire()
        baozi = consume.recv()
        lock.release()
        if baozi:
            print('%s 收到包子:%s' % (name, baozi))
        else:
            consume.close()
            break


def producer(p, n):
    produce, consume = p
    consume.close()
    for i in range(n):
        produce.send(i)
    produce.send(None)
    produce.send(None)
    produce.close()


if __name__ == '__main__':
    produce, consume = Pipe()
    lock = Lock()
    c1 = Process(target=consumer, args=((produce, consume), 'c1', lock))
    c2 = Process(target=consumer, args=((produce, consume), 'c2', lock))
    p1 = Process(target=producer, args=((produce, consume), 10))
    c1.start()
    c2.start()
    p1.start()

    produce.close()
    consume.close()

    c1.join()
    c2.join()
    p1.join()
    print('主进程')











































