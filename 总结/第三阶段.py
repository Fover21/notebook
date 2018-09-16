
1.HTML
	1.定义：超文本标记语言
	2.HTML标签的结构
		HTML的结构：
			head——>给浏览器看的内容
					存在标签
					title—>标签
					style—>CSS样式
					link—>CSS样式
					script—>JS
					meta—>
			body——>给用户看的内容
		HTML标签的语法：
			<head 属性1=值1 属性2=值2></head>
			<body></body>
			<mata>
	3.Body标签中的常用标签
		1.常用标签的分类
			1.独占一行的	块级标签
				1.h1~h6	标题数越大标题越小
				2.p		段落
				3.div		块
				4.hr		一条水平线
				5.li  		#列表中的一项
				6.tr		表格中的一行
			2.在一行显示的		行内标签/内联标签
				1.a		超链接
				2.span	行内元素
				3.img	图片
				4.b/I/u/s	加粗、斜体、下划线、删除
			3.其他
				1.ul		无序列表（其中的行li）
				2.ol		有序列表（其中的行li）
				3.dl dt 	标题列表
				4.table	表格		分为<thead>和<bhead> <tr>为行名称<td>为行内容
				5.lable	标签
				6.br		换行
				7.textarea	多行文本框

			4.特殊字符
				空格			&nbsp;
				>			&gt;
				<			&lt;
				&			&amp;
				￥			&yen;
				版权©️		&copy;
				注册®️		&reg;
		2.标签的嵌套
			标签可以嵌套标签
			注意事项
				1.尽量不要用内联标签包块儿级标签
				2.p标签不能嵌套p标签
				3.p标签不能嵌套div标签
		3.获取用户输入的标签
			1.form标签
				一个容器，包住所有获取用户输入的标签
				-action属性
				-method属性
				-enctype属性
			2.input属性
				text			文本框
				password		文本密码框
				email		email格式文本框
				date			日期
				file			文本选择框
				
				checkbox	多选框
				radio		单选框
	
				button		普通按钮	通常用JS给它绑定事件
				submit		提交按钮	默认将form表单的数据提交
				reset			重置按钮	将当前form中的输入框都清空
			3.select标签	选择下拉框
			4.textarea标签	一个大的文本框
			5.form表单提交任务的注意事项：
				{“k1”: “v1”}
				1.form标签必须把获取用户输入的标签包起来
				2.form标签必须有action属性和method
				3.form中的获取用户输入的标签必须要有name属性

2.CSS
		1. CSS语法
			选择器 {属性1：值1;...;}
		2. CSS导入方式
			1. 行内样式-->把css样式写到标签的style属性里
			2. style标签中定义
			3. 写在单独的css文件中，通过link标签导入
		3. CSS选择器
			1. 基本选择器
				1. ID选择器      --> HTML标签都有唯一的ID
				2. 类选择器      --> HTML标签可以设置class属性
				3. 标签选择器    --> 大范围使用
				4. 通用选择器 *
			2. 组合选择器
				1. div p    后代选择器
				2. div>p    儿子选择器
				3. div+p    毗邻选择器
				4. div~p    弟弟选择器 
			3. 分组和嵌套（全班都没想起来的）
				div, p {}
				div.c1 {}
			4. 属性选择器
				1. div[s14]              找到有s14这个属性的div标签
				2. input[type='email']   找到type是email的input标签
			5. 伪类选择器
				1. :hover     --> 鼠标移动到标签上时应用的样式
				2. :focus     --> input标签获取焦点时应用的样式
			6. 伪元素选择器
				p:before {    --> 在P标签内部的最前面追加一个内容
					content: "*";
					color: red;
				}
				p:after {     --> 在P标签内部的最后面追加一个内容
					
				}
				清除浮动：
				.clearfix:after{
					content: "";
					clear: both;
					display: block;
				}
		4. CSS选择器的优先级
			1. 样式名一样的话
				类似 变量覆盖 最后加载的那个样式生效
			2. 样式名不一样
				根据 权重计算
				内联样式(1000)>ID选择器(100)>类选择器(10)>元素选择器(1)>继承(0)
			3. 不讲道理的
				!important
		5. CSS属性
			1. 文字属性相关
				1. font-family: "字体1", "字体2", 
				2. font-size        字体大小
				3. font-weight		字体粗细
				4. color            字体颜色
					1. 英文的颜色名    red
					2. 16进制颜色代码  #FF0000
					3. RGB             rgb(255, 0, 0)
					4. rgba(255, 0, 0, 0.4)
			2. 宽和高
				1. width             宽
				2. height			 高
					只有块儿级标签设置宽和高才有效
			3. 背景
				background
				
				background-color: red
				background-image: url(...)
			4. 文本样式
				1. 水平居中
					text-align: center
				2. 单行文本的垂直居中
					line-height=父标签的高度
				3. 文本装饰线
					text-decoration: none/under-line/over-line/line-through
			5. CSS盒子模型
				内容-->padding-->border-->margin
			6. 浮动
				float: left/right
				浮动的副作用
			7. 定位
				1. 相对定位     --> 相对自己原来在的位置做定位
				2. 绝对定位     --> 相对自己已经定位过的祖先标签
				3. 固定定位     --> 相对于屏幕做定位
			8. 溢出
				overflow: hidden/scroll/auto
			9. 边框
				border: 1px solid red;
				border-radius: 50%
			10. display
				1. block
				2. inline
				3. inline-block
				4. none

