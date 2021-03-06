广义的封装：实例化一个对象，给对象空间封装一些属性。
狭义的封装：私有制

私有成员：私有静态字段，私有方法，私有对象属性


对于私有静态字段，私有方法，私有对象属性,类的外部不能访问.
----# 实例化对象不能访问私有静态字段，私有方法，私有对象属性
----# 类名不能访问私有静态字段，私有方法，私有对象属性

对于私有静态字段，私有方法，私有对象属性,类的内部可以访问.
对于私有静态字段，私有方法，私有对象属性来说,只能在本类中内部访问,类的外部,派生类均不可访问.

python中用双下划线开头的方式将属性隐藏起来（设置成私有的）
----#其实这仅仅是一种变形操作
----#类中所有下划线开头的名称如__x都会自动变形成：_类名__x的形式
----这种自动变形的特点：
--------1.类中定义的__x只能在内部使用，如self.__x，引用的就是变形得到结果。
--------2.这种变形其实正是针对外部的变形，在外部是无法通过__x这个名字访问到的
--------3.在子类定义的时候__x不会覆盖在父类定义的__x，因为子类中变形成：_子类名__x,而父类中变成：_父类名__x
			即双下划线开头的属性在继承给子类时，子类是无法覆盖的。

		这种变形需要注意的问题：
------------1.这种机制也并没有真正意义上限制我们从外部直接访问属性，知道了类名和属性名就可以拼出名字：_类名__属性名
------------2.变形的过程只在类的定义是发生一次，在定义后的复制操作，不会变形。
------------3.在继承中，父亲如果不让子类覆盖自己的方法，可以将方法定义为私有的。


封装不是单纯意义上的隐藏

1.封装数据
----将数据隐藏起来不是目的。隐藏起来然后对外提供操作该数据的接口，然后我们可以在接口附加上对该数据操作的限制
	以此完成对数据属性操作的严格性。
2.封装方法
----目睹是隔离复杂度。
	提示：在编程语言里面，对外提供的接口（接口可以理解为一个入口），可以是函数，称为接口函数，这与接口的概念
			不一样，接口代表一组接口函数的集合。