********Bootstrap框架********

****Bootstrap介绍****

Bootstrap是Twitter开源的基于HTML、CSS、JavaScript的前端框架。
它是为实现快速开发Web应用程序而设计的一套前端工具包。
它支持响应式布局，并且在V3版本之后坚持移动设备优先。

****为什么要使用Bootstrap？****

在Bootstrap出现之前：
命名：重复、复杂、无意义（想个名字费劲）
样式：重复、冗余、不规范、不和谐
页面：错乱、不规范、不和谐
在使用Bootstrap之后： 各种命名都统一并且规范化。 页面风格统一，画面和谐。

****Bootstrap下载****

官方地址：https://getbootstrap.com
中文地址：http://www.bootcss.com/

****Bootstrap环境搭建****

目录结构：

bootstrap-3.3.7-dist/
├── css  // CSS文件
│   ├── bootstrap-theme.css  // Bootstrap主题样式文件
│   ├── bootstrap-theme.css.map
│   ├── bootstrap-theme.min.css  // 主题相关样式压缩文件
│   ├── bootstrap-theme.min.css.map
│   ├── bootstrap.css
│   ├── bootstrap.css.map
│   ├── bootstrap.min.css  // 核心CSS样式压缩文件
│   └── bootstrap.min.css.map
├── fonts  // 字体文件
│   ├── glyphicons-halflings-regular.eot
│   ├── glyphicons-halflings-regular.svg
│   ├── glyphicons-halflings-regular.ttf
│   ├── glyphicons-halflings-regular.woff
│   └── glyphicons-halflings-regular.woff2
└── js  // JS文件
    ├── bootstrap.js
    ├── bootstrap.min.js  // 核心JS压缩文件
    └── npm.js

处理依赖
由于Bootstrap的某些组件依赖于jQuery，所以请确保下载对应版本的jQuery文件，来保证Bootstrap相关组件运行正常。


****Bootstrap全局样式****

排版、按钮、表格、表单、图片等我们常用的HTML元素，Bootstrap中都提供了全局样式。
我们只要在基本的HTML元素上通过设置class就能够应用上Bootstrap的样式，从而使我们的页面更美观和谐。

**标题相关**

*标题*

<h1>一级标题36px</h1>
<h2>二级标题30px</h2>
<h3>三级标题24px</h3>
<h4>四级标题18px</h4>
<h5>五级标题14px</h5>
<h6>六级标题12px</h6>
<!--除了使用h标签，Bootstrap内置了相应的全局样式-->
<!--内联标签应用标题样式-->
<span class="h1">一级标题36px</span>
<span class="h2">二级标题30px</span>
<span class="h3">三级标题24px</span>
<span class="h4">四级标题18px</span>
<span class="h5">五级标题14px</span>
<span class="h6">六级标题12px</span>

*副标题*

<!--一级标题中嵌入小标题-->
<h1>一级标题<small>小标题</small></h1>

**文本对齐**

<!--文本对齐-->
<p class="text-left">文本左对齐</p>
<p class="text-center">文本居中</p>
<p class="text-right">文本右对齐</p>

**文本大小写**

<!--大小写-->
<p class="text-lowercase">Lowercased text.</p>
<p class="text-uppercase">Uppercased text.</p>
<p class="text-capitalize">Capitalized text.</p>

**表格**

	Class			  描述
.table-striped		条纹状表格
.table-bordered		带边框的表格
.table-hover		鼠标悬停变色的表格
.table-condensed	紧缩型表格
.table-responsive	响应式表格

**状态类**

Class 			描述
.active		鼠标悬停在行或单元格上时所设置的颜色
.success	标识成功或积极的动作
.info		标识普通的提示信息或动作
.warning	标识警告或需要用户注意
.danger		标识危险或潜在的带来负面影响的动作

**表单**

内联表单
表单状态
带图标的表单

**按钮**

<a class="btn btn-default" href="#" role="button">Link</a>
<button class="btn btn-default" type="submit">Button</button>
<input class="btn btn-default" type="button" value="Input">
<input class="btn btn-default" type="submit" value="Submit">

