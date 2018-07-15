1.is 和 == 的区别

	id()官网描述
		def id(*args, **kwargs): # real signature unknown
	    """
	    Return the identity of an object.
	    
	    This is guaranteed to be unique among simultaneously existing objects.
	    (CPython uses the object's memory address.)
	    """
	    pass

	   这个id()和is有什么关系呢。
	   		注意：is比较的就是id()计算出来的结果。由于id侍帮助我们查看某数据对象的内存地址。
	   				那么is比较的就是数据(对象的内存地址)。
	   				最终我们通过is可以查看两个变量使用的是否是同一个对象。

	   	== 双等表示的是判断是否相等。
	   		注意：这个双等比较的的是具体的值，而不是内存地址。


	   	例子：
	   		s1 = "哈哈"
			s2 = "哈哈"
			print(s1 == s2) # True
			print(s1 is s2) # True 原因是有缓存的存在 导致两个变量量指向的是同⼀一个对象
			l1 = [1, 2, 3]
			l2 = [1, 2, 3]
			print(l1 == l2) # True, 值是⼀一样的 print(l1 is l2) # False, 值是假的

2.python3的encode()和decode()
	在python3的内存中. 在程序运行阶段. 使⽤用的是unicode编码. 
	因为unicode是万国码. 什么内容都可以进行显示. 那么在数据传输和存储的时候由于unicode比较浪费空间和资源. 
	需要把unicode转存成UTF-8或者GBK进行存储. 怎么转换呢. 
	在python中可以把⽂字信息进行编码. 编码之后的内容就可以进行传输了了. 
	编码之后的数据是bytes类型的数据.其实啊.还是原来的数据只是经过编码之后表现形式发生了改变而已.

	bytes 的表现形式
		1.英文 b'nihao'英文的表现形式和字符串没什么两样
		2.中文 b'\xc4\xe3\xba\xc3'这是一个汉子‘你好’的utf-8的bytes表现形式


	字符串在传输时转化为bytes->encode(字符集)来实现。
	英⽂编码之后的结果和源字符串一致. 
	中文编码之后的结果根据编码的不同. 编码结果 也不同. 
	我们知道.一个中⽂的UTF-8编码是3个字节. 一个GBK的中文编码是2个字节. 
	编码之后的类型就是bytes类型. 在网络传输和存储的时候我们python是保存和存储的bytes
	类型. 那么在对方接收的时候. 也是接收的bytes类型的数据. 
	我们可以使⽤用decode()来进行解码操作. ->把bytes类型的数据还原回我们熟悉的字符串。

	例子：编码和解码的时候都需要制定编码格式.

			s = "我是文字"
			bs = s.encode("GBK") # 我们这样可以获取到GBK的⽂字 
			# 把GBK转换成UTF-8
			# ⾸首先要把GBK转换成unicode. 也就是需要解码
			s = bs.decode("GBK") # 解码
			# 然后需要进行重新编码成UTF-8
			bss = s.encode("UTF-8") # 重新编码
			print(bss)