CSS一些常用属性
	********CSS一些常用属性*******
0.去掉下划线 ：text-decoration:none ;
1.加上下划线： text-decoration: underline;
2.调整文本和图片的位置（也就是设置元素的垂直对齐方式）：vertical-align:-20px;
3.外边距：margin
4.内边距：padding
5.居中；margin 0 auto;(只是针对盒子居中)
6内联标签是不可以设置长宽的，有时候就得把内联标签变成块级标签或者块级内联标签，这就用到了display标签。。
　　1.将内联标签转换成块级标签：display:block;
　　2.将块级标签转换成内联标签：display:inline;
　　3.块级内联标签：display；inline-block;
　　　块级内联标签可以像块级一样可设长宽，也可像内联一样在一行显示
6.隐藏的两个方法：display:none; #隐藏了会顶上去
　　　　　　　　　visibility :hidden; #隐藏了不会顶上去
7.隐藏溢出的两个方法：overflow :auto;
　　　　　　　　　　　overflow :scoll;  #带滚动条
8.文本水平居中：text-align:center;
   文本垂直居中：line-height;
9.伪类；
　　1.没访问之前： a:link{color:red;} 
　　2.鼠标悬浮时： a:hover{color:green;}
　　3.访问过后： a:visited{color:yellow;}
　　4.鼠标点击时 a:active{color:blue;}
　　5.在p标签属性为c2的后面加上内容
　　p.c2:after{
　　　　content:'hello';
　　　　color:red;
　　}
6.在p标签属性为c2的钱面加上内容
　　p.c2:before{
　　　　content:'啦啦啦';
　　　　color:red;
　　}
10.position的四种属性
　　1.static：默认位置
　　2.fixed：完全脱离文档流，固定定位(以可视窗口为参照物)
　　3.relative:相对定位(参照的是自己本身的位置)，没有脱离文档流，没有顶上去，会保持自己的位置不动。可以使用top left进行定位
　　4.absolute:绝对定位：脱离了文档流（参照的是按已定位的父级标签定位，如果找不到会按body的去找）
注意！！：将定位标签设置为absolute，将他的父级标签设置为定位标签 （relative）

11.float和position的区别
　　float：半脱离文档流
　　position：全脱离文档流
12.z-index 属性设置元素的堆叠顺序。拥有更高堆叠顺序的元素总是会处于堆叠顺序较低的元素的前面。
13.透明度：opacity:0.4;
14.边框弧度：border-radius: 50%;#圆
15.去除列表前面的标志：list-style:none;
16.对齐上面和左边最顶部：padding:0; margin:0;
17.字体加粗样式： font-weight: 900; 
18.需要注意的几个逻辑表达式的问题，下面的这个和js的&&，||用法是一样的
　　print(3 and 5) #两个为真才为真
　　print(0 and 3) #0是假就不判断后面了，直接成假了
　　print(0 or 3) #有一个为真就为真
　　print(2 or 3) #2已经为真了那么就不会去判断后面了



