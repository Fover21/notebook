================JQuery===========

JQuery
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
			   1）选择器
				1. 基本选择器
					1. $("div")
					2. $("#d1")
					3. $(".c1")
					4. $("*")
				2. 组合选择器
					1. $("div, .c1")      --> 找到所有div标签和有c1样式类的标签
				3. 层级选择器
					1. $("#d1 span")      --> id是d1标签下面所有的span标签（子子孙孙）
					2. $("#d1>span")      --> id是d1标签下面一层的span标签（子代儿子）
					3. $("label+input")   --> 找到紧挨着label标签的input标签（紧挨着的兄弟）
					4. $(".c1~div")       --> 找到c1样式类下面的div标签（不挨着也行的兄弟）
				4. 属性选择器
					1. $("[s14]")
					2. $("[type='text']")
					3. $("[type!='text']")
					4.$(“[type!='text’][id=‘name’]”)(通过双重属性来筛选)
			   2）筛选器
				5. 基本筛选器
					1. :first/:last（拿到一堆中的第一个/最后一个）
					2. :eq()/:gt()/:lt()（根据一堆中的索引筛选）
					3. :even/:odd（根据索引的奇偶筛选）
					4. $("div:not(.c1)")  --> 找到没有c1样式类的div标签
					5. $("div:has(.c1)")  --> 找到后代中有c1样式类的div标签
				6. 表单筛选器
					1. $(":text")
					2. $(":password")
					3. ...
					4. $(":disabled")
					5. $("input:checked")
					6. $(":selected")
				7. 筛选器方法
					1. .next()/.prev()/nextAll()/nextUntil()/prevAll()/prevUntil()
					2. 
						.parent() (一直向外找)    
						.children()（找儿子这层）
						.siblings()（所有兄弟上下都找，不包括自己）
					3. .find('选择器条件')      --> 在后代查找符合要求的（子子孙孙）
					4. .filter('选择器条件')    --> 根据条件对已经找到的结果进行二次过滤
					5. .first()/.last() 		—>一堆中找复合条件的（和基本筛选器一样）
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
					5.HTML代码/文本/值
        					没有参数就是获取对应的值，
        					有参数就设置对应的值
       					 - .html()  添加html标签    .html("<span>啦啦啦。</span>")
       					 - .text()  添加文本        .text("啦啦啦。")
        					 - .val()
           						input :一个参数,获取的是input框里面的值
            						checkbox :一个参数，获取的是value的值
            						select :
                						单选：获取值
                						多选：得到的是一个数组，设置的时候也要是数组

				6. 属性操作
					1. attr	(属性,可以设置值)
					2.removeAttr
					3. prop	（属性，true/false）
					4.removeProp
8. 文档操作
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
						常用事件
   							blur([[data],fn])   失去焦点
   							focus([[data],fn])  获取焦点（ 搜索框例子）
   							change([[data],fn]) 当select下拉框中的元素发生改变的时候触发change事件(select例子)
   							click([[data],fn])  点击
   							dblclick([[data],fn]) 双击
   							scroll([[data],fn])   滚动
   							submit([[data],fn])   提交
			3. 事件委托
				原理：事件冒泡
					1. 如何阻止事件冒泡（向上传递）
						e.stopPropagation()
				目的：解决未来的标签如何绑定事件！
				语法：
					$("祖先标签").on("click", "选择器", function(){...})

					注：
						1. 阻止事件冒泡
							event.stopPropagation()
						2. 阻止默认事件的执行（通常用于阻止form表单的提交）
							event.preventDefault()
						3. 阻止后续事件的执行
							return false
9.动画效果
	基本（隐藏）
   		show([s,[e],[fn]])
   		hide([s,[e],[fn]])
   		toggle([s],[e],[fn])
	滑动
   		slideDown([s],[e],[fn])
   		slideUp([s,[e],[fn]])
   		slideToggle([s],[e],[fn])
	淡入淡出
   		fadeIn([s],[e],[fn])
   		fadeOut([s],[e],[fn])

   		fadeTo([[s],o,[e],[fn]])
      			- 淡出到0.66透明度
   		fadeToggle([s,[e],[fn]])
      			- .fadeToggle(3000, function () {
            			alert("真没用3");
        		});
自定义
animate(p,[s],[e],[fn])1.8*
   - css属性值都可以设置
    - 图片变小（漏气）


10.补充
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
用法1、$.xxx()
   $.extend({
      "GDP": function () {
         console.log("戴小红花");
      }
   });
   - 给jQuery添加扩展
   - $.GDP()

用法2、$("").xxx()
   $.fn.extend({
      "BJG": function () {
         console.log("英语八级就是好！");
      }
   })
   - 给jQuery对象添加扩展
   - $(":input").BJG()

总结：

1. 页面加载完之后才执行的JS代码
		1. DOM方式
			window.onload = function(){}
		2. jQuery方式
			$(document).ready(function(){...})	

2.Bootstrap的使用
			1. 下载
				https://v3.bootcss.com/
				
			2. 导入
				link标签导入 bootstrap.css或者bootstrap.min.css
			3. 图标
				1. Bootstrap内置的： https://v3.bootcss.com/components/
				2. font-awesome图标：http://www.fontawesome.com.cn/
				3. 阿里图标：        http://iconfont.cn/
			4. 面板
			5. ...
			4. jS插件
				1. 模态框
				2. 轮播图

3. 插件
		弹出插件SweetAlert：http://mishengqiang.com/sweetalert/

