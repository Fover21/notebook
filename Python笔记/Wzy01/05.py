1.
	dict保存的数据不是按照我们添加进去的顺序保存的. 是按照hash表的顺序保存的. 而hash表 不是连续的. 所以不能进⾏切片⼯工作. 它只能通过key来获取dict中的数据.
2.
	字典的嵌套
3.
	keys()    拿到dict_keys([])
	values()	拿到dict_values([])
	items()		拿到dict_items([()])
4.
	解构，解包
		a,b = [1,2]
		a = 1
		b = 2

		a,b = (1,2)
		a = 1
		b = 2
5.
	遍历dict
		for item in dict.items():
			k, v = item
			print(k, v)

		for k ,v in dict.items():
			print(k, v)

	dic = {1: 'a', 2: 'b',3: 'c'}
	for a in dic: #直接循环字典拿到key
		print(a)
		print(dic[a])