先来安利一下：字典的键必须是可哈希的。（通俗理解就是不可变的，比如，int,str,tuple.因为这样就可以将你这个键固定好，查的时候很快！）

1.字典的增加
	1）赋值操作
		D[key] = value
	2）setdefault()
	    def setdefault(self, k, d=None): # real signature unknown; restored from __doc__
        """ D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D """
        pass

        用法:如果只有一个参数，功能与get()方法一样，用来查询(见后面)。
			如果有两个参数，第一个参数k为键，第二个参数d为值。
			如果有两个参数，第一个参数k不存在，那么会将这个键值对存入字典D中。
						如果第一个参数k存在，那么原字典D中键为k的值不变。
		注意:该方法有返回值，一个参数与get()方法一样。
						两个参数，返回，进行完setdefault()操作后再对字典进行get()操作。

		例子：
			dic = {'haixing': "还行"}
			dic.setdefault('haixing', '我爱你')#如果存在不会替换
			print(dic) #->{'haixing': '还行'}
			dic = {'haixing': "还行"}
			dic.setdefault('hello', '我爱你')#如果不存在加入字典
			print(dic)	#->{'haixing': '还行', 'hello': '我爱你'}

2.字典的删除
	1）pop()
	    def pop(self, k, d=None): # real signature unknown; restored from __doc__
        """
        D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised
        """
        pass

        用法:如果只有一个参数k，那么将会删除键k对应的键值对，如果没有键k那么将会报错。
        	如果有两个操作，那么将会删除键k对应的键值对，如果没有键k那么将会输出默认值d。
        注意：有返回值。返回k键k对应的值value。

        例子：
        	dic = {'woaini': '我爱你', 'zhongguo': '中国', 'qinaide': '亲爱的'}
			res = dic.pop('woaini')   #返回value值
			print(res) #->我爱你
			print(dic) #->{'zhongguo': '中国', 'qinaide': '亲爱的'}

			dic = {'woaini': '我爱你', 'zhongguo': '中国', 'qinaide': '亲爱的'}
			res = dic.pop('wi','啊啊啊')   #返回默认值值
			print(res) #->啊啊啊
			print(dic) #->{'woaini': '我爱你', 'zhongguo': '中国', 'qinaide': '亲爱的'}

    2）del
    	del D[key]  删除key对应的键值对

    3）popitem()
    	def popitem(self): # real signature unknown; restored from __doc__
        """
        D.popitem() -> (k, v), remove and return some (key, value) pair as a
        2-tuple; but raise KeyError if D is empty.
        """
        pass

        用法:随机删除一组键值对。并以元组的形式返回所删键值对。如果字典D为空则报错。

        例子：
        	dic = {'woaini': '我爱你', 'zhongguo': '中国', 'qinaide': '亲爱的'}
			res = dic.popitem()# 随机删除一个，返回键值组成的一个元组
			print(res) #->('qinaide', '亲爱的')
			print(dic) #->{'woaini': '我爱你', 'zhongguo': '中国'}

     4）clear()
     	D.clear()  直接清空字典，返回{}

