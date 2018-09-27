Django之模板语法

目录：
    一、什么是模板
    二、模板语法分类
        - 模板语法之变量：语法{{}}
        - 模板语法之标签：语法为{% tag %}
        - 模板语法之过滤器：语法{{obj|filter__name:param}}
        - 自定义标签和过滤器

一、什么是模板
    - 只要是在html里面的模板语法就不是html文件了，这样的文件叫做模板。

二、模板的语法分类
    - 模板语法之变量：语法为{{}}
        - 在Django模板中遍历复杂数据结构的关键是句点字符 . （也就是点）

        - views.py
            def index(request):
                name = "hello haiyan"
                    i = 200
                    l = [11,22,33,44,55]
                    d = {"name":"haiyan","age":20}
                    
                    class People(object): #继承元类
                        def __init__(self,name,age):
                            self.name = name
                            self.age = age
                        def __str__(self):
                            return self.name+str(self.age)
                        def dream(self):
                            return "你有梦想吗？"
                    #实例化
                    person_jack = People("jack",10)
                    person_tom = People("tom",34)
                    person_ward = People("ward",34)
                    person_list = [person_ward,person_jack,person_tom]
                    
                    return render(request,"index.html",
                                  {
                                  "name":name,
                                  "i":i,
                                  "l":l,
                                  "d":d,  #键对应的是模板里的名字。值对应的是上面定义的变量
                                  "person_jack":person_jack,
                                  "person_tom":person_tom,
                                  "person_list":person_list,
                                  }
                                  )
                # return render(request,"index.html",locals())
                #用locals()可以不用写上面的render了。不过用locals()，views里面用什么名。模板里面就得用什么名
                # locals()局部的：用了locals就相当于都得按照上面的那样

            - templates.index.hrtml
                
                <h4>变量{{ z }}:深度查询</h4><hr>
                <h3>{{ name }}</h3>
                <p>{{ i }}</p>
                <p>{{ l }}</p>
                <p>{{ d }}</p>
                <p>{{ l.0 }}------》取单个值可通过句点符（也就是点）</p>
                <p>{{ l.4 }}</p>
                <p>{{ d.name }}</p>
                <p>{{ d.age }}-----》字典也可以根据句点符取值，一个点就搞定了。
                然而在前端页面中是看不到你的模板语法的，当你点击审查元素的
                时候，你就会发现，偷偷的换过来了</p>
                <p>{{ person_tom.name }}</p>
                <p>{{ person_jack.age }}</p>
                <p>{{ person_tom.dream }}</p>  <!-- .方法的时候，注意当前的dream方法是没有参数的-->
                <p>{{ person_list.2 }}</p>  <!--单个取值-->
                <p>{{ person_list.1.name }}</p>
                <!-- 那怎么让对象变成字符串呢？在index视图函数里里面再加上一个__str__内置方法-->
                <!--__str__是对象字符串的改变-->

        注意：句点也可以用来引用对象的方法（无参数方法）
                <h4> 字典：{{ dic.name.upper }}</h4>

    - 模板语法之标签：语法为{% tag %}
        - 标签看起来像是这样的：{% tag %}.
        - 标签比变量更加复杂：一些在输出中创建文本，一些通过循环或逻辑来控制流程，
            一些加载其后的变量将使用到的额外信息加到模板中
            一些标签需要开始和结束标签（例如{% tag %}...标签 内容...{% endtag %}）
        1)for标签（注：循环序号可以通过{{forloop}}显示）
            
            <h3>循环取值1</h3><hr>
            {% for item in person_list %}
                <p>{{ item.name }},{{ item.age }}</p>
            {% endfor %}

            <h3>循环取值2:倒序</h3><hr>
            {% for item in person_list reversed %}
                <!--序号从1开始-->
                <p>{{ forloop.counter }}->{{ item.name }},{{ item.age }}</p>
                <!--序号从0开始-->
                <p>{{ forloop.counter0 }}->{{ item.name }},{{ item.age }}</p>
                <!-- 序号倒序 -->
                <p>{{ forloop.revcounter }}->{{ item.name }},{{ item.age }}</p>
            {% endfor %}

            <h3>循环取值3：字典</h3><hr>
            {% for k,v in d.items %}
                <p>{{ k }},{{ v}}</p>
            {% endfor %}

        2）for...empty:for标签带有一个可选的{% empty %}从句，以便在給出的是空的或者没有被找到时，可以有所操作。
            
            % for person in person_list %}
                <p>{{ person.name }}</p>

            {% empty %}
                <p>sorry,no person here</p>
            {% endfor %}

        3）if标签：{% if %}会对一个变量求值，如果它的值是“True”（存在、不为空、且不是boolean类型的false值），对应的内容块会输出。

            {% if i > 300 %}
                <p>大于{{ i }}</p>
            {% elif i == 200  %}
                <p>等于{{ i }}</p>
            {% else %}
                <p>小于{{ i }}</p>
            {% endif %}

        4）with:使用一个简单地名字缓存一个复杂的变量，当你使用需要使用一个“昂贵的”方法（比如访问数据库）很多次的时候是非常有用的
            
            {% with total=business.employees.count %}
                {{ total }} employee{{ total|pluralize }}
            {% endwith %}
            <p>{{ person_list.2.name }}</p>
            {% with name=person_list.2.name %}
                <p>{{ name }}</p>
            {% endwith %}

        5）csrf_token:这个标签用于跨站请求伪造保护
            - 提交数据的时候就会做安全机制，当你点击提交的时候就会出现一个forbbiddon的错误，
                就是用settings配置里的scrd做安全机制的，可以注释或者在form表单下面添加
                一个{% 5）csrf_token %}，这才是真正的解决办法，注释不是解决办法

                <h3>scrf_token</h3>
                <form action="/tag/" method="post">
                    {% csrf_token %}
                    <p><input type="text" name="haiyan"></p>
                    <input type="submit">
                </form>
    - 模板语法之过滤器：语法{{obj|filter__name:param}}
        
        - 简单介绍一些常用的模板过滤器
        1、default：如果一个变量是false或者为空，使用给定的默认值。否则，使用变量的值。例如：

        <p>default过滤器：{{ li|default:"如果显示为空，设置的解释性的内容" }}</p>
        2、length：返回值的长度。它对字符串和列表都起作用。例如：

        {{ value|length }}
        如果 value 是 ['a', 'b', 'c', 'd']，那么输出是 4。

        3、filesizeformat：将值格式化为一个 “人类可读的” 文件尺寸 （例如 '13 KB', '4.1 MB', '102 bytes', 等等）。例如：

        {{ value|filesizeformat }}
        如果 value 是 123456789，输出将会是 117.7 MB。

        4、date：如果 value=datetime.datetime.now()

        {{ value|date:"Y-m-d" }}
        5、slice  ：切片

        如果 value="hello world"

        {{ value|slice:"2:-1" }}
        6、truncatechars  截断

        如果字符串字符多于指定的字符数量，那么会被截断。截断的字符串将以可翻译的省略号序列（“...”）结尾。

        参数：要截断的字符数

        例如：

        <p>截断字符：{{ content|truncatechars:20 }}</p>
        <p>截断单词：{{ content|truncatewords:4 }}</p>
        如果content是“I am is haiyan,how are you asd df dfgfdgdg?

        输出结果： 截断字符：I am is haiyan,ho...

        输出结果 ：截断单词：I am is haiyan,how ...

        7、safe

        Django的模板中会对HTML标签和JS等语法标签进行自动转义，原因显而易见，这样是为了安全。但是有的时候我们可能不希望这些HTML元素被转义，比如我们做一个内容管理系统，后台添加的文章中是经过修饰的，这些修饰可能是通过一个类似于FCKeditor编辑加注了HTML修饰符的文本，如果自动转义的话显示的就是保护HTML标签的源文件。为了在Django中关闭HTML的自动转义有两种方式，如果是一个单独的变量我们可以通过过滤器“|safe”的方式告诉Django这段代码是安全的不必转义。比如：

        value="<a href="">点击</a>"

        {{ value|safe}}
        <p>{{ label }}</p>  <!--为了安全系统会把标签变成字符串-->
        <p>{{ label|safe }}</p>    <!--加上safe，确定你的数据是安全的才能被当成是标签-->

    - 自定义标签和过滤器

        1、在settings中的INSTALLED_APPS配置当前app，不然django无法找到自定义的simple_tag.

        2、在app中创建templatetags模块(模块名只能是templatetags)

        3、在templatetags里面创建任意 .py 文件，

        如：my_tags.py


        from django import template
        from django.utils.safestring import mark_safe

        register = template.Library()   #register的名字是固定的,不可改变
        @register.filter   过滤器
        def multi(x,y):
            return x*y

        @register.simple_tag  标签
        def multitag(x,y,z):
            return x*y*z
        @register.simple_tag  标签
        def my_input(id,arg):
        　　 result = "<input type='text' id='%s' class='%s' />" %(id,arg,)
        　　 return mark_safe(result)

        4、在使用自定义simple_tag和filter的html文件中导入之前创建的 my_tags.py

        {% load my_tags %}
        5、使用simple_tag和filter（如何调用）

        过滤器： {{ var|filter_name:参数 }} # 参数只能是两个，一个参数是变量var ，一个是参数是后面的那个参数

        标签： {% simple_tag 参数1 参数2 ... %}


        -------------------------------.html
        {% load xxx %}

        # num=12
        {{ num|multi:2 }} #24

        {{ num|multi:"[22,333,4444]" }}   相当于复制了，吧[22,333,4444]乘了num遍
        {% multitag 2 5 6 %} 参数不限,但不能放在if for语句中 {% simple_tag_multi num 5 %}

        
        自定义过滤器函数的参数只能两个，可以进行逻辑判断
        自定义标签无参数限制，不能进行逻辑判断
        {% if i|multi:5 > 1000 %}   <!-- 判断i*5>1000 -->
            <p>大于{{ i }}</p>
        {% else %}
            <p>大于等于{{ i }}</p>
        {% endif %}










