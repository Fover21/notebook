在python中使用正则表达式

1.转义符
正则表达式中的转义：
'\('表示匹配小括号
[()+*/?&.] 在字符组中一些特殊的字符会现出原形
所有的\s\d\w\S\D\W\n\t都表示他原本的意义
[-]只有写在字符组的首位的时候表示普通的减号
写在其它位置的时候表示范文[1-9]如果就是想匹配减号[1\-9]

Python中的转义符
分析过程：
'\n'#\是转义符 赋予这个n一个特殊的意义 表示一个换行符
print('\\n')
print(r'\n')
转义：python '\\\\n' 正则 '\\n'
结论：
r'\\n' r'\n'  在python中

2.re模块

准备：
flags有很多可选值：

re.I(IGNORECASE)忽略大小写，括号内是完整的写法
re.M(MULTILINE)多行模式，改变^和$的行为
re.S(DOTALL)点可以匹配任意字符，包括换行符
re.L(LOCALE)做本地化识别的匹配，表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境，不推荐使用
re.U(UNICODE) 使用\w \W \s \S \d \D使用取决于unicode定义的字符属性。在python3中默认使用该flag
re.X(VERBOSE)冗长模式，该模式下pattern字符串可以是多行的，忽略空白字符，并可以添加注释


1）匹配方法 findall() search() mathc()
(1)findall()
def findall(pattern, string, flags=0):
    """Return a list of all non-overlapping matches in the string.

    If one or more capturing groups are present in the pattern, return
    a list of groups; this will be a list of tuples if the pattern
    has more than one group.

    Empty matches are included in the result."""
    return _compile(pattern, flags).findall(string)

用法：所有的匹配结果都返回在一个列表中，如果没有匹配上就返回一个空列表。

例子：
import re
res = re.findall(r'\w+', r'Jake@tom')
print(res)
结果：
['Jake', 'tom']

(2)search()
def search(pattern, string, flags=0):
    """Scan through string looking for a match to the pattern, returning
    a match object, or None if no match was found."""
    return _compile(pattern, flags).search(string)

用法：返回第一个匹配到的对象，可以调用这个对象的 group()方法返回第一个匹配到的值。没有匹配上返回None。

例子：
import re
res1 = re.search(r'\d+', r'222T333')
print('search', res1)
print(res1.group())
结果：
search <_sre.SRE_Match object; span=(0, 3), match='222'>
222

(3)match()
def match(pattern, string, flags=0):
    """Try to apply the pattern at the start of the string, returning
    a match object, or None if no match was found."""
    return _compile(pattern, flags).match(string)

用法：和search用法一样，唯一区别就是只在字符串开始匹配

例子：
import re
res2 = re.match(r'\d+', r'222T333')#与search区别就是只在字符串开始匹配
print('match', res2)
print(res2.group())
结果：
match <_sre.SRE_Match object; span=(0, 3), match='222'>
222

2）切割和替换 sub() subn() split()
(1)sub()
def sub(pattern, repl, string, count=0, flags=0):
    """Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the match object and must return
    a replacement string to be used."""
    return _compile(pattern, flags).sub(repl, string, count)

用法：根据（pattern）正则表达式规则将匹配好的字符串替换为新字符串（repl）,string为目标串，count可以指定替换次数

例子：
import re
res = re.sub(r'\d+', 'SSS',r'222XXX333V3')
print(res)
结果：
SSSXXXSSSVSSS

(2)subn()
def subn(pattern, repl, string, count=0, flags=0):
    """Return a 2-tuple containing (new_string, number).
    new_string is the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in the source
    string by the replacement repl.  number is the number of
    substitutions that were made. repl can be either a string or a
    callable; if a string, backslash escapes in it are processed.
    If it is a callable, it's passed the match object and must
    return a replacement string to be used."""
    return _compile(pattern, flags).subn(repl, string, count)

用法：根据（pattern）正则表达式规则将匹配好的字符串替换为新字符串（repl）,string为目标串，count可以指定替换次数.
返回的结果是元组，其中有替换结果和替换次数

例子：
import re
res = re.subn(r'\d+', 'SSS',r'222XXX333V3')
print(res)
结果：
('SSSXXXSSSVSSS', 3)

(3)split()
def split(pattern, string, maxsplit=0, flags=0):
    """Split the source string by the occurrences of the pattern,
    returning a list containing the resulting substrings.  If
    capturing parentheses are used in pattern, then the text of all
    groups in the pattern are also returned as part of the resulting
    list.  If maxsplit is nonzero, at most maxsplit splits occur,
    and the remainder of the string is returned as the final element
    of the list."""
    return _compile(pattern, flags).split(string, maxsplit)

用法：按照正则表达式匹配好的字符串去切割目标字符串，匹配对个结果会先拿第一个结果切割目标串，
切割完后拿第二个结果切割这两个字符串，以此类推。可以指定最大切割次数，返回一个列表。

例子：
import re
res = re.split(r'\d+', r'333FF444FF44')
print(res)
结果：
['', 'FF', 'FF', '']

