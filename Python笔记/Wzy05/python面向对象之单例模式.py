单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某
一个类只有一个实例存在。当你希望在整个系统中，某个类只能出现一个实例时，单例对象就
能派上用场。
单例类：如果一个类，从头到尾只开辟了一块属于对象的空间，那么这个类就是一个单例类。


准备工作：
----#__init__()方法叫初始化方法
----#__new__()方法叫构造方法

例子：
<1>
class A:
    def __new__(cls, *args, **kwargs):
        print('new')
    def __init__(self):
        print('init')
a = A()
结果：new

<2>
class A:
    def __new__(cls, *args, **kwargs):
        print('new')
        obj = super().__new__(cls)
        return obj
    def __init__(self):
        print('init')
a = A()
结果：new
	 init

需要知道，我们实例化对象的时候，会有三个步骤：
1.开辟一个空间，给对象
2.把对象的空间传给self，并执行init方法
3.将这个对象的空间返回给调用者

第一步的开辟一个空间就是构造函数 __new__(）来完成的。
第二步，将对象空间传给self，我们从例子<1>可以看出，
不返回空间，self是不会收到的，所以我们给出了例子<2>
这样第二步就执行了。
第三步，我们将对象的空间返回给调用者。

__new__()方法在什么时候执行？
答：在实例化之后，__init__()之前，先执行 __new__()来创建一块空间

了解这些，我们就开始写一个单例类：
单例类：如果一个类，从头到尾只开辟了一块属于对象的空间，那么这个类就是一个单例类。

例子：
<1>
class Single:
    __INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if not cls.__INSTANCE:
            cls.__INSTANCE = super().__new__(cls)
        return cls.__INSTANCE


s0 = Single()
s1 = Single()
print(s0)
print(s1)
结果：
	<__main__.Single object at 0x10e7f0630>
	<__main__.Single object at 0x10e7f0630>

<2>
class Foo:
    __INSTANCE = None

    @classmethod
    def get_instance(cls):
        if cls.__INSTANCE:
            return cls.__INSTANCE
        else:
            cls.__INSTANCE = Foo()
            return cls.__INSTANCE
f0 = Foo()
f1 = Foo()
print(f0.get_instance())
print(f1.get_instance())
结果：
	<__main__.Foo object at 0x10f4354e0>
	<__main__.Foo object at 0x10f4354e0>
