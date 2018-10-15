# 用户认知———auth模块



>### 一、auth模块

>from django.contrib import auth

>###### 1、authenticate()：验证用户输入的用户名和密码是否相同
>
>- 提供了用户认证，即__验证用户名以及密码是否正确__,一般需要usernamepassword两个关键字参数
>
>- 如果认证信息有效，会返回一个User对象。authenticate()会在User对象上设置一个属性标识，那
>
>  种认证，后端认证了该用户，且信息在后面的登录过程中是需要的。当我们试图登录一个从数据库
>
>  中直接取出来不经过authenticate()的User对象会报错的！！！
>
>###### 2、login(HttpRequest,user):登录
>
>- 该函数接受一个HttpRequest对象，以及一个认证的User对象
>
>- 此函数使用django的session框架给每个已认证的用户附加上session id等信息。
>
>  ```python
>  from django.contrib.auth import authenticate, login
>     
>  def my_view(request):
>    username = request.POST['username']
>    password = request.POST['password']
>    user = authenticate(username=username, password=password)
>    if user:
>      login(request, user)
>      # Redirect to a success page.
>      ...
>    else:
>      # Return an 'invalid login' error message.
>      ...
>  ```
>
>###### 3、logout(request):注销用户
>
>- 该函数接受一个HttpRequest对象，无返回值，当调用该函数是时，当请求的session信息会全部
>
>  清除。该用户即使没有登录，使用该函数也不会登录。
>
>  ```python
>  from django.contrib.auth import logout
>     
>  def logout_view(request):
>    logout(request)
>    # Redirect to a success page.
>  ```
>
>###### 4、user对象的is_authenticated()
>
>- 要求
>
>  - 用户登录后才能访问某些页面
>  - 如果用户没有登录就访问该页面的话直接跳转登录页面
>  - 用户在跳转的登录界面中完成登录后，自动访问跳转到之前访问的地址
>
>- 方法一
>
>  ```python
>  def my_view(request):
>    if not request.user.is_authenticated():
>      return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
>  ```
>
>- 方法二：django已经为我们设计好了一个用于次情况的装饰器：login_request()
>
>  ```python
>  from django.contrib.auth.decorators import login_required
>        
>  @login_required
>  def my_view(request):
>    ...
>  ```
>
>  若用户没有登录，则会跳转到django默认的登录URL'/account/login'(这个值可以在settings文件中
>
>  通过LOGIN_URL进行修改）。并传递当前访问url的绝对路径（登录成功后，会重定向该路径）

>### 二、User对象

>- User对象属性：
>
>  - username
>  - password（必填项）password用哈希算法保存到数据库
>  - is_staff：用户是否拥有网站的管理权限
>  - is_active：是否允许用户登录，设置为‘False’，可以不用删除用户来禁止用户登录
>
>- is_authenticated()
>
>  - 如果是真正的User对象，返回值恒为True。用于检测用户是否已经通过认证。
>
>  - 通过认证并不意味着用户拥有任何权限，甚至也不检查该用户是否处于激活状态，这只是表明
>
>    用户成功通过了认证。
>
>    - 这个方法很重要，在后台使用
>    - request.user.is_authenticated()判断用户是否已经登录，如果True则可以向前台展示
>    - -request.user.name
>
>- 创建用户**create_user** 
>
>  ```python
>  from django.contrib.auth.models import User
>  user = User.objects.create_user（username='',password='',email=''）
>  ```
>
>- check_passw(passwd):密码检测
>
>  用户需要修改密码的时候 首先要让他输入原来的密码 ，如果给定的字符串通过了密码检查，返回 
>
>  True
>
>- 修改密码：set_password()
>
>  ```python
>  user = User.objects.get(username='')
>  user.set_password(password='')
>  user.save　
>  ```
>

### 三、简单实例

>
>
>登录：
>
>```python
>def log_in(request):
>    print(request.POST)
>    if request.method =="POST":
>        username = request.POST.get("username")
>        password = request.POST.get("password")
>        print(username,password)
>        user=auth.authenticate(username=username,password=password)#验证用户名和密码
>        if user:
>            #如果认证成功，就让登录，这个login里面包括了session操作和cookie
>            auth.login(request,user)
>            return redirect("/chakan/")
>        else:
>            s = "用户名和密码输入错误"
>            return render(request,"login.html",{"s":s})
>    return render(request,"login.html")
>```
>
>
>
>修改密码：
>
>```python
>def set_pwd(request):
>    if request.method=="POST":
>        oldpassword = request.POST.get("oldpassword")
>        newpassword = request.POST.get("newpassword")
>        #得到当前登录的用户，判断旧密码是不是和当前的密码一样
>        username = request.user  #打印的是当前登录的用户名
>        user = User.objects.get(username=username)  #查看用户
>        ret = user.check_password(oldpassword)  #检查密码是否正确
>        if ret:
>            user.set_password(newpassword) #如果正确就给设置一个新密码
>            user.save()  #保存
>            return redirect("/login/")
>        else:
>            info = "输入密码有误"
>            return render(request,"set_pwd.html",{"info":info})
>    return render(request,"set_pwd.html")
>```
>
>
>
>注册：
>
>```python
>def reg(request):
>    if request.method=="POST":
>        username = request.POST.get("username")
>        password = request.POST.get("password")
>        #得到用户输入的用户名和密码创建一个新用户
>        User.objects.create_user(username=username,password=password)  #User是以个对象
>        s = "恭喜你注册成功，现在可以登录了"
>        return redirect("/login/")
>    return render(request,"reg.html")
>```
>
>
>
>注销：
>
>```python
>def log_out(request):
>    auth.logout(request)
>    return redirect("/login/")
>```