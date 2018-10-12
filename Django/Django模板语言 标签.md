# Django模板语言 标签

## 内置标签引用

### 1. autoescape

控制自动转义是否可用. 这种标签带有任何 `on` 或 `off` 作为参数的话，他将决定转义块内效果。 该标签会以一个`endautoescape`作为结束标签.

当自动转义生效时，所有变量内容会被转义成HTML输出（在所有过滤器生效后） 这等同与手动将[`escape`](https://yiyibooks.cn/__trs__/xx/Django_1.11.6/ref/templates/builtins.html#std:templatefilter-escape)筛选器应用于每个变量。

> 实例:
>
> 1)
>
> ```html
> <!-- index.html文件 -->
> <body>
>     <p>{{ text }}</p>
>     {% autoescape off %}
>         {{ text }}
>     {% endautoescape %}
> </body>
> ```
>
> 如果: text = "\<b>文本内容\</b>"
>
> 页面显示结果:
>
> \<b>文本内容\</b>
>
> **文本内容**
>
> 2)
>
> ```html
> <!-- index.html文件 -->
> <body>
>     <p>{{ text }}</p>
>     {% autoescape off %}
>         {{ text|escape }}
>     {% endautoescape %}
> </body>
> ```
>
> 页面显示结果:
>
> \<b>文本内容\</b>
>
> \<b>文本内容\</b>
>
> *使用了escape过滤器, 则对text文本转义*

#### Django转义默认是开启的, 关闭转义有两种方式

**(1) safe **  一般作用于单行文本

**(2) autoescape off**  一般作用于块级内容  

> 实例:
>
> 1)
>
> ```html
> <body>
>     <p>{{ text }}</p>
>     {% autoescape on %}
>         {{ text }}
>     {% endautoescape %}
> </body>
> ```
>
> 页面显示结果:
>
> \<b>文本内容\</b>
>
> \<b>文本内容\</b>
>
> 2)
>
> ```html
> <body>
>     <p>{{ text|safe }}</p>
>     {% autoescape off %}
>         {{ text }}
>     	{{ text|escape }}
>     {% endautoescape %}
> </body>
> ```
>
> 页面显示结果:
>
> **文本内容**
>
> **文本内容**



### 2. block

一般在父模板可以使用block标签, 把变化的内容可以包裹在block标签内; 子模板引用父模板后, 可以使用block标签重写内容, 覆盖父模板中原来的内容.

> 实例:
>
> ```html
> <!-- 父模板html -->
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <meta name="viewport" content="width=device-width, initial-scale=1.0">
>     <meta http-equiv="X-UA-Compatible" content="ie=edge">
>     <title>年度页面</title>
> </head>
> <body>
>     <div>
>         <p>这是年度新闻</p>
>     </div>
>     {% block content %}
>     <p>页面主体内容</p>
>     {% endblock content %}
> </body>
> </html>
> 
> 
> <!-- 子模板一 html -->
> {% extends 'show_year.html' %}
> 
> 
> <!-- 子模板二 html -->
> {% extends 'show_year.html' %}
> 
> {% block content %}
>  <p>子模板中内容</p>
> {% endblock %}
> ```
>
> 子模板的显示结果:
>
> 子模板一:
>
> 这是年度新闻
>
> 页面主题内容
>
> 子模板二:
>
> 这是年度新闻
>
> 子模板中内容



### 3. comment

在 `{% comment %}` 和 `{% endcomment %}`，之间的内容会被忽略，作为注释。相当于多行注释

> 示例:
>
> ```html
> {% comment %}
>     <b>粗体</b>
>     <div>
>         <p>这是Index页面</p>
>     </div>
> {% endcomment %}
> ```
>
> 这部分注释的内容, 在服务器端就直接忽略到了, 不会发送给客户端.



### 4. csrf_token

这个标签用于跨站请求伪造保护.

客户端在提交表单到服务端时, 如果表单中不写这个标签, 服务端会直接返回`403 Forbidden`的错误. 把这个标签写到表单中, 可以避免发生这个错误.

