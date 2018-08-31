********HTML********


**Web服务本质**

import socket
sk = socket.socket()
sk.bind(("127.0.0.1", 8080))
sk.listen(5)
while True:
    conn, addr = sk.accept()
    data = conn.recv(8096)
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")#http协议 简化
    conn.send(b"<h1>Hello world!</h1>")#发送内容
    conn.close()
sk.close()

浏览器发送请求-->HTTP协议-->服务器接受请求-->服务端返回响应-->服务端把HTML文件内容发送给浏览器-->浏览器渲染页面


What HTML?

*超文本标记语言（Hypertext Markup Language，HTML）是一种用于创建网页标记语言

*本质上是浏览器可识别的规则，我们按照规则写网页，浏览器根据规则渲染我们的页面。
对于不同的浏览器，对于同一个标签可能会有不同的解释。（兼容性问题）

*网页文件的扩展名：.html或.htm

*HTML是一种标记语言，他不是一种编程语言，HTML使用标签来描述网页。


****HTML文档结构****

*最基本的HTML文档**
<!DOCTYPE html>
<html lang = 'zh-CN'>
<head>
	<meta chrset = 'UTF-8'>
	<title> 标题 </title>
</head>
<body>

</body>
</html>

#解释

1.<!DOCTYPE html>声明为HTML5文档

2.<html></html>是文档的开始标记语言和结束标记，是HTML页面的根本元素，在他们之间是文档的头部(head)和主题(body)

3.<head></head>定义了HTML文档的开头部分。他们之间的内容不会在浏览器的文档窗口显示。包含了文档的元（meta）数据

4.<title></title>定义了网页标题，在浏览器标题栏显示

5.<body></body>之间的文本是可见的网页主体内容

注意：
对于中文网页需要使用<meta charset='utf-8'>声明编码。否则会出现乱码。这些浏览器会设置GBK为默认编码，则需要我们设为
<meta charset='gbk'>

****HTML标签格式****

*HTML标签是由尖括号包围的关键字
*HTML标签通常是成对出现的，比如：<div>和</div>，第一个标签是开始，第二个标签是结束。结束标签会有斜线。
*也有一部分标签是单独呈现的，比如：<br/>、<hr/>、<img src="1.jpg" />等。
*标签里面可以有若干属性，也可以不带属性。

****标签的语法

<标签名 属性1=“属性值1” 属性2=“属性值2”……>内容部分</标签名>
<标签名 属性1=“属性值1” 属性2=“属性值2”…… />

几个很重要的属性：
id：定义标签的唯一ID，HTML文档树中唯一
class：为html元素定义一个或多个类名（classname）(CSS样式类名)
style：规定元素的行内样式（CSS样式

****HTML注释

<!--注释内容-->

****<!DOCTYPE>标签****

<!DOCTYPE> 声明必须是HTML文档的第一行，位于<html>标签之前
<!DOCTYPE> 声明不是HTML标签，他是指示web浏览器关于页面使用哪个HTML版本进行编写的指令

****HTML常用标签****


**head内常用的标签**

1.<title></title> 定义网页的标题
2.<style></style> 定义内部样式表
3.<script><script>定义JS代码或引入外部JS文件
4.<link/> 引入外部样式文件
5.<meta/>定义网页原信息

****Meta标签

Meta标签介绍：

<meta>元素可提供有关页面的原信息（mata-information）,针对搜索引擎和更新频度的描述和关键词。
<meta>标签位于文档的头部，不包含任何内容。
<meta>提供的信息是用户不可见的。
meta标签的组成：meta标签共有两个属性，它们分别是http-equiv属性和name 属性，不同的属性又有不
同的参数值，这些不同的参数值就实现了不同的网页功能。

1.http-equiv属性：相当于http的文件头作用，它可以向浏览器传回一些有用的信息，以帮助正确地显示
网页内容，与之对应的属性值为content，content中的内容其实就是各个参数的变量值。

<!--2秒后跳转到对应的网址，注意引号-->
<meta http-equiv="refresh" content="2;URL=https://www.baidu.com">
<!--指定文档的编码类型-->
<meta http-equiv="content-Type" charset=UTF8">
<!--告诉IE以最高级模式渲染文档-->
<meta http-equiv="x-ua-compatible" content="IE=edge">

