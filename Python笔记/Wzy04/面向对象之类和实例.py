1.类的定义
	定义是用过class关键字
		class Student(object):
			pass
	class 后面紧接着是类名，即Student，类名通常是大写开头的单词，
	紧接着是(object),表示该类是从哪个类继承下来的。如果没有合适
	的继承类，就使用object类，这个是所有类最终都会继承的类。

	定义好了Student类，就可以根据Student类创建出Student的实例，
	创建实例是通过类名+()实现的

	res = Student()
	print(res)#<__main__.Student object at 0x1035d35c0>
	print(Student)#<class '__main__.Student'>

	可以看到，res指向的是一个Student实例，而Student本省则是一个类。

	可以自由的给实例变量绑定属性，eg. 给res绑定一个name属性
	res.name = 'Jake'
	print(res.name)#Jake

	由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们
	认为必须绑定的属性强制填写进去，通过定义一个特殊的__init__方法
	在创建实例的时候，把name，age，sex等属性绑定上去。
	    def __init__(self, name, age, sex):
	        self.name = name
	        self.age = age
	        self.sex =sex
	    注：__init__是双下划线

	注意：
		__init__方法第一个参数永远是，self。表示创建的实例本身，
		因此，在__init__方法内部，就可以把各种属性绑定到self，
		因此，self就指向创建的实例本身。
		有了__init__方法，在创建实例的时候，就不能传入空的参数了
		必须传入与__init__方法匹配的参数，但self不需要传，Python
		解释器自己会把实例变量传进去。

		res = Student('Jake', 60, '男')
		print(res.age)#60

	和普通方法相比，在类中定义的函数只有一点不同，就是第一个参数永远
	都是self，并且调用时，不用传递参数。除此之外，与类的方法与普通方
	法没有什么区别。

	总结：
		__dict__ : 可查询类和对象中内容，并以字典形式返回。
		1.类名+() ---->实例化一个对象
		2.这个时候会自动执行__init__方法，并且将对象传给__init__的self参数
		3.给对象封装相应的属性。

2.数据封装
	面向对象编程的一个重要的特点就是数据封装。
	在上面的Student类中，每个实例都拥有各自的name,age,sex这些数据。
	既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从
	外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，
	这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本
	身是关联起来的，我们称之为类的方法：

	class Student(object):
	    def __init__(self, name, age, sex):
	        self.name = name
	        self.age = age
	        self.sex =sex

	    def print_message(self):
	        print('%s:%s:%s' % (self.name, self.age, self.sex))

	res = Student('Jake', 60, '男')
	res.print_message()#Jake:60:男

	这样一来，我们从外部看Student类，就只需要知道，创建实例需要给出name,age,sex
	而如何打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很
	容易，但却不用知道内部实现的细节。封装的另一个好处就是，可以给Student类增加新
	的方法。

	总结：
		1.类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都是
		互相独立的，互不影响。
		2.方法就是与实例绑定的函数，和普通函数不同，方法可以直接返回实例的数据。
		3.Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然他们
		都是同一类的不同实例，但拥有的变量名称都可能不同。