当把csrf_token写到表单中后, 其实客户端在提交数据时, 会提交一个`name=csrfmiddlewaretoken`, `value`为随机的64位字符给服务端, 服务端收到后, 会根据这串字符校验客户端的合法性.(如果想看这个csrfmiddlewaretoken的具体内容,可以打开浏览器的调试控制台; 你会看到一个属性type='hidden'的input标签, `value`已经有默认值).

> 表单
>
> ```html
> <form action="" method="POST">
>     {% csrf_token %}
>     <input type="text" name="name" placeholder="姓名">
>     <button type="submit">提交</button>
> </form>
> ```



### 5. cycle

每当这个标签被访问,则传出一个它的可迭代参数的元素。 第一次访问返回第一个元素,第二次访问返回第二个参数,以此类推. 一旦所有的变量都被访问过了，就会回到最开始的地方，重复下去

> 实例:
>
> 1) 这个标签在循环中特别有用:
>
> ```html
> {% for o in some_list %}
>     <tr class="{% cycle 'row1' 'row2' %}">
>         ...
>     </tr>
> {% endfor %}
> ```
>
> 第一次迭代产生的HTML引用了 `row1`类，第二次则是`row2`类，第三次 又是`row1` 类，如此类推。
>
> 2) 你也可以使用变量， 例如，如果你有两个模版变量, `rowvalue1`和`rowvalue2`, 你可以让他们的值像这样替换:
>
> ```html
> {% for o in some_list %}
>     <tr class="{% cycle rowvalue1 rowvalue2 %}">
>         ...
>     </tr>
> {% endfor %}
> ```
>
> 被包含在cycle中的变量将会被转义。 你可以禁止自动转义:
>
> ```html
> {% for o in some_list %}
>     <tr class="{% autoescape off %}{% cycle rowvalue1 rowvalue2 %}{% endautoescape %}">
>         ...
>     </tr>
> {% endfor %}
> ```
>
> 你能混合使用变量和字符串：
>
> ```html
> {% for o in some_list %}
>     <tr class="{% cycle 'row1' rowvalue2 'row3' %}">
>         ...
>     </tr>
> {% endfor %}
> ```



### 6. debug

输出整个调试信息，包括当前上下文和导入的模块。



### 7. extends

表示当前模板继承自一个父模板  

这个标签可以有两种用法:  

+ `{% extends "base.html" %}` (要有引号).继承名为`"base.html"`的父模板
+ `{％ extends 变量 ％}`使用`variable` 如果变量被计算成一个字符串，Django将会把它看成是父模版的名字。 如果变量被计算到一个`Template`对象，Django将会使用那个对象作为一个父模版。

通常模板名称是相对于模板加载器的根目录。 字符串参数也可以是以`./`或`../`开头的相对路径。 例如，假设以下目录结构：

```
dir1/
    template.html
    base2.html
    my/
        base3.html
base1.html
```

在`template.html`中，以下路径将有效：

```
{% extends "./base2.html" %}
{% extends "../base1.html" %}
{% extends "./my/base3.html" %}
```



### 8. filter

通过一个或多个过滤器对内容过滤。 作为灵活可变的语法，多个过滤器被管道符号相连接，且过滤器可以有参数。

注意块中*所有的*内容都应该包括在`endfilter` 和`filter` 标签中。

**注: **`escape`和`safe`过滤器不是可接受的参数。 而应使用`autoescape`标记来管理模板代码块的自动转义。

> 实例:
>
> ```html
> {% filter force_escape|lower %}
>     This text will be HTML-escaped, and will appear in all lowercase.
> {% endfilter %}
> 
> {% autoescape off %}
> {% filter force_escape|lower %}
>     This text will be HTML-escaped, and will appear in all lowercase.
> {% endfilter %}
> {% endautoescape %}
> ```



### 9. firstof

输出第一个不为`False`参数。 如果传入的所有变量都为`False`，就什么也不输出。

例如:

```html
{% firstof var1 var2 var3 %}
```

它等价于:

```html
{% if var1 %}
    {{ var1 }}
{% elif var2 %}
    {{ var2 }}
{% elif var3 %}
    {{ var3 }}
{% endif %}
```

当然你也可以用一个默认字符串作为输出以防传入的所有变量都是False：

```html
{% firstof var1 var2 var3 "default value" %}
```



### 10. for

循环组中的每一个项目，并让这些项目在上下文可用。 举个例子，展示`athlete_list`中的每个成员：

