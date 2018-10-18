# Ajax

>
>
>### Ajax准备知识：JSON
>
>>什么是 JSON ？
>>
>>- JSON 指的是 JavaScript 对象表示法（JavaScript Object Notation）
>>
>>- JSON 是轻量级的文本数据交换格式
>>
>>- JSON 独立于语言 *
>>
>>- JSON 具有自我描述性，更易理解
>>
>>   JSON 使用 JavaScript 语法来描述数据对象，但是 JSON 仍然独立于语言和平台。JSON 解析器和 JSON 库支持许多不同的编程语言。
>>
>>>
>>>
>>>合格的json对象：
>>>
>>>```
>>>["one", "two", "three"]
>>>{ "one": 1, "two": 2, "three": 3 }
>>>{"names": ["张三", "李四"] }
>>>[ { "name": "张三"}, {"name": "李四"} ]　
>>>```
>>>
>>> 不合格的json对象：
>>>
>>>```
>>>{ name: "张三", 'age': 32 }  　　　　　　 // 属性名必须使用双引号
>>>[32, 64, 128, 0xFFF] 　　　　　　　　　　  // 不能使用十六进制值
>>>{ "name": "张三", "age": undefined }    // 不能使用undefined
>>>{ "name": "张三",
>>>  "birthday": new Date('Fri, 26 Aug 2011 07:13:10 GMT'),
>>>  "getName":  function() {return this.name;}  // 不能使用函数和日期对象
>>>}
>>>```
>>>
>>>###### stringify与parser方法
>>>
>>>>
>>>>
>>>>JavaScript中关于JSON对象和字符串转换的两个方法：
>>>>
>>>>JSON.parse(): 用于将一个 JSON 字符串转换为 JavaScript 对象　
>>>>
>>>>```
>>>>JSON.parse('{"name":"alex"}');
>>>>JSON.parse('{name:"alex"}') ;      // 错误
>>>>JSON.parse('[18,undefined]') ;     // 错误
>>>>```
>>>>
>>>>JSON.stringify(): 用于将 JavaScript 值转换为 JSON 字符串。　
>>>>
>>>>```
>>>>JSON.stringify({"name":"alex"})
>>>>```
>
>### Ajax简介
>
>>
>>
>>AJAX（Asynchronous Javascript And XML）翻译成中文就是“异步的Javascript和
>>
>>XML”。即使用Javascript语言与服务器进行异步交互，传输的数据为XML（当然
>>
>>，传输的数据不只是XML）。
>>
>>AJAX 不是新的编程语言，而是一种使用现有标准的新方法。
>>
>>AJAX 最大的优点是在不重新加载整个页面的情况下，可以与服务器交换数据并更
>>
>>新部分网页内容。（这一特点给用户的感受是在不知不觉中完成请求和响应过程）
>>
>>AJAX 不需要任何浏览器插件，但需要用户允许JavaScript在浏览器上执行。
>>
>>- 同步交互：客户端发出一个请求后，需要等待服务器响应结束后，才能发出第
>>
>>  二个请求；
>>
>>- 异步交互：客户端发出一个请求后，无需等待服务器响应结束，就可以发出第
>>
>>  二个请求。
>>
>>#### **示例**
>>
>>**页面输入两个整数，通过AJAX传输到后端计算出结果并返回。**
>>
>>>html代码
>>>
>>>```
>>><!DOCTYPE html>
>>><html lang="en">
>>><head>
>>>  <meta charset="UTF-8">
>>>  <meta http-equiv="x-ua-compatible" content="IE=edge">
>>>  <meta name="viewport" content="width=device-width, initial-scale=1">
>>>  <title>AJAX局部刷新实例</title>
>>></head>
>>><body>
>>>
>>><input type="text" id="i1">+
>>><input type="text" id="i2">=
>>><input type="text" id="i3">
>>><input type="button" value="AJAX提交" id="b1">
>>>
>>><script src="/static/jquery-3.2.1.min.js"></script>
>>><script>
>>>  $("#b1").on("click", function () {
>>>    $.ajax({
>>>      url:"/ajax_add/",
>>>      type:"GET",
>>>      data:{"i1":$("#i1").val(),"i2":$("#i2").val()},
>>>      success:function (data) {
>>>        $("#i3").val(data);
>>>      }
>>>    })
>>>  })
>>></script>
>>></body>
>>></html>
>>>```
>>>
>>>views.py
>>>
>>>```
>>>def ajax_demo1(request):
>>>    return render(request, "ajax_demo1.html")
>>>
>>>
>>>def ajax_add(request):
>>>    i1 = int(request.GET.get("i1"))
>>>    i2 = int(request.GET.get("i2"))
>>>    ret = i1 + i2
>>>    return JsonResponse(ret, safe=False)
>>>```
>>>
>>>urls.py
>>>
>>>```
>>>urlpatterns = [
>>>    ...
>>>    url(r'^ajax_add/', views.ajax_add),
>>>    url(r'^ajax_demo1/', views.ajax_demo1),
>>>    ...   
>>>]
>>>```
>>
>>### Ajax常见应用场景
>>
>>>
>>>
>>>搜索引擎根据用户输入的关键字，自动提示检索关键字。
>>>
>>>还有一个很重要的应用场景就是注册时候的用户名的查重。
>>>
>>>其实这里就使用了AJAX技术！当文件框发生了输入变化时，使用AJAX技术向服
>>>
>>>务器发送一个请求，然后服务器会把查询到的结果响应给浏览器，最后再把后端
>>>
>>>返回的结果展示出来。
>>>
>>>- 整个过程中页面没有刷新，只是刷新页面中的局部位置而已！
>>>- 当请求发出后，浏览器还可以进行其他操作，无需等待服务器的响应！
>>>
>>>![](/Users/busensei/Desktop/ajax.png)
>>>
>>>当输入用户名后，把光标移动到其他表单项上时，浏览器会使用AJAX技术向服
>>>
>>>务器发出请求，服务器会查询名为lemontree7777777的用户是否存在，最终服
>>>
>>>务器返回true表示名为lemontree7777777的用户已经存在了，浏览器在得到结
>>>
>>>果后显示“用户名已被注册！”。
>>>
>>>- 整个过程中页面没有刷新，只是局部刷新了；
>>>- 在请求发出后，浏览器不用等待服务器响应结果就可以进行其他操作；
>>
>>### Ajax的优缺点
>>
>>>
>>>
>>>#### 优点：
>>>
>>>- AJAX使用JavaScript技术向服务器发送异步请求；
>>>- AJAX请求无须刷新整个页面；
>>>- 因为服务器响应内容不再是整个页面，而是页面中的部分内容，所以AJAX性能高；
>
>### jQuery实现Ajax
>
>>
>>
>>最基本的jQuery发送AJAX请求示例：
>>
>>```
>><!DOCTYPE html>
>><html lang="zh-CN">
>><head>
>>  <meta charset="UTF-8">
>>  <meta http-equiv="x-ua-compatible" content="IE=edge">
>>  <meta name="viewport" content="width=device-width, initial-scale=1">
>>  <title>ajax test</title>
>>  <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
>></head>
>><body>
>><button id="ajaxTest">AJAX 测试</button>
>><script>
>>  $("#ajaxTest").click(function () {
>>    $.ajax({
>>      url: "/ajax_test/",
>>      type: "POST",
>>      data: {username: "ward", password: 123456},
>>      success: function (data) {
>>        alert(data)
>>      }
>>    })
>>  })
>></script>
>></body>
>></html>
>>```
>>
>>#### views.py：
>>
>>```
>>def ajax_test(request):
>>    user_name = request.POST.get("username")
>>    password = request.POST.get("password")
>>    print(user_name, password)
>>    return HttpResponse("OK")
>>```
>>
>>###### $.ajax参数
>>
>>>
>>>
>>>data参数中的键值对，如果值值不为字符串，需要将其转换成字符串类型。
>>>
>>>```
>>>  $("#b1").on("click", function () {
>>>    $.ajax({
>>>      url:"/ajax_add/",
>>>      type:"GET",
>>>      data:{"i1":$("#i1").val(),"i2":$("#i2").val(),"hehe": JSON.stringify([1, 2, 3])},
>>>      success:function (data) {
>>>        $("#i3").val(data);
>>>      }
>>>    })
>>>  })
>>>```
>
>### Ajax请求如何设置csrf_token
>
>>
>>
>>方式一：
>>
>>>
>>>
>>>通过获取隐藏的input标签中的csrfmiddlewaretoken值，放置在data中发送。
>>>
>>>```
>>>$.ajax({
>>>  url: "/cookie_ajax/",
>>>  type: "POST",
>>>  data: {
>>>    "username": "Q1mi",
>>>    "password": 123456,
>>>    "csrfmiddlewaretoken": $("[name = 'csrfmiddlewaretoken']").val()  // 使用jQuery取出csrfmiddlewaretoken的值，拼接到data中
>>>  },
>>>  success: function (data) {
>>>    console.log(data);
>>>  }
>>>})
>>>```
>>
>>方式二：
>>
>>>
>>>
>>>通过获取返回的cookie中的字符串 放置在请求头中发送。
>>>
>>>注意：需要引入一个jquery.cookie.js插件。
>>>
>>>```
>>>$.ajax({
>>>  url: "/cookie_ajax/",
>>>  type: "POST",
>>>  headers: {"X-CSRFToken": $.cookie('csrftoken')},  // 从Cookie取csrftoken，并设置到请求头中
>>>  data: {"username": "ward", "password": 123456},
>>>  success: function (data) {
>>>    console.log(data);
>>>  }
>>>})
>>>```
>>>
>>>或者用自己写一个getCookie方法：
>>>
>>>```
>>>function getCookie(name) {
>>>    var cookieValue = null;
>>>    if (document.cookie && document.cookie !== '') {
>>>        var cookies = document.cookie.split(';');
>>>        for (var i = 0; i < cookies.length; i++) {
>>>            var cookie = jQuery.trim(cookies[i]);
>>>            // Does this cookie string begin with the name we want?
>>>            if (cookie.substring(0, name.length + 1) === (name + '=')) {
>>>                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
>>>                break;
>>>            }
>>>        }
>>>    }
>>>    return cookieValue;
>>>}
>>>var csrftoken = getCookie('csrftoken');
>>>
>>>function csrfSafeMethod(method) {
>>>  // these HTTP methods do not require CSRF protection
>>>  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
>>>}
>>>
>>>$.ajaxSetup({
>>>  beforeSend: function (xhr, settings) {
>>>    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
>>>      xhr.setRequestHeader("X-CSRFToken", csrftoken);
>>>    }
>>>  }
>>>});
>>>```
>>>
>>>每一次都这么写太麻烦了，可以使用$.ajaxSetup()方法为ajax请求统一设置。
>>>
>>>注意：
>>>
>>>如果使用从cookie中取csrftoken的方式，需要确保cookie存在csrftoken值。
>>>
>>>如果你的视图渲染的HTML文件中没有包含 {% csrf_token %}，Django可能不会设置CSRFtoken的cookie。
>>>
>>>这个时候需要使用ensure_csrf_cookie()装饰器强制设置Cookie。(加一个就行)
>>>
>>>```
>>>django.views.decorators.csrf import ensure_csrf_cookie
>>>
>>>@ensure_csrf_cookie
>>>def login(request):
>>>    pass
>>>```

## 序列化



### Django内置的serializers

```
def books_json(request):
    book_list = models.Book.objects.all()[0:10]
    from django.core import serializers
    ret = serializers.serialize("json", book_list)
    return HttpResponse(ret)
```