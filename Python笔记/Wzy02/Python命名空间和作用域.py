准备知识：
	1.在Python解释器开始执行之后，机会在内存中开辟一个空间，每当遇到
	一个变量的时候，就把变量和值之间的关系记录下来，但是当遇到函数定义
	的时候，解释器只是把函数名读入内存，表示这个函数存在，至于函数内部
	的变量和逻辑，解释器是不关心的。也就是说一开始的时候函数只是加载进
	来，仅此而已，只有当函数被调用和访问的时候解释器才会根据函数内部声
	明的变量来进行开辟变量的内部空间。随着函数执行完毕，这些函数内部变
	量占用的空间也会随着函数执行完毕而清空。

	例子：
		def fun():
    		a = 10000
			print(a)
		fun()
		print(a) # a不存在了了已经..

	2.命名空间
		在一个Python程序的任何一个地方，都存在几个可用的命名空间。
		我们存放名字和值的关系的空间起个名字，叫命名空间。
		我们的变量在存储的时候就存在这片空间的。
			（1）分类：
				1）每个函数都有自己的命名空间，叫做局部命名空间，
				它记录了函数的变量，包括函数的参数和局部定义的变量。
				2）每个模块都拥有自己的命名空间，叫做全局命名空间，
				它记录了模块的变量，包括函数、类、其他导入的模块、
				模块级的变量和常量。
				3）还有就是内置命名空间，任何模块均可访问，它存放着
				内置的函数和异常。

				加载顺序：内置命名空间，全局命名空间，局部命名空间(函数被执行)

				取值顺序：局部命名空间，全局命名空间，内置命名空间

				注意：嵌套函数的情况
					1.先在当前(嵌套的或lambda)函数的命名空间搜索
					2.然后是在父函数的命名空间中搜索
					3.接着是模块命名空间中搜索
					4.左后在内置命名空间中搜索
			（2）生命周期：
				命名空间的生命周期不同的命名空间在不同的时刻创建，
				有不同的生存期。
     				1、内置命名空间在 Python 解释器启动时创建，
     				会一直保留，不被删除。
     				2、模块的全局命名空间在模块定义被读入时创建，
     				通常模块命名空间也会一直保存到解释器退出。
     				3、当函数被调用时创建一个局部命名空间，当函
     				数返回结果或抛出异常时，被删除。每一个递归
     				调用的函数都拥有自己的命名空间。
     
     3.作用域
     	L :local,局部作用域，即函数定义的变量
     	E :enclosing,嵌套的父级函数的局部作用域，
     		即包含此函数的上级函数的局部作用域但不是全局
     	G :global,	全局变量,就是模块级别定义的变量。
     	B :built-in，系统固定模块里面的变量。比如int等。
     		搜索变量的优先级顺序：LEGB


1.globals() 和 locals()
	
	globals() 获取到全局作用域(内置,全局)中的所有名字
	locals() 查看当前作用域中的所有名字
	例子：
		a = 10
		def func():
   			a = 20
		    print(a)    # 就近原则
		    print(globals())  # globals() 获取到全局作用域(内置,全局)中的所有名字
		    print(locals())  # locals() 查看当前作用域中的所有名字
		func()
		打印内容：
		（1）#20
		（2）#{'__name__': '__main__', '__doc__': None, '__package__': None,
			# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x10cee7400>,
			# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 
			#'__file__': '/Users/busensei/wzy/test.py', '__cached__': None, 'a': 10, 
			#'func': <function func at 0x10ce6eea0>}
        （3）#{'a': 20}

2.global 和 nonlocal
　　　　global:寻找全局作用域中的内容（声明在局部作用域里使用全局作用域的变量）
　　　　nolocal :声明在局部作用域里,使用上层局部作用域的变量, 且上层不可以是全局变量

		通过例子来加深理解：
			<1>
				a = 10
				def func():
    				global a    # a 不再是局部变量. 是全局变量
				    a = 30  # 把全局中的a重新赋值成30
				    print(a)  #30
				func()
				print(a)  #30

			<2>
				a = 10
				def func1():
				    a = 40
				    def func2():
				        nonlocal a  # 找局部作用域中 离他最近的那个变量引入进来
				        a = 20
				        print(a)#20   这时被引入的变量a的值从40变成了20
				    func2()
				    print(a)#20 这时这层的a已经被20所覆盖  
				func1()
				print(a)#10 nonlocal是在他外层找到值停止，如果没有到全局就回报错，不会到全局

				结果：
					20
					20
					10

			<3>
				a = 10
				def fun1():
				    a = 20
				    def fun3():
				        def fun2():
				            nonlocal a
				            a = a + a
				            print(a)#40
				        fun2()
				    fun3()
				    print(a)#40
				fun1()
				print(a)#10

				结果：
					40
					40
					10

			<4>
				a = 10
				def fun1():
				    def fun3():
				        b = 30
				        def fun2():
				            global a
				            nonlocal b
				            a = a + b
				            print(a)#40
				        fun2()
				    fun3()
				    print(a)#40
				fun1()
				print(a)#40

				结果：
					40
					40
					40

			<练习>
				a = 1
				def fun_1():
				    a = 2
				    def fun_2():
				        nonlocal a
				        a = 3
				        def fun_3():
				            a = 4
				            print(a)
				        print(a)
				        fun_3()
				        print(a)
				    print(a)
				    fun_2()
				    print(a)
				print(a)
				fun_1()
				print(a)

				结果：
					1
					2
					3
					4
					3
					3
					1

















