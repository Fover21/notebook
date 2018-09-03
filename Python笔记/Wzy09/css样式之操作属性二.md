********css样式之属性操作********

一、文本属性

1.text-align:cnter 			文本居中
2.line heigth 				垂直居中 ：行高，和高度对应
3.vertical-align    		设置图片与文本的距离
4.text-decoration:none 		去掉超链接下划线
5.要是给a标签修改颜色的时候，就定到a标签上，用继承有时候是搞不定的
因为继承的级别是很低的，如果a标签设置了样式，是不会继承父亲的
6.text-indent:30px			首行缩进
7.font-style:oblique 或者italic....(设置字体的样式为斜体)


二、背景属性

background-color:背景颜色
background-image:url('11.jpg'); 背景图片链接
background-repeat:repeat-x; x轴平铺
background-repeat:no-repeat; 不重复
background-position:400px 200px 调整背景的位置（距左。距右）
background-position: center:center; 背景居中

简写：
background: url('11.jpg') no-repeat center;

三、边框属性

常用属性

简写：border :1px soild red;
deshed:虚线
只加有一个方向的：border-right :1px soild red;

四、列表属性

去掉列表前面的标志：ul li{list-style:none;}
去掉列表前面的空格：ul{padding:0}

上面两行也可写成下面一行
去掉盒子上面的间隙：\*{margin:0; padding :0;}


五、display属性

display属性

1.将块级标签设置 成内联标签：display： inline；
2.将内联标签设置 成块级标签：display： block；
3.内联块级标签：像块级标一样可设长宽，也可像内联一样在一行显示：display：inline-block
4.display：none；把不想让用户看到的给隐藏了（很重要的一个属性）
5.visibility：hidden；也是隐藏

注意：与visibility：hidden的区别
visibility:hidden：可以隐藏某个元素，但隐藏的元素仍需占用与未隐藏之前一样的空间。也就是说，该元素虽然被隐藏了，但仍然会影响布局。

display:none：可以隐藏某个元素，且隐藏的元素不会占用任何空间。也就是说，该元素不但被隐藏了，而且该元素原本占用的空间也会从页面布局中消失


六、边距的塌陷问题

1.兄弟div
上面的div的margin-bottom和下面的div的margin-top会塌陷，也就是会取上下两者margin里面最大值作为显示值。

2.父子div
如果父级div没有border，padding，inlinecontent，子级div的margin会一直向上找，直到找到某个标签包括border，padding，inline content中的其中一个，然后按此div 进行margin；

![](https://images2017.cnblogs.com/blog/1184802/201709/1184802-20170921170416900-1754321835.png)


解决方法：

这两种会改变结构：
1.加上padding
2.加入border
不改变结构
3.overflow:hidden


溢出问题

解决溢出的方法
        overflow:auto;
　　　　 overflow: hidden;
        overflow:scoll; #加上滚动条


七、清除浮动

clear语法：
　　clear：none |  left  | right  | both
1.clear：left 清除的是左边的浮动
2.clear：both :保证左右两边都没有浮动

注意：
　　排序的时候是一个标签一个标签的排
　　如果上一个是浮动的，就紧贴个上一个
　　如果上一个不是浮动的，就和上一个保持垂直不变


八、float父级的塌陷问题
loat它不是完全脱离，它是半脱离的。像是文字环绕的就是用float实现的。float是不覆盖文字的
半脱离的，吧文字给挤过去了。

解决方案：
1.<div style='clear：both'></div>
    也可以不加div
    2.用after 
    .header:after{
        content:""; #内容为空
        display:block; #块级标签
        clear:both; #清楚浮动的功能
    }
    
    约定的名字：clearfix
    .clearfix:after{
        content:""; #内容为空
        display:block; #块级标签
        clear:both; #清楚浮动的功能（可以做到一个自动切换的功能）
    }



九、position(定位)属性

position的四种属性
1.static：默认位置
2.fixed：完全脱离文档流，固定定位(以可视窗口为参照物)
3.relative:相对定位(参照的是自己本身的位置)没有脱离文档流，没有顶上去，会保持自己的位置不动。可以使用top   left  进行定位
4.absolute:绝对定位：脱离了文档流（参照的是按已定位的父级标签定位，如果找不到会按body的去找）

注意：将定位标签设置为absolute，将他的父级标签设置为定位标签 （relative）



十、float和position的区别

float：半脱离文档流
position：全脱离文档流















