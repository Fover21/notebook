********JQuery文档操作********

1、CSS
    .css()
      - .css("color")  -> 获取color css值
      - .css("color", "#ff0000") -> 设置值
      - .css({"color": "#cccccc", "border": "1px solid #ff0000"})  -> 设置多个值
      - .css(["color", "border"])  -> 获取多个值
   .offset
       - 获取相对位置
       - 比较的对象是html (窗口)
   .position
        - 获取相对已经定位的父标签的位置
        - 比较的是最近的那个做过定位的祖先标签
   .scrollTop([val])
      - 返回顶部的例子
   .scrollLeft([val])
   尺寸：
    height([val|fn])
      - 元素的高度
   width([val|fn])
       - 元素的宽度
   innerHeight()
      - 带padding的高度
   innerWidth()
       - 带padding的宽度
   outerHeight([soptions])
      - 在innerHeight的基础上再加border的高度
   outerWidth([options])
       - 在innerHeight的基础上再加border的高度

2、文档操作
内部插入
    A.append(B)       吧B添加到A的后面
    A.appendTo(B)     吧A添加到B的后面
    A.prepend(B)      吧B添加到A的前面
    A.prependTo(B)    吧A添加到B的前面
外部插入
    A.after(B)        吧B添加到A的后面
    A.insertAfter(B)  吧A添加到B的后面
    A.before(B)       吧B添加到A的前面
    A.insertBefore(B) 吧A添加到B的前面

    包裹
    wrap(html|ele|fn)
      A.wrap(B)  --> B包A
   unwrap()   不抱
      - 不要加参数

   wrapAll(html|ele)  都包(作为整体包)，只包你选中的那个
   wrapInner(html|ele|fn)  里面包
    替换
    replaceWith(content|fn)
      A.replaceWith(B)  --> B替换A

   replaceAll(selector)
      A.replaceAll(B)   --> A替换B

    删除
    empty()
      - 清空 内部清空
   remove([expr])
      - 删除 整体都删除
   detach([expr])
      - 剪切  多保存在变量中，方便再次使用
    克隆/复制
    clone([Even[,deepEven]])

3、动画
基本
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
4. 事件处理

   之前绑定事件的方式：
      1. onclick=clickMe();  function clickMe() {}
      2. ele.onclick = function(){}
      3. ele.addEventListener("click", function(){})  js事件委派

   jQuery绑定事件的方式：
      1. $(ele).on("click", function(){})
      2. $("tbody").delegate(".btn-warning", "click", function(){})  这个3.几的版本没有这个方法了，这是3.几以前版本有的方法
      3. $("tbody").on("click",".btn-warning",function(){})  jQuery的事件委派