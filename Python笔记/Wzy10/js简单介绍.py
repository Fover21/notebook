********JavaScript概述********

****ECMAScript和JavaScript的关系****

1996年11月，JavaScript的创造者--Netscape公司，决定将JavaScript提交给国际标准化组织ECMA，
希望这门语言能够成为国际标准。次年，ECMA发布262号标准文件（ECMA-262）的第一版，规定了浏览器
脚本语言的标准，并将这种语言称为ECMAScript，这个版本就是1.0版。

该标准一开始就是针对JavaScript语言制定的，但是没有称其为JavaScript，有两个方面的原因。
一是商标，JavaScript本身已被Netscape注册为商标。而是想体现这门语言的制定者是ECMA，而
不是Netscape，这样有利于保证这门语言的开发性和中立性。

因此ECMAScript和JavaScript的关系是，前者是后者的规格，后者是前者的一种实现

****ECMAScript的历史****
1992年Nombas开发出C-minus-minus(C--)的嵌入式脚本语言(最初绑定在CEnvi软件中).
后将其改名ScriptEase.(客户端执行的语言)

Netscape(网景)接收Nombas的理念,(Brendan Eich)在其Netscape Navigator 2.0产
品中开发出一套livescript的脚本语言.Sun和Netscape共同完成.后改名叫Javascript

微软随后模仿在其IE3.0的产品中搭载了一个JavaScript的克隆版叫Jscript.

为了统一三家,ECMA(欧洲计算机制造协会)定义了ECMA-262规范.国际标准化组织及国际电
工委员会（ISO/IEC）也采纳 ECMAScript 作为标准（ISO/IEC-16262）。从此，Web 
浏览器就开始努力（虽然有着不同的程度的成功和失败）将 ECMAScript 作为 JavaScript
实现的基础。EcmaScript是规范.


年份		名称				描述
1997	ECMAScript 1	第一个版本
1998	ECMAScript 2	版本变更
1999	ECMAScript 3 	添加正则表达式	添加try/catch

 		ECMAScript 4	没有发布
2009	ECMAScript 5	添加"strict mode"严格模式添加JSON支持
2011	ECMAScript 5.1	版本变更
2015	ECMAScript 6	添加类和模块
2016	ECMAScript 7	增加指数运算符（**）	增加Array.prototype.includes

注：ES6就是指ECMAScript6.

尽管 ECMAScript 是一个重要的标准，但它并不是 JavaScript 唯一的部分，当然，也不是唯
一被标准化的部分。实际上，一个完整的 JavaScript 实现是由以下 3 个不同部分组成的：

核心（ECMAScript） 
文档对象模型（DOM） Document object model (整合js，css，html)
浏览器对象模型（BOM） Broswer object model（整合js和浏览器）
简单地说，ECMAScript 描述了JavaScript语言本身的相关内容。
简单地说，ECMAScript 描述了以下内容：
语法 
类型 
语句 
关键字 
保留字 
运算符 
对象 (封装 继承 多态) 基于对象的语言.使用对象.

JavaScript 是脚本语言
JavaScript 是一种轻量级的编程语言。
JavaScript 是可插入 HTML 页面的编程代码。
JavaScript 插入 HTML 页面后，可由所有的现代浏览器执行。

********JavaScript基础********

1.****JavaScript引入方式****

**scrip标签内些代码**

<script>
  // 在这里写你的JS代码
</script>

**引入额外的JS文件**

<script src="myscript.js"></script>

2.****JavaScript语言规范****

**注释**

// 这是单行注释

/*
这是
多行注释
*/

**结束符**

JavaScript中的语句要以分号（;）为结束符。

3.****JavaScript语言****

数据类型
number     -----  数值
boolean    -----  布尔值
string     -----  字符串
undefined  -----  undefined
null       -----   null
object     -----  对象

**变量声明**

JavaScript的变量名可以使用_，数字，字母，$组成，不能以数字开头。
声明变量使用 var 变量名; 的格式来进行声明
1.声明变量时不用声明变量类型，全部使用var关键字 
var a;
a = 3;
2.一行可以声明多个变量.并且可以是不同类型

var name="jack", age=20, job="loyal";

注意：
1）变量名是区分大小写的。
2）推荐使用驼峰式命名规则。
3）保留字不能用做变量名。

补充：
1）ES6新增了let命令，用于声明变量。其用法类似于var，但是所声明的变量只在let命令所在的代码块内有效。
例如：for循环的计数器就很适合使用let命令。

