继承：
	单继承和多继承
1.初识
class Father(object): #如果不写object默认继承
	pass

class Son(Father): #括号里面的称为：父类或基类或超类  括号外面的称为：子类或派生类
	pass

class Animal:

    breath = '呼吸'

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self):
        print(self)#111   #<__main__.Person object at 0x111ac3710>
        print('动物都需要进食....')


class Person(Animal):
    pass

print(Person.breath)#呼吸
Person.eat(111)#动物都需要进食....

p1 = Person('Jake', '男', 20)
print(p1.breath)#呼吸
print(p1)#<__main__.Person object at 0x111ac3710>
p1.eat()#动物都需要进食....

结果：
	呼吸
	111
	动物都需要进食....
	呼吸
	<__main__.Person object at 0x111ac3710>
	<__main__.Person object at 0x111ac3710>
	动物都需要进食....

总结：
	子类以及子类实例化的对象，可以访问父类的任何方法和变量。
	类名可以访问父类的所有内容。
	子类实例化的对象也可以访问父类所有内容。




只执行父类的方法:子类中不要定义与父类同名的方法
只执行子类的方法:在子类创建这个方法.

既要执行子类的方法,又要执行父类的方法?
有两种解决方法.1.通过类名。2.通过super()函数
    1,Animal.__init__(self, name, sex, age)
    2,super().__init__(name,sex,age)

class Animal:

    breath = '呼吸'

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self, argv):
        print('%s吃%s' % (self.name, argv))


class Person(Animal):
    def __init__(self, name,sex,age,wing): 
        # Animal.__init__(self, name, sex, age)
        super().__init__(name,sex,age)  #  super(Brid,self).__init__(name,sex,age)
        self.wing = wing

    def eat(self,argv):
        super().eat(argv)
        print('吃...')

p1 = Person('鹦鹉','男',20,'绿翅膀')
print(p1.__dict__)
p1.eat('金蝉')

结果：
	{'name': '鹦鹉', 'sex': '男', 'age': 20, 'wing': '绿翅膀'}
	鹦鹉吃金蝉
	吃...


2.进阶

类: 经典类, 新式类
新式类: 凡是继承object类都是新式类.
    python3x 所有的类都是新式类,因为python3x中的类都默认继承object.

经典类: 不继承object类都是经典类
    python2x:(既有新式类,又有经典类) 所有的类默认都不继承object类,
    		 所有的类默认都是经典类.你可以让其继承object.


单继承: 新式类,经典类查询顺序一样.

多继承:
     新式类: 遵循广度优先.
     经典类: 遵循深度优先.

多继承的新式类  广度优先 : 一条路走到倒数第二级,判断,如果其他路能走到终点,则返回走另一条路.如果不能,则走到终点.
多继承的经典类  深度优先 : 一条路走到底.































