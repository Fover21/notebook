******函数******

**函数定义**

//普通函数定义
function f1() {
    console.log("Hello word!")
}

//带参数的函数
function f2(a, b) {
    console.log(arguments); //内置的arguments对象
    console.log(arguments.length);
    console.log(a, b);
}

//带返回值的函数
function sum(a, b) {
    return a+b;
}

sum(2, 3);

//匿名函数方式
var lam = function (a, b) {
    return a+b;
};

lam(2, 3);

//立即执行函数
(function (a, b) {
    return a + b;
})(1, 2);

补充：

ES6中允许使用“箭头”（=>）定义函数。
var f = v => v;
// 等同于
var f = function(v){
  return v;
}

如果箭头函数不需要参数或需要多个参数，就是用圆括号代表参数部分：

var f = () => 5;
// 等同于
var f = function(){return 5};

var sum = (num1, num2) => num1 + num2;
// 等同于
var sum = function(num1, num2){
  return num1 + num2;
}


**函数中的arguments参数**

function add(a,b){
  console.log(a+b);
  console.log(arguments.length)
}

add(1,2)

输出：
3
2

注意：函数只能返回一个值，如果要返回多个值，只能将其放在数组或对象中返回

**函数的全局变量和局部变量和作用域**

局部变量：

在JavaScript函数内部声明的变量（使用 var）是局部变量，所以只能在函数内部访问它（该变量的作用域是函数内部）。
只要函数运行完毕，本地变量就会被删除。

全局变量：

在函数外声明的变量是全局变量，网页上的所有脚本和函数都能访问它。

变量生存周期：

JavaScript变量的生命期从它们被声明的时间开始。

局部变量会在函数运行以后被删除。

全局变量会在页面关闭后被删除。

作用域

首先在函数内部查找变量，找不到则到外层函数查找，逐步找到最外层。



****词法分析****

JavaScript中在调用函数的那一瞬间，会先进行词法分析。

词法分析的过程：

当函数调用的前一瞬间，会先形成一个激活对象：Avtive Object（AO），并会分析一下三个方面：

1.函数参数，如果有，则将次参数赋值给AO，且值为undefined。如果没有，则不做任何操作。
2.函数局部变量，如果AO上有同名的值，则不做任何操作。如果没有，则将次变量赋值给AO，并且值为undefined。
3.函数声明，如果AO上有，则会将AO上的对象覆盖。如果没有，则不做任何操作。

函数内部无论是使用参数还是使用局部变量都到AO上找。

例子1：

var age = 18;
function foo(){
  console.log(age);
  var age = 20;
  console.log(age);
}
foo();

例子2：

var age = 18;
function foo(){
  console.log(age);
  var age = 20;
  console.log(age);
  function age(){
    console.log("hello");
  }
  console.log(age);
}
foo();


分析过程：

词法分析过程：
1、分析参数，有一个参数，形成一个 AO.age=undefine;
2、分析变量声明，有一个 var age, 发现 AO 上面已经有一个 AO.age，因此不做任何处理
3、分析函数声明，有一个 function age(){...} 声明， 则把原有的 age 覆盖成 AO.age=function(){...};

最终，AO上的属性只有一个age，并且值为一个函数声明

执行过程：
注意：执行过程中所有的值都是从AO对象上去寻找

1、执行第一个 console.log(age) 时，此时的 AO.age 是一个函数，所以第一个输出的一个函数
2、这句 var age=20; 是对 AO.age 的属性赋值， 此时AO.age=20 ，所以在第二个输出的是 20
3、同理第三个输出的还是20, 因为中间再没有改变age值的语句了

******内置对象和方法******

JavaScript中的所有事物都是对象：字符串、数字、数组、日期，等等。在JavaScript中，对象是拥有属性和方法的数据。

注意var s1 = "abc"和var s2 = new String("abc")的区别：typeof s1 --> string而 typeof s2 --> Object

类型			内置对象和方法		介绍
数据类型		Number				数字对象
			String 				字符串对象
			Boolean				布尔值对象

组合对象		Array				数组对象
			Math				数学对象
			Date				日期对象

高级对象		Object   			自定义对象
			Error 				错误对象
			Function 			函数对象
			RegExp 				正则表达式对象
			Golobal				全局对象

****自定义对象****

JavaScript的对象（object）本质上是键值对的集合（Hash结构），但是只能用字符串作为键。

var a = {"name": "Tom", "age": 18};
console.log(a.name);
console.log(a["age"]);

变量对象中的内容：

var a = {"name": "Tom", "age": 18};
for (var i in a){
  console.log(i, a[i]);
}


**创建对象**

var person=new Object();  // 创建一个person对象
person.name="Tom";  // person对象的name属性
person.age=18;  // person对象的age属性

注意：
ES6中提供了Map数据结构。它类似于对象，也是键值对的集合，但是“键”的范围不限于字符串，
各种类型的值（包括对象）都可以当做键。
也就是说，Object结构提供了“字符串--值”的对应，Map结构提供了“值--值”的对应，是一种
更完善的Hash结构实现。

var m = new Map();
var o = {p: "Hello World"}

m.set(o, "content"}
m.get(o)  // "content"

m.has(o)  // true
m.delete(o)  // true
m.has(o) // false

扩展：


// 父类构造函数
var Car = function (loc) {
  this.loc = loc;
};

// 父类方法
Car.prototype.move = function () {
  this.loc ++;
};

// 子类构造函数
var Van = function (loc) {
  Car.call(this, loc);
};

