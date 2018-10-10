## Django模板语言，过滤器整理

#### 1. add

**{{ value|add:"2" }}**

把add后的参数加给value；

处理时，过滤器首先会强制把两个值转换成Int类型。 如果强制转换失败, 它会试图使用各种方式吧两个值相加。

> 实例：
>
> {{  arg|add:val }}
>
> 1）arg是5，val是3，将会输出8
>
> 2）arg是5，val是'3'，将会输出8
>
> 3）arg是'jason'，val是'2'，将会输出jason2
>
> 4）arg是'jason'，val是2，将会输出空
>
> 5）arg是[1, 2, 3]，val是[4]，将会输出[1, 2, 3, 4]



#### 2. addslashes

{{ value|addslashes }}

在引号前面加上斜杆

像这样：

如果`value` 是 `"I'm using Django"`, 输出将变成 `"I\'m using Django"`



#### 3. capfirst

{{ value|capfirst}}

将变量的第一个字母变成大写，如果第一个字符不是字母，则过滤器不生效

如果 `"value"` 是 `"django"`, 输出将变成 `Django`。



#### 4. center

{{ value|center:16}}

使"value"在给定的宽度范围内居中。



#### 5. cut

移除value中所有的与给出的变量相同的字符串

{{ value|cut:" "}}

如果`value`为`“String with spaces”`，输出将为`"Stringwithspaces"`。



#### 6. date

根据给定格式对一个date变量格式化

可用的格式字符串：