```html
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}
</ul>
```

可以利用`{% for obj in list reversed %}`反向完成循环。

如果你需要循环一个包含列表的列表，可以通过拆分每一个二级列表为一个独立变量来达到目的。 举个例子，如果你的内容包括一个叫做`points`的(x,y) 列表，你可以像以下例子一样输出points列表：

```html
{% for x, y in points %}
    There is a point at {{ x }},{{ y }}
{% endfor %}
```

如果你想访问一个字典中的项目，这个方法同样有用。 举个例子：如果你的内容包含一个叫做`data`的字典，下面的方式可以输出这个字典的键和值：

```html
{% for key, value in data.items %}
    {{ key }}: {{ value }}
{% endfor %}
```

请记住，对于点运算符，字典键查找优先于方法查找。如果要在模板中使用这些方法（`items`，`values`，`keys`等），请避免添加名为字典方法的键。

for循环可用的参数:

| 变量                  | 描述                                 |
| --------------------- | ------------------------------------ |
| `forloop.counter`     | 当前循环的索引值（索引从1开始）      |
| `forloop.counter0`    | 当前循环的索引值（索引从0开始）      |
| `forloop.revcounter`  | 当前循环的倒序索引值（索引从1开始）  |
| `forloop.revcounter0` | 当前循环的倒序索引值（索引从0开始）  |
| `forloop.first`       | 如果这是第一次循环，返回True         |
| `forloop.last`        | 如果这是最后一次循环，则为True       |
| `forloop.parentloop`  | 对于嵌套循环，这是当前循环的外层循环 |



### 11. for...empty

`for` 标签带有一个可选的`{% empty %}` 从句，以便在给出的组是空的或者没有被找到时，可以有所操作。

```html
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>Sorry, no athletes in this list.</li>
{% endfor %}
</ul>
```

它和下面的例子作用相等，但是更简洁、更清晰甚至可能运行起来更快：

```html
<ul>
  {% if athlete_list %}
    {% for athlete in athlete_list %}
      <li>{{ athlete.name }}</li>
    {% endfor %}
  {% else %}
    <li>Sorry, no athletes in this list.</li>
  {% endif %}
</ul>
```



### 12. if

`{% if %}`会对一个变量求值，如果它的值是“True”（存在、不为空、且不是boolean类型的false值），这个内容块会输出：

```html
{% if athlete_list %}
    Number of athletes: {{ athlete_list|length }}
{% elif athlete_in_locker_room_list %}
    Athletes should be out of the locker room soon!
{% else %}
    No athletes.
{% endif %}
```

上述例子中，如果`athlete_list`不为空，就会通过使用`{{ athlete_list|length }}`过滤器展示出athletes的数量。

正如你所见，`if`标签之后可以带有一个或者多个`{% elif %}` 从句，也可以带有一个`{% else %}`从句以便在之前的所有条件不成立的情况下完成执行。 这些从句都是可选的。

`if`标签可以使用`not`，`and`或`or`来测试多个变量的布尔值.



### 13. include

加载模板并以标签内的参数渲染。 这是一种可以引入别的模板的方法。

模板名可以是变量或者是硬编码的字符串，可以用单引号也可以是双引号.

下面这个示例包括模板`"foo/bar.html"`的内容：

```html
{% include "foo/bar.html" %}
```

