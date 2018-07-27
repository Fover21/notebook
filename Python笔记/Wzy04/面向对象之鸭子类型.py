python没有多态?他有什么? 他有鸭子类型.
鸭子类型 : 看着像鸭子,他就是鸭子.

比如一些类，他们中有一些方法，有着相同的功能，
这时为我们将这些相同功能的名字命名为一样的。
那么这些类 都互称为鸭子.

class Str:
    def index(self):
        pass

class List:
    def index(self):
        pass

class Tuple:
    def index(self):
        pass

 python为弱类型语言，处处是多态。