3.JavaScript

JS三大部分：
			1. 基础语法
			2. 操作浏览器对象   BOM
			3. 操作文档上的标签 DOM
	
	3. JS导入方式
		1. 直接写在页面的Script标签内部
		2. 将JS代码写在单独的一个js文件然后通过页面上的script标签的src属性导入
	
	4. JS基础语法
		//   注释
		；	结束符
		1. 数据类型
			1. 数字（number）
				parseInt()
				parseFloat()
				NaN      --> Not a Number
			2. 字符串
				属性：
					length
				方法：
					
			3. 布尔值
			4. null	（类型为object）
			5. undefined
			6. 对象
				1. 数组（列表）
				2. 自定义对象（字典）
					
		2. 运算符
			注意强等于和弱等于的区别
			1. 算术运算符
			2. 赋值运算符
			3. 比较运算符
			4. 逻辑运算符
		3. 流程控制
			1. if else
			2. for 循环
			3. switch
			4. while


1. JS要学的内容
			1. JS基础语法
			2. BOM(操作浏览器)
			3. DOM(操作文档内容)
		2. JS导入方式
			1. 将JS代码直接写到script标签中
			2. 将JS代码写到js文件中，通过script的src属性导入
		3. JS的语法基础
			1. 注释  //
			2. 语句要加结束符;
			3. 变量声明  可用$
		4. JS中的数据类型
			1. 数字number
				NaN 
				parseInt()
				parseFloat()
				
			2. 字符串string
				1. .length
				2. .trim()
				3. .slice()
				4. ...
			3. 布尔值boolean
				0、null、""、undefined、NaN 都是假
			4. undefined
				1. 变量光声明没有赋值 var a;
				2. 函数没有返回值默认返回undefined
			5. object
				null      --> 手动清空一个变量
				数组Array
					数组常用方法
					sort排序
					遍历一个数组 --> 使用for循环根据索引迭代
				
			6. 类型查询
				typeof 
		5. 运算符
			1. 算术运算符
				++和--
			2. 比较运算符
				=== 强等于
			3. 逻辑运算符
				&&  ||  !
			4. 赋值运算符
				= += -= *= /=				
		6. 	流程控制语句
			1. if ... else ...
			2. if ... else if .... else ...
			3. switch (变量)
				case "a"：
				...
				break;
				default:
				...
			4. for循环
				for (var i=0;i<10;i++){...}
				for (;;){...}
			5. while循环
				while (条件){...}


1. JS中的函数
		1. 函数的三种形式
			1. 普通函数
			2. 匿名函数
			3. 自执行函数
		2. 函数的注意事项
			1. 参数
			2. 返回值
			3. 变量作用域
			4. 词法分析
	2. 内置对象和方法
		1. 日期对象
			new Date()
			注意：
				getMonth()返回数据的取值范围是 0~11
		2. JSON对象
			JSON.parse
			JSON.stringify
		3. RegExp对象
			1. 两种方式
				1. new RegExp('^1[3-9][0-9]{9}$')
				2. /^1[3-9][0-9]{9}$/
			2. 三个注意事项：
				1. test()不传值相当于传了一个undefined，undefined会被当成"undefined"来处理
				2. 增则表达式中间不要加空格
				3. 注意全局匹配模式g的lastIndex属性
		4. Math对象