通常模板名称是相对于模板加载器的根目录。 字符串参数也可以是以`./`或`../`开头的相对路径，如[`extends`](https://yiyibooks.cn/__trs__/xx/Django_1.11.6/ref/templates/builtins.html#std:templatetag-extends)标签中所述。



### 14. load

加载自定义模板标签集。

举个例子, 下面这模板将会从`package`包中载入所有`otherlibrary` 和`somelibrary` 中已经注册的标签和过滤器:

```html
{% load somelibrary package.otherlibrary %}	
```

你还可以使用`from`参数从库中选择性加载单个过滤器或标记。 在下面这个示例中，名为`somelibrary`和`bar`的模板标签/过滤器将从`foo`加载：

```html
{% load foo bar from somelibrary %}
```



### 15. now

显示最近的日期或事件,可以通过给定的字符串格式显示。

> 实例:
>
> ```html
> {% now 'Y-m-d H:i:s' %}
> ```
>
> 输出类似:
>
> 2018-10-11 07:05:40

您也可以使用语法`{％ now “Y” as current_year ％}`将输出（作为字符串）存储在变量中。 This is useful if you want to use `{% now %}` inside a template tag like `blocktrans` for example:

```html
{% now "Y" as current_year %}
{% blocktrans %}Copyright {{ current_year }}{% endblocktrans %}
<!-- 使用blocktrans标签需要在html文件头部加上 {% load i18n %}, 导入已有的i18n模板-->
```



### 16. regroup

用相似对象间共有的属性重组列表.

This complex tag is best illustrated by way of an example: say that `cities` is a list of cities represented by dictionaries containing `"name"`,`"population"`, and `"country"` keys:

```python
cities = [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
]
```

...并且您想显示按国家/地区排序的分层列表，如下所示：

- 印度
  - 孟买：19,000,000
  - 加尔各答：15,000,000
- 美国
  - 纽约：20,000,000
  - 芝加哥：7,000,000
- 日本
  - 东京：33,000,000

你可以使用`{% regroup %}`标签来给每个国家的城市分组。 以下模板代码片段将实现这一点：

```html
{% regroup cities by country as country_list %}

<ul>
{% for country in country_list %}
    <li>{{ country.grouper }}
    <ul>
        {% for city in country.list %}
          <li>{{ city.name }}: {{ city.population }}</li>
        {% endfor %}
    </ul>
    </li>
{% endfor %}
</ul>
```

让我们来看看这个例子。 `{% regroup %}`有三个参数： 你想要重组的列表, 被分组的属性, 还有结果列表的名字. 在这里，我们通过`country_list`属性重新分组`country`列表，并调用结果`cities`。

`{％ regroup ％}`产生一个清单（在本例中为`country_list`的**组对象**。 组对象是具有两个字段的[`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple)的实例：

- `grouper` - 按分组的项目（例如，字符串“India”或“Japan”）。
- `list` - 此群组中所有项目的列表（例如，所有城市的列表，其中country ='India'）。

**在Django更改1.11：**

组对象已从字典更改为[`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple)。

Because `{% regroup %}` produces [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple) objects, you can also write the previous example as:

```html
{% regroup cities by country as country_list %}

<ul>
{% for country, local_cities in country_list %}
    <li>{{ country }}
    <ul>
        {% for city in local_cities %}
          <li>{{ city.name }}: {{ city.population }}</li>
        {% endfor %}
    </ul>
    </li>
{% endfor %}
</ul>
```

请注意，`{％ regroup ％}`不会对其输入进行排序！ 我们的例子依赖于事实：`cities`列表首先由`country`排序。 如果`country`列表*不*通过`cities`对其成员进行排序，则重新分组将天真显示单个国家/地区的多个组。 例如，假设`cities`列表已设置为此（请注意，国家/地区未分组在一起）：

```python
cities = [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
]
```

对于`cities`的输入，示例`{％ regroup ％}`以上将导致以下输出：

- 印度
  - 孟买：19,000,000
- 美国
  - 纽约：20,000,000
- 印度
  - 加尔各答：15,000,000
- 美国
  - 芝加哥：7,000,000
- 日本
  - 东京：33,000,000

另一个解决方案是使用[`dictsort`](https://yiyibooks.cn/__trs__/xx/Django_1.11.6/ref/templates/builtins.html#std:templatefilter-dictsort)过滤器对模板中的数据进行排序，如果您的数据在字典列表中：

```html
{% regroup cities|dictsort:"country" by country as country_list %}
```



### 17. resetcycle

重置先前的[循环](https://yiyibooks.cn/__trs__/xx/Django_1.11.6/ref/templates/builtins.html#cycle)，以便在下一次遇到时从其第一个项目重新启动。 没有参数， `{% resetcycle %}` 会重置模板中定义的最后一个`{% cycle %}`

用法示例：

```html
{% for coach in coach_list %}
    <h1>{{ coach.name }}</h1>
    {% for athlete in coach.athlete_set.all %}
        <p class="{% cycle 'odd' 'even' %}">{{ athlete.name }}</p>
    {% endfor %}
    {% resetcycle %}
{% endfor %}
```

这个示例将返回下面的HTML：

```html
<h1>José Mourinho</h1>
<p class="odd">Thibaut Courtois</p>
<p class="even">John Terry</p>
<p class="odd">Eden Hazard</p>

<h1>Carlo Ancelotti</h1>
<p class="odd">Manuel Neuer</p>
<p class="even">Thomas Müller</p>
```

注意第一个块以`class="odd"`结束，新的以`class="odd"`开头。 没有`{％ resetcycle ％}`标签，第二个块将以`class="even"`



### 18. spaceless

删除HTML标签之间的空白格. 包括制表符和换行.

用法示例:

```html
{% spaceless %}
    <p>
        <a href="foo/">Foo</a>
    </p>
{% endspaceless %}
```

这个示例将返回下面的HTML：

```html
<p><a href="foo/">Foo</a></p>
```

注: 仅删除 *tags* 之间的空格 – 而不是标签和文本之间的。  



### 19. url

返回与给定视图和可选参数匹配的绝对路径引用（不带域名的URL）。 在解析后返回的结果路径字符串中，每个特殊字符将使用[`iri_to_uri()`](https://yiyibooks.cn/__trs__/xx/Django_1.11.6/ref/utils.html#django.utils.encoding.iri_to_uri)编码。

这是一种不违反DRY原则的输出链接的方式，它可以避免在模板中硬编码链接路径。

```html
{% url 'some-url-name' v1 v2 %}
```

第一个参数是[`url()`](https://yiyibooks.cn/__trs__/xx/Django_1.11.6/ref/urls.html#django.conf.urls.url) `name`。 它可以是一个被引号引起来的字符串或者其他的上下文变量. 其他参数是可选的并且应该以空格隔开，这些值会在URL中以参数的形式传递. 上面的例子展示了如何传递位置参数. 当然你也可以使用关键字参数.

```html
{% url 'some-url-name' arg1=v1 arg2=v2 %}
```

不要把位置参数和关键字参数混在一起使用。 URLconf所需的所有参数都应该存在。

例如，假设您有一个视图`app_views.py`，其URLconf接受客户端ID（此处`client()`是视图文件`app_views.client`）。 URLconf行可能如下所示：

```html
('^client/([0-9]+)/$', app_views.client, name='app-views-client')
```

如果你的应用中的URLconf 已经被包含到项目 URLconf 中，比如下面这样

```html
('^clients/', include('project_name.app_name.urls'))
```

然后，在模板中，您可以创建一个此视图的链接，如下所示：

```html
{% url 'app-views-client' client.id %}
```

模板标签会输出如下的字符串 `/clients/client/123/`.

如果您要检索名称空间网址，请指定完全限定名称：

```html
{% url 'myapp:view-name' %}
```



### 20. widthratio

为了创建条形图等，此标签计算给定值与最大值的比率，然后将该比率应用于常量。

像这样：

```html
<img src="bar.png" alt="Bar"
     height="10" width="{% widthratio this_value max_value max_width %}" />
```

如果`max_width`是175，`max_value`是200，并且`this_value`是100，则上述示例中的图像将是88像素宽（因为175 / 200 = .875； .875 * 100 = 87.5，上舍入为88）。

在某些情况下，您可能想要捕获变量中的`widthratio`的结果。 它可以是有用的，例如，在`blocktrans`像这样：

```html
{% widthratio this_value max_value max_width as width %}
{% blocktrans %}The width is: {{ width }}{% endblocktrans %}
```



### 21. with

使用一个简单地名字缓存一个复杂的变量 ，当你需要使用一个“昂贵的”方法（比如访问数据库）很多次的时候是非常有用的

像这样:

```html
{% with total=business.employees.count %}
    {{ total }} employee{{ total|pluralize }}
{% endwith %}
```

填充变量（以上示例`total`）仅适用于`{％ 与 ％} t5>`和`{％ endwith ％}`标签。

你可以分配多个上下文变量：

```html
{% with alpha=1 beta=2 %}
    ...
{% endwith %}
```



参考文档: https://yiyibooks.cn/xx/Django_1.11.6/ref/templates/builtins.html#ref-templates-builtins-tags