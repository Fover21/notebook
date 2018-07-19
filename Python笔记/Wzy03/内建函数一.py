内建函数
	
	1. 
		abs(number)
		用法：返回数字的绝对值

	2.
		all(iterable)
		用法：如果iterable的所有元素都是真值，就返回True，否则返回False

	3.
		any(iterable)
		用法：如果iterable的所有元素都是假值，就返回False，否则返回True

	4.
		ascii(object)
		用法：对非ASCII字符进行转义

	5.
		bin(integer)
		用法：将整数转换为以字符串表示的二进制字面量

	6. 
		bool(x)
		用法：将x解读为布尔值，并返回True和False

	7.
		bytes()
		用法：返回一个可修改的bytes对象

	8.
		callbale(object)
		用法：检查对象是否可被调用

	9.
		chr(number)
		用法：返回一个字符，其Unicode码点为指定数字

	10.
		classmethod(func)
		用法：根据实例方法，创建一类方法。

	11.
		complex(real,imag)
		用法：返回一个复数，其实部和虚部都为指定值

	11.5
		delattr(object,name)
		用法：删除指定对象的指定属性。
	
	12.
		dict([mapping -or- sequence])
		用法：创建一个字典，可根据另一种映射或（key，value）列表来创建，也可以使用关键字参数来调用

	13.
		dir([object])
		用法：列出当前可见作用域中的（大部分）命令，或列出指定对象的（大部分）属性

	14.
		divmod(a,b)
		用法：返回（a//b,a%b）（对于浮点数有一些特殊规则）

	15.
		enumerate(iterable)
		用法：迭代iterable中所有的（index，item）。可提供关键字star，以便不从开头开始迭代。

	16.
		eval(string[,globals[,locals]])
		用法：计算以字符串表示的表达式，还可在指定的全局和局部作用域内进行

	17.
		filter(function,sequence)
		用法：返回一个列表，其中包含指定序列中这样的元素，即对其应用指定的函数时，结果为真。

	18.
		float(object)
		用法：将字符串或数字转换为浮点数

	19.
		format(value[,format_spec])
		用法：返回对指定字符串设置格式后的结果。格式设置规范的作用与字符串方法format一样

	20.
		frozenset([iterable])
		用法：创建一个不可修改的集合，这意味着可将其添加到其他集合中

	21.
		getattr(object,name[,default])
		用法：返回指定对象中指定属性的值，还可给这个属性指定默认值

	22.
		globals()
		用法：返回一个表示当前全局作用域的字典

	23.
		hasattr(object,name)
		用法：检查指定对象是否包含指定的属性

	24.
		help([object])
		用法：调用内置的帮助系统，打印有关对象的帮助信息。

	25.
		hex(number)
		用法：将数字转换为十六进制的字符串

	26.
		id(object)
		用法：返回指定对象独一无二的ID

	27.
		input([prompt])
		用法：以字符串的方式返回用户输入的数据，还可显示指定的提示语

	28.
		int(object[,radix])
		用法：将字符串或数字转换为整数，还可指定基数

	29.
		isinstance(object,classinfo)
		用法：检测object是否是classinfo的实例，其中参数classinfo可以是类对象，类型对象，或类和类型对象元组

	30.
		issubclass(class1,class2)
		用法：检测class1是否是class2的子类（每个类都被视为他自己的子类）

	31.
		iter(object[,sentinel])
		用法：返回一个迭代器对象，即object.__iter__().这个迭代器对象用于迭代序列（如果object支持__getitem__）
			如果指定了sentinel，这个迭代器将不断调用object，直到返回sentinel

	32.
		len(object)
		用法：返回指定对象的长度（包含的项谁数）

	33.
		list([sequence])
		用法：创建一个列表，也可根据指定的序列创建列表。

	34.
		locals()
		用法：返回一个当前局部作用域的字典（请不要修改这个字典）

	35.
		map(function,sequence,...)
		用法：创建一个列表，其中包含对指定序列包含的项执行指定函数返回的值

	36.
		max(object1[,object2,...])
		用法：如果object1不是空序列，就返回其中最大的元素，否则返回提供的参数（object1，object2等）中最大的那个

	37.
		min(object1[,object2,...])
		用法：如果object1不是空序列，就返回其中最小的元素，否则返回提供的参数（object1，object2等）中最小的那个

	38.
		next(iterator[,default])
		用法：返回iterator.__next__()的值，还可指定默认值，他指定在到达了迭代器末尾时将返回的值。

	39.
		object()
		用法：返回一个object实例，object是所有新式类的基类。

	40.
		oct(number)
		用法：将整数转换为八进制字符串

	41.
		open(filename[,mode[,bufsize]])
		用法：打开一个文件并返回一个文件对象，（还有其他可选参数，如指定编码和错误处理方式的参数）

	42.
		ord(char)
		用法：返回执行字符的Unicode码点

	43.
		pow(x,y[,z])
		用法：返回x的y次方，还可以将结果对z求模

	44.
		print(x,...)
		用法：将0个或更多参数作为一行打印到标准输出，并用空格分割参数。可使用关键字参数
			sep，end，file和flush调整这种行为。

	45.
		property([fget[,fset[,fdel[,doc]]]])
		用法：根据一组存取函数创建一个特性

	46.
		range([start,]stop[,step])
		用法：根据参数start（包含，默认为0），stop（不包含）和step（默认为1）以序列的方式返回指定范围内的一些列值

	47.
		repr(object)
		用法：返回对象的字符串表示，通常用做eval 的参数

	48.
		reversed(sequence)
		用法：返回一个反向迭代序列的迭代器

	49.
		round(float[,n])
		用法：将指定的浮点数圆整到小数点n位（默认为0为）

	50.
		set([iterable])
		用法：返回一个集合，如果指定了iterable,该集合的元素将是从中取得的

	51.
		setattr(object,name,value)
		用法：将指定对象的指定属性设置为指定的值

	52.
		sorted(iterable[,cmp][,key][,reverse])
		用法：返回一个排序后的列表，其中的元素来着iterable.可选参数与列表的方法sort相同

	53.
		staticmethod(func)
		用法：根据实例方法创建一个静态（类）方法

	54.
		str(object)
		用法：返回指定对象的格式良好的字符串表示

	55.
		sum(sqp[,start])
		用法：计算数字序列中所有元素的总和，再加上可选参数start的值（默认为0），然后返回结果

	56.
		super([type[,obj/type]])
		用法：讲一个方法调用委托给超类的代理

	57.
		tuple([sequence])
		用法：创建一个元组。如果指定了可选参数secquence，该元组包含的项将于该参数指定的序列相同

	58.
		type(object)
		用法：返回指定对象类型

	59.
		type(name,bases,dict)
		用法：返回一个新的类型对象，其名称，基类和作用域由相应的参数指定

	60.
		vars([object])
		用法：返回一个表示局部作用域的字典或一个包含指定对象属性的属性的字典（请不要修改这个字典）

	61.
		zip(sequence1,...)
		用法：返回一个元组迭代器，其中每个元组都包含提供序列的相应项。返回的列表与提供的最短序等长。





















