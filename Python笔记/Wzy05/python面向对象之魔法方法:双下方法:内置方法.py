1.__new__ and __init__ 
这两个方法都是在实例化的时候执行，__new__ 在 __init__ 之前执行，并且
如果实例化的时候封装属性，__new__也是必须要传的，而且__new__必须有返回
值，而且这个返回值就是对象的内存空间而且会传给__init__的self参数，而且
封装的属性也会传给__init__.

class A:
    def __new__(cls, *args, **kwargs):
        print('我执行了')
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        print('我也执行了')


a = A('Tom')

结果：
	我执行了
	我也执行了

单例模式：
class A:
    __INS = None

    def __new__(cls, *args, **kwargs):
        if not cls.__INS:
            cls.__INS = super().__new__(cls)
        return cls.__INS


a0 = A()
a1 = A()
a2 = A()
print(a0)
print(a1)
print(a2)

结果：
	<__main__.A object at 0x105e93518>
	<__main__.A object at 0x105e93518>
	<__main__.A object at 0x105e93518>

2. __hash__  当调用hash函数，字典的快速查询 创建字典，集合的时候自动调用，为什么字典和集合的创建会调用？
那是因为字典和集合的创建是根据hash函数直接生成哈希值存储的，查询的时候是特别快的。必须有返回值，且为整数。

class A:
    def __hash__(self):
        print('我执行了')
        return 1


a0 = A()
hash(a0)
dic = {a0: '1'}
s = {a0}

结果：
	我执行了
	我执行了
	我执行了

3.item系列  和 obj使用[]访问值有关系 

__getitem__   obj[key] / obj[start:end] 自动执行
__setitem__	  obj[key] = value 赋值的时候自动执行
__delitem__   del obj[key]  del 的时候执行 

class A:
    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __delitem__(self, key):
        return delattr(self, key)


a = A()

a['k'] = 'v'  # __setitem__
print(a['k'])  # __getitem__
print(a.__dict__)
del a['k']  # __delitem__
print(a.__dict__)

4.__call__  obj() 和 类()() 自动执行

class A:
    def __call__(self, *args, **kwargs):
        print('我执行了')


a = A()

A()()
a()

结果：
	我执行了
	我执行了

5.__len__ 该方法是对象在调用 len() 这个内置函数的时候自动触发。必须有返回值，且为整数类型

class A:
    def __len__(self):
        print('我执行了')
        return 1

a = A()
len(a)

结果：
	我执行了

6.  __eq__  当执行 == 这个魔法糖时自动执行 __eq__ 方法 ，必须有返回值，且为bool

class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return True if self.name == other.name and self.age == other.age else False



a0 = A('W', 18)
a1 = A('W', 18)
a2 = A('W', 18)
a3 = A('W', 18)

a4 = A('W', 18)

a5 = A('W', 18)
a6 = A('W', 18)
print(a0, a1)
print(a0 == a1)
print(a3 == a0 == a4)  # ==这个语法 是完全和__eq__

结果：
	<__main__.A object at 0x109422438> <__main__.A object at 0x1094224e0>
	True
	True

7. __str__ and __repr__ 


# __str__ : str(obj),要求必须实现了__str__,要求这个方法的返回值必须是字符串str类型
        # print(obj) '%s'%s(obj) str(obj) 这三种情况会自动触发

# __repr__: 是__str__的备胎.如果有__str__方法,那么
		# print %s str都先去执行__str__方法,并且使用__str__的返回值
        # 如果没有__str__,那么 print %s str都会执行repr
        # repr(obj),%r

# 在子类中使用__str__,先找子类的__str__,没有的话要向上找,只要父类不是object,就执行父类的__str__
# 但是如果出了object之外的父类都没有__str__方法,就执行子类的__repr__方法,如果子类也没有,
# 还要向上继续找父类中的__repr__方法.
# 一直找不到 再执行object类中的__str__方法


8. __del__ del obj 和 垃圾回收机制回收这个对象所占内存的时候。
比如就是某对象借用了操作系统的资源，还要通过析构方法归还回去这时会自动调用：文件资源，网络资源
class A:
    def __del__(self):
        # 析构方法 del A的对象 会自动触发这个方法
        print('执行我了')


a = A()
del a  # 对象的删除 del

结果：
	我执行了
如果不用del obj 也会执行，因为程序运行完垃圾回收会回收a这时还会执行__del__方法。
