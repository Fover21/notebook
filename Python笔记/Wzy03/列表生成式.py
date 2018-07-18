列表生成式
	
	列表生成式即List Comprehensions ,是Python内置的非常简单却强大的可以用来创建list的生成式

	例子：
		要生成list [1,2,3,4,5] 可以用 list(range(1,6))
		但是如果要生成[1*1,2*2,3*3,4*4,5*5]怎么办？
		一种方法是循环
			L = []
			for i in range(1,6):
				L.append(i*i)
			print(L)
			但是循环太繁琐，而列表生成式则可以用一句代替循环生成上面的list

		另一种方法：
			准备好我要装B了：
			L = [i * i for i in range(1,6)]
			print(L)#[1, 4, 9, 16, 25]

			注意：写列表生成式时，把要生成的元素i*i放在前面，就可以把list创建出来。


			for 循环后面还可以加if判断。

			例子 : 
				L = [i * i for i in range(1,6) if i % 2 == 0]
				print(L) #[4, 16]

			for 循环后面还可以使用两层循环，生成全排列。

			例子:
				L = [a + b for a in 'ASD' for b in 'qwe']
				print(L)#['Aq', 'Aw', 'Ae', 'Sq', 'Sw', 'Se', 'Dq', 'Dw', 'De']

				相当于：
				L = []
				for a in 'ASD':
    				for b in 'qwe':
        				s = a + b
        				L.append(s)
				print(L)

			在下也是听说，三层和三层以上用的比较少。


	运用列表生成式可以写出很简洁的代码。

			for 循环其实可以同时使用两个甚至多个变量，

			例子:
				dic = {1 : 'a', 2 : 'b', 3 : 'c'}
				for k,v in dic.items():
					print(k,'---',v)

					结果：
						1 --- a
						2 --- b
						3 --- c
			因此，列表生成式为：
				dic = {1 : 'a', 2 : 'b', 3 : 'c'}
				L = [k + '---' + v for k ,v in dic.items()]
				print(L)#['1---a', '2---b', '3---c']


                    list1 = [1, 2, 3, 4]
                    list2 = ['a', 'b', 'c', 'd']

                    dic = {list1[i]: list2[i] for i in range(len(list2))}
                    print(dic)