1. BOM
			1. location  --> 浏览器URL相关
				1. location.href            --> 获取当前访问的URL
				2. location.href="新URl"    --> JS控制页面跳转到指定的URL
				3. location.reload()        --> 重新加载当前页面
			2. 其他的了解即可
			3. 弹出框系列
				1. alert()  ***
				2. confirm()
				3. prompt() 
			4. 计时器
				1. 一段时间之后做某件事
					- setTimeout(函数, 毫秒数)
					- clearTimeout(计时器的id)
				2. 每隔一段时间做某件事
					- setInterval(函数, 毫秒数)
					- clearInterval(计时器的id)
		2. DOM
			1. DOM树的概念 --> JS通过DOM就可以操作页面上的标签和属性
			2. 查找标签
				1. 直接查找
					1. document.getElementById("id值")             --> 找到具体的标签对象
					2. document.getElementsByClassName("样式类名") --> 找到标签对象的数组
					3. document.getElementsByTagName("标签名")     --> 找到标签对象的数组
					
				2. 间接查找
					1. parentElement
					2. children
					3. firstElementChild
					4. lastElementChild
					5. nextElementSibling
					6. previousElementSibling
			3. 标签操作
				1. 创建标签
					1. document.createElement("标签名")   *****
				2. 给标签添加内容
					1. .innerText
					2. .innerHTML="<a href="">a标签</a>"
				3. 把创建的标签对象添加到文档树中
					1. 父标签.appendChild(新标签)
					2. 父标签.insertBefore(新标签，子标签)
				4. 删除标签
					1. 父标签.removeChild(要删除的子标签)
				5. 替换
					1. 父标签.replaceChild(新标签，旧标签)
			4. 属性操作
				1. getAttribute()
				2. setAttribute()
				3. removeAttribute()
			5. 获取值（input/select/textarea）
				1. .value
				2. .value="要设置的值"
			6. 操作样式
				1. 操作class
					1. className     --> 字符串格式的样式类
					2. classList     --> 数组格式的样式类
					3. classList.remove()
					4. classList.add()
					5. classList.contains()
					6. classList.toggle()
				2. 直接操作CSS样式
					font-size
					标签对象.style.fontSize="18px"
			7. 事件
				1. 常用事件
					onlick
					onfocus
					onblur
					onbchange
				2. 事件的绑定方式
					1. 直接在标签里写obclick="函数名()"
					2. 通过JS找到标签给它绑定事件
						标签对象.onclick=function(){
						 ...
						}
			

2.内容
	1. 页面的标签加载完之后执行
		window.onload=function(){...}
	2. 通常会把给标签绑定事件的JS代码都放在body标签的最后面
	
	3. 计时器的大练习
	
	4. jQuery:https://www.cnblogs.com/liwenzhou/p/8178806.html
		1. jQuery是什么？
		
		2. jQuery的使用
			1. 下载jQuery
				jQuery的版本
					1.x  √
					2.x
					3.x  √
			2. 导入jQuery(先导入后使用！！！)
				一个页面只需要导入一次就可以了！！！
			3. 使用
				1. 基础语法：
					jQuery
					$   一般用这个     --> import gevent as g		
					
		3. 	查找标签
			1. 选择器
				1. 基本选择器
					1. $("#id值")
					2. $("标签名")
					3. $(".class名")
					4. $("*")
					5. $("div.c1")
					6. $("div,.c1")
				2. 层级选择器
					1. $("div .c1")     --> div下面子子孙孙中的有c1样式类的标签
					2. $("div>.c1")     --> div下面儿子中的有c1样式类的标签
					3. $("label+input") --> 找到紧挨着label标签下面的input标签
					4. $("div~p")       --> 找到div同级下面的所有的p标签
				3. 属性选择器
					1. $("[s14]")
					2. $("[type='submit']")
					3. $("[type!='submit']")
				4. 基本筛选器
					1. $("div:first")/$("div:last")
					2. $("div:eq(3)")/$("div:gt(3)")/$("div:lt(3)")
					3. $("div:even")/$("div:odd")
					4. $("div:not(.c1)")   --> 找到没有c1样式类的div标签
					5. $("div:has(.c1)")   --> 找到内部有c1样式类的div标签
				5. 表单筛选器
					1. $(":text")/$(":password") ...
					2. $("input:checked")
					3. $(":selected")
			
			2. 筛选器
				1. 上一个
				2. 下一个
				3. 祖先标签
				4. 儿子和兄弟
				4. 查找
				5. 筛选
			
			3. 操作class
				1. addClass()
				2. removeClass()
				3. hasClass()
				4. toggleClass()