*按钮样式*

<!-- Standard button -->
<button type="button" class="btn btn-default">（默认样式）Default</button>
<!-- Provides extra visual weight and identifies the primary action in a set of buttons -->
<button type="button" class="btn btn-primary">（首选项）Primary</button>
<!-- Indicates a successful or positive action -->
<button type="button" class="btn btn-success">（成功）Success</button>
<!-- Contextual button for informational alert messages -->
<button type="button" class="btn btn-info">（一般信息）Info</button>
<!-- Indicates caution should be taken with this action -->
<button type="button" class="btn btn-warning">（警告）Warning</button>
<!-- Indicates a dangerous or potentially negative action -->
<button type="button" class="btn btn-danger">（危险）Danger</button>
<!-- Deemphasize a button by making it look like a link while maintaining button behavior -->
<button type="button" class="btn btn-link">（链接）Link</button>

*按钮大小*

<p>
  <button type="button" class="btn btn-primary btn-lg">（大按钮）Large button</button>
  <button type="button" class="btn btn-default btn-lg">（大按钮）Large button</button>
</p>
<p>
  <button type="button" class="btn btn-primary">（默认尺寸）Default button</button>
  <button type="button" class="btn btn-default">（默认尺寸）Default button</button>
</p>
<p>
  <button type="button" class="btn btn-primary btn-sm">（小按钮）Small button</button>
  <button type="button" class="btn btn-default btn-sm">（小按钮）Small button</button>
</p>
<p>
  <button type="button" class="btn btn-primary btn-xs">（超小尺寸）Extra small button</button>
  <button type="button" class="btn btn-default btn-xs">（超小尺寸）Extra small button</button>
</p>

**图片**

<img src="..." class="img-responsive" alt="Responsive image">

*图片形状*

<img src="..." alt="..." class="img-rounded">
<img src="..." alt="..." class="img-circle">
<img src="..." alt="..." class="img-thumbnail">

**辅助类**

*文本颜色*

<p class="text-muted">...</p>
<p class="text-primary">...</p>
<p class="text-success">...</p>
<p class="text-info">...</p>
<p class="text-warning">...</p>
<p class="text-danger">...</p>

*背景颜色*

<p class="bg-primary">...</p>
<p class="bg-success">...</p>
<p class="bg-info">...</p>
<p class="bg-warning">...</p>
<p class="bg-danger">...</p>



*关闭按钮*

<button type="button" class="close" aria-label="Close"><span aria-hidden="true">&times;</span></button>

*下拉三角*

<span class="caret"></span>

*快速浮动*

<div class="pull-left">...</div>
<div class="pull-right">...</div>

*内容块居中*

<div class="center-block">...</div>

*清除浮动*

<!-- Usage as a class -->
<div class="clearfix">...</div>

*显示与隐藏*

<div class="show">...</div>
<div class="hidden">...</div>


*******常用Bootstrap组件*******

1.字体图标
2.下拉菜单
3.按钮组
4.输入框俎
5.导航
6.分页
7.标签和徽章
8.页头
9.缩率图
10.进度条

模拟滚动的进度条：
var $d1 = $("#d1");
var width = 0;
var theID = setInterval(setValue, 200);

function setValue() {
  if (width === 100) {
    clearInterval(theID);
  } else {
    width++;
    $d1.css("width", width+"%").text(width+"%");
  }
}


********响应式开发********

****为什么要进行响应式开发？****
随着移动设备的流行，网页设计必须要考虑到移动端的设计。同一个网站为了兼容PC端和移动端显示，就需要进行响应式开发。

****什么是响应式？****
利用媒体查询，让同一个网站兼容不同的终端（PC端、移动端）呈现不同的页面布局。

****用到的及时：****

CSS3@media查询
用于查询设备是否符合某一特定条件，这些特定条件包括屏幕尺寸、是否可触摸、屏幕精度、横屏竖屏等信息。

常见属性：

device-width, device-height 屏幕宽、高
width,height 渲染窗口宽、高
orientation 设备方向
resolution 设备分辨率
语法：

