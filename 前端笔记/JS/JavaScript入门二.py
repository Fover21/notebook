*********BOM和DOM********

JavaScript分为 ECMAScript，DOM，BOM。

 
BOM（Browser Object Model）是指浏览器对象模型，它使 JavaScript 有能力与浏览器进行“对话”。

DOM （Document Object Model）是指文档对象模型，通过它，可以访问HTML文档的所有元素。

 
Window对象是客户端JavaScript最高层对象之一，由于window对象是其它大部分对象的共同祖先，
在调用window对象的方法和属性时，可以省略window对象的引用。例如：window.document.write()
可以简写成：document.write()。

******window对象（BOM）*******

所有浏览器都支持window对象。他表示浏览器窗口。

*如果文档包含框架（frame 或 iframe 标签），浏览器会为 HTML 文档创建一个 window 对象，并为每个框架创建一个额外的 window 对象。

*没有应用于 window 对象的公开标准，不过所有浏览器都支持该对象。

所有 JavaScript 全局对象、函数以及变量均自动成为 window 对象的成员。

全局变量是 window 对象的属性。全局函数是 window 对象的方法。

接下来要讲的HTML DOM 的 document 也是 window 对象的属性之一。

一些常用的Window方法：

window.innerHeight - 浏览器窗口的内部高度
window.innerWidth - 浏览器窗口的内部宽度
window.open() - 打开新窗口
window.close() - 关闭当前窗口

****window的子对象****

**navigator对象（了解即可）**

浏览器对象，通过这个对象可以判定用户所使用的浏览器，包含了浏览器相关信息。

navigator.appName 	// Web浏览器全称
navigator.appVersion　　// Web浏览器厂商和版本的详细字符串
navigator.userAgent　　// 客户端绝大部分信息
navigator.platform　　　// 浏览器运行所在的操作系统

**screen对象（了解即可）**

屏幕对象，不常用。

一些属性：

screen.availWidth - 可用的屏幕宽度
screen.availHeight - 可用的屏幕高度

**history对象（了解即可）**

window.history 对象包含浏览器的历史。

浏览历史对象，包含了用户对当前页面的浏览历史，但我们无法查看具体的地址，可以简单的用来前进或后退一个页面。

history.forward()  // 前进一页
history.back()  // 后退一页

**location对象**

window.location 对象用于获得当前页面的地址 (URL)，并把浏览器重定向到新的页面。

常用属性和方法：

location.href  获取URL
location.href="URL" // 跳转到指定页面
location.reload() 重新加载页面

**弹出框**

可以在 JavaScript 中创建三种消息框：警告框、确认框、提示框。

*警告框

警告框经常用于确保用户可以得到某些信息。
当警告框出现后，用户需要点击确定按钮才能继续进行操作。

语法：
alert("你看到了吗？");

*确认框（了解即可）

确认框用于使用户可以验证或者接受某些信息。
当确认框出现后，用户需要点击确定或者取消按钮才能继续进行操作。
如果用户点击确认，那么返回值为 true。如果用户点击取消，那么返回值为 false。

语法：
confirm("你确定吗？")

*提示框（了解即可）

提示框经常用于提示用户在进入页面前输入某个值。
当提示框出现后，用户需要输入某个值，然后点击确认或取消按钮才能继续操纵。
如果用户点击确认，那么返回值为输入的值。如果用户点击取消，那么返回值为 null。

语法：
prompt("请在下方输入","你的答案")

****计时相关****

通过使用 JavaScript，我们可以在一定时间间隔之后来执行代码，而不是在函数被调用后立即执行。我们称之为计时事件。

setTimeout()

语法：
var t=setTimeout("JS语句",毫秒)
setTimeout() 方法会返回某个值。在上面的语句中，值被储存在名为 t 的变量中。假如你希望取消这个 setTimeout()，你可以使用这个变量名来指定它。

setTimeout() 的第一个参数是含有 JavaScript 语句的字符串。这个语句可能诸如 "alert('5 seconds!')"，或者对函数的调用，诸如 alertMsg()"。

第二个参数指示从当前起多少毫秒后执行第一个参数（1000 毫秒等于一秒）。

clearTimeout()

语法：
clearTimeout(setTimeout_variable)
举个例子：

// 在指定时间之后执行一次相应函数
var timer = setTimeout(function(){alert(123);}, 3000)
// 取消setTimeout设置
clearTimeout(timer);
setInterval()

setInterval() 方法可按照指定的周期（以毫秒计）来调用函数或计算表达式。

setInterval() 方法会不停地调用函数，直到 clearInterval() 被调用或窗口被关闭。由 setInterval() 返回的 ID 值可用作 clearInterval() 方法的参数。

语法：

setInterval("JS语句",时间间隔)
返回值

一个可以传递给 Window.clearInterval() 从而取消对 code 的周期性执行的值。

clearInterval()

clearInterval() 方法可取消由 setInterval() 设置的 timeout。

clearInterval() 方法的参数必须是由 setInterval() 返回的 ID 值。

语法：

clearInterval(setinterval返回的ID值)
举个例子：

// 每隔一段时间就执行一次相应函数
var timer = setInterval(function(){console.log(123);}, 3000)
// 取消setInterval设置
clearInterval(timer);


*********DOM********

DOM（Document Object Model）是一套对文档的内容进行抽象和概念化的方法。 

