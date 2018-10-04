===========itertools模块==========
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
利用python的itertools可以轻松地进行排列组合运算

itertools的方法基本上都返回迭代器

比如

•itertools.combinations('abcd',2)

　　　　这个方法从序列abcd中任选两个进行组合，返回一个迭代器，以tuple的形式输出所有组合，如('a','b'),('a','c')....等等。总共是C24 =6种组合

•itertools.permutations（'abc',2）

　　　　和combinations类似，为排序，输出的迭代器，里面内容是('a','b'),('b','a')....等等，一共是A2 3=6种组合

•itertools.product('abc','123')

　　　　相当于是下面这样的代码

for element1 in list1:
    for element2 in list2:
        yield element1,element2
            
            
            
            　　　　计算多个迭代器的笛卡尔积。

•itertools.combinations_with_replacement('abc',2)

　　　　和combinations相比之差别在于可重复，即结果中会有('a','a'),('b','b')等出现

==============================================

除了以上纯排列组合之外，itertools还提供很多很便利的方法

•itertools.imap()与map函数相似，但是返回迭代器

　　　　比如imap(pow,[1,2],[1,2])

　　　　//函数做参数，后跟若干个iterable对象。跟几个取决于前面那个函数有几个参数。而imap的操作是讲多个iterable对象中的元素一一对应地进行给出的函数操作

　　　　在这个例子中，最终迭代器中的内容就是pow(1,1)=1,pow(2,2)=4,pow(3,3)=27

•itertools.compress('ABCD',[1,0,1,0])

　　　　根据后者列表中的1和0所指出的真假情况，取舍前面给出的序列中的值，返回这些值为内容的迭代器

　　　　这个例子中最后的内容就是'A'和'C'

•itertools.chain(list1,list2...)

　　　　将参数中的iterable对象按顺序合并起来，返回的迭代器将按顺序给出这些对象中的元素

　　　　如果list(chain(list1,list2,list3...))相当于是list1+list2+list3...把这几个list合并起来了

•itertools.count(n)

　　　　返回一个无限的迭代器，内容是从n开始一个一个往上加的整数

•itertools.cycle(list)

　　　　返回一个无限迭代器，不断迭代list中的所有内容

•itertools.ifilter(func,seq)

　　　　对seq中的元素一个一个依次放进func，func是个针对某个值做出判断返回True或者False的函数。

　　　　返回的迭代器里面的内容仅为经过func判断后为True的那些元素，和filter()类似
