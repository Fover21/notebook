# Vue组件系统之全局组件的注册

>```html
><div id='app'>
>	<global-component></global-component>
></div>
>	
><script>
>    // 注册
>    Vue.component(
>        // 第一个是组件名称  第二个object
>        "global-component", {
>            // 组件内容  抱一个div-单个根元素
>            template: `<div><h3>{{ db }}</h3></div>`,
>            // data必须是函数
>            data(){
>                // return中写数据
>                return {
>                    db: 'hello',
>                }
>            }
>        }
>    );
>    
>    new Vue({
>        el: '#app',
>        // template: `<global-component></global-component>`
>    })
></script>
>```
>
>```html
><div id='app'>
>	
></div>
>	
><script>
>    // 注册组件
>    Vue.component(
>        // 第一个是组件名称  第二个object
>        "global-component", {
>            // 组件内容  抱一个div-单个根元素，包在app这个div中
>            template: `<div><h3>{{ db }}</h3></div>`,
>            // data必须是函数
>            data(){
>                // return中写数据
>                return {
>                    db: 'hello',
>                }
>            }
>        }
>    );
>    
>    new Vue({
>        el: '#app',
>        // 根元素会替换div
>        template: `<global-component></global-component>`
>    })
></script>
>```
>
>全局组件
>
>```html
>// 总结
>Vue.component(
>        // 第一个是组件名称  第二个object
>        "global-component", {
>            // 组件内容  抱一个div-单个根元素，包在app这个div中
>            template: `<div><h3>{{ db }}</h3></div>`,
>            // data必须是函数
>            data(){
>                // return中写数据
>                return {
>                    db: 'hello',
>                },
>			computed: {},
>			watch: {},
>			methods: {},
>            }
>        }
>    );
>
>new Vue({
>        el: '#app',
>        // 根元素会替换div
>        template: `<global-component></global-component>`
>    })
>
>// data 必须是函数
>// 没有属性
>```

# 组件系统之组件的复用

>```html
><div id='app'>
>	<global-component></global-component>
>    <global-component></global-component>
>    <global-component></global-component>
></div>
>	
><script>
>    // 注册
>    Vue.component(
>        // 第一个是组件名称  第二个object
>        "global-component", {
>            // 组件内容  抱一个div-单个根元素
>            template: `<div><h3>{{ db }}</h3></div>`,
>            // data必须是函数
>            data(){
>                // return中写数据
>                return {
>                    db: 'hello',
>                }
>            }
>        }
>    );
>    
>    new Vue({
>        el: '#app',
>        
>    })
></script>
>```

# 组价系统之局部组件的注册

>```html
><div id='app'>
>	<app-header></app-header>
>   
></div>
>	
><script>
>    let Header = {
>      	template: `<div><h3>{{ db }}</h3></div>`,
>        data(){
>            return {
>                    db: 'hello',
>                }
>        },
>        computed: {},
>    };
>    
>    new Vue({
>        el: '#app',
>        template: `<app-header></app-header>`,
>        components: {
>            'app-header': Header
>        }
>    })
></script>
>```
>
>```html
><div id='app'>
>    <!--<App></App>-->   
></div>
>	
><script>
>    let Header = {
>      	template: `<div><h3>{{ db }}</h3></div>`,
>        data(){
>            return {
>                    db: 'hello',
>                }
>        },
>        computed: {},
>        // ...
>    };
>    // 在入口组件中注册写的局部组件
>    let App = {
>        template: `
>			<div>
>    			<app-header></app-header>
>    		</div>
>		`,
>        components: {
>            'app-header': Header
>        },
>        // 组件的私有数据
>        data(){},
>    };
>    // 根实例
>    new Vue({
>        el: '#app',
>        // 作为根被渲染
>        template: `<App></App>`,
>        components: {
>            // App:App,
>            App,
>        }
>    })
></script>
>```
>
>局部组件
>
>```html
>- 总结
>
>创建组件
>	创建局部组件，起始就是创建一个JavaScript object
>    let Header = {
>      	template: `<div><h3>{{ db }}</h3></div>`,
>        data(){
>            return {
>                    db: 'hello',
>                }
>        },
>        computed: {},
>    };
>注册组件
>	
>    new Vue({
>        el: '#app',
>        template: `<app-header></app-header>`,
>        components: {
>            'app-header': Header
>        }
>    })
>
>组件可以嵌套使用
>
>```
>
>

# Vue组件系统之父子组件的通信

>```html
><div id='app'>
>   
></div>
>	
><script>
>    // 子
>    let Header = {
>      	template: `<div><h3>{{ db }}</h3><h3>{{ fData }}</h3><</div>`,
>        data(){
>            return {
>                    db: 'hello',
>                }
>        },
>        // 接收父亲传来的数据
>        props:['fData'],
>        computed: {},
>        // ...
>    };
>    // 在入口组件中注册写的局部组件
>    // 父
>    let App = {
>        template: `
>			<div>
>    			<app-header v-bind:fData="fatherData"></app-header>
>    		</div>
>		`,
>        components: {
>            'app-header': Header
>        },
>        // 组件的私有数据
>        data(){
>            return {fatherData: 0,}
>        },
>    };
>    // 根实例
>    new Vue({
>        el: '#app',
>        // 作为根被渲染
>        template: `<App></App>`,
>        components: {
>            // App:App,
>            App,
>        }
>    })
></script>
>```