2）ES6新增const用来声明常量。一旦声明，其值就不能改变。

3）保留着列表

abstract
boolean
byte
char
class
const
debugger
double
enum
export
extends
final
float
goto
implements
import
int
interface
long
native
package
private
protected
public
short
static
super
synchronized
throws
transient
volatile


4.****JavaScript数据类型****

JavaScript拥有动态类型

var x; //此时x是undefined
var x = 1; //此时x是数字
var x = "str" //此时x是字符串

**数值（Number）**

JavaScript不区分整形和浮点型，就只有一种数字类型。

var a = 1.1;
var a = 1;
var a = 1e3;
var q = 1e-2;

还有一种NaN，表示不是一个数字（Not a Number）

常用方法：

parseInt("123") //123
parseInt("abc") //NaN
parseInt(111.1) //111
parseInt("11ss") //11
parseInt("ss11") //NaN
parseFloat("11.11") //11.11
parseFloat("11.1ss") //11.1
parseFloat("11.ss") //11
parseFloat("ss11.q") //NaN

**字符串（String）**

是由Unicode字符、数字、标点符号组成的序列；字符串常量首尾由单引号或双引号括起；JavaScript中没有
字符类型；常用特殊字符在字符串中的表达；
字符串中部分特殊字符必须加上右划线\；常用的转义字符 \n:换行 \':单引号 \":双引号 \\:右划线

var a = "Hello"
var b = "word!"
var c = a + c
console.log(c) //Helloword!

常用方法：

1）length				（这是一个属性不是方法，不需要加括号）返回长度
2）trim()				移除字符串左右两端的空白
3）trimLeft()			移除字符串左边的空白
4）trimRight()			移除字符串右边的空白
5）charAt(n)				返回字符串索引为n的字符
6）concat(value,...)		拼接
7）indexOf(substring, start)返回子串位置，第一个参数为子串，第二次个参数为从哪个位置开始找，
							如果子串存在返回索引位置，存在没找到返回-1，不存在报错
8）substring(from, to)	根据索引获取子序列（后者小交换后拿，如果后者会负数，交换后负数变为0拿）
9）slice(start, end)		切片（存在负索引，找不返回空字符串）
10）toLowerCase()		大写字母变小写
11）toUpperCase()		小写字母变大写
12）split()				分割（如果不写任何参数，原样输出，如果参数为“”（空字符串，那么会将每个字符都切割出来））

注：拼接字符串一般使用“+”

~~slice和substring的区别~~
string.slice(start, stop)和string.substring(start, stop)：

两者的相同点：
如果start等于end，返回空字符串
如果stop参数省略，则取到字符串末
如果某个参数超过string的长度，这个参数会被替换为string的长度

substirng()的特点：
如果 start > stop ，start和stop将被交换
如果参数是负数或者不是数字，将会被0替换

silce()的特点：
如果 start > stop 不会交换两者
如果start小于0，则切割从字符串末尾往前数的第abs(start)个的字符开始(包括该位置的字符)
如果stop小于0，则切割在从字符串末尾往前数的第abs(stop)个字符结束(不包含该位置字符)


补充：

