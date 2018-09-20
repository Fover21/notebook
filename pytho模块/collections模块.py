collections模块

在内置数据类型（dict、list、set、tuple）的基础上，collections模块
还提供了几个额外的数据类型：Counter、deque、defaultdict、namedtuple和OrderedDict等。

1.namedtuple: 生成可以使用名字来访问元素内容的tuple

2.deque: 双端队列，可以快速的从另外一侧追加和推出对象

3.Counter: 计数器，主要用来计数

4.OrderedDict: 有序字典

5.defaultdict: 带有默认值的字典


******namedtuple******

我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
>>> p = (1, 2)
但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
这时，namedtuple就派上了用场：

>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(1, 2)
>>> p.x
1
>>> p.y
2
复制代码
类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：

#namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])


******deque******（底层用c语言链表写的。。。）

使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
因为list是线性存储，数据量大的时候，插入和删除效率很低。

deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

>>> from collections import deque
>>> q = deque(['a', 'b', 'c'])
>>> q.append('x')
>>> q.appendleft('y')
>>> q
deque(['y', 'a', 'b', 'c', 'x'])

deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，
这样就可以非常高效地往头部添加或删除元素

>>> q.remove('a')
>>> q
deque(['y', 'b', 'c', 'x'])

>>> q.insert(2,'xxx')
>>> q
deque(['y', 'b', 'xxx', 'c', 'x'])

小结：
在insert，remove的时候，deque的平均效率要远远高于列表。
列表根据索引查看某个值得效率要高于deque。
append和pop对列表的效率是没有影响的。

*******OrderedDict******

使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict：

>>> from collections import OrderedDict
>>> d = dict([('a', 1), ('b', 2), ('c', 3)])
>>> d # dict的Key是无序的
{'a': 1, 'c': 3, 'b': 2}
>>> od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
>>> od # OrderedDict的Key是有序的
OrderedDict([('a', 1), ('b', 2), ('c', 3)])

注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：

>>> od = OrderedDict()
>>> od['z'] = 1
>>> od['y'] = 2
>>> od['x'] = 3
>>> od.keys() # 按照插入的Key的顺序返回
['z', 'y', 'x']


******defaultdict******

带有默认值的字典

有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，
将小于 66 的值保存至第二个key的值中。即： {'k1': 大于66 , 'k2': 小于66}


from collections import defaultdict

values = [11, 22, 33,44,55,66,77,88,99,90]

my_dict = defaultdict(list)

for value in  values:
    if value>66:
        my_dict['k1'].append(value)
    else:
        my_dict['k2'].append(value)

使用dict时，如果引用的Key不存在，就会抛出KeyError。
如果希望key不存在时，返回一个默认值，就可以用defaultdict

>>> from collections import defaultdict
>>> dd = defaultdict(lambda: 'N/A')
>>> dd['key1'] = 'abc'
>>> dd['key1'] # key1存在
'abc'
>>> dd['key2'] # key2不存在，返回默认值
'N/A'

******Counter******

Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，
其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。
Counter类和其他语言的bags或multisets很相似。

c = Counter('abcdeabcdabcaba')
print c
输出：Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})

****创建

Counter类创建的四种方法：

>>> c = Counter()  # 创建一个空的Counter类
>>> c = Counter('gallahad')  # 从一个可iterable对象（list、tuple、dict、字符串等）创建
>>> c = Counter({'a': 4, 'b': 2})  # 从一个字典对象创建
>>> c = Counter(a=4, b=2)  # 从一组键值对创建


****计数值的访问与缺失的键

当所访问的键不存在时，返回0，而不是KeyError；否则返回它的计数。

计数值的访问
>>> c = Counter("abcdefgab")
>>> c["a"]
>>> c["c"]
>>> c["h"]

****计数器的更新（update和subtract）

可以使用一个iterable对象或者另一个Counter对象来更新键值。
计数器的更新包括增加和减少两种。其中，

增加使用update()方法：
计数器的更新（update）
>>> c = Counter('which')
>>> c.update('witch')  # 使用另一个iterable对象更新
>>> c['h']
>>> d = Counter('watch')
>>> c.update(d)  # 使用另一个Counter对象更新
>>> c['h']

减少则使用subtract()方法
计数器的更新（subtract）
>>> c = Counter('which')
>>> c.subtract('witch')  # 使用另一个iterable对象更新
>>> c['h']
>>> d = Counter('watch')
>>> c.subtract(d)  # 使用另一个Counter对象更新
>>> c['a']
-1


*****键的修改和删除


当计数值为0时，并不意味着元素被删除，删除元素应当使用del。 
键的删除


>>> c = Counter("abcdcba")
>>> c
Counter({'a': 2, 'c': 2, 'b': 2, 'd': 1})
>>> c["b"] = 0
>>> c
Counter({'a': 2, 'c': 2, 'd': 1, 'b': 0})
>>> del c["a"]
>>> c
Counter({'c': 2, 'b': 2, 'd': 1})


****elements()

返回一个迭代器。元素被重复了多少次，在该迭代器中就包含多少个该元素。
元素排列无确定顺序，个数小于1的元素不被包含。

elements()方法 
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> list(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']

****most_common([n])

返回一个TopN列表。如果n没有被指定，则返回所有元素。
当多个元素计数值相同时，排列是无确定顺序的。

most_common()方法
>>> c = Counter('abracadabra')
>>> c.most_common()
[('a', 5), ('r', 2), ('b', 2), ('c', 1), ('d', 1)]
>>> c.most_common(3)
[('a', 5), ('r', 2), ('b', 2)] 


****浅拷贝copy

浅拷贝copy
>>> c = Counter("abcdcba")
>>> c
Counter({'a': 2, 'c': 2, 'b': 2, 'd': 1})
>>> d = c.copy()
>>> d
Counter({'a': 2, 'c': 2, 'b': 2, 'd': 1})


****算术和集合操作

+、-、&、|操作也可以用于Counter。其中&和|操作分别返回两个Counter对象各元素的最小值和最大值。
需要注意的是，得到的Counter对象将删除小于1的元素。

Counter对象的算术和集合操作
>>> c = Counter(a=3, b=1)
>>> d = Counter(a=1, b=2)
>>> c + d  # c[x] + d[x]
Counter({'a': 4, 'b': 3})
>>> c - d  # subtract（只保留正数计数的元素）
Counter({'a': 2})
>>> c & d  # 交集:  min(c[x], d[x])
Counter({'a': 1, 'b': 1})
>>> c | d  # 并集:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})


****其他常用操作

下面是一些Counter类的常用操作，来源于Python官方文档

Counter类常用操作
sum(c.values())  # 所有计数的总数
c.clear()  # 重置Counter对象，注意不是删除
list(c)  # 将c中的键转为列表
set(c)  # 将c中的键转为set
dict(c)  # 将c中的键值对转为字典
c.items()  # 转为(elem, cnt)格式的列表
Counter(dict(list_of_pairs))  # 从(elem, cnt)格式的列表转换为Counter类对象
c.most_common()[:-n:-1]  # 取出计数最少的n个元素
c += Counter()  # 移除0和负值



















