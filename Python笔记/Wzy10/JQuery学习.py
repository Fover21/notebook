********JQuery********

****JQuary介绍****

1.jQuery是一个轻量级的、兼容多浏览器的JavaScript库。
2.jQuery使用户能够更方便地处理HTML Document、Events、实现动画效果、方便地进行Ajax交互，
能够极大地简化JavaScript编程。它的宗旨就是：“Write less, do more.“


****JQuary的优势****

1.一款轻量级的JS框架。jQuery核心js文件才几十kb，不会影响页面加载速度。
2.丰富的DOM选择器,jQuery的选择器用起来很方便，比如要找到某个DOM对象的相邻元素，
JS可能要写好几行代码，而jQuery一行代码就搞定了，再比如要将一个表格的隔行变色，
jQuery也是一行代码搞定。
3.链式表达式。jQuery的链式操作可以把多个操作写在一行代码里，更加简洁。
4.事件、样式、动画支持。jQuery还简化了js操作css的代码，并且代码的可读性也比js要强。
5.Ajax操作支持。jQuery简化了AJAX操作，后端只需返回一个JSON格式的字符串就能完成与前端的通信。
6.跨浏览器兼容。jQuery基本兼容了现在主流的浏览器，不用再为浏览器的兼容问题而伤透脑筋。
7.插件扩展开发。jQuery有着丰富的第三方的插件，例如：树形菜单、日期控件、图片切换插件、弹出窗口
等等基本前端页面上的组件都有对应插件，并且用jQuery插件做出来的效果很炫，并且可以根据自己需要去
改写和封装插件，简单实用。

****JQuary的内容****

1）选择器
2）筛选器
3）样式操作
4）文本操作
5）属性操作
6）文档处理
7）事件
8）动画效果
9）插件
10）each、data、Ajax


****JQuary版本****

1.x：兼容IE678,使用最为广泛的，官方只做BUG维护，功能不再新增。因此一般项目来说，使用1.x版本就可以了，最终版本：1.12.4 (2016年5月20日)
2.x：不兼容IE678，很少有人使用，官方只做BUG维护，功能不再新增。如果不考虑兼容低版本的浏览器可以使用2.x，最终版本：2.2.4 (2016年5月20日)
3.x：不兼容IE678，只支持最新的浏览器。需要注意的是很多老的jQuery插件不支持3.x版。目前该版本是官方主要更新维护的版本。
维护IE678是一件让人头疼的事情，一般我们都会额外加载一个CSS和JS单独处理。值得庆幸的是使用这些浏览器的人也逐步减少，PC端用户已经逐步被移动端
用户所取代，如果没有特殊要求的话，一般都会选择放弃对678的支持。


****JQuary对象****

