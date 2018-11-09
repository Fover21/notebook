# ES6常用语法

### 变量的定义

>let定义变量 
>
> - 不会变量提升
> - 有全局作用域和函数作用域，块级作用域{}
> - 不能重复定义
>
>var定义变量
>
>- 会变量提升
>- 只有全局作用域和函数作用域
>- 能够重复定义

>const定义变量
>
>- 定义的是一个 常量，定义之后不能进行修改
>- 没有变量提升
>- 不能重复定义
>- 带来了块级作用域
>- 定义常量的时候必须赋值

### 模板字符串

>let username1 = "username"
>
>oDiv.innerHTML = `
>
>​	<h1>${username1}</h1>
>
>​	<h2></h2>
>
>`
>
>用反引号进行字符串的拼接
>
>用${}来存储变量

### 数据的解构和赋值

>let ary = [1,2,3]
>
>解构：
>
>let [a, b, c] = ary
>
>let obj = {
>
>​	username: 'xxx'，
>
>​	age:23
>
>}
>
>let {username, age}= obj; # 没有赋值是默认两者相同
>
>let {username:新的名字, age:新的名字}= obj;
>
>- 解构的左右两端为相同的数据类型
>
>let a=1;
>
>let b=2;
>
>[a, b] = [b, a]
>
>- 交换数据的赋值需要放入数组中

### 函数的扩展

>function foo(x, y){
>
>​	let number = y || 10;
>
>​	return number
>
>}
>
>foo(1, 2)
>
>foo(1)
>
>foo(1, 0)
>
>function foo(x, y=10){}
>
>- ES6有了默认值参数
>
>- 箭头函数
>
>  - 一个参数
>
>  - v => v;
>
>    ```
>    let foo = v => v;
>    ret = foo(10);
>    console.log(ret);  10
>    ```
>
>  - 0和或者多个参数
>
>  - let bar = (x, y)=>{return x + y;}
>
>- 箭头函数的使用规则
>
>  - 定义的时候在什么地方，将来就不会改变了
>  - 箭头函数的this指向定义时的作用域
>  - 普通函数的this指向调用者的作用域

### 类的扩展

>```
><script>
>	# ES5
>	function Person(){
>        this.username = 'xxx';
>        this.age = 20;
>	}
>	Person.prototype.showInfo = function(){
>     	console.log(this.username);   
>	}
>	let xxx = new Person();
></script>
>```
>
>```
>ES6
>
>class Person{
>    constructor (username, age, mind){
>        this.username = username;
>        this.age = age;
>        this.mind = mind;
>    }
>    // 直接写方法不需要逗号
>    showInfo(){
>        console.log(this.username, this.age. this.mind)
>    }
>}
>let  xxx = new Person('xxx', 18, '000);
>xxx.showInfo()
>
>```
>
>- class关键字定义一个类
>  - 必须有constructor方法（构造方法，如果没有，constructor{}
>  - 必须使用new来实例化，否则报错
>- 类的继承
>  - 必须在子类的constructor方法中写super方法
>
>```
>
>class Peiqi extends Person{
>	constructor (username, age){
>		super()
>        this.username = username;
>        this.age = age;
>    }    
>}
>
>let peiqi = new Peiqi('peiqi', 73)
>peiqi.shoeInfo()  # 继承了父类
>```
>
>

### 模块化编程

### 对象的单体模式

>```
>let obj = {
>    naem : 'xxx'.
>    foo(){
>        console.log(this.name);
>    }
>}
>obj.foo()  # xxx
>```
>
>- 解决了箭头函数的this指向问题



# Vue.js

### 为什么用框架

>```
>// 数据模板引擎       ----   渐进式的框架
>// v-开头的指令是帮助我们渲染数据用的
><div id='app'> {{ greeting }} </div>  	
>
>new Vue({
>    el: '#app',
>    data: {
>        greeting : 'hello Vue',
>    }
>})
>```

### Vue之常用指令（用来渲染数据）

>```
>{{ greeting }}
>```

