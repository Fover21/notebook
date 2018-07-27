Python3 多继承的MRO算法选择。MRO（Method Resolution Order）：方法解析顺序。
Python3 只保留了C3算法！

C3算法解析：

1.C3算法解析
C3算法：MRO是一个有序列表L，在类被创建时就计算出来了。
L(Child(Base1, Base2)) = [Child + merge(L(Base1), L(Base2), Base1Base2)]
L(object) = [object]
L的性质：结果为列表，列表中至少有一个元素即类自己。
+	  ：添加到列表的末尾，即[A + B] = [A, B]
merge ：
1）如果列表为空则结束，非空读merge中第一个列表的表头
2）查看该表头是否在merge中所有列表的表尾中
2）-->3）不在，则放入最终的L中，并从merge中的所有列表中删除，然后回到1）
2）-->4）在，查看当前列表是否是merge中的最后一个列表
4）-->5）不是，跳过当前列表，读merge中下一个列表的表头，然后回到2）
4）-->5）是，异常。类定义失败。
需要了解一些词的意思：
表头：列表的第一个元素（列表：ABCD，那么表头就是A，B，C，D都是表尾）
表尾：列表中表头以为的元素集合（也可以为空）
merge 简单的说就是寻找合法表头（也就是不在表尾中的表头），如果所有表中都未找到合法表头则异常

2.例子
<1>
L(D) = L(D(O))
= D + merge(L(O))
= D + O
=[D, O]

class D:
    pass


print(D.mro())#[<class '__main__.D'>, <class 'object'>]

<2>
L(B) = L(B(D,E))
= B + merge(L(D) , L(E))
= B + merge(DO , EO) # 第一个列表DO的表头D，其他列表比如EO的表尾都不含有D，所以可以将D提出来，即D是合法表头
= B + D + merge(O , EO) #从第一个开始表头是O,但是后面的列表EO的表尾中含有O所以O是不合法的，所以跳到下一个列表EO
= B + D + E + merge(O , O)
= [B,D,E,O]

class D:
    pass


class E:
    pass


class B(D, E):
    pass


print(B.mro())#[<class '__main__.B'>, <class '__main__.D'>, <class '__main__.E'>, <class 'object'>]

<3>
L(C) = [C,E,F,O]
L(A(B,C)) = A + merge(L(B),L(C),BC)
= A + merge(BDEO,CEFO,BC)#B是合法表头
= A + B + merge(DEO,CEFO,C)#D是合法表头
= A + B + D + merge(EO,CEFO,C)#E不是合法表头，跳到下一个列表CEFO，此时C是合法表头
= A + B + D + C + merge(EO,EFO)#由于第三个列表中的C被删除，为空，所以不存在第三个表，只剩下两个表；此时E是合法表头
= A + B + D + C + E + merge(O,FO)#O不是合法表头，跳到下一个列表FO，F是合法表头，
= A + B + D + C + E + F + merge(O,O)#O是合法表头
= A + B + D + C + E + F + O
= [A,B,D,C,E,F,O]

class D:
    pass


class E:
    pass


class F:
    pass


class B(D, E):
    pass


class C(E, F):
    pass


class A(B, C):
    pass


print(A.mro())#[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]