jQuery
		1. jQuery是什么？
			一个js插件， 相比较原生的DOM操作更简单、开发效率更高
		2. jQuery使用
			1. jQuery版本
				1. 版本号 1.x/2.x/3.x
					1.x 兼容IE6/7/8
				2. jquery.min.js和query.js的区别
			2. jQuery的导入
				1. 先导入后使用
				2. 导入方式：
					1. 自己下载到本地使用
					2. 使用CDN方式
			3. jQuery的调用
				1. $
				2. jQuery
			4. jQuery对象和DOM对象
				1. 注意事项
					jQuery对象才能调用jQuery的方法，DOM对象只能调用DOM方法
				2. 互相转换
					1. jQuery对象 --> DOM对象
						$("div")  --> $("div")[0]
					2. DOM对象    --> jQuery对象
						this      --> $(this)	
			5. jQuery语法
				$("选择器").方法()
				支持链式操作
			6. jQuery选择器
				1. 基本选择器
					1. $("div")
					2. $("#d1")
					3. $(".c1")
					4. $("*")
				2. 组合选择器
					1. $("div, .c1")      --> 找到所有div标签和有c1样式类的标签
				3. 层级选择器
					1. $("#d1 span")      --> id是d1标签下面所有的span标签
					2. $("#d1>span")      --> id是d1标签下面一层的span标签
					3. $("label+input")   --> 找到紧挨着label标签的input标签
					4. $(".c1~div")       --> 找到c1样式类下面的div标签
				4. 基本筛选器
					1. :first/:last
					2. :eq()/:gt()/:lt()
					3. :even/:odd
					4. $("div:not(.c1)")  --> 找到没有c1样式类的div标签
					5. $("div:has(.c1)")  --> 找到后代中有c1样式类的div标签
				5. 属性选择器
					1. $("[s14]")
					2. $("[type='text']")
					3. $("[type!='text']")
				6. 表单筛选器
					1. $(":text")
					2. $(":password")
					3. ...
					4. $(":disabled")
					5. $("input:checked")
					6. $(":selected")
				7. 筛选器方法
					1. .next()/.prev()
					2. .parent()/.children()/.siblings()
					3. .find('选择器条件')      --> 在后代查找符合要求的
					4. .filter('选择器条件')    --> 根据条件对已经找到的结果进行二次过滤
					5. .first()/.last()
					6. .not()/.has()
					7. .eq()
			7. jQuery操作样式
				1. 操作class
					1. .addClass()
					2. .removeClass()
					3. .hasClass()
					4. .toggleClass()
				2. 操作样式
					1. 操作class
					2. 操作CSS
						$("").css("color")            --> 获取选中标签的颜色值
						$("").css("color", "yellow")  --> 设置选中标签的颜色值
			3. 位置操作
				1. position()          --> 获取相对定位过的祖先元素的偏移
				2. offset()            --> 获取相对当前窗口的偏移
				3. scrollTop()         --> 相对顶部的偏移
				4. scrollLeft()        --> 相对左侧的偏移
				返回顶部示例！
			4. 尺寸操作
				1. height/width              元素
				2. innerHeight/innerWidth    元素 + 内填充
				3. outerHeight/outerWidth    元素 + 内填充 + 边框
			5. 文本操作
				1. text()
				2. html()
			6. 求值（input/select/textarea）
				1. .val()
				2. .val("新值")
				3. .val(["1", "2"])
			7. 属性操作
				1. attr
				2. prop
			1. val()取值和设置值
			2. attr()和prop()的区别
				博客上
			
2. 今日内容
	1. 操作样式之直接操作CSS
		.css("color")         --> 获取值
		.css("color", "red")  --> 设置值、
	2. 位置
		position()
		offset()
		scrollTop()
		scrollLeft()
	3. 尺寸
		height()
		width()
		innerHeight()
		innerWidth()
		outerHeight()
		outerWidth()
	2. 求值
		text()
		html()
		val()
	3. 属性
		attr()
		prop()
	