ES6中引入了模板字符串。模板字符串（template string）是增强版的字符串，用反引号（`）标识。
它可以当做普通字符串使用，也可以用来定义多行字符串，或者在字符串中嵌入变量。

// 普通字符串
`这是普通字符串！`
// 多行文本
`这是多行的
文本`
// 字符串中嵌入变量
var name = "Jack", time = "today";
`Hello ${name}, how are you ${time}?`

注意：
如果模板字符串中需要使用反引号，则在其面前要用反斜杠转义。
JSHint启用ES6语法支持:/* jshint esversion: 6 */

**布尔值（Boolean）**

Boolean类型仅有两个值：true和false，也代表1和0，实际运算中true=1,false=0
布尔值也可以看作on/off、yes/no、1/0对应true/false

var = true;
var = false;

""(空字符串)、0、null、undefined、NaN都是false

**null和undefined**

0.null表示值是空，一般在需要指定或清空一个变量时才使用，如 name = null;

1.Undefined 类型只有一个值，即 undefined。当声明的变量未初始化时，该变量的默认值是 undefined。

2.当函数无明确返回值时，返回的也是值 "undefined";

3.null表示变量的值是空，undefined则表示只声明了变量，但是没有赋值。

**对象（Object）**

JavaScript 中的所有事物都是对象：字符串、数值、数组、函数...此外，JavaScript 允许自定义对象。

JavaScript 提供多个内建对象，比如 String、Date、Array 等等。

对象只是带有属性和方法的特殊数据类型。

**数组

数组对象的作用是：使用单独的变量来存储一系列的值。

var a = [1, 2, 'abc'];
console.log(a[1]); //输出2

常用方法：
length				(属性，不需要加括号)数组大小
push(ele)			尾部追加元素
pop()				获取尾部元素
unshift(ele)		头部插入元素
shift()				头部移除元素
slice(start, end)	切片
reverse()			反转
join(sup)			将数组元素连接成字符串
concat(val,...)		连接数组
sort()				排序
forEach()			将数组的每一个元素传递给回调函数
splice()			删除元素，并向数组添加新元素
map()				返回一个数组元素调用函数处理后的值得新数组

关于sort()需要注意：

如果调用该方法时没有使用参数，将按字母顺序对数组中的元素进行排序，说得更精确点，
是按照字符编码的顺序进行排序。要实现这一点，首先应把数组的元素都转换成字符串（如有必要），
以便进行比较。

如果想按照其他标准进行排序，就需要提供比较函数，该函数要比较两个值，然后返回一个用于说明
这两个值的相对顺序的数字。比较函数应该具有两个参数 a 和 b，其返回值如下：

若 a 小于 b，在排序后的数组中 a 应该出现在 b 之前，则返回一个小于 0 的值。
若 a 等于 b，则返回 0。
若 a 大于 b，则返回一个大于 0 的值。				
			
例子：
function sortNumber(a,b){
    return a - b
}
var arr1 = [11, 100, 22, 55, 33, 44]
arr1.sort(sortNumber)

**forEach()**

语法：
forEach(function(currentValue, index, arr), thisValue)


参数											描述
function(currentValue, index, arr)			必需。 数组中每个元素需要调用的函数。
											函数参数:
											参数				描述
											currentValue	必需。当前元素
											index	可选。当前元素的索引值。
											arr	可选。当前元素所属的数组对象。
thisValue									可选。传递给函数的值一般用 "this" 值。
											如果这个参数为空， "undefined" 会传递给 "this" 值

**splice()**
语法：splice(index,howmany,item1,.....,itemX)

参数							描述
index						必需。规定从何处添加/删除元素。
							该参数是开始插入和（或）删除的数组元素的下标，必须是数字。
howmany						必需。规定应该删除多少元素。必须是数字，但可以是 "0"。
							如果未规定此参数，则删除从 index 开始到原数组结尾的所有元素。
item1, ..., itemX			可选。要添加到数组的新元素


**map**

语法：
map(function(currentValue,index,arr), thisValue)

参数									描述
function(currentValue, index,arr)	必须。函数，数组中的每个元素都会执行这个函数
									函数参数:
									参数				描述
									currentValue	必须。当前元素的值
									index			可选。当期元素的索引值
									arr				可选。当期元素属于的数组对象
thisValue							可选。对象作为该执行回调时使用，传递给函数，用作 "this" 的值。
									如果省略了 thisValue ，"this" 的值为 "undefined"

补充：

ES6新引入了一种新的原始数据类型（Symbol），表示独一无二的值。它是JavaScript语言的第7种数据类型。


**类型查询**

typeof "abc"  // "string"
typeof null  // "object"
typeof true  // "boolean"
typeof 123 // "number"

typeof是一个一元运算符（就像++，--，！，- 等一元运算符），不是一个函数，也不是一个语句。

对变量或值调用 typeof 运算符将返回下列值之一：

undefined - 如果变量是 Undefined 类型的
boolean - 如果变量是 Boolean 类型的
number - 如果变量是 Number 类型的
string - 如果变量是 String 类型的
object - 如果变量是一种引用类型或 Null 类型的


**运算符**

1.运算符分类

算术运算符：
    +   -    *    /     %       ++        -- 

比较运算符：
    >   >=   <    <=    !=    ==    ===   !==

逻辑运算符：
     &&   ||   ！

赋值运算符：
    =  +=   -=  *=   /=

字符串运算符：
    +  连接，两边操作数有一个或两个是字符串就做连接运算


2.算术运算符：自增，自减

++i:先计算后赋值
i++：先赋值后计算


3.js是一门弱语言类型
能够进行数据转换的叫做弱类型
console.log('1'==1)  //True
console.log('1'===1)  //False
  
强类型
print(1='1') //False

强类型与弱类型

静态类型语言
一种在编译期间就确定数据类型的语言。大多数静态类型语言是通过要求在使用任一变量之前声明其数据类型来保证这一点的。Java 和 C 是静态类型语言。 
动态类型语言
一种在运行期间才去确定数据类型的语言，与静态类型相反。VBScript 和 Python 是动态类型的，因为它们确定一个变量的类型是在您第一次给它赋值的时候。 
强类型语言
一种总是强制类型定义的语言。Java 和 Python 是强制类型定义的。您有一个整数，如果不明确地进行转换 ，不能将把它当成一个字符串去应用。 
弱类型语言
一种类型可以被忽略的语言，与强类型相反。JS 是弱类型的。在JS中，可以将字符串 '12' 和整数 3 进行连接得到字符串'123'，然后可以把它看成整数 123 ，所有这些都不需要任何的显示转换。 
所以说 Python 既是动态类型语言 (因为它不使用显示数据类型声明)，又是强类型语言 (因为只要一个变量获得了一个数据类型，它实际上就一直是这个类型了)。


4.NaN

var d="Tom";
    d=+d;
    alert(d);//NaN:属于Number类型的一个特殊值,当遇到将字符串转成数字无效时,就会得到一个NaN数据
    alert(typeof(d));//Number

    //NaN特点:
    
    var n=NaN;
    
    alert(n>3);//false
    alert(n<3);//false
    alert(n==3);//false
    alert(n==NaN);//false
    
    alert(n!=NaN);//NaN参与的所有的运算都是false,除了!=

5.比较运算符：

等号和非等号的同类运算符是全等号和非全等号。这两个运算符所做的与等号和非等号相同，只是它们在检查相等性前，不执行类型转换。

  console.log(2==2); //true
  console.log(2=='2'); //true  因为js是弱类型的，所以返回true

  console.log(2==='2'); //false (===判断的是类型，类型不一样就为false了)
  console.log(2!=='2'); //true ！==和===是相反的

注意：
var bResult = "Blue" < "alpha";
alert(bResult); //输出 true　　
在上面的例子中，字符串 "Blue" 小于 "alpha"，因为字母 B 的字符代码是 66，字母 a 的字符代码是 97。

比较数字和字符串

另一种棘手的状况发生在比较两个字符串形式的数字时，比如：

var bResult = "25" < "3";
alert(bResult); //输出 "true"
上面这段代码比较的是字符串 "25" 和 "3"。两个运算数都是字符串，所以比较的是它们的字符代码（"2" 的字符代码是 50，"3" 的字符代码是 51）。

不过，如果把某个运算数该为数字，那么结果就有趣了：

var bResult = "25" < 3;
alert(bResult); //输出 "false"

这里，字符串 "25" 将被转换成数字 25，然后与数字 3 进行比较，结果不出所料。

总结：

比较运算符两侧如果一个是数字类型,一个是其他类型,会将其类型转换成数字类型.
比较运算符两侧如果都是字符串类型,比较的是最高位的asc码,如果最高位相等,继续取第二位比较.

6.逻辑运算符：

console.log(1&&3); //3  两个为真才为真（0为假，其他的数字都代表真）
console.log(0&&3); //0  只要有一个为假则为假
console.log(0||3); //3  
console.log(2||3); //2

7.三元运算符

var a = 1;
var b = 2;
var c = a > b ? a : b

**流程控制**

顺序结构(从上向下顺序执行)
分支结构
循环结构

*分支结构*

1.if......else结构

if (表达式1) {
    语句1;
}else if (表达式2){
    语句2;
}else if (表达式3){
    语句3;
} else{
    语句4;

2.switch-case结构

switch基本格式
switch (表达式) {
    case 值1:语句1;break;
    case 值2:语句2;break;
    case 值3:语句3;break;
    default:语句4;
}

switch比else if结构更加简洁清晰，使程序可读性更强,效率更高

*循环语句*

for循环：（推荐使用）

语法规则：

    for(初始表达式;条件表达式;自增或自减)
    {
            执行语句
            ……
    }

for循环的另一种形式

for( 变量 in 数组或对象)
    {
        执行语句
        ……
    }

while 循环：
语法规则：

	while (条件){
	    语句1；
	    ...
	}

**异常处理**

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


