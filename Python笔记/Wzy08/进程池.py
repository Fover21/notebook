********进程池********

****进程池****

为什么要有进程池？

答：
在程序实际处理问题过程中，忙时会有成千上万的任务需要被执行，闲时可能只有零星任务。那么在成千
万个任务需要被执行的时候，我们就需要去创建成千上万个进程么？首先，创建进程需要消耗时间，销毁
程也需要消耗时间。第二即便开启了成千上万的进程，操作系统也不能让他们同时执行，这样反而会影响
序的效率。因此我们不能无限制的根据任务开启或者结束进程。那么我们要怎么做呢？

在这里，要给大家介绍一个进程池的概念，定义一个池子，在里面放上固定数量的进程，有需求来了，就
一个池中的进程来处理任务，等到处理完毕，进程并不关闭，而是将进程再放回进程池中继续等待任务。
果有很多任务需要执行，池中的进程数量不够，任务就要等待之前的进程执行任务完毕归来，拿到空闲进
才能继续执行。也就是说，池中进程的数量是固定的，那么同一时间最多有固定数量的进程在运行。这样
增加操作系统的调度难度，还节省了开闭进程的时间，也一定程度上能够实现并发效果。

******multiprocess.Pool模块******

****概念介绍

Pool([numprocess  [,initializer [, initargs]]]):创建进程池

**参数介绍

numprocess:要创建的进程数，如果省略，将默认使用cpu_count()的值（这是os模块的一个方法）
initializer:是每个工作进程启动时要执行的可调用对象，默认为None
initargs:是要传给initialiizer的参数组

**主要方法
    def apply(self, func, args=(), kwds={}):
        '''
        Equivalent of `func(*args, **kwds)`.
        '''
        assert self._state == RUN
        return self.apply_async(func, args, kwds).get()

    def map(self, func, iterable, chunksize=None):
        '''
        Apply `func` to each element in `iterable`, collecting the results
        in a list that is returned.
        '''
        return self._map_async(func, iterable, mapstar, chunksize).get()

    def apply_async(self, func, args=(), kwds={}, callback=None,
            error_callback=None):
        '''
        Asynchronous version of `apply()` method.
        '''
        if self._state != RUN:
            raise ValueError("Pool not running")
        result = ApplyResult(self._cache, callback, error_callback)
        self._taskqueue.put(([(result._job, 0, func, args, kwds)], None))
        return result

1 p.apply(func [, args [, kwargs]]):在一个池工作进程中执行func(*args,**kwargs),然后返回结果。
'''需要强调的是：此操作并不会在所有池工作进程中并执行func函数。如果要通过不同参数并发地执行func函数，
必须从不同线程调用p.apply()函数或者使用p.apply_async()'''
同步，只有func被执行完后才会继续执行代码，返回值为func的return值
同步处理任务，进程池中的所有进程都是普通进程
2 p.map(self, func, iterable, chunksize=None):
异步，自带close和join，返回值为func返回值组成的列表
3 p.apply_async(func [, args [, kwargs]]):在一个池工作进程中执行func(*args,**kwargs),然后返回结果。
'''此方法的结果是AsyncResult类的实例，callback是可调用对象，接收输入参数。当func的结果变为可用时，
将理解传递给callback。callback禁止执行任何阻塞操作，否则将接收其他异步操作中的结果。'''
异步，当func被注册进入一个进程后，程序就继续向下执行，返回一个对象，这个对象有get方法可以取到值（这是func的返回值）
obj.get() 会阻塞，知道对应的func执行完毕拿到结果。需要先close后join来保持多进程和主进程代码的同步性。
异步处理任务时，进程池中的所有进程都是守护进程
有回调函数 callback
4 p.close():关闭进程池，防止进一步操作。如果所有操作持续挂起，它们将在工作进程终止前完成
5 P.jion():等待所有工作进程退出。此方法只能在close（）或teminate()之后调用
**其他方法

1 方法apply_async()和map_async（）的返回值是AsyncResul的实例obj。实例具有以下方法
2 obj.get():返回结果，如果有必要则等待结果到达。timeout是可选的。如果在指定时间内还没有到达，将引发一场。如果
远程操作中引发了异常，它将在调用此方法时再次被引发。
3 obj.ready():如果调用完成，返回True
4 obj.successful():如果调用完成且没有引发异常，返回True，如果在结果就绪之前调用此方法，引发异常
5 obj.wait([timeout]):等待结果变为可用。
6 obj.terminate()：立即终止所有工作进程，同时不执行任何清理或结束任何挂起工作。如果p被垃圾回收，将自动调用此函数

**例子

*同步和异步*



同步
from multiprocessing import Pool
import os, time


def work(n):
    print('%s run' % os.getpid())
    time.sleep(1)
    return n * 3


if __name__ == '__main__':
    p = Pool(3)  # 进程池中从无到有创建三个进程，以后一直是这三个进程在执行任务
    for i in range(10):
        res = p.apply(work, args=(i,))  # 同步调用，直到本次任务执行完毕拿到res，等待任务work执行的过程中可能有阻塞也可能没有阻塞
                                        # 但不管该任务是否存在阻塞，同步调用都会在原地等着
        print(res)  # res为func的返回值


异步
import os
import time
import random
from multiprocessing import Pool


def work(n):
    print('%s run' % os.getpid())
    time.sleep(random.random())
    return n ** 2


if __name__ == '__main__':
    p = Pool(3)  # 进程池中从无到有创建三个进程,以后一直是这三个进程在执行任务
    res_l = []
    for i in range(10):
        res = p.apply_async(work, args=(i,))  # 异步运行，根据进程池中有的进程数，每次最多3个子进程在异步执行
        # 返回结果之后，将结果放入列表，归还进程，之后再执行新的任务
        # 需要注意的是，进程池中的三个进程不会同时开启或者同时结束
        # 而是执行完一个就释放一个进程，这个进程就去接收新的任务。
        res_l.append(res)

    # 异步apply_async用法：如果使用异步提交的任务，主进程需要使用jion，等待进程池内任务都处理完，然后可以用get收集结果
    # 否则，主进程结束，进程池可能还没来得及执行，也就跟着一起结束了
    p.close()
    p.join()
    for res in res_l:
        print(res.get())  # 使用get来获取apply_aync的结果,如果是apply,则没有get方法,因为apply是同步执行,立刻获取结果,也根本无需get


回调函数

需要回调函数的场景：进程池中任何一个任务一旦处理完了，就立即告知主进程：
我好了额，你可以处理我的结果了。主进程则调用一个函数去处理该结果，该函数即回调函数

我们可以把耗时间（阻塞）的任务放到进程池中，然后指定回调函数（主进程负责执行），
这样主进程在执行回调函数时就省去了I/O的过程，直接拿到的是任务的结果。


如果在主进程中等待进程池中所有任务都执行完毕后，再统一处理结果，则无需回调函数












