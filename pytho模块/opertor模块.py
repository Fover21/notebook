
=============operator模块简单介绍==============

简单记录一些，详细看官方文档。
operator.concat(a, b)
**operator.__concat__(a, b)**
对于 a、b序列，返回 a + b(列表合并）
                  
---------------------------------

operator.countOf(a, b)
返回 b 在 a 中出现的次数
                  
---------------------------------

perator.delitem(a, b)
**operator.__delitem__(a, b)**
删除 a 中索引为 b 的值
                  
---------------------------------
operator.getitem(a, b)
**operator.__getitem__(a, b)**
返回 a 中索引为 b 的值

---------------------------------
                  
operator.indexOf(a, b)
返回 b 在 a 中首次出现位置的索引值。

---------------------------------
                  
operator.setitem(a, b, c)
**operator.__setitem__(a, b, c)**
设置 a 中索引值为 b 的项目值更改为 c

------------------------------------------------------------------
operator 模块也为属性和项目的查找提供了一些工具。这些工具使得 map(), sorted(),tertools.groupby()
或其他函数 需要的参数的提取更方便更快速。上面的函数有一个共同点，即均接受函数参数。

operator.attrgetter(attr)
                  
operator.attrgetter(*attrs)
                  
返回一个可调用的对象，该对象从运算中获取 'attr' 。如果请求的属性不止一个的话， 返回属性的元组。
这些属性的名字可以包括 '.'。
                  
比如：
                  
f = attrgetter('name')，调用 f(b) 返回 b.name

f = attrgetter('name', 'date'), 调用 f(b) 返回 (b.name, b.date)

f = attrgetter('name.first', 'name.last'), 调用 f(b) 返回 (b.name.first, b.name.last)
   
 ------------------------------------------------------------------
                  
operator.itemgetter(item)
operator.itemgetter(*items)

返回一个可调用的对象，该对象通过运算符的 __getitem__()的方法 从运算中获取 item 。如果指定了多个
item ， 返回查找值的元组。

比如：

f = itemgetter(2), 调用 f(r) 返回 r[2]

g = itemgetter(2, 5, 3), 调用 f(r) 返回 (r[2], r[3], r[3])
                  
                  
          
          最后 operator 相关的信息对应如下：
          
          Operation    Syntax    Function
          Addition    a + b    add(a, b)
          Concatenation    seq1 + seq2    concat(seq1, seq2)
          Containment Test    obj in seq    contains(seq, obj)
          Division    a / b    div(a, b) (without future.division)
          Division    a / b    truediv(a, b) (with future.division)
          Division    a // b    floordiv(a, b)
          Bitwise And    a & b    and_(a, b)
          Bitwise Exclusive Or    a ^ b    xor(a, b)
          Bitwise Inversion    ~ a    invert(a)
          Bitwise Or    a b    or_(a, b)
          Exponentiation    a ** b    pow(a, b)
          Identity    a is b    is_(a, b)
          Identity    a is not b    is_not(a, b)
          Indexed Assignment    obj[k] = v    setitem(obj, k, v)
          Indexed Deletion    del obj[k]    delitem(obj, k)
          Indexing    obj[k]    getitem(obj, k)
          Left Shift    a << b    lshift(a, b)
          Modulo    a % b    mod(a, b)
          Multiplication    a * b    mul(a, b)
          Negation (Arithmetic)    - a    neg(a)
          Negation (Logical)    not a    not_(a)
          Positive    + a    pos(a)
          Right Shift    a >> b    rshift(a, b)
          Sequence Repetition    seq * i    repeat(seq, i)
          Slice Assignment    seq[i:j] = values    setitem(seq, slice(i, j), values)
          Slice Deletion    del seq[i:j]    delitem(seq, slice(i, j))
          Slicing    seq[i:j]    getitem(seq, slice(i, j))
          String Formatting    s % obj    mod(s, obj)
          Subtraction    a - b    sub(a, b)
          Truth Test    obj    truth(obj)
          Ordering    a < b    lt(a, b)
          Ordering    a <= b    le(a, b)
          Equality    a == b    eq(a, b)
          Difference    a != b    ne(a, b)
          Ordering    a >= b    ge(a, b)
          Ordering    a > b    gt(a, b)
                  
                  
                  
                  