>```
>v-text
><div id='app' v-text='greeting'></div>
>
>new Vue({ // 根实例
>    el: '#app',
>    data: {
>        greeting : 'hello Vue',
>    }
>})
>```
>
>```
>v-html
><div id='app' v-html='greeting'></div>
>
>new Vue({ // 根实例
>    el: '#app',
>    data: {
>        greeting : '<h1>hello Vue</h1>',
>    }
>})
>```
>
>```
>v-for
><div id='app'>
>	<ul>
>		<li v-for="aihao in hobby">{{aihao}}</li>
>	</ul>
>	<ul>
>		<li v-for="student in students">
>			姓名：{{student.name}}
>			年龄：{{student.age}}
>			爱好：{{student.hobby}}
>		</li>
>	</ul>	
></div>
>
>new Vue({ // 根实例
>    el: '#app',
>    data: {
>        hobby: ['抽烟','喝酒','烫头'],
>        students: [
>            {
>                name: '张',
>                age: 12,
>                hobby: 'girls',
>            },
>            {
>                name: '李',
>                age: 18,
>                hobby: 'boys'
>            },
>            {
>                name: '王',
>                age: 90.
>                hobby: '无',
>            }
>        ]
>    }
>})
>```
>
>```html
>v-if
><div id='app'>
>	<div v-if="role == 'girl'">
>        <h1>
>            女的
>        </h1>
>    </div>	
>    <div v-else-if="role == 'boy'">
>        <h1>
>            男的
>        </h1>
>    </div>
>    <div v-else>
>        <h1>
>            不男不女
>        </h1>
>    </div>
></div>  	
>
><script>
>    let vm = new Vue({
>        el: '#app',
>        data: {
>            role: "girl"
>        }
>    })
></script>
>```
>
>```html
>v-show
><div id='app'>
>	<div v-show="isShow">Hello Word</div>
></div>  	
>
><script>
>    let vm = new Vue({
>        el: '#app',
>        data: {
>            isShow: true
>        }
>    })
></script>
>```
>
>
>
>- v-开头的指令是帮助我们渲染数据用的
>
>- v-show切换性能高一些，用display控制的
>- v-if的切换是同append控制的，慢
>- 加载性能v-show的慢v-if加载的快
>
>```html
>v-bind //绑定
><style>
>    .active {
>        width: 10px;
>        height: 10px;
>        background-color: black;
>    }
></style>
><div id='app'>
>	<a v-bind:href="jingdong">去京东</a>
>   <div v-bind:class="{ active: isActive,..., }"></div>
>    <div v-bind:class="[ isActive,..., ]"></div>
></div>  	
>
><script>
>    let vm = new Vue({
>        el: '#app',
>        data: {
>            jingdong: "www.jd.com",
>            isActive: true,  // 1
>            isActive: 'active',
>        }
>    })
></script>
>```
>
>```html
>v-on
><style>
>    .active {
>        width: 10px;
>        height: 10px;
>        background-color: black;
>    }
></style>
><div id='app'>
>	<h1 :class="{active: isActive}">
>        sao
>    </h1>
>    // 简写<button @:click="changeColor">
>    <button v-on:click="changeColor">
>        点击变色
>    </button>
></div>  	
>
><script>
>    let vm = new Vue({
>        el: '#app',
>        data: {
>            isShow: false
>        }.
>        methods:{
>        changeColor: function(){
>        		this.isAcative = !this.isActive;
>    		},
>        changeColor1: function(){},        
>    	}
>    })
></script>
>```
>
>```html
>v-model         ----   双向数据绑定
>
><div id='app'>
>	<input v-model="name" type="text">
>   	<input type="chackbox" value="men" v-model="genders">
>    <input type="chackbox" value="women" v-model="genders">
>    <select v-model="girls">
>        <option>女友1</option>
>        <option>女友2</option>
>        <option>女友3</option>
>    </select>
>    <textarea></textarea>
>    <hr>
>    {{name}}
>    {{genders}}
>    {{girls}}
></div>  	
>
><script>
>    let vm = new Vue({
>        el: '#app',
>        data: {
>            name: 'xxx',
>            genders: [],
>            girls: [],
>        }
>    })
></script>
>```
>
>#### 指令修饰符
>
>>```html
>><div id='app'>
>>	<table border="1">
>>        <thead>
>>        	<tr>
>>            	<th>学科</th>
>>                <th>成绩</th>
>>            </tr>
>>        </thead>
>>        	<tr>
>>                <td>python</td>             // 修饰符
>>                <td><input type="text" v-model.number="python"></td>
>>        	</tr>
>>        	<tr>
>>                <td>Vue</td>				// 修饰符(失去焦点后计算)
>>                <td><input type="text" v-model.lazy="vue"></td>
>>        	</tr>
>>        	<tr>
>>                <td>Go</td>					// 去左右空格
>>                <td><input type="text" v-model.trim="go"></td>
>>        	</tr>
>>        	<tr>
>>                <td>总成绩</td>
>>                // 不合适，引入了计算属性
>>                //<td>{{python + vue + go}}</td>
>>                <td>{{sumScore}}</td>
>>        	</tr>
>>        <tbody>
>>		
>>        </tbody>
>>    </table>
>></div>  	
>>
>><script>
>>    let vm = new Vue({
>>        el: '#app',
>>        data: {
>>            python: 98,
>>            vue: 100,
>>            go: 90,
>>        },
>>        // 计算属性
>>        computed: {
>>            // 页面刷新的时候就渲染了
>>            sumScore: function(){
>>                return this.python+this.vue+this.go
>>            }
>>        },
>>        // 侦听属性
>>        // 解耦 - 监听
>>        watch: {
>>            // 数据变动的时候才执行，不会刷新页面的时候执行
>>            python: function(){
>>                // 没有return的，没有接收值
>>                return this.python + 1
>>                // 进行一些逻辑操作
>>                alert("python 被修改")
>>            }
>>        }
>>        
>>    })
>></script>
>>```
>>
>>````
>>.number
>>.lazy
>>````
>
>### 获取DOM元素
>
>>```html
>>ref="名字"
>><style>
>>    .active {
>>        width: 10px;
>>        height: 10px;
>>        background-color: black;
>>    }
>></style>
>><div id='app'>
>>    // 国定格式
>>	<div ref="myRef">peiqi</div>
>>    // 简写<button @:click="changeColor">
>>    <button v-on:click="changeColor">
>>        点击变色
>>    </button>
>></div>  	
>>
>><script>
>>    let vm = new Vue({
>>        el: '#app',
>>        data: {
>>            
>>        },
>>        methods:{
>>        changeColor: function(){
>>            	// this.$refs is a object
>>            	// this.$refs.myRef就是那个标签
>>       			this.$refs.myRef.style.color = 'red';
>>        		this.isAcative = !this.isActive;
>>    		},
>>    	}
>>    })
>></script>
>>```
>
>### 自定义指令
>
>>```html
>><style>
>>    .box {
>>        width: 100px;
>>        height: 100px;
>>        background-color: red;
>>    }
>></style>
>><div id='app' v-bind:class="{box: isShow}">
>>    <div v-pos="position">Hello Vue</div>
>></div>  	
>>
>><script>
>>    // 自定义指令
>>    Vue.directive("pos", function(el, bindding){
>>        // el标签   bindding绑定的数据
>>        if (bindding.value){
>>            el.style['position'] = 'fixed';
>>            el.style['right'] = 0;
>>            el.style['bottom'] = 0;
>>        }
>>    })
>>    let vm = new Vue({
>>        el: '#app',
>>        data: {
>>            position: true,
>>            isShow: true,
>>        },
>>    })
>></script>
>>```
>>
>>```
>>还有一种方法
>><div id="app">
>>        <div v-bind:class="{ box: isShow}" v-pos.right.bottom="leftBottom">Hello Vue!</div>
>>    </div>
>>
>>    <script>
>>        // 数据模板引擎
>>        // v-开头的指令是帮助我们渲染数据用的
>>
>>        Vue.directive("pos", function (el, bindding) {
>>            console.log("el: ", el);
>>            console.log("bindding: ", bindding);
>>            if (bindding.value) {
>>                el.style['position'] = 'fixed';
>>                for (let key in bindding.modifiers) {
>>                    el.style[key] = 0;
>>                }
>>                // el.style['right'] = 0;
>>                // el.style['bottom'] = 0;
>>            }
>>        });
>>
>>        let vm = new Vue({
>>            el: "#app",
>>            data: {
>>                leftBottom: true,
>>                isShow: true,
>>            },
>>        })
>>    </script>
>>```
>>
>>

