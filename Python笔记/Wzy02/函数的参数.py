函数的参数：

先来安利一下：定义函数的时候，我们把参数的名字和位置确定下来，函数的接口就定义完了。
			对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数返回什么样的值就够了，
			函数内部的复杂逻辑被封装起来，调用者无需了解。

	Python的函数定义非常简单，但是却非常灵活。除了正常定义的必选参数外，还可以使用默认参数，
		可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化
		调用者的代码。

	只要函数执行到return 函数就会停止执行
	# 1. 每个函数如果在函数中不写return, 默认返回None
	# 2. 我们也可以只写一个return, 也是返回None, 停止函数的执行
	# 3. return 一个返回值.  你在调用方能接受到一个返回值
	# 4. return 多个返回值. 多个值需要用,隔开   接收的位置. 接收的是元组.
	# 函数return返回多个值以元祖（tuple）存储 	

1.位置参数
	def fun(a):
		return a+a	
	print(fun(3))#6
	对于fun(a)函数，参数a就是一个位置参数。
	当我们调用fun函数时，必须传入有且仅有的一个参数x

	def fun(x,n)
		x = x **n
		return x
	print(fun(2,4))#16
	x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次付给参数x和n

2.默认参数
	def fun(x,n=2):
		x = x **n
		return x
	print(fun(2))#4
	print(fun(2,4))#16
	默认参数可以简化函数的调用。设置默认参数时，需注意：
		1）必选参数在前，默认参数在后，否则python解释器会报错
		2）如何设置默认参数：当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。
			变化小的参数就可以作为默认参数。
	使用默认参数有什么好处呢：最大的好处就是能够降低调用函数的难度。

	注意：默认参数的一个坑
			例子：
				def add(l=[]):
					l.append('a')
					return  l
				#正常调用时，结果正常
				print(add([1, 2, 3]))#[1, 2, 3, 'a']
				print(add([5, 4, 3]))#[5, 4, 3, 'a']
				#当使用默认参数调用时，一开始结果还正确，可是再此调用就不对了
				print(add())#['a']
				print(add())#['a', 'a']

				原因解释：
					Python函数在定义的时候，默认参数l的值就被计算出来了，即[],因为默认场参数l也是一个变量，
                    他指向对象[]，每次调用函数，如果改变了l的内容，则下次调用时，默认参数的内容就变了，不再
                    是函数定义时的[]了。

				注：定义默认参数要记牢一点：默认参数必须指向不变对象。

				解决上述问题：
					def add(L=None):
						if L is None:
							L=[]
						L.append('a')
						return L

3.可变参数

	def fun(*n):
	    sum = 0
	    for i in n:
	        sum += i
	    return sum
	print(fun(1,2,3))#6
	lis = [1,2,3]
	print(fun(*lis))#6
	tu = (1,2,3)
	print(fun(*tu))#6

	注意：由于参数不确定，所以我们就传入一个可变参数*n，Python允许你在list或tuple前面加一个*号，
        把list或tuple的元素变成可变参数传进去。

4.关键字参数

		可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
        而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

		def person(name, age, **kw):
    		print('name:', name, 'age:', age, 'other:', kw)
    	person('Michael', 3)#name: Michael age: 3 other: {}
    	person('A', 4, g='M', j='E')#name: A age: 4 other: {'g': 'M', 'j': 'E'}

    	关键字参数有什么用？:它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
            但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄
            是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

 5.命名关键字参数：
 		<1>
    	对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
    	def person(name, age, **kw):
    		print('name:', name, 'age:', age, 'other:', kw)
    	person('JackChen', 20, city='shanghai', addr='shanxi', zipcode=123)

    	<2>
    	如果要限制关键字参数的名字，就可以用命名关键字参数.
    	例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
    	def person(name, age, *, city, job):
    		print(name, age, city, job)
    	#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，
    	#*后面的参数被视为命名关键字参数。
    	person('Jack', 20, city='Beijing', job='Engineer')#Jack 20 Beijing Engineer

    	<3>
    	如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符
    	*了：
    	def person(name, age, *args, city, job):
    		print(name, age, args, city, job)

    	#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错.
		person('Jack', 20, 'Beijing', 'Engineer')
		#Traceback (most recent call last):
		# File "<stdin>", line 1, in <module>
		#TypeError: person() takes 2 positional arguments but 4 were given
		由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，
		但person()函数仅接受2个位置参数。

		<4>
		命名关键字参数可以有缺省值，从而简化调用：
		def person(name, age, *, city='Beijing', job):
    		print(name, age, city, job)
    	person('Jack', 20, job='Engineer')#Jack 20 Beijing Engineer

    	注意：使用命名关键字参数时，要特别注意，如果没有可变参数，
    		 就必须加一个*作为特殊分隔符。如果缺少*，
    		 Python解释器将无法识别位置参数和命名关键字参数



参数组合：
		在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
            这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：
            必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

		对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

































