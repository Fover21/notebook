# #********struct模块********#

# 1.按照指定格式将Python数据转换为字符串,该字符串为字节流,如网络传输时,
# 不能传输int,此时先将int转化为字节流,然后再发送;
# 2.按照指定格式将字节流转换为Python指定的数据类型;
# 3.处理二进制数据,如果用struct来处理文件的话,需要用’wb’,’rb’以二
# 进制(字节流)写,读的方式来处理文件;
# 4.处理c语言中的结构体;


# struct模块中的函数

# 函数										return				explain
# pack(fmt,v1,v2…)						string				按照给定的格式(fmt),把数据转换成字符串(字节流),并将该字符串返回.
# pack_into(fmt,buffer,offset,v1,v2…)		None				按照给定的格式(fmt),将数据转换成字符串(字节流),并将字节流写入以offset开始的buffer中.(buffer为可写的缓冲区,可用array模块)
# unpack(fmt,v1,v2…..)					tuple				按照给定的格式(fmt)解析字节流,并返回解析结果
# pack_from(fmt,buffer,offset)			tuple				按照给定的格式(fmt)解析以offset开始的缓冲区,并返回解析结果
# calcsize(fmt)							size of fmt			计算给定的格式(fmt)占用多少字节的内存，注意对齐方式


# 当打包或者解包的时,需要按照特定的方式来打包或者解包.该方式就是格式化字符串,
# 它指定了数据类型,除此之外,还有用于控制字节顺序、大小和对齐方式的特殊字符.

# 格式符

# 格式符		C语言类型				Python类型		Standard size
# x			pad byte(填充字节)	no value	 
# c			char				string of length 1		1
# b			signed char			integer					1
# B			unsigned char		integer					1
# ?			_Bool				bool					1
# h			short				integer					2
# H			unsigned short		integer					2
# i			int					integer					4
# I(大写的i)	unsigned int		integer					4
# l(小写的L)	long				integer					4
# L			unsigned long		long					4
# q			long long			long					8
# Q			unsigned long long	long					8
# f			float				float					4
# d			double				float					8
# s			char[]				string	 
# p			char[]				string	 
# P			void *				long	 
# 注- -!

# _Bool在C99中定义,如果没有这个类型,则将这个类型视为char,一个字节;
# q和Q只适用于64位机器;
# 每个格式前可以有一个数字,表示这个类型的个数,如s格式表示一定长度的字符串,4s表示长度为4的字符串;4i表示四个int;
# P用来转换一个指针,其长度和计算机相关;
# f和d的长度和计算机相关;

#对齐方式
# Character		Byte order		Size	Alignment
# @(默认)		本机				本机		本机,凑够4字节
# =				本机				标准		none,按原字节数
# <				小端				标准		none,按原字节数
# >				大端				标准		none,按原字节数
# !				network(大端)	标准		none,按原字节数


# 了解c语言的人，一定会知道struct结构体在c语言中的作用，它定义了一种结构，里面包含不同类型的数据(int,char,bool等等)，
# 方便对某一结构对象进行处理。而在网络通信当中，大多传递的数据是以二进制流（binary data）存在的。当传递字符串时，不必
# 担心太多的问题，而当传递诸如int、char之类的基本数据的时候，就需要有一种机制将某些特定的结构体类型打包成二进制流的字
# 符串然后再网络传输，而接收端也应该可以通过某种机制进行解包还原出原始的结构体数据。python中的struct模块就提供了这样
# 的机制，该模块的主要作用就是对python基本类型值与用python字符串格式表示的C struct类型间的转化（This module 
# performs conversions between Python values and C structs represented as Python strings.）。stuct模块
# 提供了很简单的几个函数，下面写几个例子。该模块作用是完成Python数值和C语言结构体的Python字符串形式间的转换。这可以
# 用于处理存储在文件中或从网络连接中存储的二进制数据，以及其他数据源。

# ********用途: 在Python基本数据类型和二进制数据之间进行转换
# struct模块提供了用于在字节字符串和Python原生数据类型之间转换函数，比如数字和字符串

# 它除了提供一个Struct类之外，还有许多模块级的函数用于处理结构化的值。这里有个格式符(Format specifiers)的概念，
# 是指从字符串格式转换为已编译的表示形式，类似于正则表达式的处理方式。通常实例化Struct类，调用类方法来完成转换，
# 比直接调用模块函数有效的多。下面的例子都是使用Struct类。

# 好在Python提供了一个struct模块来解决str和其他二进制数据类型的转换。


# struct的pack函数把任意数据类型变成字符串：

import struct
print(struct.pack('>I', 10240099))
#结果：b'\x00\x9c@c'
# pack的第一个参数是处理指令，'>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 后面的参数个数要和处理指令一致。
# unpack把str变成相应的数据类型：
print(struct.unpack('>I', b'\x00\x9c@c'))
#结果：(10240099,)



