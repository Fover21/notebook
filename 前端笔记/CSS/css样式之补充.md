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