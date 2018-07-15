Python文件操作
准备工作：
	1）
	使用python来读取文件是非常简单的操作，我们使用open()函数来打开一个文件，获取到文件句柄，
	然后通过文件就可以进行各种各样的操作了。根据打开方式的不同能够执行的操作也会有相应的差异。
	2）
	打开文件的方式：r,w,a,r+,w+,a+,rb,wb,ab,r+b,w+b,a+b默认使用的是r(只读)模式。
	3）
	相对路径：相对于当前程序所在的文件夹。      ../ 返回上一级目录
	绝对路径：1.从磁盘根目录寻找。 2.互联网上的一个绝对路径。
	4）

	f = open('文件路径'，mode=’文件打开方式‘，encoding='编码格式')#mode=可以省略。
	pass
	f.close()

	上面三句可以换为

	with open('文件路径'，mode=’文件打开方式‘，encoding='编码格式') as f:
		pass

	with这个会自己执行完后关闭句柄。
	5）按文件中数据的组织形式把文件分为文本文件和二进制文件两类。
	6）句柄：通俗的说就是操作文件的指挥棒，如果你打开一个文件没有关闭，但是开其他文件也用了这个句柄，这个时候文件就不知道该听谁。
文件操作常用方法：
	1）flush()
		把缓冲区的内容写入磁盘，不关闭文件。

	2）close()
		把缓冲区的内容写入磁盘，关闭文件，释放文件对象。

	3）read(size)
		从文件中读取size个直接的内容作为结果返回，
		若size省略则读取整个文件的内容作为结果返回。

	4）readline()
		从文本文件中读取1行作为字符串返回。

	5）readlines()
		把文本文件中的每行作为字符串插入列表中，返回该列表。

	6）seek(offset,whence)
		把文件指针移到新的位置。offset表示相对于whence的位置。
		whence用于设置相对位置的起点：
			0表示从文件开始计算；
			1表示从当前位置开始计算；
			2表示从文件末尾开始计算。
		若whence省略，offset表示相对文件开头的位置。

	7）tell()
		返回当前文件指针的位置

	8）write(s)
		把字符串s的内容写入文本文件或写入二进制文件。

	9）writelines(List[AnyStr])
		把字符串列表写入文本文件中，不会添加换行符。

	10）truncate(size)
		删除从当前指针位置到文件末尾的内容。若指定了size，则不论指针在什么位置都留下钱size个字节，其余的删除。


文件操作：
	1）r 以只读方式打开一个文本文件，只运行读数据，若打开的文件不存在，则产生异常。

		例子：<1>
			f = open("file.txt", mode="r", encoding="utf-8")#创建句柄
			s = f.read()
			f.close()   # 关闭句柄
			print(s)

			<2>
			f = open("file.txt", mode="r", encoding="utf-8")
			for line in f:  # 每次读取一行. 赋值给前面的line变量
   				print(line)
			#print(f.readline()) #读一行
			f.close()
			<3>
			with open("file.txt", mode="r", encoding="utf-8") as f:
    			print(f.readlines())#将每行内容存入列表中

	2）r+ 以读写方式打开一个文本文件，不删除原内容，允许读和写，若打开的文件不存在，则产生异常。

		例子：<1>
			f = open("file.txt", mode="r+", encoding="utf-8") 
			# r+模式, 默认情况下光标在文件的开头, 必须先读, 后写
			f.write("周星星")#这样将文件中第一行的前三个数据改为了周星星，光标停留在周星星之后
			s = f.read()#这里读出的内容为：光标之后的所有内容
			f.flush()
			f.close()
			print(s)

			<2>
			with open("精品", mode="r+", encoding="utf-8") as f:
			    s = f.read(3)# 不管你前面读了几个. 后面去写都是在末尾
			    f.write("哈哈")   # 1.在没有任何操作之前进行写. 在开头写  
			      				#2. 如果读取了一些内容. 再写, 写入的是最后
			    print(s)
			

	3）w 以只写方式打开一个文本文件，删除原内容，只允许写数据。若打开的文件不存在则新建并打开。

		例子：
			f = open("file.txt", mode="w", encoding="utf-8")   
			# 写入之前会情掉原来的内容
			f.write("十")
			# f.writelines(['1', '2', '3'])#不添加换行符
			f.flush()
			f.close()

	4）w+ 以读写方式打开一个文本文件，删除原内容，允许读和写，若打开的文件不存在则新建并打开。

		例子：<1>
			f = open("file.txt", mode="w+", encoding="utf-8") 
			 # w 操作.会清空原来的内容.
			print(f.read())#读出一个空行，因为被清空了
			f.write("今天天气怎么样")
			f.seek(3)#移动3个字节，也就是一个汉子
			s = f.read()#读出的内容为。。。
			print(s)#天天气怎么样
			f.flush()
			f.close()

			<2>
			f = open("亵渎", mode="w+", encoding="utf-8")  
			# w 操作.会清空原来的内容.
			f.write("今天天气怎么样")#此时光标在尾部
			f.seek(3)#默认从0开始的
			f.write('你好')#这时指针在好之后气之前（文件中内容为：今你好气怎么样）
			s = f.read()
			print(s)#气怎么样
			f.seek(0)
			s = f.read()
			print(s)#今你好气怎么样
			f.flush()
			f.close()

	5）a 以追加方式打开一个文本文件，不删除原内容，允许在文件尾部写数据，若打开的文件不存在则新建并打开。

		例子：
			with open("file.txt", mode="a", encoding="utf-8") as f:
			# 在原来的基础上进行追加内容. (不管光标在哪)
				f.write("美女")
				f.flush()
			

	6）a+ 以读写方式打开一个文本文件，不删除原内容，允许在任何位置读，但只能在文件末尾追加数据，若打开的文件不存在则新建并打开。

		例子：
			f = open("file.txt", mode="a+", encoding="utf-8")   
			# 在原来的基础上进行追加内容. #	文件内容：你好
			f.seek(3)
			s = f.read()#读取内容
			print(s) #好
			f.write("小龙女")#添加到队尾
			f.flush()
		f.close()

	7）rb,rb+,wb,wb+,ab,ab+ 他们打开的是一个二进制文件，其他操作与不加b的文本文件操作一样。

		例子：
			with open("../吃的", mode="rb") as f:
    			content = f.read()
    			print(content)

			结果为：b'\xe7\x83....'












