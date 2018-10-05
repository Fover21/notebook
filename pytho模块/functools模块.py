
 __author: ward
 data: 2018/10/5

 functools模块小结
 functools.partial
 functool.update_wrapper
 functool.wraps
 functools.reduce
 functools.cmp_to_key
 functools.total_ordering


 functools.partial
 作用:
 functools.partial 通过包装手法，允许我们 "重新定义" 函数签名
 用一些默认参数包装一个可调用对象,返回结果是可调用对象，并且可以像原始对象一样对待
 冻结部分函数位置函数或关键字参数，简化函数,更少更灵活的函数参数调用
 应用:
 典型的，函数在执行时，要带上所有必要的参数进行调用。
 然后，有时参数可以在函数被调用之前提前获知。
 这种情况下，一个函数有一个或多个参数预先就能用上，以便函数能用更少的参数进行调用。
 import functools


 def add(a, b):
     return a + b


 print(add(4, 2))
 plus3 = functools.partial(add, 3)
 plus5 = functools.partial(add, 5)
 print(plus3(4))
 print(plus3(7))
 print(plus5(10))


 functool.update_wrapper
 默认partial对象没有__name__和__doc__, 这种情况下，对于装饰器函数非常难以debug.
 使用update_wrapper(),从原始对象拷贝或加入现有partial对象
 它可以把被封装函数的__name__、module、__doc__和 __dict__都复制到封装函数去(模块级别常量WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES)
 这个函数主要用在装饰器函数中，装饰器返回函数反射得到的是包装函数的函数定义而不是原始函数定义

 def wrap(func):
     def call_it(*args, **kwargs):
         """wrap func: call_it"""
         print('before call')
         return func(*args, **kwargs)

     return call_it


 @wrap
 def hello():
     """say hello"""
     print('hello world')


 from functools import update_wrapper


 def wrap2(func):
     def call_it(*args, **kwargs):
         """wrap func: call_it2"""
         print('before call')
         return func(*args, **kwargs)

     return update_wrapper(call_it, func)


 @wrap2
 def hello2():
     """test hello"""
     print('hello world2')


 if __name__ == '__main__':
     hello()
     print(hello.__name__)
     print(hello.__doc__)

     print()
     hello2()
     print(hello2.__name__)
     print(hello2.__doc__)

 结果：
     before
     call
     hello
     world
     call_it
     wrap
     func: call_it

     before
     call
     hello
     world2
     hello2
     test
     hello


 functool.wraps
 调用函数装饰器partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)的简写

 from functools import wraps


 def wrap3(func):
     @wraps(func)
     def call_it(*args, **kwargs):
         """wrap func: call_it2"""
         print('before call')
         return func(*args, **kwargs)

     return call_it


 @wrap3
 def hello3():
     """test hello 3"""
     print('hello world3')


 结果：
 before
 call
 hello
 world2
 hello2
 test
 hello


 functools.reduce
 functools.reduce(function, iterable[, initializer])


 functools.cmp_to_key
 functools.cmp_to_key(func)

 将老式鼻尖函数转换成key函数，用在接受key函数的方法中(such as sorted(), min(), max(), heapq.nlargest(), heapq.nsmallest(), itertools.groupby())
 一个比较函数，接收两个参数，小于，返回负数，等于，返回0，大于返回整数
 key函数，接收一个参数，返回一个表明该参数在期望序列中的位置


 functools.total_ordering
 functools.total_ordering(cls)
 from functools import total_ordering


 @total_ordering
 class Student:
     def __eq__(self, other):
         return ((self.lastname.lower(), self.firstname.lower()) ==
                 (other.lastname.lower(), other.firstname.lower()))

     def __lt__(self, other):
         return ((self.lastname.lower(), self.firstname.lower()) <
                 (other.lastname.lower(), other.firstname.lower()))


 print(dir(Student))
