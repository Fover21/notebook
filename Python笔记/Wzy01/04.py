一、列表
	需要安利一下：列表和字符串数是不一样的.进行操作时列表可以发生改变，而字符串不可以，所以直接在原来的对象上操作。
	1.列表的增加
	    def append(self, p_object): # real signature unknown; restored from __doc__
        """ L.append(object) -> None -- append object to end """
        pass

        用法:在列表的最后追加一个对象。
        例子：
        	lis = [2]
			lis.append('nihao') #在列表最后追加元素
			print(lis)------>[2, 'nihao']

        def insert(self, index, p_object): # real signature unknown; restored from __doc__
        """ L.insert(index, object) -- insert object before index """
        pass

        用法:在索引index位置，添加一个对象.
        		如果index超过了给点列表的索引最大值，该对象会被插到列表最后位置。
        例子：
        	lis = [2, 3, 4]
			lis.insert(1, [3,3]) #在索引位置添加元素
			print(lis)------>[2, [3, 3], 3, 4]

			lis = [2, 3, 4]
			lis.insert(5, [3,3]) #在索引位置添加元素
			print(lis)------>[2, 3, 4, [3, 3]]

        def extend(self, iterable): # real signature unknown; restored from __doc__
        """ L.extend(iterable) -> None -- extend list by appending elements from the iterable """
        pass

        用法:用来扩展列表，但是给的参数是一个可迭代对象。是将可迭代对象的每个元素加入原列表的尾部。

        例子：
        	lis = [2]
			lis.extend(['nihao '])
			print(lis)------>[2, 'nihao ']
			lis = [2]
			lis.extend('nihai')
			print(lis)------>[2, 'n', 'i', 'h', 'a', 'i']

    2.列表的删除
        def remove(self, value): # real signature unknown; restored from __doc__
        """
        L.remove(value) -> None -- remove first occurrence of value.
        Raises ValueError if the value is not present.
        """
        pass

        用法:删除列表中第一个指定的元素value.如果该元素不存在列表中，会报错。
        例子:
        	lis = ['你好', 1, [1, 2, 2]]
			lis.remove('你好') #删除指定元素，列表中第一个出现的
			print(lis)------>[1, [1, 2, 2]]

			lis.remove('0')   #如果删除不存在的元素会报错
			print(lis)------>ValueError

        def pop(self, index=None): # real signature unknown; restored from __doc__
        """
        L.pop([index]) -> item -- remove and return item at index (default last).
        Raises IndexError if list is empty or index is out of range.
        """
        pass

        用法:如果没有参数默认删除的是列表的最后一个元素。(和栈的那个一样)
        	而index参数表示所删元素的索引。而且该方法会返回你所删元素的值。
        	如果index参数不在列表的索引范围内，会报错。
        例子：
        	lis = ['你好', 1, [1, 2, 2]]
			e = lis.pop()  #默认删除最后一个元素，有返回值
			print(e)------>[1, 2, 3]
			print(lis)------>['你好', 1]

			lis = ['你好', 1, [1, 2, 2]]
			e = lis.pop(0) #参数为所删元素的位置，如果位置不存在会报错
			print(e)------>你好
			print(lis)------>[1, [1, 2, 2]]

        def clear(self): # real signature unknown; restored from __doc__
        """ L.clear() -> None -- remove all items from L """
        pass

        用法:直接清空列表。返回[]
        例子：
        	l = [1, 2]
			lis.clear()  #直接清空列表
			print(lis)------>[]

        del L[index]          用法:直接删除索引位置的元素
       	del L[start:end]      用法:直接删除切片出来的所有元素
       	del L[start:end:step] 用法:直接删除切片出来的带步长的元素

    3.列表的修改
    	列表的修改只有索引和切片修改
    	1）索引修改
	    	lis = [1, 2, '1', '2', ['33', '44']]
			lis[4] = (2, 4)
			print(lis) ---->[11111, 2, '1', '2', (2, 4)]
			------
			lis[7] = '888'  #如果超出列表索引位置，会报错
			print(lis) ---->报错(IndexError)
		2）切片修改  注：切片修改是迭代修改
			lis = [1, 2, '1', '2', ['33', '44']]
			lis[1:] = '好好好'  #迭代修改
			print(lis)------>[1, '好', '好', '好']

			lis = [1, 2, '1', '2', ['33', '44']]
			lis[1:-1] = [1, 2, 3]
			print(lis)------>[1, 1, 2, 3, ['33', '44']]

			lis = [1, 2, '1', '2', ['33', '44']]
			lis[0:4:2] = '你好'
			print(lis)------>['你', 2, '好', '2', ['33', '44']]

			is = [1, 2, '1', '2', ['33', '44']]
			lis[0:4:4] = '你好'  #步长不能越过切片的界，否则会报错
			print(lis)------>(ValueError)
	4.列表的查询
		列表是一个可迭代对象所以可以进行for循环。
			for e in L:
				print(e)

	5.其他方法
		def count(self, value): # real signature unknown; restored from __doc__
        """ L.count(value) -> integer -- return number of occurrences of value """
        return 0

        用法:统计元素value出现的次数。

        def sort(self, key=None, reverse=False): # real signature unknown; restored from __doc__
        """ L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE* """
        pass

        用法:对列表L进行排序，默认从小到大。reverse=Falsec(从小到大)reverse=True(从大到小)
        	注:他只是一个操作，没有返回值。

        def reverse(self): # real signature unknown; restored from __doc__
        """ L.reverse() -- reverse *IN PLACE* """
        pass
        
        用法:反转列表L    
        	注:他只是一个操作，没有返回值。

        def index(self, value, start=None, stop=None): # real signature unknown; restored from __doc__
        """
        L.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present.
        """
        return 0

        用法:返回列表中value的第一个索引，或者在找不到索引的时候引发 ValueError异常，可定义索引的范围为L[start:end].

        def copy(self): # real signature unknown; restored from __doc__
        """ L.copy() -> list -- a shallow copy of L """
        return []

        (这是一个浅拷贝，等后面详细介绍深浅拷贝！)

        len(L)----->求列表L的长度。(系统内置方法)

二、元组
	俗称不可变的列表又称只读列表
	1）元组的内置方法
	    def count(self, value): # real signature unknown; restored from __doc__
        """ T.count(value) -> integer -- return number of occurrences of value """
        return 0

        用法:统计元素value出现的次数。

    	def index(self, value, start=None, stop=None): # real signature unknown; restored from __doc__
        """
        T.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present.
        """
        return 0

        用法:返回元组中value的第一个索引，或者在找不到索引的时候引发 ValueError异常，可定义索引的范围为T[start:end].

    2）注意
    	(1)
	    	tu = (1, "哈哈", [], "呵呵")
			tu[2].append("麻花") # 可以改. 没报错 
			tu[2].append("林林")
			print(tu)------>(1, '哈哈', ['麻花', '林林'], '呵呵')
			注：这里的元组的不可变的意思是子元素不可变，而子元素内部的子元素是可以变，这取决于字元素是否是可变对象。


			代码得多敲，不能光看！
















