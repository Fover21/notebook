一、jQuery事件

常用事件
   blur([[data],fn])   失去焦点
   focus([[data],fn])  获取焦点（ 搜索框例子）
   change([[data],fn]) 当select下拉框中的元素发生改变的时候触发change事件(select例子)
   click([[data],fn])  点击
   dblclick([[data],fn]) 双击
   scroll([[data],fn])   滚动
   submit([[data],fn])   提交

不常用事件
   error([[data],fn])
   focusin([data],fn)
   focusout([data],fn)
   keydown([[data],fn])   按下
   keypress([[data],fn])  按键
   keyup([[data],fn])     键松开
   mousedown([[data],fn]) 鼠标按下
   mouseenter([[data],fn])  鼠标移进去
   mouseleave([[data],fn])  鼠标离开：只有鼠标离开被选元素的时候，才会触发mouseleave事件
   mousemove([[data],fn])   鼠标移动
   mouseout([[data],fn])    鼠标离开：无论鼠标离开被选元素还是任何子元素，都会触发mouseout事件
   mouseover([[data],fn]    鼠标悬停
   mouseup([[data],fn])     鼠标弹起
   resize([[data],fn])  元素窗口发生变化
   select([[data],fn])
   unload([[data],fn])
   补充：
      文档树加载完之后绑定事件（绝大多数情况下）
      第一种：吧script放在后面。
      第二种：
      $(document).ready(function(){
         // 绑定事件的代码
         ....
      })

      简写：
      $(function($){
         // 绑定事件的代码
         ....
      });


二、jQuery扩展（很重要！！）

1、jQuery扩展语法

把扩展的内容就可以写到xxxx.js文件了，在主文件中直接导入就行了。

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


三、表格的添加 | 删除 | 编辑示例

第一种：点击编辑没有模态框，是input框编辑修改
第二种：点击编辑有模态框

补充：

- .data()
- .data("key", value) 保存值，value可以是字符串，也可以是数组，也可以是jquery对象
- .data("key") 获取值（没有值就返回undefined）
- .removeData() 删除所有

- .removeData("key") 删除key对应的value






