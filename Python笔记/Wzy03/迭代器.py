

1.迭代和可迭代协议
	1）什么叫迭代
		for i in [1,2,3,4]:  
    		print(i)

    	结果：
    		1
			2
			3
			4		

		for i in 1234
		    print(i) 

		结果：
		Traceback (most recent call last):
		  File "test.py", line 4, in <module>
		    for i in 1234:
		TypeError: 'int' object is not iterable	

		错误说，我们的1234不可迭代。上面的却可以。
		那么大胆推测，如果可以迭代，就应该可以被for循环。

		我们知道，字符串、列表、元祖、集合、字典都可以for循环
		说明他们都是可迭代的。

		那么正确的路子应该是什么样的呢，总不能凭空想象。
		from collections import Iterable   
		s = '1234'  
		l = [1,2,3,4]                
		t = (1,2,3,4)                
		d = {1:2,3:4}                
		s = {1,2,3,4}
		print(isinstance(a,Iterable))#Ture                           
		print(isinstance(l,Iterable))#Ture
		print(isinstance(t,Iterable))#Ture
		print(isinstance(d,Iterable))#Ture
		print(isinstance(s,Iterable))#Ture

		综上：可以将某个数据集内的数据“一个挨一个的取出来”，就叫做迭代。

	2）可迭代协议
		可以被迭代满足的要求就叫做可迭代协议。
		可迭代协议；就是内部实现了 __iter__() 方法

		验证：
			print(dir([1,2]))
			print(dir((1,2)))
			print(dir({1:2}))
			print(dir({1,2}))

		总结：
			可以被for循环的都是可迭代的，想要可迭代，内部必须有一个
			__iter__() 方法。

			接着分析，这个 __iter__()做了什么事情？
			print([1,2].__iter__())

			结果
			<list_iterator object at 0x1024784a8>
			这里的iterator就是迭代器。

2.迭代器
	
	可迭代后又一难题出现了，什么叫“迭代器”？
	'''
	dir([1,2].__iter__())是列表迭代器中实现的所有方法，
	dir([1,2])是列表中实现的所有方法,都是以列表的形式返
	回给我们的，为了看的更清楚，我们分别把他们转换成集合，
	然后取差集。
	'''
	#print(dir([1,2].__iter__()))
	#print(dir([1,2]))
	print(set(dir([1,2].__iter__()))-set(dir([1,2])))

	结果：
	{'__length_hint__', '__next__', '__setstate__'}

	我们看到在列表迭代器中多了三个方法，那么这三个方法都是
	干什么的呢？

		iter_l = [1,2,3,4,5,6].__iter__()#列表迭代器
		#获取迭代器中元素的长度
		print(iter_l.__length_hint__())
		#根据索引值指定从哪里开始迭代
		print('*',iter_l.__setstate__(4))
		#一个一个的取值
		print('**',iter_l.__next__())
		print('***',iter_l.__next__())

		结果：
			6
			* None
			** 5
			*** 6
	这三个方法中，能够一个一个取值的方法就是 __next__()
	在for循环中，就是在内部调用了 __next__() 方法才能取到
	一个一个的值。

	例子：
		l = [1,2,3]
		l_iter = l.__iter__()
		item = l_iter.__next__()
		print(item)#1
		item = l_iter.__next__()
		print(item)#2
		item = l_iter.__next__()
		print(item)#3
		item = l_iter.__next__()
		print(item)#StopIteration

		注意：
			如果我们一直取，直到next取到迭代器里已经没有元素了，
			就会抛出一个StopIteration异常，告诉我们，列表中已经
			没有有效元素了。

			这个时候，我们就要使用异常处理机制来把这个异常处理掉。

			例子：
				lis = ['1', '2', '3']
				it = lis.__iter__()
				while 1:
				    try:
				        res = it.__next__()
				        print(res)
				    except StopIteration:
				        break

				结果：
					1
					2
					3

	注：
		迭代器遵循迭代器协议：必须拥有 __iter__()方法和__next__()方法。

		# 迭代器的特点:
		#   1. 节省内存
		#   2. 惰性机制
		#   3. 只能往前拿. 不能反着拿

3.判断对象是迭代器还是可迭代对象
	例子：
		from collections import Iterator
		from collections import Iterable
		print(isinstance(range(10), Iterator))#False
		print(isinstance(range(10), Iterable))#Ture



		>>> from collections import Iterator
		>>> isinstance((x for x in range(10)), Iterator)
		True
		>>> isinstance([], Iterator)
		False
		>>> isinstance({}, Iterator)
		False
		>>> isinstance('abc', Iterator)
		False




		>>> from collections import Iterable
		>>> isinstance([], Iterable)
		True
		>>> isinstance({}, Iterable)
		True
		>>> isinstance('abc', Iterable)
		True
		>>> isinstance((x for x in range(10)), Iterable)
		True
		>>> isinstance(100, Iterable)
		False
