JQuery对象就是通过jQuery包装DOM对象后产生的对象。jQuery对象是 jQuery独有的。如果一个对象是 jQuery对象，那么它就可以使用jQuery里的方法：
例如$(“#i1”).html()。

$("#i1").html()的意思是：获取id值为 i1的元素的html代码。其中 html()是jQuery里的方法。

相当于： document.getElementById("i1").innerHTML;

虽然 jQuery对象是包装 DOM对象后产生的，但是 jQuery对象无法使用 DOM对象的任何方法，同理 DOM对象也没不能使用 jQuery里的方法。

一个约定，我们在声明一个jQuery对象变量的时候在变量名前面加上$：

var $variable = jQuery对像
var variable = DOM对象
$variable[0]//jQuery对象转成DOM对象

拿上面那个例子举例，jQuery对象和DOM对象的使用：

$("#i1").html();//jQuery对象可以使用jQuery的方法
$("#i1")[0].innerHTML;// DOM对象使用DOM的方法

****JQuary基础语法****

$(selector).action()


**查找标签**

*选择器*

id选择器：

$("#id")
标签选择器：

$("tagName")
class选择器：

$(".className")
配合使用：

$("div.c1")  // 找到有c1 class类的div标签
所有元素选择器：

$("*")
组合选择器：

$("#id, .className, tagName")
层级选择器：

x和y可以为任意选择器

$("x y");// x的所有后代y（子子孙孙）
$("x > y");// x的所有儿子y（儿子）
$("x + y")// 找到所有紧挨在x后面的y
$("x ~ y")// x之后所有的兄弟y

基本筛选器：

:first // 第一个
:last // 最后一个
:eq(index)// 索引等于index的那个元素
:even // 匹配所有索引值为偶数的元素，从 0 开始计数
:odd // 匹配所有索引值为奇数的元素，从 0 开始计数
:gt(index)// 匹配所有大于给定索引值的元素
:lt(index)// 匹配所有小于给定索引值的元素
:not(元素选择器)// 移除所有满足not条件的标签
:has(元素选择器)// 选取所有包含一个或多个标签在其内的标签(指的是从后代元素找)

例子：

$("div:has(h1)")// 找到所有后代中有h1标签的div标签
$("div:has(.c1)")// 找到所有后代中有c1样式类的div标签
$("li:not(.c1)")// 找到所有不包含c1样式类的li标签
$("li:not(:has(a))")// 找到所有后代中不含a标签的li标签

jQuery版自定义模态框
属性选择器：

[attribute]
[attribute=value]// 属性等于
[attribute!=value]// 属性不等于
例子：

// 示例
<input type="text">
<input type="password">
<input type="checkbox">
$("input[type='checkbox']");// 取到checkbox类型的input标签
$("input[type!='text']");// 取到类型不是text的input标签
表单常用筛选：


:text
:password
:file
:radio
:checkbox

:submit
:reset
:button

例子：

$(":checkbox")  // 找到所有的checkbox
表单对象属性:

:enabled
:disabled
:checked
:selected
例子：

找到可用的input标签

<form>
  <input name="email" disabled="disabled" />
  <input name="id" />
</form>

$("input:enabled")  // 找到可用的input标签
 找到被选中的option：

<select id="s1">
  <option value="beijing">北京市</option>
  <option value="shanghai">上海市</option>
  <option selected value="guangzhou">广州市</option>
  <option value="shenzhen">深圳市</option>
</select>

$(":selected")  // 找到所有被选中的option


*筛选器*

下一个元素

$("#id").next()
$("#id").nextAll()
$("#id").nextUntil("#i2")

上一个元素

$("#id").prev()
$("#id").prevAll()
$("#id").prevUntil("#i2")

父亲元素

$("#id").parent()
$("#id").parents()  // 查找当前元素的所有的父辈元素
$("#id").parentsUntil() // 查找当前元素的所有的父辈元素，直到遇到匹配的那个元素为止。

儿子和兄弟元素

$("#id").children();// 儿子们
$("#id").siblings();// 兄弟们

查找

搜索所有与指定表达式匹配的元素。这个函数是找出正在处理的元素的后代元素的好方法。

$("div").find("p")			等价于$("div p")

筛选

筛选出与指定表达式匹配的元素集合。这个方法用于缩小匹配的范围。用逗号分隔多个表达式。

$("div").filter(".c1")  // 从结果集中过滤出有c1样式类的			等价于 $("div.c1")

补充：

.first() // 获取匹配的第一个元素
.last() // 获取匹配的最后一个元素
.not() // 从匹配元素的集合中删除与指定表达式匹配的元素
.has() // 保留包含特定后代的元素，去掉那些不含有指定后代的元素。
.eq() // 索引值等于指定值的元素

****操作标签****

**样式操作**

样式类

addClass();// 添加指定的CSS类名。
removeClass();// 移除指定的CSS类名。
hasClass();// 判断样式存不存在
toggleClass();// 切换CSS类名，如果有就移除，如果没有就添加。

CSS

css("color","red")//DOM操作：tag.style.color="red"
示例：

$("p").css("color", "red"); //将所有p标签的字体设置为红色
位置：

offset()// 获取匹配元素在当前窗口的相对偏移或设置元素位置
position()// 获取匹配元素相对父元素的偏移
scrollTop()// 获取匹配元素相对滚动条顶部的偏移
scrollLeft()// 获取匹配元素相对滚动条左侧的偏移


.offset()方法允许我们检索一个元素相对于文档（document）的当前位置。
和 .position()的差别在于： .position()是相对于相对于父级元素的位移。

尺寸：

height()
width()
innerHeight()
innerWidth()
outerHeight()
outerWidth()

****文本操作****


HTML代码：

html()// 取得第一个匹配元素的html内容
html(val)// 设置所有匹配元素的html内容
文本值：

text()// 取得所有匹配元素的内容
text(val)// 设置所有匹配元素的内容
值：

val()// 取得第一个匹配元素的当前值
val(val)// 设置所有匹配元素的值
val([val1, val2])// 设置checkbox、select的值
示例：

获取被选中的checkbox或radio的值：

<label for="c1">女</label>
<input name="gender" id="c1" type="radio" value="0">
<label for="c2">男</label>
<input name="gender" id="c2" type="radio" value="1">
可以使用：

$("input[name='gender']:checked").val()

****属性操作****

用于ID等或自定义属性：

attr(attrName)// 返回第一个匹配元素的属性值
attr(attrName, attrValue)// 为所有匹配元素设置一个属性值
attr({k1: v1, k2:v2})// 为所有匹配元素设置多个属性值
removeAttr()// 从每一个匹配的元素中删除一个属性
用于checkbox和radio

prop() // 获取属性
removeProp() // 移除属性
注意：

在1.x及2.x版本的jQuery中使用attr对checkbox进行赋值操作时会出bug，在3.x版本的jQuery中则没有这个问题。为了兼容性，我们在处理checkbox和radio的时候尽量使用特定的prop()，不要使用attr("checked", "checked")。

<input type="checkbox" value="1">
<input type="radio" value="2">
<script>
  $(":checkbox[value='1']").prop("checked", true);
  $(":radio[value='2']").prop("checked", true);
</script>
示例：全选、反选、取消

****文档处理****

添加到指定元素内部的后面

$(A).append(B)// 把B追加到A
$(A).appendTo(B)// 把A追加到B
添加到指定元素内部的前面

$(A).prepend(B)// 把B前置到A
$(A).prependTo(B)// 把A前置到B
添加到指定元素外部的后面

$(A).after(B)// 把B放到A的后面
$(A).insertAfter(B)// 把A放到B的后面
添加到指定元素外部的前面

$(A).before(B)// 把B放到A的前面
$(A).insertBefore(B)// 把A放到B的前面
移除和清空元素

remove()// 从DOM中删除所有匹配的元素。
empty()// 删除匹配的元素集合中所有的子节点。
例子：

点击按钮在表格添加一行数据。

点击每一行的删除按钮删除当前行数据。

替换

replaceWith()
replaceAll()
克隆

clone()// 参数


****事件****

**常用事件**

click(function(){...})
hover(function(){...})
blur(function(){...})
focus(function(){...})
change(function(){...})
keyup(function(){...})


**时间绑定**

.on( events [, selector ],function(){})

events： 事件
selector: 选择器（可选的）
function: 事件处理函数


**移除事件**

.off( events [, selector ][,function(){}])
off() 方法移除用 .on()绑定的事件处理程序。

events： 事件
selector: 选择器（可选的）
function: 事件处理函数

**阻止后续事件执行**

return false; // 常见阻止表单提交等
注意：

像click、keydown等DOM中定义的事件，我们都可以使用`.on()`方法来绑定事件，但是`hover`这种jQuery中定义的事件就不能用`.on()`方法来绑定了。

想使用事件委托的方式绑定hover事件处理函数，可以参照如下代码分两步绑定事件：

$('ul').on('mouseenter', 'li', function() {//绑定鼠标进入事件
    $(this).addClass('hover');
});
$('ul').on('mouseleave', 'li', function() {//绑定鼠标划出事件
    $(this).removeClass('hover');
});


**页面加载**

当DOM载入就绪可以查询及操纵时绑定一个要执行的函数。这是事件模块中最重要的一个函数，因为它可以极大地提高web应用程序的响应速度。

两种写法：

$(document).ready(function(){
// 在这里写你的JS代码...
})
简写：

$(function(){
// 你在这里写你的代码
})

**事件委托**

事件委托是通过事件冒泡的原理，利用父标签去捕获子标签的事件。

示例：

表格中每一行的编辑和删除按钮都能触发相应的事件。

$("table").on("click", ".delete", function () {
  // 删除按钮绑定的事件
})

********动画效果*******

// 基本
show([s,[e],[fn]])
hide([s,[e],[fn]])
toggle([s],[e],[fn])
// 滑动
slideDown([s],[e],[fn])
slideUp([s,[e],[fn]])
slideToggle([s],[e],[fn])
// 淡入淡出
fadeIn([s],[e],[fn])
fadeOut([s],[e],[fn])
fadeTo([[s],o,[e],[fn]])
fadeToggle([s,[e],[fn]])
// 自定义（了解即可）
animate(p,[s],[e],[fn])

补充：

**each**

jQuery.each(collection, callback(indexInArray, valueOfElement))：

描述：一个通用的迭代函数，它可以用来无缝迭代对象和数组。数组和类似数组的对象通过一个长度属性（如一个函数的参数对象）来迭代数字索引，从0到length - 1。其他对象通过其属性名进行迭代。

li =[10,20,30,40]
$.each(li,function(i, v){
  console.log(i, v);//index是索引，ele是每次循环的具体元素。
})
输出：

010
120
230
340
.each(function(index, Element))：

描述：遍历一个jQuery对象，为每个匹配元素执行一个函数。

.each() 方法用来迭代jQuery对象中的每一个DOM元素。每次回调函数执行时，会传递当前循环次数作为参数(从0开始计数)。由于回调函数是在当前DOM元素为上下文的语境中触发的，所以关键字 this 总是指向这个元素。

// 为每一个li标签添加foo
$("li").each(function(){
  $(this).addClass("c1");
});
注意: jQuery的方法返回一个jQuery对象，遍历jQuery集合中的元素 - 被称为隐式迭代的过程。当这种情况发生时，它通常不需要显式地循环的 .each()方法：

也就是说，上面的例子没有必要使用each()方法，直接像下面这样写就可以了：

$("li").addClass("c1");  // 对所有标签做统一操作
注意：

在遍历过程中可以使用 return false提前结束each循环。

终止each循环

return false；


补充：

在匹配的元素集合中的所有元素上存储任意相关数据或返回匹配的元素集合中的第一个元素的给定名称的数据存储的值。

.data(key, value):

描述：在匹配的元素上存储任意相关数据。

$("div").data("k",100);//给所有div标签都保存一个名为k，值为100
.data(key):

描述: 返回匹配的元素集合中的第一个元素的给定名称的数据存储的值—通过 .data(name, value)或 HTML5 data-*属性设置。

$("div").data("k");//返回第一个div标签中保存的"k"的值
.removeData(key):

描述：移除存放在元素上的数据，不加key参数表示移除所有保存的数据。

$("div").removeData("k");  //移除元素上存放k对应的数据


****插件****
jQuery.extend(object)

jQuery的命名空间下添加新的功能。多用于插件开发者向 jQuery 中添加新函数时使用。

示例：


<script>
jQuery.extend({
  min:function(a, b){return a < b ? a : b;},
  max:function(a, b){return a > b ? a : b;}
});
jQuery.min(2,3);// => 2
jQuery.max(4,5);// => 5
</script>

jQuery.fn.extend(object)

一个对象的内容合并到jQuery的原型，以提供新的jQuery实例方法。


<script>
  jQuery.fn.extend({
    check:function(){
      return this.each(function(){this.checked =true;});
    },
    uncheck:function(){
      return this.each(function(){this.checked =false;});
    }
  });
// jQuery对象可以使用新添加的check()方法了。
$("input[type='checkbox']").check();
</script>

单独写在文件中的扩展：


(function(jq){
  jq.extend({
    funcName:function(){
    ...
    },
  });
})(jQuery);


