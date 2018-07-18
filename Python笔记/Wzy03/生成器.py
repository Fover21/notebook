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
                注意：函数创建一次生成一个生成器，所以我们会将创建的生
                    成器赋值给一个变量。如果直接用函数本身这个生成器，
                    我们没用一次生成一个新的生成器对象，所以，我们一
                    般都将创建的生成器赋给一个变量。
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
					行 next(f) 就会报错了。最后的yield后面一般不写东西。


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


    接下来我们来看send⽅方法, send和next()一样都可以让生成器执行到下一个yield.
        例子；
            def eat():
                print("我吃什么啊")
                a = yield "馒头"
                print("a=",a)
                b = yield "⼤大饼"
                print("b=",b)
                c = yield "韭菜盒⼦子"
                print("c=",c)
                yield "GAME OVER"
            gen = eat() # 获取⽣生成器器
            ret1 = next(gen)
            print(ret1)
            ret2 = gen.send("胡辣汤")
            print(ret2)
            ret3 = gen.send("狗粮")
            print(ret3)
            ret4 = gen.send("猫粮")
            print(ret4)
            
            结果：
                我吃什么啊
                馒头
                a= 胡辣汤
                ⼤大饼
                b= 狗粮
                韭菜盒⼦子
                c= 猫粮
                GAME OVER
                    
        send和next()区别:
            1. send()和next()都是让生成器向下走一次
            2. send可以给上一个yield的位置传递值,不能给最后一个yield发送值.
                在第一次执行生成器代码的时候不能使用send()
                    
                    
        三道题：
            <1>
            def add(a, b):
                return a+b
            def Test():
                for i in range(4):
                    yield i
            g = Test()
            for n in [2, 10]:
                g = (add(n, i) for i in g)
            print(list(g))
                
            结果：
                [20, 21, 22, 23]
            分析：
                print(list(g))这个语句之前都是准备阶段，只程序走到
                print(list(g))这个语句这里程序才会执行，那么在此程
                序执行的准备阶段前面做了什么事呢：
                    到for循环这
                        n = 2
                        g = (add(n, i) for i in Test())
                        n = 10
                        g = (add(n, i) for i in add(n, i) for i in Test())
                        这个时候执行list(g)其实执行的只是n==10的时候
                        结果：[20, 21, 22, 23]

            <2>
            def func():
                print('1')
                yield 'This is one step'
                print('2')
                yield 'This is two step'
                print('3')
                yield 'This is theree step'
            it = func()#函数返回生成器
            print(list(it))
            
            结果：
            1
            2
            3
            ['This is one step', 'This is two step', 'This is theree step']
            
            <3>
            def func():
                print(111)
                yield 222
            g = func() # 生成器g
            g1 = (i for i in g) # 生成器g1. 但是g1的数据来源于g
            g2 = (i for i in g1) # 生成器器g2. 来源g1
            print(list(g)) # 获取g中的数据. 这时func()才会被执行. 打印111.获取到222. g完毕.
            print(list(g1)) # 获取g1中的数据. g1的数据来源是g. 但是g已经取完了了. g1 也就没有数据了
            print(list(g2)) # 和g1同理
            
            结果：
                111
                [222]
                []
                []



					    Form zero to hero
