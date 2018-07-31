什么是反射？#是什么
答：用字符串数据类型的变量名来访问这个变量的值
反射的方法：getattr hasattr setattr delattr
好处：优化代码

1.getattr
	用法：getattr(object, name[,default]) -> value
	返回object中name字符串对应的方法和属性，不存在返回默认值default。
	如果没有传default，那么找不到就会报错
	#用在哪，怎么用？
	#类   静态属性，静态方法，类方法
	class A:
	    ATTR = '静态属性'
	    @classmethod
	    def func0(cls):
	        print('类方法')
	    @staticmethod
	    def func1():
	        print('静态方法')
	#反射查看属性
	print(getattr(A, 'ATTR'))
	#反射调用类方法
	getattr(A, 'func0')()
	#反射调用静态方法
	getattr(A, 'func1')()

	#对象   对象属性，对象方法
	class B:
	    def __init__(self, name):
	        self.name = name
	    def func0(self):
	        print('普通方法')
	b = B('Jake')
	#反射查看对象属性
	print(getattr(b, 'name'))
	#反射查看对象方法
	getattr(b, 'func0')()

	#模块
	import os
	print(os.sep)
	print(getattr(os, 'sep'))

	#反射自己模块中的内容，需要先找到自己当前文件所在的命名空间
	import sys
	def func0():
	    print('my_func0')
	my_namespace = sys.modules['__main__']
	my_namespace.func0()
	getattr(my_namespace, 'func0')()

2.hasattr
	用法：hasattr(object, name) #判断object中有没有一个name字符串对应的方法和属性
								#如果存在返回True，不存在返回False，一般与getattr配合使用
	class A:
	    ATTR = '静态属性'
	print(hasattr(A, 'ATTR'))#Trule
	print(hasattr(A, 's'))#False

3.setattr
	用法：setattr(object, name, value)
	修改object中name字符串对应的属性name变为value
	class A:
	    ATTR = '静态属性'
	    @staticmethod
	    def func1():
	        print('静态方法')
	setattr(A, 'ATTR', '静态属性大哥')
	print(A.ATTR)

4.delattr
	用法：delattr(object, name)
	删除object中name字符串对应的属性和方法
	class A:
	    ATTR = '静态属性'
	    @staticmethod
	    def func1():
	        print('静态方法')
	print(A.__dict__)
	delattr(A, 'ATTR')
	delattr(A, 'func1')
	print(A.__dict__)
