Python面向对象之接口类（抽象类）:就是制定一个规范。

比如定义了一个接口类（抽象类）（他们是不可以进行实例化的，这就是他为什么是制定一个规范的原因）。
他的定义是需要abc模块，要变的就是他的方法，比如下面的pay方法，
定义好一个抽象类（接口类）Payment，他用装饰器@abstractmethod将pay方法装饰
这样，其他类如果都继承了Payment方法，其他类中就都需要有一个pay方法，如果没有就会报错。

就好比，起初我没有微信支付类，但是如果后续项目需要加微信支付此功能，支付的方法我可以起各种名字。
但是为了统一支付接口，我们继承抽象类Payment后，我们的支付接口名就必须用pay.

这就是接口类（抽象类的用途）

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):  # 抽象类（接口类）
    @abstractmethod
    def pay(self):  # 制定一个规范
        pass


class Alipay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        print('使用支付宝花了%s钱' % (self.money,))


class Jdpay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        print('使用京东支付了%s钱' % (self.money,))


class Wechatpay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        print('使用微信支付了%s钱' % (self.money,))

w1 = Wechatpay(200)
a1 = Alipay(150)
j1 = Jdpay(100)
w1.pay()
a1.pay()
j1.pay()