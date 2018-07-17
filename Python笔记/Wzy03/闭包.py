闭包

	学习闭包前先要知道

	函数名的运用
		函数名就是一个变量，但是他是一个特殊的变量，与括号配合可以执行函数的变量。

		1.函数名的内存地址

			def func():
    			print('hello')
			print(func)	

			结果：
				<function func at 0x10ef39ea0>

		2.函数名可以赋值给其他变量

			def func():
			    print("hello")
			print(func)
			a = func # 把函数当成一个变量赋值给另一个变量
			a() #函数调用func()

			结果：
				<function func at 0x10a5a5ea0>
				hello	

		3.函数名可以当做容器类的元素

			def func1():
			    print("呵")
			def func2():
			    print("呵")
			def func3():
			    print("呵")
			def func4(): 
			    print("呵")
			lst = [func1, func2, func3]
			for i in lst:
			    i()

			结果：
				呵
				呵
				呵

		4.函数名可以当做函数的参数

			def func():
			    print("吃了了么")
			def func2(fn):
			    print("我是func2")
			    fn() # 执行传递过来的fn
			    print("我是func2")
			func2(func) # 把函数func当成参数传递给func2的参数fn.

			结果：
				我是func2
				吃了了么
				我是func2

		5.函数名可以作为函数的返回值

			def func_1():
			    print("这⾥是函数1")
			    def func_2():
			        print("这⾥是函数2")
			    print("这⾥是函数1")
			    return func_2
			fn = func_1() # 执行函数1. 函数1返回的是函数2, 这时fn指向的就是上⾯函数2
			fn() # 执⾏上面返回的函数

			结果：
				这⾥是函数1
				这⾥是函数1
				这⾥是函数2

闭包：
	闭包就是内层函数对外层函数（非全局）的变量的引用。叫闭包。


	我们可以使用__closure__来检测函数是否是闭包. 
	使用函数名.__closure__返回cell就是闭包. 返回None就不是闭包

	def outer():
		name = "我爱你中国"
		# 内部函数
		def inner():
		    print(name)
		return inner
	fn = outer() # 访问外部函数, 获取到内部函数的函数地址
	fn() # 访问内部函数
	print(fn.__closure__)

	def fu():
	    print('e')
	fu()
	print(fu.__closure__)

	结果：
		我爱你中国
		(<cell at 0x104994708: str object at 0x1049ee2a0>,)
		e
		None


	 def outer():
	    name = "我爱你中国"
	    # 内部函数
		def inner():	
	        print(name)
	    return inner
	fn = outer() # 访问外部函数, 获取到内部函数的函数地址 
	fn() # 访问内部函数

	结果：
		我爱你中国

	def func1():
    	def func2():
        	def func3():
            	print("嘿嘿")
        	return func3
    	return func2
	func1()()()

	结果：
		嘿嘿

	闭包好处：
		由于我们在外界可以访问内部函数. 那这个时候内部函数访问的时间和时机
		就不一定了, 因为在外部, 我们可以选择在任意的时间去访问内部函数. 
		这个时候. 想一想. 我们之前说过, 如果一个函数执行完毕. 则这个函数
		中的变量以及局部命名空间中的内容都将会被销毁. 在闭包中. 如果变量被
		销毁了. 那内部函数将不能正常执行.所以，python规定. 如果你在内部函
		数中访问了外层函数中的变量. 那么这个变量将不会消亡. 将会常驻在内存中.
		也就是说. 使⽤用闭包, 可以保证外层函数中的变量在内存中常驻.














