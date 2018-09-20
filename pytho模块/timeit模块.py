python中的计时器：timeit模块

(1)
timeit
	- 通常在一段程序的前后都用上time.time()然后进行相减就可以得到一段程序的运行时间，不过python提供了更强大的计时库：timeit


举例说明：


--timeit
# 导入timeit.timeit
from timeit import timeit

# 看执行1000000次x=1的时间：
a = timeit('x=1')

# 看x=1的执行时间，执行1次(number可以省略，默认值为1000000)：
b =timeit('x=1', number=1)

# 看一个列表生成器的执行时间,执行1次：
c =timeit('[i for i in range(10000)]', number=1)

# 看一个列表生成器的执行时间,执行10000次：
d = timeit('[i for i in range(100) if i%2==0]', number=10000)

print(a, b, c, d)


# 测试一个函数执行的时间
from timeit import timeit


def func():
    s = 0
    for i in range(1000):
        s += i
    print(s)


# timeit(函数名_字符串，运行环境_字符串，number=运行次数)
t = timeit('func()', 'from __main__ import func', number=1000) #运行1000次的执行时间
print(t)


（2）
repeat
	- 由于电脑永远都有其他程序也在占用着资源，你的程序不可能最高效的执行。所以一般都会进行多次试验，取最少的执行时间为真正的执行时间。


举例说明：


--repeat
from timeit import repeat


def func():
    s = 0
    for i in range(1000):
        s += i


# repeat和timeit用法相似，多了一个repeat参数，表示重复测试的次数(可以不写，默认值为3.)，返回值为一个时间的列表。
t = repeat('func()', 'from __main__ import func', number=100, repeat=5)
print(t)
print(min(t))