| 格式化字符 | 描述                                                         | 示例输出                                                     |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| a          | `'a.m.'`或`'p.m.'`（请注意，这与PHP的输出略有不同，因为这包括符合Associated Press风格的期间） | `'a.m.'`                                                     |
| A          | `'AM'`或`'PM'`。                                             | `'AM'`                                                       |
| b          | 月，文字，3个字母，小写。                                    | `'jan'`                                                      |
| B          | 未实现。                                                     |                                                              |
| c          | ISO 8601格式。 （注意：与其他格式化程序不同，例如“Z”，“O”或“r”，如果值为naive datetime，则“c”格式化程序不会添加时区偏移量（请参阅[`datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo)） 。 | `2008-01-02T10:30:00.000123+02:00`或`2008-01-02T10:30:00.000123`如果datetime是天真的 |
| d          | 月的日子，带前导零的2位数字。                                | `'01'`到`'31'`                                               |
| D          | 一周中的文字，3个字母。                                      | `“星期五”`                                                   |
| e          | 时区名称 可能是任何格式，或者可能返回一个空字符串，具体取决于datetime。 | `''`、`'GMT'`、`'-500'`、`'US/Eastern'`等                    |
| E          | 月份，特定地区的替代表示通常用于长日期表示。                 | `'listopada'`（对于波兰语区域，而不是`'Listopad'`）          |
| f          | 时间，在12小时的小时和分钟内，如果它们为零，则分钟停留。 专有扩展。 | `'1'`，`'1:30'`                                              |
| F          | 月，文，长。                                                 | `'一月'`                                                     |
| g          | 小时，12小时格式，无前导零。                                 | `'1'`到`'12'`                                                |
| G          | 小时，24小时格式，无前导零。                                 | `'0'`到`'23'`                                                |
| h          | 小时，12小时格式。                                           | `'01'`到`'12'`                                               |
| H          | 小时，24小时格式。                                           | `'00'`到`'23'`                                               |
| i          | 分钟。                                                       | `'00'`到`'59'`                                               |
| I          | 夏令时间，无论是否生效。                                     | `'1'`或`'0'`                                                 |
| j          | 没有前导零的月份的日子。                                     | `'1'`到`'31'`                                                |
| l          | 星期几，文字长。                                             | `'星期五'`                                                   |
| L          | 布尔值是否是一个闰年。                                       | `True`或`False`                                              |
| m          | 月，2位数字带前导零。                                        | `'01'`到`'12'`                                               |
| M          | 月，文字，3个字母。                                          | `“扬”`                                                       |
| n          | 月无前导零。                                                 | `'1'`到`'12'`                                                |
| N          | 美联社风格的月份缩写。 专有扩展。                            | `'Jan.'`，`'Feb.'`，`'March'`，`'May'`                       |
| o          | ISO-8601周编号，对应于使用闰年的ISO-8601周数（W）。 对于更常见的年份格式，请参见Y。 | `'1999年'`                                                   |
| O          | 与格林威治时间的差异在几小时内。                             | `'+0200'`                                                    |
| P          | 时间为12小时，分钟和'a.m。'/'p.m。'，如果为零，分钟停留，特殊情况下的字符串“午夜”和“中午”。 专有扩展。 | `'1 am'`，`'1:30 pm' / t3>，'midnight'，'noon'，'12：30 pm' / T10>` |
| r          | [**RFC 5322**](https://tools.ietf.org/html/rfc5322.html)格式化日期。 | `'Thu, 21 Dec 2000 16:01:07 +0200'`                          |
| s          | 秒，带前导零的2位数字。                                      | `'00'`到`'59'`                                               |
| S          | 一个月的英文序数后缀，2个字符。                              | `'st'`，`'nd'`，`'rd'`或`'th'`                               |
| t          | 给定月份的天数。                                             | `28` to `31`                                                 |
| T          | 本机的时区。                                                 | `'EST'`，`'MDT'`                                             |
| u          | 微秒。                                                       | `000000` to `999999`                                         |
| U          | 自Unix Epoch以来的二分之一（1970年1月1日00:00:00 UTC）。     |                                                              |
| w          | 星期几，数字无前导零。                                       | `'0'`（星期日）至`'6'`（星期六）                             |
| W          | ISO-8601周数，周数从星期一开始。                             | `1`，`53`                                                    |
| y          | 年份，2位数字。                                              | `'99'`                                                       |
| Y          | 年，4位数。                                                  | `'1999年'`                                                   |
| z          | 一年中的日子                                                 | `0`到`365`                                                   |
| Z          | 时区偏移量，单位为秒。 UTC以西时区的偏移量总是为负数，对于UTC以东时，它们总是为正。 | `-43200`到`43200`                                            |

> 实例：
>
> now = datetime.datetime.now()
>
> 1）{{ now|date:'Y-m-d H:i:s'}}
>
> 输出类似：2018-10-09 11:15:22
>
> 2）{{ now|date }}
>
> 输出类似：Oct. 9, 2018
>
> 传递的格式可以是预定义的格式[`DATE_FORMAT`](https://yiyibooks.cn/__trs__/xx/Django_1.11.6/ref/settings.html#std:setting-DATE_FORMAT)，[`DATETIME_FORMAT`](https://yiyibooks.cn/__trs__/xx/Django_1.11.6/ref/settings.html#std:setting-DATETIME_FORMAT)，[`SHORT_DATE_FORMAT`](https://yiyibooks.cn/__trs__/xx/Django_1.11.6/ref/settings.html#std:setting-SHORT_DATE_FORMAT)或[`SHORT_DATETIME_FORMAT`](https://yiyibooks.cn/__trs__/xx/Django_1.11.6/ref/settings.html#std:setting-SHORT_DATETIME_FORMAT)
>
> 3）{{ now|date:"DATETIME_FORMAT" }}
>
> 输出类似：Oct. 9, 2018, 11:19 a.m.



#### 7. default

如果value的计算结果为`False`，则使用给定的默认值。 否则，使用该value。

{{ value|default:"nothing" }}



#### 8. default_if_none

{{ value|default_if_none:"nothing"}}

当且仅当value为`None`，则使用给定的默认值。 否则，使用该value。

注意，如果给出一个空字符串，默认值将*不*被使用。



#### 9. dictsort

{{ value|dictsort:"name" }}

接受一个字典列表，并返回按参数中给出的键排序后的列表。

> 实例：
>
> Value = [
> ​	{'name': 'zed', 'age': 19},
> ​	{'name': 'amy', 'age': 22},
> ​	{'name': 'joe', 'age': 31},
> ]
>
> {{ Value|dictsort:'name' }}
> {{ Value|dictsort:'age' }}
>
> 输出：
>
> [{'name': 'amy', 'age': 22}, {'name': 'joe', 'age': 31}, {'name': 'zed', 'age': 19}]
>
> [{'name': 'zed', 'age': 19}, {'name': 'amy', 'age': 22}, {'name': 'joe', 'age': 31}]



#### 10. dictsortreversed

获取字典列表，并返回按照参数中给出的键按相反顺序排序的列表。 这与上面的过滤器完全相同，但返回的值将是相反的顺序。



#### 11. divisibleby

{{ value|divisibleby:“2” }}

如果value可以被给出的参数整除，则返回 `True`

> 实例：
>
> value = 12
>
> {{ value|divisibleby:“2” }}
>
> 输出：True



#### 12. filesizeformat

格式化为“可读”文件大小（即`'13 KB'`，`t4> MB'`，`'102 bytes'`等）。

{{ value|filesizeformat }}

> 实例：
>
> value = 1234567890
>
> {{ value|filesizeformat }}
>
> 输出：1.1 GB



#### 13. first

{{ value|first }}

返回序列中的第一项（字符串、列表、元组等）

如果`value`是列表`['a'， 'b'， 'c'] `，输出将为`'a'`。



#### 14. floatformat

当不使用参数时，将浮点数舍入到小数点后一位；使用参数时，保留参数指定的位数

> 实例:
>
> pi = 3.1415926
>
> {{ pi|floatformat }}
>
> {{ pi|floatformat:0 }}
>
> {{ pi|floatformat:2 }}
>
> 输出:
>
> 3.1
> 3
> 3.14



#### 15. get_digit

给定一个整数，返回所请求的数字，其中1是最右边的数字，2是第二个最右边的数字等。 返回无效输入的原始值（如果输入或参数不是整数，或参数小于1）。否则，输出总是一个整数。

> 实例:
>
> {{ value|get_digit:"2" }}
>
> 如果`value`为`123456789`，则输出将为`8`。



#### 16. join

使用字符串连接列表，例如Python的`str.join(list)`

{{ value|join:" // " }}

如果`value`是列表`['a'， 'b'， 'c']，输出将为“a // b // C“。`



#### 17. last

返回列表中的最后一个项目

{{  value|last }}

如果`value`是列表`['a'， 'b'， 'c']，输出将为'c'`



#### 18. length

返回值的长度

{{ value|length }}

如果`value`是`['a'， 'b'， 'c'， 'd']`或`"abcd"`，输出将为`4`。

对于未定义的变量，过滤器返回`0`。



#### 19. length_is

如果值的长度是参数，则返回`True`，否则返回`False`。

{{ value|length_is:"4" }}

如果value是['a'， 'b'， 'c'， 'd']或"abcd"，输出将为True。



#### 20. linebreaks

替换纯文本中的换行为正确的HTML标签；单独的一个换行变成(`<br/>`) ，原文本用p标签包裹起来。

如果`value`为`Joel\nis a slug`，输出将为`<p>Joel<br/>is a slug</p>`。



#### 21. linebreaksbr

与linebreaks类似, 区别是, linebreaksbr只替换换行, 替换完成后没有p标签包裹.

如果`value`为`Joel\nis a slug`，输出将为`Joel<br/>is a slug`。



#### 22. linenumbers

输出多行文本时, 在行前显示行号.

{{ value|linenumbers }}

如果`value`为：

> one
> two
> three

输出将是：

>1. one
>2. two
>3. three


#### 23. ljust

将给定宽度的字段中的值左对齐。

"{{ value|ljust:"10" }}"

如果`value`为`Django`，则输出将为`“Django ”`。



#### 24. lower

将字符串转换为全部小写。

如果`value`是`ABC`, 则输出将为`abc`



#### 25. make_list

返回转换为列表的值。

{{ value|make_list }}

如果`value`是字符串`"Joel"`，输出将是列表`['J'， 'o' ， 'e'， 'l']`。 如果`value`为`123`，输出将为列表`['1', '2', '3']`。



#### 26. pluralize

如果值不是1则返回一个复数形式 , 通常用 `'s'`表示.

例如:

> You have {{ num_messages }} message{{ num_messages|pluralize }}.

如果`num_messages`是`1`，则输出将为 `You have 1 message.` 如果`num_messages`是`2`，输出将为 `You have 2 messages.`

另外如果你需要的不是 `'s'`后缀的话, 你可以提供一个备选的参数给过滤器;

例如：

> You have {{ num_walruses }} walrus{{ num_walruses|pluralize:"es" }}.

对于非一般形式的复数,你可以同时指定 单复数形式，用逗号隔开.

例如：

> You have {{ num_cherries }} cherr{{ num_cherries|pluralize:"y,ies" }}.



#### 27. pprint

用于调试, 方便查看.



#### 28. random

返回给定列表中的随机项。

{{ value|random }}

如果value是['a', 'b', 'c', 'd'], 输出可能是'c'.



#### 29. rjust

右对齐给定宽度字段中的值。



#### 30. safe

将字符串标记为在输出之前不需要进一步的HTML转义。 当自动转义关闭时，此过滤器不起作用。



#### 31. safeseq

将[`safe`](https://yiyibooks.cn/__trs__/xx/Django_1.11.6/ref/templates/builtins.html#std:templatefilter-safe)过滤器应用于序列的每个元素。 与对序列进行操作的其他过滤器（例如[`join`](https://yiyibooks.cn/__trs__/xx/Django_1.11.6/ref/templates/builtins.html#std:templatefilter-join)）一起使用非常有用。

{{ some_list|safeseq|join:", " }}



#### 32. slice

返回列表的一部分。

{{ some_list|slice:":2" }}

如果`some_list`为`['a', 'b', 'c']`，那么输出将是`['a', 'b']`。



#### 33. striptags

尽一切可能努力剥离所有[X] HTML标签。

{{ value|striptags }}

如果value为"\<b>cu ti\</b>", 输出结果为cuti(不带样式).



#### 34. time

根据给定的格式格式化时间。

> 实例:
>
> now = datetime.datetime.now()
>
> {{ now|time:'H:i:s' }}
>
> 输出类似:
>
> 13:25:53



### 35. timesince

将日期格式设为自该日期起的时间（例如，“4天，6小时”）。

> 实例:
>
> now = datetime.datetime.now()
>
> blog_date = now - datetime.timedelta(days=2)
>
> {{ blog_date|timesince:now }}
>
> {{ now|timesince:blog_date }}
>
> 输出类似:
>
> 2 days
> 0 minutes



#### 36. timeuntil

与timesince类似

> 实例:
>
> now = datetime.datetime.now()
>
> blog_date = now - datetime.timedelta(days=2)
>
> {{ blog_date|timeuntil:now }}
>
> {{ now|timeuntil:blog_date }}
>
> 输出类似:
>
> 0 minutes
> 2 days



#### 37. title

将字符串中的每个单词首字母转为大写

{{ value|title }}

如果`value`为`“my FIRST post”`，输出将为`“My First Post”`。



#### 38. truncatechars

如果字符串字符多于指定的字符数量，那么会被截断。 截断的字符串将以可翻译的省略号序列（“...”）结尾。

{{ value|truncatechars:9 }}

如果`value`为`“myFIRSTpost”`，输出将为`“MyFirst...”`。



#### 39.truncatewords

在一定数量的字后截断字符串。

{{ value|truncatewords:2 }}

如果`value`为`“my name is post”`，输出将为`“My name ...”`。



#### 40. upper

将字符串转换为大写形式

{{ value|upper }}

如果`value`是`abc`, 则输出将为`ABC`



#### 41. urlencode

转义要在URL中使用的值。

{{ value|urlencode }}

如果`value`为`"https://www.example.org/foo?a=b&c=d"`，输出将为`"https%3A//www.example.org/foo%3Fa%3Db%26c%3Dd"`

可以提供包含不应该转义的字符的可选参数。

如果未提供，则'/'字符被假定为安全的。 当*所有*字符应该转义时，可以提供空字符串。 像这样：

{{ value|urlencode:"" }}

如果`value`为`"https://www.example.org/"`，输出将为`"https%3A%2F%2Fwww.example.org%2F"`



#### 42. wordcount

返回字数(单词数)

{{ value|wordcount }}

如果`value`是`“Joel is a slug”，输出将为4`



#### 43. wordwrap

以指定的行长度换行单词。

