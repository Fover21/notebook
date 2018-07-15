字典常用的就是，他的去重。

set集合是python的一个基本数据类型.
set中的元素是不重复的.⽆无序的.⾥面的元素必须是可hash的(int, str, tuple,bool)。
我们可以这样来记. set就是dict类型的数据但是不保存value, 只保存key. set也⽤{}表⽰
注意:
	set中的元素是不重复的, 且无序的.
	使⽤用这个特性.我们可以使⽤用set来去掉重复
	set集合中的元素必须是可hash的, 但是set本身是不可hash得. set是可变的。

set集合增删改查

1.增加
    def add(self, *args, **kwargs): # real signature unknown
        """
        Add an element to a set.
        
        This has no effect if the element is already present.
        """
        pass

        用法：添加一个元素到集合。重复的内容不会被添加到set集合。

        例子：
        	s = {"刘大哥", '关大哥', "张大哥"}
			s.add("赵子龙")
			print(s)
			s.add("赵子龙") # 重复的内容不不会被添加到set集合中 
			print(s)


    def update(self, *args, **kwargs): # real signature unknown
        """ Update a set with the union of itself and others. """
        pass

        用法：迭代更新

        例子：
        	s = {"刘大哥", '关大哥', "张大哥"} 
        	s.update("赵子龙") # 迭代更更新 
        	print(s)
			s.update(["阿斗", "卧龙","凤雏"]) 
			print(s)

2.删除
    def pop(self, *args, **kwargs): # real signature unknown
        """
        Remove and return an arbitrary set element.
        Raises KeyError if the set is empty.
        """
        pass

    	用法：随机删除一个元素，如果集合为空，会报错。

    	例子：

	    	s = {"刘大哥", '关大哥', "王大哥","张哥哥"} 
	    	item = s.pop() # 随机弹出⼀一个.
			print(s)
			print(item)

    def remove(self, *args, **kwargs): # real signature unknown
        """
        Remove an element from a set; it must be a member.
        
        If the element is not a member, raise a KeyError.
        """
        pass

    	用法：删除集合中指定成员，如果成员不存在会报错。

    	例子：
    		s = {"刘大哥", '关大哥', "王大哥","张哥哥"}
    		s.remove("关大哥") # 直接删除元素
			# s.remove("⻢马") # 不不存在这个元素. 删除会报错 
			print(s)

        def discard(self, *args, **kwargs): # real signature unknown
        """
        Remove an element from a set if it is a member.
        
        If the element is not a member, do nothing.
        """
        pass

    	用法：删除集合中指定成员，如果该集合不存在所删除成员，不做任何操作，也不会报错。

    	例子：
    		s = {1, 3, 4, 5}
			print(s)#{1, 3, 4, 5}
			s.discard(3)
			print(s)#{1, 4, 5}
			s.discard(66)
			print(s)#{1, 4, 5}

        def clear(self, *args, **kwargs): # real signature unknown
        """ Remove all elements from this set. """
        pass

    	clear()  清空set集合。
    	注意：set集合如果是空的。打印出来的是set()。需要和dict区分。
    	例子：
    		s = {1, 3, 4, 5}
			s.clear()
			print(s)。#set()

3.修改
	set 集合中的数据没有索引，也没有办法定位一个元素。所以没有办法直接修改。
	我们可以采用：
		1）先删除后添加的方式
		2）将set转为list删除元素后将list转为set

4.查询
	set是一个可迭代对象，所以可以进行for循环
		for x in s:
			print(x)

5.常用操作

	1.求差集（-）
	    def difference(self, *args, **kwargs): # real signature unknown
        """
        Return the difference of two or more sets as a new set.
        
        (i.e. all elements that are in this set but not the others.)
        """
        pass

        例子：
        	s1 = {1, 3, 5, 7, 9}
			s2 = {1, 3, 6, 8, 10}
			print(s1-s2)#{9, 5, 7}
			print(s1.difference(s2))#{9, 5, 7}
			print(s2-s1)#{8, 10, 6}
			print(s2.difference(s1))#{8, 10, 6}


    2.求交集（&）
        def intersection(self, *args, **kwargs): # real signature unknown
        """
        Return the intersection of two sets as a new set.
        
        (i.e. all elements that are in both sets.)
        """
        pass

        例子：
        	s1 = {1, 3, 5, 7, 9}
			s2 = {1, 3, 6, 8, 10}
			print(s1&s2)#{1, 3}
			print(s1.intersection(s2))
			print(s2&s1)#{1, 3}
			print(s2.intersection(s1))


    3.求对称差集（^）
        def symmetric_difference(self, *args, **kwargs): # real signature unknown
        """
        Return the symmetric difference of two sets as a new set.
        
        (i.e. all elements that are in exactly one of the sets.)
        """
        pass

        例子：
        	s1 = {1, 3, 5, 7, 9}
			s2 = {1, 3, 6, 8, 10}
			print(s1 ^ s2)#{5, 6, 7, 8, 9, 10}
			print(s1.symmetric_difference(s2))#{5, 6, 7, 8, 9, 10}
			print(s2 ^ s1)#{5, 6, 7, 8, 9, 10}
			print(s2.symmetric_difference(s1))#{5, 6, 7, 8, 9, 10}


    4.求并集（|）
        def union(self, *args, **kwargs): # real signature unknown
        """
        Return the union of sets as a new set.
        
        (i.e. all elements that are in either set.)
        """
        pass

        例子：
        	s1 = {1, 3, 5, 7, 9}
			s2 = {1, 3, 6, 8, 10}
			print(s1 | s2)#{1, 3, 5, 6, 7, 8, 9, 10}
			print(s1.union(s2))#{1, 3, 5, 6, 7, 8, 9, 10}
			print(s2 | s1)#{1, 3, 5, 6, 7, 8, 9, 10}
			print(s2.union(s1))#{1, 3, 5, 6, 7, 8, 9, 10}

    5.子集
         def issubset(self, *args, **kwargs): # real signature unknown
        """ Report whether another set contains this set. """
        pass

        例子：
        	s1 = {"1", "2"}
			s2 = {"1", "2", "3"}
			# ⼦子集
			print(s1 < s2) # set1是set2的⼦子集吗? True 
			print(s1.issubset(s2))

    6.超集
    	def issuperset(self, *args, **kwargs): # real signature unknown
        """ Report whether this set contains another set. """
        pass

        例子：
	        s1 = {"1", "2"}
			s2 = {"1", "2", "3"}
	        print(s1 > s2) # set1是set2的超集吗? False 
	        print(s1.issuperset(s2))




