// 继承父类的方法
Van.prototype = Object.create(Car.prototype);
// 修复 constructor
Van.prototype.constructor = Van;
// 扩展方法
Van.prototype.grab = function () {
  /* ... */
};


****Data对象****

**创建对象**

/方法1：不指定参数
var d1 = new Date();
console.log(d1.toLocaleString());
//方法2：参数为日期字符串
var d2 = new Date("2004/3/20 11:12");
console.log(d2.toLocaleString());
var d3 = new Date("04/03/20 11:12");
console.log(d3.toLocaleString());
//方法3：参数为毫秒数
var d3 = new Date(5000);
console.log(d3.toLocaleString());
console.log(d3.toUTCString());

//方法4：参数为年月日小时分钟秒毫秒
var d4 = new Date(2004,2,20,11,12,0,300);
console.log(d4.toLocaleString());  //毫秒并不直接显示

**Data对象的方法**

var d = new Date(); 
//getDate()                 获取日
//getDay ()                 获取星期
//getMonth ()               获取月（0-11）
//getFullYear ()            获取完整年份
//getYear ()                获取年
//getHours ()               获取小时
//getMinutes ()             获取分钟
//getSeconds ()             获取秒
//getMilliseconds ()        获取毫秒
//getTime ()                返回累计毫秒数(从1970/1/1午夜)


******JSON对象******

var str1 = '{"name": "Tom", "age": 18}';
var obj1 = {"name": "Tom", "age": 18};
// JSON字符串转换成对象
var obj = JSON.parse(str1); 
// 对象转换成JSON字符串
var str = JSON.stringify(obj1);

******REgExp对象******

//RegExp对象

//创建正则对象方式1
// 参数1 正则表达式(不能有空格)
// 参数2 匹配模式：常用g(全局匹配;找到所有匹配，而不是在第一个匹配后停止)和i(忽略大小写)

// 用户名只能是英文字母、数字和_，并且首字母必须是英文字母。长度最短不能少于6位 最长不能超过12位。

// 创建RegExp对象方式（逗号后面不要加空格）
var reg1 = new RegExp("^[a-zA-Z][a-zA-Z0-9_]{5,11}$");

// 匹配响应的字符串
var s1 = "bc123";

//RegExp对象的test方法，测试一个字符串是否符合对应的正则规则，返回值是true或false。
reg1.test(s1);  // true

// 创建方式2
// /填写正则表达式/匹配模式（逗号后面不要加空格）
var reg2 = /^[a-zA-Z][a-zA-Z0-9_]{5,11}$/;

reg2.test(s1);  // true


// String对象与正则结合的4个方法
var s2 = "hello world";

s2.match(/o/g);         // ["o", "o"]             查找字符串中 符合正则 的内容
s2.search(/h/g);        // 0                      查找字符串中符合正则表达式的内容位置
s2.split(/o/g);         // ["hell", " w", "rld"]  按照正则表达式对字符串进行切割
s2.replace(/o/g, "s");  // "hells wsrld"          对字符串按照正则进行替换

// 关于匹配模式：g和i的简单示例
var s1 = "name:Tom age:18A";

s1.replace(/a/, "哈哈哈");      // "n哈哈哈me:Tom age:18A"
s1.replace(/a/g, "哈哈哈");     // "n哈哈哈me:Tom 哈哈哈ge:18A"      全局匹配
s1.replace(/a/gi, "哈哈哈");    // "n哈哈哈me:Tom 哈哈哈ge:18哈哈哈"  不区分大小写


// 注意事项1：
// 如果regExpObject带有全局标志g，test()函数不是从字符串的开头开始查找，而是从属性regExpObject.lastIndex所指定的索引处开始查找。
// 该属性值默认为0，所以第一次仍然是从字符串的开头查找。
// 当找到一个匹配时，test()函数会将regExpObject.lastIndex的值改为字符串中本次匹配内容的最后一个字符的下一个索引位置。
// 当再次执行test()函数时，将会从该索引位置处开始查找，从而找到下一个匹配。
// 因此，当我们使用test()函数执行了一次匹配之后，如果想要重新使用test()函数从头开始查找，则需要手动将regExpObject.lastIndex的值重置为 0。
// 如果test()函数再也找不到可以匹配的文本时，该函数会自动把regExpObject.lastIndex属性重置为 0。

var reg3 = /foo/g;
// 此时 regex.lastIndex=0
reg3.test('foo'); // 返回true
// 此时 regex.lastIndex=3
reg3.test('xxxfoo'); // 还是返回true
// 所以我们在使用test()方法校验一个字符串是否完全匹配时，一定要加上^和$符号。

// 注意事项2(说出来你可能不信系列)：
// 当我们不加参数调用RegExpObj.test()方法时, 相当于执行RegExpObj.test("undefined"), 并且/undefined/.test()默认返回true。
var reg4 = /^undefined$/;
reg4.test(); // 返回true
reg4.test(undefined); // 返回true
reg4.test("undefined"); // 返回true


******Math******

abs(x)      返回数的绝对值。
exp(x)      返回 e 的指数。
floor(x)    对数进行下舍入。
log(x)      返回数的自然对数（底为e）。
max(x,y)    返回 x 和 y 中的最高值。
min(x,y)    返回 x 和 y 中的最低值。
pow(x,y)    返回 x 的 y 次幂。
random()    返回 0 ~ 1 之间的随机数。
round(x)    把数四舍五入为最接近的整数。
sin(x)      返回数的正弦。
sqrt(x)     返回数的平方根。
tan(x)      返回角的正切。