@media mediatype and|not|only (media feature) {
    CSS-Code;
}
不同的媒体使用不同的stylesheet

<link rel="stylesheet" media="mediatype and|not|only (media feature)" href="mystylesheet.css">
viewport

手机浏览器是把页面放在一个虚拟的"窗口"（viewport）中，通常这个虚拟的"窗口"（viewport）比屏幕宽，这样就不用
把每个网页挤到很小的窗口中（这样会破坏没有针对手机浏览器优化的网页的布局），用户可以通过平移和缩放来看网页的不
同部分。

设置viewport

一个常用的针对移动网页优化过的页面的 viewport meta 标签大致如下：

<meta name=”viewport” content=”width=device-width, initial-scale=1, maximum-scale=1″>
width：控制 viewport 的大小，可以指定的一个值，如果 600，或者特殊的值，如 device-width 为设备的宽度（单位为缩放为 100% 时的 CSS 的像素）。
height：和 width 相对应，指定高度。
initial-scale：初始缩放比例，也即是当页面第一次 load 的时候缩放比例。
maximum-scale：允许用户缩放到的最大比例。
minimum-scale：允许用户缩放到的最小比例。
user-scalable：用户是否可以手动缩放。
Bootstrap的栅格系统

container
row
column
注意事项： 使用Bootstrap的时候不要让自己的名字与Bootstrap的类名冲突。


********JavaScrip插件********

****常用的Bootstrap自带插件****

**模态框**

模态框的HTML代码放置的位置
务必将模态框的HTML代码放在文档的最高层级内（也就是说，尽量作为 body 标签的直接子元素），以避免其他组件影响模态框的展现和/或功能。

*HTML代码*

<!-- 触发模态框的按钮 -->
<button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">
  Launch demo modal
</button>

<!-- 模态框 -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="myModalLabel">Modal title</h4>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

注意事项：
1.通过为模态框设置 .bs-example-modal-lg和 .bs-example-modal-sm来控制模态框的大小。
2.通过 .fade类来控制模态框弹出时的动画效果（淡入淡出效果）。
3.通过在 .modal-bodydiv中设置 .row可以使用Bootstrap的栅格系统。

*调用方式*

1.通过data属性

通过在一个触发弹出模态框的元素（例如：按钮）上添加 data-toggle="modal"属性，然后设置 data-target="#foo"属性或 href="#foo"属性，用来指向被控制的模态框。

<button type="button" data-toggle="modal" data-target="#myModal">显示模态框</button>

2.通过JS代码调用

$('#myModal').modal("show");  // 显示
$('#myModal').modal("hide")   // 隐藏

常用参数：

名称				可选值			默认值				描述
backdrop	true/false/'static'	true	false表示有没有遮罩层，'static'表示点击遮罩层不关闭模态框
keyboard	true/false			true	键盘上的 esc 键被按下时关闭模态框。
show		true/false			true	模态框初始化之后就立即显示出来。

方法：
$('#myModal').modal({
  keyboard: false
})

**轮播图**

*HTML代码*
<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
    <li data-target="#carousel-example-generic" data-slide-to="1"></li>
    <li data-target="#carousel-example-generic" data-slide-to="2"></li>
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner" role="listbox">
    <div class="item active">
      <img src="..." alt="...">
      <div class="carousel-caption">
        ...
      </div>
    </div>
    <div class="item">
      <img src="..." alt="...">
      <div class="carousel-caption">
        ...
      </div>
    </div>
    ...
  </div>

  <!-- Controls -->
  <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>

可以再为图片添加介绍信息

<div class="item">
  <img src="..." alt="...">
  <div class="carousel-caption">
    <h3>...</h3>
    <p>...</p>
  </div>
</div>

方法：

设置切换间隔为2秒，默认是5秒。

$('.carousel').carousel({
  interval: 2000
})

****其他常用插件****

待续。。。

********Bootstrap实例精选：********

1.封面图
2.Carousel
3.博客页面
4.控制台
5.登录页
6.Offcanvas