3）进阶 compile() finditer()
(1)compile()*****时间效率
def compile(pattern, flags=0):
    "Compile a regular expression pattern, returning a pattern object."
    return _compile(pattern, flags)

用法：把正则表达式编译为正则表达式对象
作用：节省时间，只有在多次使用某一个相同的正则表达式的时候，才会帮助我们提高效率。

例子：
import re
res = re.compile(r'\d+')
print(res)
结果：
re.compile('\\d+')

(2)finditer()*****空间效率
def finditer(pattern, string, flags=0):
    """Return an iterator over all non-overlapping matches in the
    string.  For each match, the iterator returns a match object.

    Empty matches are included in the result."""
    return _compile(pattern, flags).finditer(string)

用法：根据正则表达式匹配字符串得到 一个迭代器，迭代器中每个元素都是一个对象，每个
对象都可通过 group()方法获取对应的匹配值。

例子：
import re
res = re.compile(r'\d+')
res = re.finditer(r'\d+', r'sss444ff333f')
print(res)
for r in res:
    print(r, '--------', r.group())

结果：
<callable_iterator object at 0x106f29668>
<_sre.SRE_Match object; span=(3, 6), match='444'> -------- 444
<_sre.SRE_Match object; span=(8, 11), match='333'> -------- 333

3.正则表式进阶（很重要）
分组与re模块的组合使用
1）分组 () 与 findall() finditer()
import re
#findall会优先显示分组中的内容，如果在第左半边括号后加上?:就会取消分组优先
#(?:正则表达式) 取消优先
#如果有一个分组，那么就将匹配好的元素放到一个列表中，如果分组有两个以上，那么这些元组组成一个元组存到列表中
res = re.findall(r'<(\w+)>', r'<a>我爱你中国</a><h1>亲爱的母亲</h1>')
print(res)
res = re.findall(r'<(?:\w+)>', r'<a>我爱你中国</a><h1>亲爱的母亲</h1>')
print(res)
结果：
['a', 'h1']
['<a>', '<h1>']


#不会优先分组中内容，可以通过group(分组名)来得到分组中的值
import re
res = re.finditer(r'<(?:\w+)>', r'<a>我爱你中国</a><h1>亲爱的母亲</h1>')
for i in res:
    print(i.group())

结果：
<a>
<h1>

2）分组命名  分组与 search()
#（？P<name>正则表达式）表示给分组起名字
#（？P=name）表示使用这个分组，这里匹配到的内容应该和分组中内容完全一致
<1>
import re
#search匹配的是第一次匹配好的值
#得到的结果可以使用结果.group()方法得到
#如果search与分组配合使用给group传参数，第一个分组内容传1的到第一分组内容，以此类推
#groups()函数的到一个所有分组的集合以元组形式返回
res = re.search(r'<(\w+)>(\w+)</(\w+)>', r'<a>hello</a>')
print(res.group())
print(res.group(1))
print(res.group(2))
print(res.group(3))
print(res.groups())
结果：
<a>hello</a>
a
hello
a
('a', 'hello', 'a')

<2>
import re
res = re.search(r'<(?P<name>\w+)>\w+</(?P=name)>', r'<a>hello</a>')
print(res.group('name'))
print(res.group())

res = re.search(r'<(?P<name>\w+)>\w+</(?P=name)>', r'<a>hello</h1><a>hello</a>')
print(res.group('name'))

结果：
a
<a>hello</a>
a

<3>
import re

res = re.search(r'<(?P<tt>\w+)>(?P<cc>\w+)</\w+>', r'<a>hello</h1><a>hello</a>')
print(res.group('tt'))
print(res.group('cc'))
print(res.group())

结果：
a
hello
<a>hello</h1>

3）通过索引使用分组
#\1表示使用第一组，匹配到的内容必须和第一组中的内容完全一致。
import re
#\1表示使用第一组，匹配到的内容必须和第一组中的内容完全一致。
res = re.search(r'<(\w+)>\w+</\1>', r'<a>hello</a>')
print(res.group(1))
print(res.group())
结果：
a
<a>hello</a>

4）分组与 split()
切割后的结果会保留分组内被切割的内容
import re
ret = re.split('(\d+)','Tom18Jake20Json22')
print(ret)

结果：
['Tom', '18', 'Jake', '20', 'Json', '22', '']


总结：
# 在python中使用正则表达式
    # 转义符 : 在正则中的转义符 \ 在python中的转义符
    # re模块
        # findall search match
        # sub subn split
        # compile finditer
    # python中的正则表达式
        # findall 会优先显示分组中的内容,要想取消分组优先,(?:正则表达式)
        # split 遇到分组 会保留分组内被切掉的内容
        # search 如果search中有分组的话,通过group(n)就能够拿到group中的匹配的内容
# 正则表达式进阶
    # 分组命名
        # (?P<name>正则表达式) 表示给分组起名字
        # (?P=name)表示使用这个分组,这里匹配到的内容应该和分组中的内容完全相同
    # 通过索引使用分组
        # \1 表示使用第一组,匹配到的内容必须和第一个组中的内容完全相同
