********在python程序中的进程操作********

之前我们已经了解了很多进程相关的理论知识，了解进程是什么应该不再困难了，刚刚我们已经了解了，
运行中的程序就是一个进程。所有的进程都是通过它的父进程来创建的。因此，运行起来的python程序
也是一个进程，那么我们也可以在程序中再创建进程。多个进程可以实现并发效果，也就是说，当我们的
程序中存在多个进程的时候，在某些时候，就会让程序的执行速度变快。以我们之前所学的知识，并不能
实现创建进程这个功能，所以我们就需要借助python中强大的模块。

****multiprocessing模块****

 仔细说来，multiprocess不是一个模块而是python中一个操作、管理进程的包。 之所以叫multi是
 取自multiple的多功能的意思,在这个包中几乎包含了和进程有关的所有子模块。由于提供的子模块非
 常多，为了方便大家归类记忆，我将这部分大致分为四个部分：创建进程部分，进程同步部分，进程池
 部分，进程之间数据共享。


#由该类实例化得到的对象，表示一个子进程中的任务（尚未启动）
class Process(object):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        self.name = ''
        self.daemon = False
        self.authkey = None
        self.exitcode = None
        self.ident = 0
        self.pid = 0
        self.sentinel = None

    def run(self):
        pass

    def start(self):
        pass

    def terminate(self):
        pass

    def join(self, timeout=None):
        pass

    def is_alive(self):
        return False

PS：
1.需要使用关键字的方式来指定参数
2.args指定的我传给target函数的位置参数，是一个元组形式，必须有逗号

参数介绍：
1.group参数未使用，值始终为None
2.target表示调用的对象，即子进程要执行的任务
3.args表示调用对象的位置参数元组
4.kwargs表示调用对象的字典
5.name为子进程的名称


方法介绍：
1. p.start():启动进程，并调用改进程中的p.run()
2. p.run():进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法
3. p.terminate():强制终止进程p,不会进行任何清理操作，如果p创建了子进程没改子进程就成为僵尸进程，
使用该方法需要特别小心这种情况。如果p还保存了一个锁，那么也将不会被释放，而导致死锁。
4. p.is_alive():如果p仍然运行，返回True
5. p.join([timeout]):主线程等待p终止（强调：是主线程处于等待，而p是处于运行状态）。timeout是可选
的超时时间，需要强调的是,p.join()只能join住start开启的进程，而不能join住run开启的进程。



属性介绍
1. p.daemon:默认值为False，如果设为True，代表p为后台运行的守护进程，当p的父进程终止时，p也随之终止。
并且设定为True后，p不能创建自己的新进程，必须在p.start()之前设置。
2. p.name:进程的名称
3. p.pid:进程的pid
4. p.exitcode:进程在运行时为None，如果为-N，表示被信号N结束了
5. p.authkey:进程的身份验证键,默认是由os.urandom()随机生成的32字符的字符串。这个键的用途是为涉及网
络连接的底层进程间通信提供安全性，这类连接只有在具有相同的身份验证键时才能成功


在Windows中使用process模块的注意事项
在Windows操作系统中由于没有fork(linux操作系统中创建进程的机制)，在创建子进程的时候会自动 import 启
动它的这个文件，而在 import 的时候又执行了整个文件。因此如果将process()直接写在文件中就会无限递归创
建子进程报错。所以必须把创建子进程的部分使用if __name__ ==‘__main__’ 判断保护起来，import 的时候 ，
就不会递归运行了。


**使用Process模块创建进程

方式一

from multiprocessing import Process
import os
import time


def func(s):
    print(s)
    print('子进程pid:%s', os.getpid())  # 获取进程id
    print('子进程ppid:%s', os.getppid())  # 获取进程父亲id


if __name__ == '__main__':
    p = Process(target=func, args=('Tome',))
    p.start()
    time.sleep(1)
    print('主进程pid:%s', os.getpid())


方式二

