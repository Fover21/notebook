内置函数二：

	1.lambda   (匿名函数)
		为了解决一些简答的需求而设计的一句话函数。不需要def来声明。
		def func(n):
		    return n*n
		print(func(10))#100

		f = lambda n: n*n
		print(f(10))#100

		注意：
			语法：函数名 = lambda 参数:返回值

			1.函数的参数可以有多个。多个参数之间用逗号隔开。
			2.匿名函数不管多复杂，只能写一行，且逻辑结束后直接返回数据
			3.返回值和正常的函数一样，可以是任意数据类型。

		匿名函数并不是说一定没有名字，这里前面的变量就是一个函数名，说他是匿名原有
		是我们通过__name__查看的时候咩有名字的，统一都叫做lambda。在调用的时候
		没有什么特别之处。像正常的函数调用。

	2.sorted    (排序函数)
		语法：soret(Iterable,key=None,reverse=False)
			Iterable:可迭代对象
			key:排序规则（排序函数），在soret内部会将可迭代对象中的每一个元素
				传递给这个函数的参数，根据函数运算的结果进行排序。
			recerse:是否是倒序。True：倒序，False：正序。
			<1>
			lst = [1,5,3,4,6]
			lst2 = sorted(lst)
			print(lst) # 原列表不会改变 
			print(lst2) # 返回的新列表是经过排序的

			结果：
				[1, 5, 3, 4, 6]
				[1, 3, 4, 5, 6]
			<2>
			dic = {1:'A', 3:'C', 2:'B'}
			print(sorted(dic)) # 如果是字典. 则返回排序过后的key

			结果：
				[1, 2, 3]
			<3>
			# 根据字符串长度进行排序
			lst = ["哈哈", "我爱你", "中国", "亲爱的母亲"]
			# 计算字符串串长度 
			def func(s):
			    return len(s)
			print(sorted(lst, key=func))

			结果：
				['哈哈', '中国', '我爱你', '亲爱的母亲']
			<4>
			 # 根据字符串长度进行排序
			lst = ["哈哈", "我爱你", "中国", "亲爱的母亲"]
			# 计算字符串长度 
			print(sorted(lst, key=lambda s: len(s)))

			结果：
				['哈哈', '中国', '我爱你', '亲爱的母亲']
			<5>
			lst = [{"id":1, "name":'a', "age":18},
			       {"id":2, "name":'b', "age":16},
			       {"id":3, "name":'c', "age":17}]
			# 按照年龄对学生信息进行排序
			print(sorted(lst, key=lambda e: e['age']))

			结果：
				[{'id': 2, 'name': 'b', 'age': 16}, {'id': 3, 'name': 'c', 'age': 17}, {'id': 1, 'name': 'a', 'age': 18}]


	3.filter  (筛选函数)
		语法：filter(function,Iterable)
			function:用来筛选的函数，在filter中会自动的把iteratable中的元素传递给function
					然后根据function返回True或者False来判断是否保留此数据。
			Iterable:可迭代对象

			例子：
				lis = [
				    {'id': 1, 'age':30},
				    {'id': 2, 'age':40},
				    {'id': 3, 'age':20},
				    {'id': 4, 'age':40}

				]
				ll = filter(lambda dic: dic['age'] >= 40,lis)#返回一个迭代器
				print(list(ll))#[{'id': 2, 'age': 40}, {'id': 4, 'age': 40}]

	4.map    (映射函数)
		语法：map(function,Iterable)
			可以根据可迭代对象中的每一个元素进行映射。分别去执行function

		例子：
			<1>
			#计算列表中每个元素的平方 ,返回新列列表
			def func(e):
			    return e*e
			mp = map(func, [1, 2, 3, 4, 5])
			print(mp)
			print(list(mp))

			结果：
				<map object at 0x1037503c8>
				[1, 4, 9, 16, 25]
			<2>
			#改写成lambda
			print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))

			结果：
				[1, 4, 9, 16, 25]
			<3>
			# 计算两个列表相同位置的数据的和
			lst1 = [1, 2, 3, 4, 5]
			lst2 = [2, 4, 6, 8, 10]
			print(list(map(lambda x, y: x+y, lst1, lst2)))

			结果：
				[3, 6, 9, 12, 15]
