当网页被加载时，浏览器会创建页面的文档对象模型（Document Object Model）。

HTML DOM 模型被构造为对象的树。

https://images2018.cnblogs.com/blog/867021/201803/867021-20180312215352312-132101897.png

*DOM标准规定HTML文档中的每个成分都是一个节点(node)：

文档节点(document对象)：代表整个文档
元素节点(element 对象)：代表一个元素（标签）
文本节点(text对象)：代表元素（标签）中的文本
属性节点(attribute对象)：代表一个属性，元素（标签）才有属性
注释是注释节点(comment对象)　

*JavaScript 可以通过DOM创建动态的 HTML：

JavaScript 能够改变页面中的所有 HTML 元素
JavaScript 能够改变页面中的所有 HTML 属性
JavaScript 能够改变页面中的所有 CSS 样式
JavaScript 能够对页面中的所有事件做出反应


****查找标签****

**直接查找**

document.getElementById("id名")				根据ID获取一个标签
document.getElementsByClassName("class名")	根据class属性获取
document.getElementsByTagName("标签名")		根据标签名获取标签集合

注意：
涉及到DOM操作的JS代码应该放在文档的哪个位置。

**间接查找**

parentElement				父节点标签元素
children					所有子标签
firstElementChild			第一个子标签元素
lastElementChild			最后一个子标签元素
nextElementSibing			下一个兄弟标签元素
previousElementSibling		上一个兄弟标签元素


****节点操作****

**创建节点**

语法：

createElement(标签名)

示例：
var divElement = document.createElement("div");

**添加节点**

语法：
追加一个子节点（作为最后的子节点）
somenode.appendChild(newnode);

把增加的节点放在某个节点的前边。
somenode.insertBefore(newnode, 某个节点);

示例：
var imgEle=document.createElement("img");
imgEle.setAttribute("src", "http://image11.m1905.cn/uploadfile/s2010/0205/20100205083613178.jpg");
var d1Ele = document.getElementById("d1");
d1Ele.appendChild(imgEle);

**删除节点**

语法：
获得要删除的元素，通过父元素调用删除。

removeChild(要删除的节点)

**属性节点**


获取文本节点的值：

var divEle = document.getElementById("d1")
divEle.innerText
divEle.innerHTML
设置文本节点的值：

var divEle = document.getElementById("d1")
divEle.innerText="1"
divEle.innerHTML="<p>2</p>"


attribute操作

var divEle = document.getElementById("d1");
divEle.setAttribute("age","18")
divEle.getAttribute("age")
divEle.removeAttribute("age")

// 自带的属性还可以直接.属性名来获取和设置
imgEle.src
imgEle.src="..."


**获取值操作**

语法：
elementNode.value

适用于以下标签：

.input
.select
.textarea

var iEle = document.getElementById("i1");
console.log(iEle.value);
var sEle = document.getElementById("s1");
console.log(sEle.value);
var tEle = document.getElementById("t1");
console.log(tEle.value);

**class的操作**

className  获取所有样式类名(字符串)

classList.remove(cls)  删除指定类
classList.add(cls)  添加类
classList.contains(cls)  存在返回true，否则返回false
classList.toggle(cls)  存在就删除，否则添加

**指定CSS操作**

obj.style.backgroundColor="red"
JS操作CSS属性的规律：

1.对于没有中横线的CSS属性一般直接使用style.属性名即可。如：

obj.style.margin
obj.style.width
obj.style.left
obj.style.position

2.对含有中横线的CSS属性，将中横线后面的第一个字母换成大写即可。如：

obj.style.marginTop
obj.style.borderLeftWidth
obj.style.zIndex
obj.style.fontFamily

****事件****

HTML 4.0 的新特性之一是有能力使 HTML 事件触发浏览器中的动作（action），比如当用户点击某个 
HTML 元素时启动一段 JavaScript。下面是一个属性列表，这些属性可插入 HTML 标签来定义事件动作



**常用事件**

onclick        当用户点击某个对象时调用的事件句柄。
ondblclick     当用户双击某个对象时调用的事件句柄。

onfocus        元素获得焦点。               
onblur         元素失去焦点。               应用场景：用于表单验证,用户离开某个输入框时,代表已经输入完了,我们可以对它进行验证.
onchange       域的内容被改变。             应用场景：通常用于表单元素,当元素内容被改变时触发.（select联动）

onkeydown      某个键盘按键被按下。          应用场景: 当用户在最后一个输入框按下回车按键时,表单提交.
onkeypress     某个键盘按键被按下并松开。
onkeyup        某个键盘按键被松开。
onload         一张页面或一幅图像完成加载。
onmousedown    鼠标按钮被按下。
onmousemove    鼠标被移动。
onmouseout     鼠标从某元素移开。
onmouseover    鼠标移到某元素之上。

onselect      在文本框中的文本被选中时发生。
onsubmit      确认按钮被点击，使用的对象是form。


**绑定方式**

方式一：

<div id="d1" onclick="changeColor(this);">点我</div>
<script>
  function changeColor(ths) {
    ths.style.backgroundColor="green";
  }
</script>
注意：
this是实参，表示触发事件的当前元素。
函数定义过程中的ths为形参。

方式二：


<div id="d2">点我</div>
<script>
  var divEle2 = document.getElementById("d2");
  divEle2.onclick=function () {
    this.innerText="呵呵";
  }
</script>



