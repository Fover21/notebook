一、JQuery基础

1.为什么要用jquery？
    写起来简单，省事，开发效率高，兼容性好
2、什么是jQuery?
    jQuery是一个兼容多浏览器的JavaScript库
3、如何使用jQuery？
    1、导入 <script src="jquery-x.x.x.js"></script>
           或者<script src="jquery-x.x.x.min.js"></script>
    2、语法规则：$("")
4、JS和jQuery的区别？
    jQuery就是用JS写的
    js是基础，jQuery是工具
5、jQuery介绍
    - 版本
      - 1.x
         兼容IE8。。。
      - 3.x
         最新
   - .min.xx
      压缩的：生产环境用
   -  没有压缩的（没有.min.xx）：开发用
6、 jQuery知识点
    　　html:裸体的人
    　　css:穿了衣服的人
   　　 JS：让人动起来
7、选择器：
   1、基本选择器
        - ID选择器                  $("#id的值")
        - 类选择器（class）          $(".class的值")
        - 标签选择器(html标签)       $("标签的名字")
        - 所有标签                  $("*")

        - 组合选择器                $("xx,xxx")
   2、层级选择器
        - 从一个标签的子子孙孙去找    $("父亲 子子孙孙")
        - 从一个标签的儿子里面找      $("父亲>儿子标签")
        - 找紧挨着的标签             $("标签+下面紧挨着的那个标签")
        - 找后面所有同级的           $("标签~兄弟")

8、jQuery对象：
        - 用jQuery选择器查出来的就是jQuery对象
        - jQuery对象，他就可以使用jQuery方法，不能使用DOM的方法

        - DOM对象和jQuery对象转换：
            - $(".c1")[0] --> DOM对象
            - $(DOM对象)

9、筛选器
        - 写在引号里面的
            基本筛选器
            　　$(" :first")  					找第一个
            　　$(" :not('')")  					不是/非
            　　$("#i1>input":not('.c1,.c2'))
            　　$(" :even")     					偶数
            　　$(" :odd")      					奇数
            　　$(" :eq(index)")       			找等于index的
            　　$(" :gt(index)")       			找大于index的
            　　$(" :lt(index)")       			找小于index的
            　　$(" :last")     					最后一个
            　　$(" :focus")    					焦点

 			内容==========
            　　$(" .c1:contains('我是第一个')")    包含文档的内容的标签
            　　$(" :empty")     标签内容为空的
            　　$(" :has("标签名")    包含标签的标签
            　　$(" :parent")    找有孩子的父亲
            　　$("#i7").parent()   找i7的父亲
            可见性========
            　　$(" :hidden")   找到隐藏的
            　　$(" :visible")  找不隐藏的，也就是显示的
         　　属性==========
            　　input[name]  --> 找有name属性的input
            　　input[type='password']  --> 类型是password的input标签
            表单==========
           　　 :input
            　　:password
            　　:checkbox
           　　 :radio
            　　:submit
           　　 :button
            　　:image
            　　:file
            表单对象属性=========
                :enable   可选的
                :disable  不可选
                :checked  选中的
                :selected 下拉框选中
        - 写在信号外面当方法用的
            过滤===========
            $("").first()   找第一个
            $("").parent()  找父亲
            $("").eq(index) 找等于index的
            .hasClass()  判断有没有某个类的
         查找
            .children() 找孩子
            .find()  查找
            .next()  下面的
            .nextAll()  下面所有的
            .nextUntil() 找下面的直到找到某个标签为止

            .parent() 找父亲
            .parents() 找所有的父亲
            .parentsUntil()  直到找到你要找的那个父亲为止

            .prev()  上面的
            .prevAll()  上面的所有
            .prevUntil()  上面的直到找到某个标签为止

            .siblings()  所有的兄弟

- toggleClass()  切换|开关：有就移除，没有就添加

- addClass("hide")  添加类

- removeClass("hide") 删除类