1. 文档操作
		创建标签用：document.createElement("div")
		
		1. 内部添加
			1. 前面加
				1. $(A).prepend(B)
				2. $(A).prependTo(B)
			2. 后面加
				1. $(A).append(B)
				2. $(B).appendTo(A)
		2. 外部添加
			1. 前面加
				1. $(A).before(B)
				2. $(B).insertBefore(A)
			2. 后面加
				1. $(A).after(B)
				2. $(B).insertAfter(A)
		
		3. 移除和清空
			1. remove()   --> 把选中过的标签从文档树中移除
			2. empty()    --> 把选中的标签内部的元素都移除
		4. 替换
			1. $(A).replaceWith(B)
			2. $(B).replaceAll(A)
		5. clone
			clone()/clone(true)
			注意参数true,加上true会把标签绑定的事件也复制
			
	2. 事件
		1. jQuery绑定事件的方式
			1. 给标签绑定事件的方式
				1. 在标签上写 onclick=函数();
				2. 在js代码中 标签对象.onclick = function(){}
			2. jQuery绑定事件
				1. $("选择器").click(function(){...});
				2. $("").on("click", "子选择器", function(){...})--> 事件委托--> 原理是事件冒泡
			3. 事件委托
				原理：事件冒泡
					1. 如何阻止事件冒泡（向上传递）
						e.stopPropagation()
				目的：解决未来的标签如何绑定事件！
				语法：
					$("祖先标签").on("click", "选择器", function(){...})

 今日内容
	jQuery中文文档：http://jquery.cuishifeng.cn/

	1. 阻止事件冒泡
		event.stopPropagation()
	2. 阻止默认事件的执行（通常用于阻止form表单的提交）
		event.preventDefault()
	3. 阻止后续事件的执行
		return false
	4. jQuery内置动画
		写个例子，看一下效果。有个印象就好
	5. 补充
		1. each
			1. $.each(要遍历的对象, function(){...})
			2. $("").each(function(){
			  // this 是进入循环体的当前标签
			  console.log(this);
			})
			3. 退出本层循环
				return
			4. 退出each循环
				return false
		2. .data()
			1. .data(key, value) --> 存值
			2. .data(key)        --> 根据key取值
			3. .data()           --> 取所有键值对
			4. .removeData(key)  --> 根据key删除值
			5. .removeData()     --> 删除所有键值对
		3. 扩展
			1. $.extend()        --> 给jQuery扩展自定义方法
			2. $.fn.extend()     --> 给jQuery对象扩展自定义方法
	
	6. 以后页面的开发
		1. DOM里只需记忆document.createElement()
		2. 主要使用jQuery操作


今日内容
	1. 页面加载完之后才执行的JS代码
		1. DOM方式
			window.onload = function(){}
		2. jQuery方式
			$(document).ready(function(){...})	
	2. Bootstrap
		1. Bootstrap是什么？
			twitter公司开源的一个前端开发框架。（一坨HTML、CSS和JS的代码）
		2. Bootstrap的版本
			3.3.版本
		3. Bootstrap的使用
			1. 下载
				https://v3.bootcss.com/
				
			2. 导入
				link标签导入 bootstrap.css或者bootstrap.min.css
		4. 常用样式类
			1. 容器
				1. container
				2. container-fluid
			2. 栅格系统
				把一行均分成最多12列
				可以设置标签占多少列
				
				1. row表示一行
				2. col-xx-**表示一列
					xx: 表示样式适用的屏幕尺寸
						- xs  手机
						- sm  平板
						- md  桌面显示器
						- lg  超大屏幕
					**：表示占多少份
						- 取值范围： 1~12
				3. col-xx-offset-**:
					表示左侧空几份！
				4. 列支持再嵌套（再写一行，分成12份）
				5. 列排序
					1. col-xx-push-*  --> 往右推
					2. col-xx-pull-*  --> 往左拉
			3. 布局样式
			4. 表格
			5. 表单
			6. 按钮
			7. 图片
			8. 辅助类
				1. 文本颜色
				2. 背景颜色
				3. 快速浮动
				4. 清除浮动






1. Bootstrap
		1. 图标
			1. Bootstrap内置的： https://v3.bootcss.com/components/
			2. font-awesome图标：http://www.fontawesome.com.cn/
			3. 阿里图标：        http://iconfont.cn/
		2. 面板
		3. ...
		4. jS插件
			1. 模态框
			2. 轮播图

	2. 插件
		弹出插件SweetAlert：http://mishengqiang.com/sweetalert/