2.names属性：主要用于描述网页，与之对应的属性值为content，content中的内容主要是便于搜索引擎
机器人查找信息和分类信息用的

<meta name="keywords" content="meta总结,html meta,meta属性,meta跳转">
<meta name="description" content="Python">


******body内常用表标签******

****基本标签（块级标签和内联标签）****

<b>加粗</b>
<i>斜体</i>
<u>下划线</u>
<a>删除</a>

<p>段落标签</p>

<h1>标题1</h1>
<h2>标题2</h2>
<h3>标题3</h3>
<h4>标题4</h4>
<h5>标题5</h5>
<h6>标题6</h6>

<!--换行-->
<br>

<!--水平线-->
<hr>


****特殊字符****

空格------&nbsp;
>--------&gt;
<--------&lt;
&--------&amp;
￥--------&yen;
版权(©️)---&copy;
注册(®️)---&reg;



****div标签和span标签****

div标签用来定义一个块级元素，并无实际的意义。主要通过CSS样式为其赋予不同的表现。
span标签用来定义内联(行内)元素，并无实际的意义。主要通过CSS样式为其赋予不同的表现。

块级元素与行内元素的区别：
所谓块元素，是以另起一行开始渲染的元素，行内元素则不需另起一行。如果单独在网页中插入这两个元素，不会对页面产生任何的影响。
这两个元素是专门为定义CSS样式而生的。

注意：

关于标签嵌套：通常块级元素可以包含内联元素或某些块级元素，但内联元素不能包含块级元素，它只能包含其它内联元素。

p标签不能包含块级标签，p标签也不能包含p标签。

****img标签****

<img src='图片路径' alt='图片未加载成功时的提示' title='鼠标悬浮时提示信息' width='宽' height='高（宽高只有一个会等比缩放）'>

****a标签****
超链接标签

所谓的超链接是指从一个网页指向一个目标的连接关系，这个目标可以是另一个网页，
也可以是相同网页上的不同位置，还可以是一个图片，一个电子邮件地址，一个文件，
甚至是一个应用程序。

什么是URL？
URL是统一资源定位器(Uniform Resource Locator)的缩写，也被称为网页地址，是因特网上标准的资源的地址。
URL举例
http://www.baidu.com/stu/index.html
http://111.13.100.91/stu/index.html

URL地址由4部分组成
第1部分：为协议：http://、ftp://等 
第2部分：为站点地址：可以是域名或IP地址
第3部分：为页面在站点中的目录：stu
第4部分：为页面名称，例如 index.html
各部分之间用“/”符号隔开。

<a href='https://www.baidu.com' target='_blank'>点击我</a>

href属性指定目标网页地址。该地址可以有几种类型：
1.绝对URL-指向另一个站点（不如 href = 'https://www.baidu.com'）
2.相对URL-指向当前站点中确切的路径（href = 'index.html'）
3.锚URL-指向页面中的锚（href = '#top'）

target:
1._blank表示在新标签页中打开目标页面
2._self表示在当前标签页中打开目标页面

****列表*****

1.无序列表 

<ul type="disc">
	<li>第一项</li>
	<li>第二项</li>
</ul>

type属性：
1.disc（实心圆点，默认值）
2.circle（空心圆圈）
3.square（实行方块）
4.none（无样式）

2.有序列表
<ol type="1" start="2">
	<li>第一项</li>
	<li>第二项</li>
</ol>

type属性：
1.1数字列表，默认值
2.A大写字母
3.a小写字母
4.I大写罗马
5.i小写罗马


3.标题列表

<dl>
	<dt>标题1</dt>
	<dt>内容1</dt>
	<dt>标题2</dt>
	<dt>内容1</dt>
	<dt>内容2</dt>
</dl>


****表格****

表格是一个二维数据空间，一个表格由若干行组成，一行又有若干单元格组成，单元格里面可以
包括文字。列表。图案。表单。数字符号。预置文本和其它的表格等内容。
表格最重要的目的是显示表格类数据。
表格类数据是值最适合组织为表格格式（即按行和列组织）的数据

