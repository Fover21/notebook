********线程池********


Python标准模块--Concurrent.futures

1.介绍

Concurrent.futures模块提供了高度封装的异步调用接口
ThreadPoolExecutor:线程池，提供异步调用
ProcessPoolExecutor:进程池，提供异步调用

Both implement the same interface, which is defined by the abstract Executor class.

2.基本方法

#submit(fn, *args, **kwargs)
异步提交任务

#map(func, *iterables, timeout=None, chunksize=1) 
取代for循环submit的操作

#shutdown(wait=True) 
相当于进程池的pool.close()+pool.join()操作
wait=True，等待池内所有任务执行完毕回收完资源后才继续
wait=False，立即返回，并不会等待池内的任务执行完毕
但不管wait参数为何值，整个程序都会等到所有任务执行完毕
submit和map必须在shutdown之前

#result(timeout=None)
取得结果

#add_done_callback(fn)
回调函数


****ProcessPoolExecutor****


# 介绍
'''
The ProcessPoolExecutor class is an Executor subclass that uses a pool of processes 
to execute calls asynchronously. ProcessPoolExecutor uses the multiprocessing module,
 which allows it to side-step the Global Interpreter Lock but also means that only 
 picklable objects can be executed and returned.

class concurrent.futures.ProcessPoolExecutor(max_workers=None, mp_context=None)
An Executor subclass that executes calls asynchronously using a pool of at most 
max_workers processes. If max_workers is None or not given, it will default to 
the number of processors on the machine. If max_workers is lower or equal to 0,
then a ValueError will be raised.
'''

# 用法
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import os, time, random


def task(n):
    print('%s is runing' % os.getpid())
    time.sleep(random.randint(1, 3))
    return n ** 2


if __name__ == '__main__':

    executor = ProcessPoolExecutor(os.cpu_count() + 1)

    futures = []
    for i in range(11):
        future = executor.submit(task, i)
        futures.append(future)
    executor.shutdown(True)
    print('+++>')
    for future in futures:
        print(future.result())

*****ThreadPoolExecutor****

#介绍
'''
ThreadPoolExecutor is an Executor subclass that uses a pool of threads to execute calls asynchronously.
class concurrent.futures.ThreadPoolExecutor(max_workers=None, thread_name_prefix='')
An Executor subclass that uses a pool of at most max_workers threads to execute calls asynchronously.

Changed in version 3.5: If max_workers is None or not given, it will default to the number of processors 
on the machine, multiplied by 5, assuming that ThreadPoolExecutor is often used to overlap I/O instead of
 CPU work and the number of workers should be higher than the number of workers for ProcessPoolExecutor.

New in version 3.6: The thread_name_prefix argument was added to allow users to control the threading.
Thread names for worker threads created by the pool for easier debugging.
'''


#用法
#与ProcessPoolExecutor相同



*****map****


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import os, time, random


def task(n):
    print('%s is runing' % os.getpid())
    time.sleep(random.randint(1, 3))
    return n ** 2


if __name__ == '__main__':
    executor = ThreadPoolExecutor(os.cpu_count() * 5)

    # for i in range(41):
    #     future=executor.submit(task,i)

    executor.map(task, range(1, 42))  # map取代了for+submit

****回调函数****

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Pool
import requests
import json
import os


def get_page(url):
    print('<进程%s> get %s' % (os.getpid(), url))
    respone = requests.get(url)
    if respone.status_code == 200:
        return {'url': url, 'text': respone.text}


def parse_page(res):
    res = res.result()
    print('<进程%s> parse %s' % (os.getpid(), res['url']))
    parse_res = 'url:<%s> size:[%s]\n' % (res['url'], len(res['text']))
    with open('db.txt', 'a') as f:
        f.write(parse_res)


if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]

    # p=Pool(3)
    # for url in urls:
    #     p.apply_async(get_page,args=(url,),callback=pasrse_page)
    # p.close()
    # p.join()

    p = ProcessPoolExecutor(3)
    for url in urls:
        p.submit(get_page, url).add_done_callback(parse_page)  # parse_page拿到的是一个future对象obj，需要用obj.result()拿到结果

























