
Python十进制数学计算模块decimal
Python提供了decimal模块用于十进制数学计算，它具有以下特点：

提供十进制数据类型，并且存储为十进制数序列；
有界精度：用于存储数字的位数是固定的，可以通过decimal.getcontext（）.prec=x 来设定，不同的数字可以有不同的精度
浮点：十进制小数点的位置不固定（但位数是固定的）
decimal的构建：

可以通过整数、字符串或者元组构建decimal.Decimal，对于浮点数需要先将其转换为字符串

decimal的context：

decimal在一个独立的context下工作，可以通过getcontext来获取当前环境。例如前面提到的可以通过decimal.getcontext().prec来设定小数点精度（默认为28）：

>>> from decimal import Decimal as D
>>> from decimal import getcontext
>>> getcontext()
Context(prec=6, rounding=ROUND_HALF_EVEN, Emin=-999999999, Emax=999999999, capitals=1, flags=[Rounded, Inexact], traps=[DivisionByZero, InvalidOperation, Overflow])
>>> getcontext().prec = 6
>>> D(1)/D(3)
Decimal('0.333333')
decimal和float性能对比：

python -mtimeit -s 'from decimal import Decimal as D' 'D("1.2")+D("3.4")'
python -mtimeit -s 'from decimal import Decimal as D' '1.2+3.4'
我在虚拟机中测试前者耗时是后者的1.7k倍，但这在某些运算（例如财务运算）中是值得的，但如果要对非整数做上百次的运算，应坚持使用float。


from decimal import * 即可调用decimal模块中的内容。
1. Decimal类型的优点
Decimal类型是在浮点类型的基础上设计的，但是它在几个地方上要优于floating point：
1）Decimal类型可以非常精确地在计算机中存储，而学过c++的都知道，浮点型在计算机中是无法精确存储的，比如1.1和2.2在计算机中存储后，运算（1.1+2.2）表达式的值结果会是3.3000000000000003；Decimal类型则不会出现这种情况。同样，由于无法精确存储，浮点型也就无法精确计算（相对于Decimal类型），可以再测试（0.1+0.1+0.1-0.3）两种类型的计算结果。
2）Decimal类型会自动保留小数点后面不需要的0，以与输入的精度相匹配，比如下面小程序中的例子：浮点型的1.20+1.30结果是2.5；而Decimal类型结果是2.50，这样貌似比较人性化。
3）Decimal类型可以根据需要自己设置小数点后精度。通过getcontext().prec = x （x为你想要的精度来设置，getcontext()函数下面再详细介绍）。
4）Decimal类型有很强的管理功能，它能够根据需要设置，来控制输出的格式，得到或者忽略某类错误（如除0，可以设置忽略它，而得到一个Infinity的Decimal值）。

2. decimal模块的构成
文档说，decimal模块主要由三部分构成：the decimal number ，the context of arithmetic ，signals 。
1）decimal number是不可改变的常量，它也不会截取小数点后多余的0；除了正常的数外， 它还包括'Infinity'，'-Infinity'，'NaN'等数。
2）the context of arithmetic是当前计算环境的一些参数，包括精度位数prec，舍弃位数规则rounding，指数的最大值最小值Emin、Emax，科学计数法e的大小写Capitals，指数是否超出范围clamped，运算结果的标志flags，哪些操作要触发traps等。
3）signals是在运算过程中产生的一些状态，这些状态可以根据需要用来提示、忽略、报错等。
signals和flags、traps是对应的，假设运算过程中产生了除0这样一个状态，那么flags中就会产生一个DivisionByZero为1这样的信息，接着如果在traps中包含这个操作，那么python就会报个异常出来。这样一个处理机制，可以人为的设置自己需要的信息或异常提示，而把另外一些忽略。


3. context

可以用getcontext()函数得到当前运算环境的参数，直接打印 print (get context())，以我的为例子

Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999999, Emax=999999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, Overflow, DivisionByZero])

其中，prec精度为28，是默认值，可以通过getcontext().prec = 10这样来设置自己想要的精度；rounding的规则是ROUND_HALF_EVEN （具体下面介绍），此外还有其他一些规则，感兴趣的可以查阅文档或自己测试；traps数组表明当前如果出现这三种状态会报异常。当然，其中的参数都可以自己修改。

值得一提的是，精度值的修改只在运算中才会体现出来，比如精度是5，输入Decimal(’1.222222222‘)，输出仍然是这个数；但是Decimal('1.222222222') + Decimal('1.11111111') 的结果精度就为6了。

4. Signals

decimal模块中提供了10种signals，下面简单介绍一下：

1）Clamped：越界，指数超出Emin或Emax范围；如果发生，则会在小数部分添加0来表示；

2）DecimalException；

3）DivisionByZero：在除法运算中出现，除数为0；如果不捕捉该错误，则返回Infinity或-Infinity；

4）Inexact：不精确，使用round函数舍弃的小数部分中包含除0以外的数字；

5）InvalidOperation：无效计算或计算无意义，比如两个无穷大相减等；如果不捕捉该错误，则返回NaN（Not a Number）；

6）Overflow：在round后指数超出Emax范围，如果不捕捉，则根据round规则来判断返回什么值；

7）Rounded：如果round操作舍弃了小数，不管是不是0，都发生；如果不捕捉，则返回 值未改变；

8）Subnormal：指数值过小；如果不捕捉，则返回  值不变；

9）Underflow：指数值太小，且round操作向0逼近；

10）FloatOperation：如果不捕捉，则混合float型和Decimal型的操作可以执行；如果捕捉，则只有相等判断和显式转换可以执行，其余的都报错。



5. Round类型

Decimal中大致有以下几种类型，做简单介绍一下，如有错误，希望指正：

1）ROUND_UP：舍弃小数部分非0时，在前面增加数字，如 5.21 -> 5.3；

2）ROUND_DOWN：舍弃小数部分，从不在前面数字做增加操作，如5.21->5.2；

3）ROUND_CEILING：如果Decimal为正，则做ROUND_UP操作；如果Decimal为负，则做ROUND_DOWN操作；

4）ROUND_FLOOR：如果Decimal为负，则做ROUND_UP操作；如果Decimal为正，则做ROUND_DOWN操作；

5）ROUND_HALF_DOWN：如果舍弃部分>.5，则做ROUND_UP操作；否则，做ROUND_DOWN操作；

6）ROUND_HALF_UP：如果舍弃部分>=.5，则做ROUND_UP操作；否则，做ROUND_DOWN操作；

7）ROUND_HALF_EVEN：如果舍弃部分左边的数字是奇数，则做ROUND_HALF_UP操作；若为偶数，则做ROUND_HALF_DOWN操作；
