# 基于AJax实现的登录

### 一、需要知道的知识点

>
>
>1、刷新验证码。给src属性加一个？号。加个？会重新去请求
>
>```html
> //给验证码刷新
>        $(".vialdCode_img").click(function () {
>         方式一：dom方法
>            $(this)[0].src+="?"}
>         方式二：jQuery的attr方法
>            $(this).attr("src",$(this).attr("src")+'?')
>        })
>    })
>```
>
>2、当登录成功跳转，或者注册成功跳转
>
>```html
> $(".register").click(function () {
>            location.href = '/register/'
>  });
>```
>
>3、超时后消失
>
>```html
>setTimeout(foo, 3000)
>function foo() {
>                $(".error").html("")
>            }
>```
>
>4、auth模块的使用
>
>```python
>from django.contrib import auth
>```
>
>>几个常用方法：
>>
>>1、authenticate():验证用户输入的用户名和密码是否相同
>>
>>提供了用户认证，即验证用户名以及密码是否是正确，一般需要username password两个关键字参数
>>
>>```python
>>user = authenticate(username='someone',password='somepassword')
>>```
>>
>>2、login(HttpRequest, user):登录
>>
>>该函数接受一个HttpRequest对象，以及一个认证了的User对象
>>
>>此函数使用django的session框架给某个已认证的用户附加上session id等信息。
>>
>>```python
>>from django.contrib.auth import authenticate, login
>>   
>>def my_view(request):
>>  username = request.POST['username']
>>  password = request.POST['password']
>>  user = authenticate(username=username, password=password)
>>  if user:
>>    login(request, user)
>>    # Redirect to a success page.
>>    ...
>>  else:
>>    # Return an 'invalid login' error message.
>>    ...
>>```
>>
>>3、logout(request):注销用户
>>
>>该函数接受一个HttpRequest对象，无返回值。当调用该函数时，当前请求的session信息会全部清除。该
>>
>>用户即使没有登录，使用该函数也不会报错。
>>
>>```python
>>from django.contrib.auth import logout
>>   
>>def logout_view(request):
>>  logout(request)
>>  # Redirect to a success page.
>>```
>>
>>4、user对象的is_authenticated()
>>
>>要求：
>>
>>　　1、用户登录后才能访问某些页面
>>
>>　　2、如果用户没有登录就访问该页面的话直接跳转登录页面
>>
>>　　3、用户在跳转的登录界面中完成登录后，自动访问跳转到之前访问的地址
>>
>>```python
>>def my_view(request):
>>  if not request.user.is_authenticated():
>>    return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
>>```
>>
>>在后台用request.user.is_authenticated()判断用户是否已经登录，如果true则可以向前台展示
>>
>>request.user.name
>>
>>### User对象的几个方法
>>
>>1、创建用户:create_user
>>
>>```python
>>from django.contrib.auth.models import User
>>user = User.objects.create_user（username='',password='',email=''）
>>```
>>
>>2、check_password(password):密码检查
>>
>>用户需要修改密码的时候，需要先让他输入原来的密码，如果给定的字符串通过了密码检测，返回True
>>
>>3、修改密码：set_password()
>>
>>```python
>>user = User.objects.get(username='')
>>user.set_password(password='')
>>user.save　
>>```

### 二、具体实现的登录

