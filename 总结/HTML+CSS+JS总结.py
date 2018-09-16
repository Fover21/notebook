==================HTML（超文本标记语言）==========


<!DOCTYPE> 声明位于文档中的最前面的位置，处于 <html> 标签之前。此标签可告知浏览器文档使用哪种 HTML 或 XHTML 规范。

HTML标签的结构		
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
				
				注意：
					form表单功能：表单用于向服务器传输数据，从而实现用户与web服务器的交互。
								表单能够包含input系列标签，比如文本字段、复选框、单选框、提交按钮等等。
      						   表单还可以包含textarea、select、fieldset和 label标签。
					表单属性：
							action: 表单提交到哪.一般指向服务器端一个程序,程序接收到表单提交过来的数据（即表单元素值）作相应处理
     					     method: 表单的提交方式 post/get默认取值就是get

================CSS（层叠样式表）==============

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

			2. 属性选择器
				1. div[s14]              找到有s14这个属性的div标签
				2. input[type='email']   找到type是email的input标签

			3 分组和嵌套
				div,  p {}   （找到div和p）
				div .c1 {}	（找到div下的类名为c1的）

			4. 组合选择器
				1. div p    后代选择器（子子孙孙）
				2. div>p    儿子选择器（子代中只找儿子）
				3. div+p    毗邻选择器（紧挨着的兄弟，往后找）
				4. div~p    弟弟选择器 （不挨着只要是弟弟就行，往后找）

			5. 伪类选择器
				1. :hover     --> 鼠标移动到标签上时应用的样式
				2. :focus     --> input标签获取焦点时应用的样式
				
				了解：
		a:link（没有接触过的链接）,用于定义了链接的常规状态。

        a:hover（鼠标放在链接上的状态）,用于产生视觉效果。
        
        a:visited（访问过的链接）,用于阅读文章，能清楚的判断已经访问过的链接。
        
        a:active（在链接上按下鼠标时的状态）,用于表现鼠标按下时的链接状态。
        
        伪类选择器 : 伪类指的是标签的不同状态:
        
                   a ==> 点过状态 没有点过的状态 鼠标悬浮状态 激活状态
        
        a:link {color: #FF0000} /* 未访问的链接 */
        
        a:visited {color: #00FF00} /* 已访问的链接 */
        
        a:hover {color: #FF00FF} /* 鼠标移动到链接上 */
        
        a:active {color: #0000FF} /* 选定的链接 */ 格式: 标签:伪类名称{ css代码; }
			
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

2.css的优先级
所谓CSS优先级，即是指CSS样式在浏览器中被解析的先后顺序。
样式表中的特殊性描述了不同规则的相对权重，它的基本规则是：

1 内联样式表的权值最高               style=""－－－－－－－－－－－－1000；
2 统计选择符中的ID属性个数。       #id －－－－－－－－－－－－－－100
3 统计选择符中的CLASS属性个数。 .class －－－－－－－－－－－－－10
4 统计选择符中的HTML标签名个数。 p －－－－－－－－－－－－－-－1

			1. 样式名一样的话
				类似 变量覆盖 最后加载的那个样式生效
			2. 样式名不一样
				根据 权重计算
				内联样式(1000)>ID选择器(100)>类选择器(10)>元素选择器(1)>继承(0)
			3. 不讲道理的
				!important

3.CSS常用属性
		    1. 文字属性相关
				1. font-family: "字体1", "字体2", 
				1.5 font-heighe: xxpx; 字体行高
				2. font-size        字体大小
				3. font-weight		字体粗细
				4. color            字体颜色
					1. 英文的颜色名    red
					2. 16进制颜色代码  #FF0000
					3. RGB             rgb(255, 0, 0)
					4. rgba(255, 0, 0, 0.4)
				5.水平对齐方式
					text-align 属性规定元素中的文本的水平对齐方式。
						left      把文本排列到左边。默认值：由浏览器决定。
						right    把文本排列到右边。
						center 把文本排列到中间。
						justify 实现两端对齐文本效果
			2. 宽和高
				1. width             宽
				2. height			 高
					只有块儿级标签设置宽和高才有效
			3. 背景
				background（可简写）
				
				background-color: red
				background-image: url(...)
				background-repeat: no-repeat;(不平铺) repeat(平铺)
				background-position: right left top bottpm (图片位置)
			4. 文本样式
				1. 水平居中
					text-align: center
				2. 单行文本的垂直居中
					line-height=父标签的高度
				3. 文本装饰线
					text-decoration: none/under-line/over-line/line-through
			5. CSS盒子模型
				内容-->padding-->border-->margin
					◦	margin:            用于控制元素与元素之间的距离；margin的最基本用途就是控制元素周围空间的间隔，从视觉角度上达到相互隔开的目的。
					◦	padding:           用于控制内容与边框之间的距离；   
					◦	Border(边框):     围绕在内边距和内容外的边框。
					◦	Content(内容):   盒子的内容，显示文本和图像。
				
				补充：
margin:10px 20px 20px 10px；

        上边距为10px
        右边距为20px
        下边距为20px
        左边距为10px

margin:10px 20px 10px;

        上边距为10px
        左右边距为20px
        下边距为10px

margin:10px 20px;

        上下边距为10px
        左右边距为20px

margin:25px;

        所有的4个边距都是25px
					
			6. 浮动
				float: left/right
				浮动的副作用
				清除浮动
				clear语法：
　　					clear：none |  left  | right  | both
					1.clear：left 清除的是左边的浮动
					2.clear：both :保证左右两边都没有浮动
				注意：
　　					排序的时候是一个标签一个标签的排
　　					如果上一个是浮动的，就紧贴个上一个
　　					如果上一个不是浮动的，就和上一个保持垂直不变
			7. 定位
				1. 相对定位     --> 相对自己原来在的位置做定位
				2. 绝对定位     --> 相对自己已经定位过的祖先标签
				3. 固定定位     --> 相对于屏幕做定位
			position的四种属性
			1.static：默认位置
			2.fixed：完全脱离文档流，固定定位(以可视窗口为参照物)
			3.relative:相对定位(参照的是自己本身的位置)，没有脱离文档流，没有顶上去，会保持自己的位置不动。可以使用top             left  进行定位
			4.absolute:绝对定位：脱离了文档流（参照的是按已定位的父级标签定位，如果找不到会按body的去找）

			注意：将定位标签设置为absolute，将他的父级标签设置为定位标签 （relative）	
			float：半脱离文档流 position：全脱离文档流		

			8. 溢出
				overflow: hidden/scroll/auto
				解决溢出的方法
        			overflow:auto;
　　　　 			overflow: hidden;
  			     overflow:scoll; #加上滚动条
			9. 边框
				border: 1px solid red;
				border-radius: 50%
			10. display
				1. block
				2. inline
				3. inline-block
				4. none
					display属性
					1.将块级标签设置成内联标签：disply：inline;
					2.将内联标签设置成块级标签：disply：block;
					3.内联块级标签：像块级一样可设长宽，也可像内联一样在一行显示：display:inline-block;
					4.display:none; 吧不想让用户看到的给隐藏了（很重要的一个属性）
					5.visibility :hiddon； 也是隐藏
 
				注意与visibility:hidden的区别：
　　					visibility:hidden：可以隐藏某个元素，但隐藏的元素仍需占用与未隐藏之前一样的空间。也就是说，该元素虽然被                                    隐藏了，但仍然会影响布局。
　　					display:none：可以隐藏某个元素，且隐藏的元素不会占用任何空间。也就是说，该元素不但被隐藏了，而且该元                                  素原本占用的空间也会从页面布局中消失

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


==================JavaScript===========
1.大纲：1. JS基础语法   2. BOM(操作浏览器)   3. DOM(操作文档内容)

2.JS导入方式
		1. 直接写在页面的Script标签内部
		2. 将JS代码写在单独的一个js文件然后通过页面上的script标签的src属性导入
3.基础语法
	1.
		//注释
		；结束符
		$变量声明可用
	2.数据类型
		1.数字（Number）
			不区分整型数值和浮点型数值;
			parseInt()
			parseFloat()
			NaN      --> Not a Number
		2.字符串（string）
			是由Unicode字符、数字、标点符号组成的序列；
			字符串常量首尾由单引号或双引号括起；
			JavaScript中没有字符类型；常用特殊字符在字符串中的表达；
			字符串中部分特殊字符必须加上右划线\；
			常用的转义字符 \n:换行 \':单引号 \":双引号 \\:右划线
			
			字符串创建(两种方式)
       				① 变量 = “字符串”
       				② 字串串对象名称 = new String (字符串)
			属性：
				length
			方法：
 x.toLowerCase()        －－－－转为小写
 x.toUpperCase()        －－－－转为大写
 x.trim()               －－－－去除字符串两边空格       


－－－－字符串查询方法

x.charAt(index)         －－－－str1.charAt(index);－－－－获取指定位置字符，其中index为要获取的字符索引

x.indexOf(index)－－－－查询字符串位置
x.lastIndexOf(findstr)  

x.match(regexp)         －－－－match返回匹配字符串的数组，如果没有匹配则返回null
x.search(regexp)        －－－－search返回匹配字符串的首字符位置索引

                        示例：
                        var str1="welcome to the world of JS!";
                        var str2=str1.match("world");
                        var str3=str1.search("world");
                        alert(str2[0]);  // 结果为"world"
                        alert(str3);     // 结果为15
                        

－－－－子字符串处理方法

x.substr(start, length) －－－－start表示开始位置，length表示截取长度
x.substring(start, end) －－－－end是结束位置

x.slice(start, end)     －－－－切片操作字符串
                        示例：
                            var str1="abcdefgh";
                            var str2=str1.slice(2,4);
                            var str3=str1.slice(4);
                            var str4=str1.slice(2,-1);
                            var str5=str1.slice(-3,-1);

                            alert(str2); //结果为"cd"
                            
                            alert(str3); //结果为"efgh"
                            
                            alert(str4); //结果为"cdefg"
                            
                            alert(str5); //结果为"fg"

x.replace(findstr,tostr) －－－－    字符串替换

x.split();                 －－－－分割字符串
                                 var str1="一,二,三,四,五,六,日"; 
                                var strArray=str1.split(",");
                                alert(strArray[1]);//结果为"二"
                                
x.concat(addstr)         －－－－    拼接字符串
		3.布尔值（boolean）
			Boolean类型仅有两个值：true和false，也代表1和0，实际运算中true=1,false=0
			布尔值也可以看作on/off、yes/no、1/0对应true/false	
		4.undefined
		5.null
		6对象（数组，字典）
	3. 运算符
		注意强等于和弱等于的区别
		1. 算术运算符		++和--
		2. 赋值运算符	= += -= *= /=
		3. 比较运算符	=== 强等于
		4. 逻辑运算符	&&  ||  !
	4. 流程控制
		1. if else
		2. for 循环
		3. switch
		4. while/do…while
	5.异常处理
		try {
    			//这段代码从上往下运行，其中任何一个语句抛出异常该代码块就结束运行
		}
		catch (e) {
   			 // 如果try代码块中抛出了异常，catch代码块中的代码就会被执行。
   			 //e是一个局部变量，用来指向Error对象或者其他抛出的对象
		}
		finally {
     		//无论try中代码是否有异常抛出（甚至是try代码块中有return语句），finally代码块中始终会被执行。
		}
		注：主动抛出异常 throw Error('xxxx')

4.JS中的函数
		1. 函数的三种形式
			1. 普通函数
			2. 匿名函数
			3. 自执行函数
		2. 函数的注意事项
			1. 参数
			2. 返回值
			3. 变量作用域
			4. 词法分析
5.内置对象和方法
		1. 日期对象
			var now = new Date()
			注意：
				getMonth()返回数据的取值范围是 0~11
			获取日期和时间
				getDate()                 获取日
				getDay ()                 获取星期
				getMonth ()               获取月（0-11）
				getFullYear ()            获取完整年份
				getYear ()                获取年
				getHours ()               获取小时
				getMinutes ()             获取分钟
				getSeconds ()             获取秒
				getMilliseconds ()        获取毫秒
				getTime ()                返回累计毫秒数(从1970/1/1午夜)
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
				//该对象中的属性方法 和数学有关.
				abs(x)    返回数的绝对值。
				exp(x)    返回 e 的指数。
				floor(x)对数进行下舍入。
				log(x)    返回数的自然对数（底为e）。
				max(x,y)    返回 x 和 y 中的最高值。
				min(x,y)    返回 x 和 y 中的最低值。
				pow(x,y)    返回 x 的 y 次幂。
				random()    返回 0 ~ 1 之间的随机数。
				round(x)    把数四舍五入为最接近的整数。
				sin(x)    返回数的正弦。
				sqrt(x)    返回数的平方根。
				tan(x)    返回角的正切。
			5.数组对象
1========
2 //        数组对象的属性和方法
 3           var arr = [11,55,'hello',true,656];
 4 //      1.join方法
 5         var arr1 = arr.join('-'); //将数组元素拼接成字符串，内嵌到数组了，
 6         alert(arr1);                //而python中内嵌到字符串了
 7 //        2.concat方法(链接)
 8         var v = arr.concat(4,5);
 9         alert(v.toString())  //返回11,55,'hello',true,656,4,5
10 //        3.数组排序reserve  sort
11 //        reserve:倒置数组元素
12         var li = [1122,33,44,20,'aaa',2];
13         console.log(li,typeof (li));  //Array [ 1122, 33, 44, 55 ] object
14         console.log(li.toString(), typeof(li.toString())); //1122,33,44,55 string
15         alert(li.reverse());  //2,'aaa',55,44,33,1122
16 //         sort :排序数组元素
17         console.log(li.sort().toString()); //1122,2,20,33,44,aaa  是按照ascii码值排序的
18 //        如果就想按照数字比较呢?（就在定义一个函数）
19 //        方式一
20         function intsort(a,b) {
21             if (a>b){
22                 return 1;
23             }
24             else if (a<b){
25                 return -1;
26             }
27             else{
28                 return 0;
29             }
30         }
31         li.sort(intsort);
32         console.log(li.toString());//2,20,33,44,1122,aaa
33 
34 //        方式二
35         function Intsort(a,b) {
36             return a-b;
37         }
38         li.sort(intsort);
39         console.log(li.toString());
40         // 4.数组切片操作
41         //x.slice(start,end);
42         var arr1=['a','b','c','d','e','f','g','h'];
43         var arr2=arr1.slice(2,4);
44         var arr3=arr1.slice(4);
45         var arr4=arr1.slice(2,-1);
46         alert(arr2.toString());//结果为"c,d"
47         alert(arr3.toString());//结果为"e,f,g,h"
48         alert(arr4.toString());//结果为"c,d,e,f,g"
49 //        5.删除子数组
50         var a = [1,2,3,4,5,6,7,8];
51         a.splice(1,2);
52         console.log(a) ;//Array [ 1, 4, 5, 6, 7, 8 ]
53 //        6.数组的push和pop
54 //        push:是将值添加到数组的结尾
55         var b=[1,2,3];
56         b.push('a0','4');
57         console.log(b) ; //Array [ 1, 2, 3, "a0", "4" ]
58 
59 //        pop；是讲数组的最后一个元素删除
60         b.pop();
61         console.log(b) ;//Array [ 1, 2, 3, "a0" ]
62         //7.数组的shift和unshift
63         unshift: 将值插入到数组的开始
64         shift: 将数组的第一个元素删除
65         b.unshift(888,555,666);
66         console.log(b); //Array [ 888, 555, 666, 1, 2, 3, "a0" ]
67 
68         b.shift();
69         console.log(b); //Array [ 555, 666, 1, 2, 3, "a0" ]
70 //        8.总结js的数组特性
71 //        java中的数组特性：规定是什么类型的数组,就只能装什么类型.只有一种类型.
72 //        js中的数组特性
73 //            js中的数组特性1：js中的数组可以装任意类型,没有任何限制.
74 //            js中的数组特性2： js中的数组,长度是随着下标变化的.用到多长就有多长.
75     </script>

=================JavaScript BOM对象和DOM对象=======

1.BOM对象
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

2.DOM对象
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