3.字典的修改
	1）赋值操作
		D[key] = value [通过键key来修改]

		例子:
		dic = {'qian': 1000000, 'zhongguo': '中国', 'qinaide': '亲爱的'}
		dic['qian'] = '我喜欢'
		print(dic) #->{'qian': '我喜欢', 'zhongguo': '中国', 'qinaide': '亲爱的'}

	2）update()
	    def update(self, E=None, **F): # known special case of dict.update
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """
        pass

        用法:D.update(E),将字典E中的键值对并到D中，如果存在键key相等，将会被覆盖。

        例子：
        	dic1 = {'1': 11111, "2": 222222, '3':  33333}
			dic2 = {'4': 44444,'2': '二二二二'}
			dic1.update(dic2)  #将dic2里面的内容追加到dic1中，如果dic1中存在dic2的内容则被dic2覆盖
			print(dic1) #->{'1': 11111, '2': '二二二二', '3': 33333, '4': 44444}
			print(dic2) #->{'4': 44444, '2': '二二二二'}

4.字典的查询
	1）那key当索引
		D[key] ->返回键key对应的值value

		例子：
			dic = {'及时雨': '宋江', '易大师': '剑圣', '大宝剑': '盖伦'}
			print(dic['易大师']) #->剑圣
			print(dic['提莫'])  #会报错

	2）get()
	    def get(self, k, d=None): # real signature unknown; restored from __doc__
        """ D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None. """
        pass

        用法:如果只有一个参数k，如果k存在，那么将会返回k对应的值value。
        					如果k不存在，那么将会返回None。
        	如果有两个参数，d为默认值，如果k存在那么将会返回k对应的值value。
        							如果不存在将会返回默认值d。

        例子：
       		dic = {'及时雨': '宋江', '易大师': '剑圣', '大宝剑': '盖伦'}
			print(dic.get('易大师')) #->剑圣        #存在返回value值    
			print(dic.get('提莫'))   #——>None      #不存在返回None     
			print(dic.get('提莫','迅捷')) #->迅捷   #不存在返回第二个参数的默认值 

    3）setfefaule()
    	def setdefault(self, k, d=None): # real signature unknown; restored from __doc__
        """ D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D """
        pass

        用法:如果只有一个参数，功能与get()方法一样，用来查询。
			如果有两个参数，第一个参数k为键，第二个参数d为值。
			如果有两个参数，第一个参数k不存在，那么会将这个键值对存入字典D中。
						如果第一个参数k存在，那么原字典D中键为k的值不变。
		例子：
			dic = {'及时雨': '宋江', '易大师': '剑圣', '大宝剑': '盖伦'}
			print(dic.setdefault('易大师'))   #->剑圣   #一个参数和get返回值一样
			print(dic.setdefault('提莫'))  #->None    #一个参数和get返回值一样

			dic = {'及时雨': '宋江', '易大师': '剑圣', '大宝剑': '盖伦'}
			print(dic.setdefault('提莫','迅捷')) #->迅捷   #将他加入列表再执行get操作
			print(dic.setdefault('易大师','迅捷')) #->剑圣  #将他加入列表再执行get操作

5.其他相关操作
	1）keys()
	    def keys(self): # real signature unknown; restored from __doc__
        """ D.keys() -> a set-like object providing a view on D's keys """
        pass

        用法:将字典D中的所有键key以列表的形式取出，放入一个dict_keys()中，他可用来遍历。

        例子：
        	dic1 = {'1': 11111, "2": 222222, '3':  33333}
			print(dic1.keys()) #->dict_keys(['1', '2', '3'])
            for i in dic1.keys():
                print(i)

    2）values()
        def values(self): # real signature unknown; restored from __doc__
        """ D.values() -> an object providing a view on D's values """
        pass

        用法:将字典D中的所有值value以列表的形式取出，放入一个dict_values()中，他可用来遍历。

        例子：
        	dic1 = {'1': 11111, "2": 222222, '3':  33333}
			print(dic1.values())#->dict_values([11111, 222222, 33333])
            for i in dic1.values():
                print(i)
    
    3）items()
        def items(self): # real signature unknown; restored from __doc__
        """ D.items() -> a set-like object providing a view on D's items """
        pass

        用法:将字典D中的所有键值对以列表的形式取出，键值对以元组形式存，放入一个dict_items()中，他可用来遍历。

        例子：
        	dic1 = {'1': 11111, "2": 222222, '3':  33333}
			print(dic1.items())#->dict_items([('1', 11111), ('2', 222222), ('3', 33333)])
            for i in dic1.items():
                print(i)

    4）fromkeys()
        def fromkeys(*args, **kwargs): # real signature unknown
        """ Returns a new dict with keys from iterable and values equal to value. """
        pass

        用法：给一个可迭代对象的所有元素，给他们相同的值value。用来初始化
        例子：
		dic = dict.fromkeys([1,2,3,4], 'ss')
		print(dic)  #->{1: 'ss', 2: 'ss', 3: 'ss', 4: 'ss'}

    5）copy()
        def copy(self): # real signature unknown; restored from __doc__
        """ D.copy() -> a shallow copy of D """
        pass

        对字典D进行浅拷贝，返回一个和D相同键值对的新字典。
        浅拷贝后面介绍


        代码得多敲，不能光看。