> - urlspy
>
>   ```python
>   urlpatterns = [
>        url(r'^admin/', admin.site.urls),
>        url(r'^login/$', views.login),
>        url(r'^index/$', views.index),
>        url(r'^get_vaildCode_img/$', views.get_vaildCode_img),
>        url(r'^log_out/$', views.log_out),
>   ]
>   ```
>
> - view.py
>
>   ```python
>   def login(request):
>       if request.method=="GET":
>           return render(request, "login.html")
>       else:
>           username = request.POST.get("username")
>           password = request.POST.get("password")
>           vialdCode = request.POST.get("vialdCode")
>           ret = {"flag":False,"error_msg":None}
>           if vialdCode.upper() == request.session.get("keep_valid_code").upper():
>               user = auth.authenticate(username=username, password=password)
>               if user:
>                   #如果验证成功就让登录
>                   auth.login(request,user)
>                   ret["flag"] = True
>               else:
>                   ret["error_msg"] = "用户名和密码错误"
>           else:
>               ret["error_msg"] = "验证码错误"
>       return HttpResponse(json.dumps(ret))
>   
>   def index(request):
>       #验证是不是当前进来的那个用户，如果用户已经登录了就可以看到页面
>       # 如果没有登录就不让看见主页面，就直接返回登录页面
>       if not request.user.is_authenticated():
>           return redirect("/login/")
>       else:
>           return render(request, "index.html")
>   
>   def log_out(request):
>       auth.logout(request)
>       return redirect("/login/")
>   def get_vaildCode_img(request):
>       # 方式一：这样的方式吧路径写死了，只能是那一张图片
>       # import os
>       # path = os.path.join(settings.BASE_DIR,"static","image","3.jpg")
>       # with open(path,"rb") as f:
>       #     data = f.read()
>       # return HttpResponse(data)
>       # 方式二：每次都显示不同的图片，利用pillow模块，安装一个pillow模块
>       # from PIL import Image
>       # img = Image.new(mode="RGB",size=(120,40),color="green") #首先自己创建一个图片,参数size=(120,40) 代表长和高
>       # f = open("validcode.png","wb")#然后把图片放在一个指定的位置
>       # img.save(f,"png")  #保存图片
>       # f.close()
>       # with open("validcode.png","rb") as f:
>       #     data = f.read()
>       # return HttpResponse(data)
>       # 方式三：
>       # 方式二也不怎么好，因为每次都要创建一个保存图片的文件，我们可以不让吧图片保存到硬盘上，
>       # 在内存中保存，完了自动清除，那么就引入了方式三：利用BytesIO模块
>       # from io import BytesIO
>       # from PIL import Image
>       # img = Image.new(mode="RGB",size=(120,40),color="blue")
>       # f = BytesIO()  #内存文件句柄
>       # img.save(f,"png")  #保存文件
>       # data = f.getvalue()#打开文件(相当于python中的f.read())
>       # return HttpResponse(data)
>   
>       # 方式四：1、添加画笔，也就是在图片上写上一些文字
>       #         2、并且字体随机，背景颜色随机
>       from io import BytesIO
>       from PIL import Image,ImageDraw,ImageFont
>       import random
>       #随机创建图片
>       img = Image.new(mode="RGB",size=(120,40),color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
>       draw = ImageDraw.Draw(img,"RGB")
>       # 画干扰线
>       for i in range(5):
>           x1 = random.randint(0, 120)
>           y1 = random.randint(0, 40)
>           x2 = random.randint(0, 120)
>           y2 = random.randint(0, 40)
>   
>           draw.line((x1, y1, x2, y2), fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
>   
>       font = ImageFont.truetype("static/font/kumo.ttf",20)  #20表示20像素
>   
>       str_list = []  #吧每次生成的验证码保存起来
>       # 随机生成五个字符
>       for i in range(5):
>           random_num = str(random.randint(0, 9))  # 随机数字
>           random_lower = chr(random.randint(65, 90))  # 随机小写字母
>           random_upper = chr(random.randint(97, 122))  # 随机大写字母
>           random_char = random.choice([random_num, random_lower, random_upper])
>           print(random_char,"random_char")
>           str_list.append(random_char)
>           # (5 + i * 24, 10)表示坐标，字体的位置
>           draw.text((5+i*24,10),random_char,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),font=font)
>       print(str_list,"str_list")
>       f = BytesIO()#内存文件句柄
>       img.save(f,"png")   #img是一个对象
>       data = f.getvalue()  #读取数据并返回至HTML
>       valid_str = "".join(str_list)
>       print(valid_str,"valid_str")
>       request.session["keep_valid_code"] = valid_str   #吧保存到列表的东西存放至session中
>       return HttpResponse(data)
>   ```
>
> - template
>
>   - login.html
>
>     ```html
>     <!DOCTYPE html>
>     <html lang="en">
>     <head>
>         <meta charset="UTF-8">
>         <meta http-equiv="X-UA-Compatible" content="IE=edge">
>         <meta name="viewport" content="width=device-width">
>         <title>Title</title>
>         <link rel="stylesheet" href="/static/bootstrap-3.3.7-dist/css/bootstrap.min.css">
>         <link rel="stylesheet" href="/static/css/login.css">
>     </head>
>     <body>
>     <div class="container">
>         <div class="row">
>             <div class="col-md-1=10">
>                 <form class="form-horizontal" id="form_data" action="/login/" method="post">
>                     {% csrf_token %}
>                     <div class="form-group">
>                         <label for="username" class="col-sm-2 control-label">用户名</label>
>                         <div class="col-sm-5">
>                             <input type="text" class="form-control" id="username" placeholder="username" name="username">
>                         </div>
>                     </div>
>                     <div class="form-group">
>                         <label for="password" class="col-sm-2 control-label">密码</label>
>                         <div class="col-sm-5">
>                             <input type="password" class="form-control" id="password" placeholder="password" name="password">
>                         </div>
>                     </div>
>                     <div class="form-group">
>                         <div class="row">
>                             <div class="col-md-6 col-md-offset-1">
>     {#                            文字部分#}
>                                 <label for="vialdCode" class="col-sm-2 control-label">验证码</label>
>                                  <div class="col-sm-5">
>                                     <input type="text" class="form-control vialdCode_text" id="vialdCode" placeholder="验证码" name="vialdCode">
>                                 </div>
>     {#                            图片部分#}
>                                  <div class="col-md-5">
>                                 <img class="vialdCode_img" src="/get_vaildCode_img/" alt="" width="200px" height="100px">
>     {#                                 <a href=""></a>     #}
>                             </div>
>                             </div>
>     
>                         </div>
>                     </div>
>                     <div class="form-group">
>                         <div class="col-sm-offset-2 col-sm-10">
>                             <div class="checkbox">
>                                 <label>
>                                     <input type="checkbox"> 下次自动登录
>                                 </label>
>                             </div>
>                         </div>
>                     </div>
>                     <div class="form-group">
>                         <div class="col-sm-offset-2 col-sm-10">
>                             <p>
>                                 <button type="button" class="btn btn-success login">登录</button>
>                                 <span class="error has-error"></span></p>
>                             <p>
>                                 <button type="button" class="btn btn-primary register">注册</button>
>                             </p>
>                         </div>
>                     </div>
>                 </form>
>             </div>
>         </div>
>     </div>
>     <script src="/static/jquery-3.2.1.min.js"></script>
>     <script src="/static/bootstrap-3.3.7-dist/js/bootstrap.min.js"></script>
>     <script src="https://cdn.bootcss.com/jquery-cookie/1.4.1/jquery.cookie.js"></script>
>     
>     <script>
>         $(function () {
>             //给登录按钮增加事件
>             $(".login").click(function () {
>                 function foo() {
>                     $(".error").html("")
>                 }
>     
>                 //用post的话就可以不用ajax了，ajax里面都包括了
>                 $.post({
>                     url: '/login/',
>                     headers: {"X-CSRFToken": $.cookie('csrftoken')},
>                     data: $("#form_data").serialize(),
>                     {#            contentType:'application/json',#}
>                     success: function (data) {
>                         var data = JSON.parse(data);
>                         console.log(typeof data);
>                         if (data["flag"]) {
>                             window.location.href = '/index/'
>                         }
>                         else {
>                             $(".error").html(data["error_msg"]);
>                             setTimeout(foo, 3000)
>                         }
>                     }
>                 })
>             });
>     
>             //给注册按钮增加事件
>             $(".register").click(function () {
>                 window.location.href = '/register/'
>             });
>     
>             //#给验证码刷新
>             $(".vialdCode_img").click(function () {
>     {#            方式一：dom方法#}
>     {#            $(this)[0].src+="?"#}
>     {#            方式二：jQuery的attr方法#}
>                 $(this).attr("src",$(this).attr("src")+'?')
>             })
>         })
>     
>     </script>
>     </body>
>     </html>
>     ```
>
>   - index.html
>
>     ```html
>     <!DOCTYPE html>
>     <html lang="en">
>     <head>
>         <meta charset="UTF-8">
>         <meta http-equiv="X-UA-Compatible" content="IE=edge">
>         <meta name="viewport" content="width=device-width">
>         <title>Title</title>
>     </head>
>     <body>
>     <h1>hello{{ request.user.username }}</h1>
>     <button><a href="/log_out/">注销</a></button>
>     </body>
>     </html>
>     ```
>
>   - login.css
>
>     ```html
>     .container {
>         margin-top: 100px;
>         margin-left: 330px;
>     }
>     
>     .error {
>         color: red;
>     }
>     
>     .btn {
>         width: 200px;
>     }
>     .vialdCode_img{
>         width: 200px;
>         height: 40px;
>     }
>     ```
>