# Vue组件系统之子父组件的通信

>```html
><div id='app'>
></dic>
>
><script>
>    // 子
>    let Header = {
>      	template: `<div> 
>				<button @click='sonClick'>点击改变字体大小</button>
>    		</div>`,
>        methods: {
>            sonClick: function(){
>                // 儿子的的行为传给父亲
>                this.$emit("change-size", 0.1)
>            }  
>        },
>        computed: {},
>        // ...
>    };
>    // 父
>    let App = {
>        template: `
>			<div>
>    			<span :style="{ fontSize: postFontSize + 'em' }">我是字体</span>
>    			<app-header v-on:change-size="fatherClick"></app-header>
>    		</div>
>		`,
>        components: {
>            'app-header': Header
>        },
>        // 组件的私有数据
>        data(){
>            return {
>                postFontSize: 1,
>            }
>        },
>        methods: {
>            // 自己定义的change-size事件，一直在监听，等着儿子传来的信息
>            fatherClick: function(value){
>                this.postFontSize += value;
>            }
>        }
>    };
>    // 根实例
>    new Vue({
>        el: '#app',
>        // 作为根被渲染
>        template: `<App></App>`,
>        components: {
>            // App:App,
>            App,
>        }
>    })
>    
></script>
>```

# Vue组件系统之混入（mixin）

>```html
><div id='app'>
></dic>
>		<my-header></my-header>
>        <p></p>
>        <my-app></my-app>
><script>
>    let Header = {
>      	template: `<div> 
>				<button @click='show('xxx')'>点击显示xxx来了</button>
>				<button @click='hide('xxx')'>点击显示xxx去了</button>
>    		</div>`,
>        methods: {
>            show: function(name){
>                console.log(name+'来了');
>            },
>            hide: function(name){
>                console.log(name+'来了');
>            },
>        },
>    };
>    let App = {
>        template: `
>			<div>
>    			<button @mouseenter='show('000')'>点击显示000来了</button>
>				<button @mouseleve='hide('000')'>点击显示000去了</button>
>    		</div>
>		`,
>        methods: {
>            show: function(name){
>                console.log(name+'来了');
>            },
>            hide: function(name){
>                console.log(name+'来了');
>            },
>        }
>    };
>    // 根实例
>    new Vue({
>        el: '#app',
>        components: {
>            "my-header": Header,
>            "my-app": App,
>        }
>    })
>    
></script>
>```
>
>```html
><div id='app'>
>    <my-header></my-header>
>        <p></p>
>        <my-app></my-app>
></dic>
>
><script>
>    let mixs = {
>        methods:{
>            show: function(name){
>                    console.log(name+'来了');
>                },
>            hide: function(name){
>                    console.log(name+'来了');
>                },
>        }
>    }
>    let Header = {
>      	template: `<div> 
>				<button @click='show('xxx')'>点击显示xxx来了</button>
>				<button @click='hide('xxx')'>点击显示xxx去了</button>
>    		</div>`,
>        mixins: [mixs],
>    };
>    let App = {
>        template: `
>			<div>
>    			<button @mouseenter='show("000")'>点击显示000来了</button>
>				<button @mouseleve='hide("000")'>点击显示000去了</button>
>    		</div>
>		`,
>        mixins: [mixs],
>    };
>    // 根实例
>    new Vue({
>        el: '#app',
>        components: {
>            "my-header": Header,
>            "my-app": App,
>        }
>    })
>    
></script>
>```
>
>

# Vue组件系统之插槽\<slot>\</slot>

>```html
>- 内容分发
><style>
>    .box {
>        width: 50px;
>        height: 50px;
>        float: left;
>    }
></style>
><div id='app'>
>	<global-component>首页</global-component>
>    <global-component>免费</global-component>
>    <global-component>收费</global-component>
></div>
>	
><script>
>    // 注册全局组件
>    Vue.component(
>        "global-component", {
>            template: `<div class="box"><slot></slot></div>`,
>        }
>    );
>    
>    new Vue({
>        el: '#app',
>    })
></script>
>```

# Vue组件系统之具名插槽

>```html
><style>
>    .box {
>        width: 50px;
>        height: 50px;
>        float: left;
>    }
></style>
><div id='app'>
>	<global-component>
>    	<div slot='home'>首页</div>
>        <div slot='free'>免费</div>
>        <div slot='toll'>收费</div>
>    </global-component>
></div>
>	
><script>
>    // 注册全局组件
>    Vue.component(
>        "global-component", {
>            template: `<div class="box">
>					<slot name="home"></slot>
>					<slot name="free"></slot>
>					<slot name="toll"></slot>
>    			</div>`,
>        }
>    );
>    
>    new Vue({
>        el: '#app',
>    })
></script>
>```