from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, na):
        self.na = na
        super().__init__()  # 必须继承init  因为Process有一些属性有自己的功能

    def run(self):
        print('我是%s' % self.na)
        print('这里是子进程！')


if __name__ == '__main__':
    p = MyProcess('Tone')
    p.start()  # 是指，解释器告诉系统，去帮我开启一个进程   就绪状态


jion方法

from multiprocessing import Process
import time


def f(name):
    print('hello', name)
    time.sleep(1)
    print('我是子进程')


if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    # p.join()  #感知一个子进程的结束，将异步变同步
    print('我是父进程')


进程之间的数据隔离问题

from multiprocessing import Process


def work():
    global n
    n = 0
    print('子进程内: ', n)


if __name__ == '__main__':
    n = 100
    p = Process(target=work)
    p.start()
    print('主进程内: ', n)


进阶，多个进程同时运行（注意子进程的执行顺序不是根据启动顺序决定的）

**多个进程同时运行

方式一
import time
from multiprocessing import Process


def func(name):
    print('hello', name)
    time.sleep(1)


if __name__ == '__main__':
    p_lst = []
    for i in range(5):
        p = Process(target=func, args=('Tom',))
        p.start()
        p_lst.append(p)

方式二

import time
from multiprocessing import Process


class MyProcess(Process):

    def __init__(self, na):
        super().__init__()
        self.na = na

    def run(self):
        print('hello', self.na)
        time.sleep(1)


if __name__ == '__main__':
    p_lst = []
    for i in range(5):
        p = MyProcess('Tom')
        p.start()
        p_lst.append(p)



**多个进程同时运行，再谈join方法（1）
import time
from multiprocessing import Process


def func(name):
    print('hello', name)
    time.sleep(1)


if __name__ == '__main__':
    p_lst = []
    for i in range(5):
        p = Process(target=func, args=('Tom',))
        p.start()
        p_lst.append(p)
        p.join()
    print('父进程在执行')


**多个进程同时运行，在谈join方法（2）

import time
from multiprocessing import Process


def func(name):
    print('hello', name)
    time.sleep(1)


if __name__ == '__main__':
    p_lst = []
    for i in range(5):
        p = Process(target=func, args=('Tom',))
        p.start()
        p_lst.append(p)
    [p.join() for p in p_lst]
    print('父进程在执行')


****守护进程****

会随着主进程的结束而结束。

主进程创建守护进程

　　其一：守护进程会在主进程代码执行结束后就终止

　　其二：守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children

注意：进程之间是互相独立的，主进程代码运行结束，守护进程随即终止


例子：
import os
import time
from multiprocessing import Process


class Myprocess(Process):
    def __init__(self, person):
        super().__init__()
        self.person = person

    def run(self):
        print(os.getpid(), self.name)
        print('%s正在和女主播聊天' % self.person)


p = Myprocess('Tom')
p.daemon = True  # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
p.start()
time.sleep(10)  # 在sleep时查看进程id对应的进程ps -ef|grep id
print('主进程')


from multiprocessing import Process
import time


def foo():
    print(123)
    time.sleep(1)
    print("end123")


def bar():
    print(456)
    time.sleep(3)
    print("end456")


p1 = Process(target=foo)
p2 = Process(target=bar)

p1.daemon = True
p1.start()
p2.start()
time.sleep(0.1)
print("main-------")  # 打印该行则主进程代码结束,则守护进程p1应该被终止.#可能会有p1任务执行的打印信息123,因为主进程打印main----时,p1也执行了,但是随即被终止.


****多进程中的其他方法****


from multiprocessing import Process
import time
import random

class Myprocess(Process):
    def __init__(self,person):
        self.name=person
        super().__init__()

    def run(self):
        print('%s正在和网红脸聊天' %self.name)
        time.sleep(random.randrange(1,5))
        print('%s还在和网红脸聊天' %self.name)


p1=Myprocess('Tom')
p1.start()

p1.terminate()#关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活
print(p1.is_alive()) #结果为True

print('开始')
print(p1.is_alive()) #结果为False