表格基本结构：

<table>
	<thead>
		<tr>
			<td>序号</td>
			<td>姓名</td>
			<td>爱好</td>
		</tr>
	</theaf>
	<tbody>
		<tr>
			<td>1</td>
			<td>tom</td>
			<td>吃老鼠</td>
		</tr>
		<tr>
			<td>2</td>
			<td>Jacl</td>
			<td>吃奶酪</td>
		</tr>
	</tbody>
</table>



属性：
1.border：表格边框
2.cellpadding：内边距
3.cellspacing：外边距
4.width：像素百分比（最好通过css来设置长度）
5.rowspan：单元格竖跨多少行
6.colspan：单元格横跨多少列（即合并单元格）

****form（表单）****

功能；
表单用于向服务器传输数据，从而实现用户与web服务器的交互

表单能够包含input系列标签，比如文本字段、复选框、单选框、提交按钮等等

表单还可以包含textarea、select、fieldest和lable标签


***表单属性

1.accept-charset   规定在被提交表单中使用的字符集（默认：页面字符集）
2.action     规定在何处提交表单的地址（URL）（提交页面）
3.autocomplete  规定浏览器应该自动完成表单（默认：开启）
4.enctype 	规定被提交数据的编码（默认：url-encoded）
5.method 	规定在提交表单时所用的HTTP方法（默认GET）
6.name 		规定识别表单的名称（对于DOM使用：document.forms.name）
7.novalidate规定浏览器不验证表单
8.target	规定action属性中地址的目标（默认_self）

***表单元素

基本概念：

HTML表单是HTML元素中较为复杂的部分，表单往往和脚本、动态页面、数据处理等功能相结合，因此它是制作动态网站很重要的内容。
表单一般用来收集用户的输入信息
表单工作原理：
访问者在浏览有表单的网页时，可填写必需的信息，然后按某个按钮提交。这些信息通过Internet传送到服务器上。 
服务器上专门的程序对这些数据进行处理，如果有错误会返回错误信息，并要求纠正错误。
当数据完整无误后，服务器反馈一个输入完成的信息。


******input******

<input>元素会根据不同的type属性，变化为多种形态

type属性值	表现形式		对应代码

text		单行输入文本	<input type="text" />
password	密码输入框	<input type="password"  />
date		日期输入框	<input type="date" />
checkbox	复选框		<input type="checkbox" checked="checked"  />
radio		单选框		<input type="radio"  />
submit		提交按钮		<input type="submit" value="提交" />
reset		重置按钮		<input type="reset" value="重置"  />
button		普通按钮		<input type="button" value="普通按钮"  />
hidden		隐藏输入框	<input type="hidden"  />
file		文本选择框	<input type="file"  />


属性说明：

1.name：表单提交时的“键”，注意和id的区别
2.value：表单提交时对应项的值
	type = “button”，“reset”，“submit”时，为按钮上显示的文本信息
	type = “text”，“password”，“hidden“时，为输入框的初始值
	type = ”checkbox“，”radio“，”file“时，为输相关联的值
3.checked：radio和checkbox默认被选中的项
4.readonly：text和password设置只读
5.disabled：所有input均适用


******select标签******

<from action="" method="post">
	<select name="city" id="city">
		<option value="1">北京</option>
		<option selected="selected" value="2">成都</option>
		<option value="3">西安</option>
	</select>
</form>

属性说明：

1.multiple：布尔属性，设置后为多选，否则默认单选
2.disabled：禁用
3.selected：默认选中该项
4.value：定义提交时的选项值


******lable标签******

定义：<lable>标签为input元素定义标注（标记）

说明：
1.label元素不会向用户呈现任何特殊效果
2.<lable>标签的for属性值应当与相关元素的id属性值相同

<form>
	<lable for="username">用户名</lable>
	<input type="text" id="username" name="username">
</form>



******textarea多行文本******

<textarea name="memo" id="memo" cols="30" rows="10">
	默认内容
</textarea>

属性说明：
1.name:名称
2.rows:行数
3.cols:列数
4.disable:禁用






























































