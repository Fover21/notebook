# Ajax实现文件的上传

>
>
>### 准备
>
>>
>>
>>###### ajax的参数补充
>>
>>>
>>>
>>>- type不写的话默认是GET
>>>
>>>- dataType和ContentType：
>>>
>>>　　　　dataType: 浏览器发给服务器希望返回的数据类型 。。
>>>
>>>​				如果明确地指定目标类型，就可以使用data Type。
>>>
>>>　　　　ContentType:
>>>　　　　　　请求头里有：浏览器告诉服务器内容的类型
>>>
>>>　　　　　　响应头里也有：服务器响应浏览器的内容
>>
>>###### JS和JQuery之间的转换
>>
>>>
>>>
>>>- jQuery对象加[0]就转换成了dom对象
>>>- dom对象加$符就转换成了jquery对象
>>
>>###### processDate
>>
>>>
>>>
>>>- processDate 默认为True ，预处理；     如果改为False，不做预处理
>
>### csrf跨站请求伪造
>
>>
>>
>>如果把type:"GET"  改为type:"POST" 会报一个Forbidden的错
>>
>>解决办法有三种：
>>
>>方式一：
>>
>>```
>>     $.ajaxSetup({
>>            data:{csrfmiddlewaretoken:'{{ csrf_token }}'}
>>        });
>>     注意：要放在ajax请求的前面，在发送之前组装一组字符串，在第一步render的时候就发了
>>     所以有局限性：
>>        如果把JS代码放到静态文件中，不会渲染，不会执行{{csrf_token}},只能在HTML页面中使用
>>```
>>
>>方式二：自己组装一组键值对  （ 推荐）
>>
>>```
>><form>
>>{% csrf_token %}
>></form>
>>  data:{
>>        csrfmiddlewaretoken:$("[name='csrfmiddlewaretoken']").val(),
>>        name:$(":text").val(),
>>        pwd:$(":password").val()
>>  },
>>```
>>
>>方式三：自己设置头信息
>>
>>```
>><script src="https://cdn.bootcss.com/jquery-cookie/1.4.1/jquery.cookie.js"></script>
>>
>> $.ajax({
>>            url:"/serialize/",
>>            type:"POST",
>>            headers:{"X-CSRFToken":$.cookie('csrftoken')},
>>        })
>>```
>
>### JQuery.serialize()
>
>>
>>
>>`serialize()`函数用于**序列化一组表单元素，将表单内容编码为用于提交的字符串**。
>>
>>`serialize()`函数常用于将表单内容序列化，以便用于AJAX提交。
>>
>>该函数主要根据**用于提交**的**有效**表单控件的name和value，将它们拼接为一个可直接用于表单提交的文本
>>
>>字符串，该字符串已经过标准的URL编码处理(字符集编码为UTF-8)。
>>
>>该函数不会序列化不需要提交的表单控件，这和常规的表单提交行为是一致的。例如：不在<form>标签内
>>
>>的表单控件不会被提交、没有name属性的表单控件不会被提交、带有disabled属性的表单控件不会被提
>>
>>交、没有被选中的表单控件不会被提交。
>>
>>```
>>与常规表单提交不一样的是：常规表单一般会提交带有name的按钮控件，而serialize()函数不会序列化带有name的按钮控件。更多详情请点击这里。
>>```
>>
>>语法：
>>
>>```
>>jQueryObject.serialize( )
>>```
>>
>>`serialize()`函数的返回值为String类型，返回将表单元素编码后的可用于表单提交的文本字符串。
>>
>>请参考下面这段初始HTML代码：
>>
>>```
>><form name="myForm" action="http://www.365mini.com" method="post">
>>    <input name="uid" type="hidden" value="1" />
>>    <input name="username" type="text" value="张三" />
>>    <input name="password" type="text" value="123456" />
>>    <select name="grade" id="grade">
>>        <option value="1">一年级</option>
>>        <option value="2">二年级</option>
>>        <option value="3" selected="selected">三年级</option>
>>        <option value="4">四年级</option>
>>        <option value="5">五年级</option>
>>        <option value="6">六年级</option>
>>    </select>
>>    <input name="sex" type="radio" checked="checked" value="1" />男
>>    <input name="sex" type="radio" value="0" />女
>>    <input name="hobby" type="checkbox" checked="checked" value="1" />游泳
>>    <input name="hobby" type="checkbox" checked="checked" value="2" />跑步
>>    <input name="hobby" type="checkbox" value="3" />羽毛球
>>    <input name="btn" id="btn" type="button" value="点击" />
>></form>
>>```
>>
>> 对<form>元素进行序列化可以直接序列化其内部的所有表单元素。
>>
>>```
>>// 序列化<form>内的所有表单元素
>>// 序列化后的结果：uid=1&username=%E5%BC%A0%E4%B8%89&password=123456&grade=3&sex=1&hobby=1&hobby=2
>>alert( $("form").serialize() );
>>```
>>
>>我们也可以直接对部分表单元素进行序列化。
>>
>>```
>>// 序列化所有的text、select、checkbox表单元素
>>// 序列化后的结果：username=%E5%BC%A0%E4%B8%89&password=123456&grade=3&hobby=1&hobby=2
>>alert( $(":text, select, :checkbox").serialize() );
>>```
>>
>>示例：
>>
>>```
>> 1 <!DOCTYPE html>
>> 2 <html lang="en">
>> 3 <head>
>> 4     <meta charset="UTF-8">
>> 5     <meta http-equiv="X-UA-Compatible" content="IE=edge">
>> 6     <meta name="viewport" content="width=device-width">
>> 7     <title>Title</title>
>> 8 </head>
>> 9 <body>
>>10 <form name="myForm" action="http://www.365mini.com" method="post">
>>11     <input name="uid" type="hidden" value="1" />
>>12     <input name="username" type="text" value="张三" />
>>13     <input name="password" type="text" value="123456" />
>>14     <select name="grade" id="grade">
>>15         <option value="1">一年级</option>
>>16         <option value="2">二年级</option>
>>17         <option value="3" selected="selected">三年级</option>
>>18         <option value="4">四年级</option>
>>19         <option value="5">五年级</option>
>>20         <option value="6">六年级</option>
>>21     </select>
>>22     <input name="sex" type="radio" checked="checked" value="1" />男
>>23     <input name="sex" type="radio" value="0" />女
>>24     <input name="hobby" type="checkbox" checked="checked" value="1" />游泳
>>25     <input name="hobby" type="checkbox" checked="checked" value="2" />跑步
>>26     <input name="hobby" type="checkbox" value="3" />羽毛球
>>27     <input name="btn" id="btn" type="button" value="点击" />
>>28 </form>
>>29 <script src="/static/jquery-3.2.1.min.js"></script>
>>30 <script src="https://cdn.bootcss.com/jquery-cookie/1.4.1/jquery.cookie.js"></script>
>>31 <script>
>>32     $("#btn").click(function () {
>>33 {#        方式一#}
>>34         //$.ajaxSetup({
>>35           // data:{csrfmiddlewaretoken:'{{ csrf_token }}'}
>>36         //});
>>37         $.ajax({
>>38             url:"/serialize/",
>>39             type:"POST",
>>40 {#            方式三#}
>>41             headers:{"X-CSRFToken":$.cookie('csrftoken')},
>>42             //data:$("form").serialize(),   //序列form表单所有的
>>43             data:$(":text,:password,:checkbox").serialize(),  //序列自己选择的
>>44             success:function (data) {
>>45                 var data=JSON.parse(data);  //js中的反序列化
>>46                 console.log(data);
>>47                 console.log(typeof data);
>>48                 $(".error").html(data);
>>49             }
>>50         })
>>51     })
>>52 </script>
>>53 </body>
>>54 </html>
>>```
>>
>>
>>
>>```
>>1 def serialize(request):
>>2     # form = request.POST
>>3     # print(form)
>>4     name = request.POST.get("username")
>>5     password = request.POST.get("password")
>>6     checked = request.POST.getlist("hobby")
>>7     print(name,password,checked)
>>8     return HttpResponse(json.dumps(name))
>>```
>>
>>```
>>当有好多input的时候，就得一一对应的吧所有的数据发过去的，这样显得麻烦，我们用序列化
>>jQuery.serialize()
>>
>>data:$("form").serialize(),   //序列form表单所有的
>>data:$(":text,:password,:checkbox").serialize(),  //序列自己选择的
>>
>>在服务端获取数据
>>form = request.POST   
>>print(form)   #获取所有
>>name = request.POST.get("username")
>>password = request.POST.get("password")
>>checked = request.POST.getlist("hobby")
>>print(name,password,checked)#获取单个
>>```
>
># 文件上传：
>
>>
>>
>>**1、Form表单上传文件**
>>
>>文件和其他的数据类型不一样，是一个二进制的形式
>>Form上传文件的时候切记要加上：**enctype="multipart/form-data"**
>>
>>formupload.html
>>
>>```
>><form action="/formupload/" method="post" enctype="multipart/form-data">
>>    {% csrf_token %}
>>    <p>姓名：<input type="text" name="username"></p>
>>    <p>密码：<input type="password" name="password"></p>
>>    <p>头像：<input type="file" name="file"></p>
>>    <p><input type="submit" value="提交"></p>
>></form>
>>```
>>
>>view.py
>>
>>```
>>def formupload(request):
>>    if request.method == "POST":
>>        username = request.POST.get("username")
>>        password = request.POST.get("password")
>>        # file = request.FILES   #拿到的是一个句柄
>>        file_obj = request.FILES.get("file")
>>        print(file_obj,file_obj.name)
>>        print(type(file_obj),type(file_obj.name))   #<class 'django.core.files.uploadedfile.InMemoryUploadedFile'>   <class 'str'>
>>        with open(file_obj.name,"wb") as f:
>>            for i in file_obj:
>>                f.write(i)
>>        return HttpResponse("上传成功...")
>>    return render(request,"formupload.html")
>>```
>>
>>**2、Ajax上传文件（利用FormData）：***既可以处理二进制，又可以处理字典，列表啊等*
>>
>>FormData是什么呢？
>>
>>XMLHttpRequest Level 2添加了一个新的接口`FormData`.利用`FormData对象`,我们可以通过JavaScript用
>>
>>一些键值对来模拟一系列表单控件,我们还可以使用XMLHttpRequest的`send()`方法来异步的提交这个"表
>>
>>单".比起普通的ajax,使用`FormData`的最大优点就是我们可以异步上传一个二进制文件.
>>
>>所有主流浏览器的较新版本都已经支持这个对象了，比如Chrome 7+、Firefox 4+、IE 10+、Opera 12+、
>>
>>Safari 5+。
>>
>>注意：下文中的几个需要解释的
>>
>>```
>>$("#upload") 拿到的是一个集合
>>$("#upload")[0]  就是一个dom对象
>>$("#upload")[0].files   拿到的是一个filelist
>>$("#upload")[0].files[0]  拿到的是当前最近的文件对象 
>>```
>>
>>要是使用FormData一定要加上：
>>
>>一定要加上：
>>
>>　　contentType：false 
>>　　processDate：false #不做预处理
>>
>>ajaxupload.html
>>
>>```
>><!DOCTYPE html>
>><html lang="en">
>><head>
>>    <meta charset="UTF-8">
>>    <meta http-equiv="X-UA-Compatible" content="IE=edge">
>>    <meta name="viewport" content="width=device-width">
>>    <title>Title</title>
>></head>
>><body>
>><p>姓名<input type="text" name="username"></p>
>><p>头像<input type="file" id="upload"></p>
>><p><button class="btnnn">提交</button><span class="tishi"></span></p>
>><script src="/static/jquery-3.2.1.min.js"></script>
>><script src="https://cdn.bootcss.com/jquery-cookie/1.4.1/jquery.cookie.js"></script>
>><script>
>>    $(".btnnn").click(function () {
>>         var formData=new FormData();
>>        formData.append("username",$(":text").val());
>>        formData.append("file",$("#upload")[0].files[0]);
>>        $.ajax({
>>            url:"/get_upload/",
>>            type:"POST",
>>            headers:{"X-CSRFToken":$.cookie('csrftoken')},
>>            data:formData,
>>            contentType:false,
>>            processData:false,
>>            success:function (data) {
>>                $(".tishi").html("上传成功")
>>            }
>>
>>        })
>>    })
>></script>
>></body>
>></html>
>>```
>>
>> view.py
>>
>>```
>>def ajaxupload(request):
>>    return render(request,"ajaxupload.html")
>>
>>def get_upload(request):
>>    if request.method == "POST":
>>        print("FIFLE", request.FILES)
>>        file_obj = request.FILES.get("file")
>>        print(file_obj.name, "-----")
>>        file_obj = request.FILES.get("file")
>>        with open(file_obj.name, "wb") as f:
>>            for i in file_obj:
>>                f.write(i)
>>        return HttpResponse("上传成功")
>>```

