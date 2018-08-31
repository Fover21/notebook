
queue队列 ：使用import queue

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
