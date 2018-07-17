生成器
	
	通过列表生成式，我们可以直接创建一个列表。但是受内存限制，列表容量肯定是有限的。
	而且，创建一个很多很多元素的列表，不仅占用很大的内存空间，如果我们仅仅访问前几
	元素，那后面绝大多数的元素占用的空间就白白浪费了。

	所以，如果列表元素可以按照某种算法推算出来，那多好！这样就不必浪费空间了，这样
	你好我好大家好。

	在Python中，这种一边循环一边计算的机制，称为生成器：generator

	要创建一个generator，有很多种方法。
		1）只要把一个列表生成式的[]改为()，就创建了一个generator。
			L = [i * i for i in range(5)]
			print(L)#[0, 1, 4, 9, 16]

			g = (i * i for i in range(5))
			print(g)#<generator object <genexpr> at 0x111136ca8>

			创建L和g的区别仅在于最外层[]和(),L是一个list而g是一个genratot。

			我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？
			我们可以通过  next(g)挨个拿其中的元素，最后一个取完之后再进行 next()操作会
			报错（StopIteration）。
			一个一个取是在太繁琐，我们可以用for循环，因为genertor是一个可迭代对象。
			g = (i * i for i in range(5))
			for i in g:
				print(i) #用for循环来迭代，并且不需要关心StopIteration报错。

		2）用函数来实现。
			比如，斐波那契数列：1，1，2，3，5，8，13，21，34....
			用列表生成式写不出来，但是我们可以用函数把它打印出来：
			def fib(number):
			    n, a, b = 0, 0, 1
			    while n < number:
			        print(b)
			        a, b = b, a + b
			        n = n + 1
			    return 'OK!'

			print(fib(5))
			结果：
				1
				1
				2
				3
				5
				OK!
			我们可以看出从第一个元素开始，推算出后续任意的元素。很像generator。
			
			要把fib函数变成generator，只需要把 print(b)改为 yield b就可以了：
			def fib(number):
			    n, a, b = 0, 0, 1
			    while n < number:
			        yield b
			        a, b = b, a + b
			        n = n + 1
			    return 'OK!'

			print(fib(5))#<generator object fib at 0x105606ca8>

			注意：
				这里难理解的就是generator和函数的执行流程是不一样的。
				函数是顺序执行，遇到return语句或者最后一行函数语句就
				返回。
				generetor的函数，在每次调用 next()的时候执行，遇到
				yield语句返回，再次执行时从上次返回的yield语句处继续
				执行。

				例子：
					def odd():
					    print('step 1')
					    yield 1
					    print('step 2')
					    yield(3)
					    print('step 3')
					    yield(5)

					f = odd()
					print(next(f))
					print(next(f))
					print(next(f))

					结果：
						step 1
						1
						step 2
						3
						step 3
						5
					执行三次后再执行 next(f) 就会报错了。
					可以看到odd不是普通函数，而是generator遇到yield就会中断
					下次又继续执行，执行三次后已经没有yield可以执行，所以再执
					行 next(f) 就会报错了。


			把函数改为generator后，我们基本不这么用 next()来获取下一个返回值
			而是直接使用for循环来迭代。
			比如上面的fib函数。

				def fib(number):
				    n, a, b = 0, 0, 1
				    while n < number:
				        yield b
				        a, b = b, a + b
				        n = n + 1
				    return 'OK!'

				for i in fib(5):
				    print(i)
				结果：
					1
					1
					2
					3
					5

				注意：用for循环调用generator时，发现拿不到generator的return
					语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误
					返回值包含在StopIteration的value中。

					（关于如何捕获，异常处理见。）

					    Form zero to hero
