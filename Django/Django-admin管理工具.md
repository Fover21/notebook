# admin组件使用

>
>
>Django提供了基于web的管理工具
>
>Django 自动管理工具是 django.contrib 的一部分。你可以在项目的 settings.py 中的
>
> INSTALLED_APPS 看到它：
>
>```python
># Application definition
>
>INSTALLED_APPS = [
>    'django.contrib.admin',
>    'django.contrib.auth',
>    'django.contrib.contenttypes',
>    'django.contrib.sessions',
>    'django.contrib.messages',
>    'django.contrib.staticfiles',
>    "app01"
>]
>```
>
>django.contrib是一套庞大的功能集，它是Django基本代码的组成部分。



### 激活管理工具

>
>
>通常在生成项目的时候会在urls.py中自动设置好
>
>```python
>from django.conf.urls import url
>from django.contrib import admin
>
>urlpatterns = [
>    url(r'^admin/', admin.site.urls),
>
>]
>```
>
>当这一切配置好后，Django管理工具就可以运行了。





### 使用管理工具

>
>
>启动开发服务器，然后在浏览器中访问 http://127.0.0.1:8000/admin/，得到登陆界面，
>
>你可以通过命令 **python manage.py createsuperuser** 来创建超级用户。
>
>为了让 admin 界面管理某个数据模型，我们需要先注册该数据模型到 admin
>
>```python
>from django.db import models
>
># Create your models here.
>
>
>class Author(models.Model):
>
>    name=models.CharField( max_length=32)
>    age=models.IntegerField()
>
>
>    def __str__(self):
>        return self.name
>
>class Publish(models.Model):
>
>    name=models.CharField( max_length=32)
>    email=models.EmailField()
>
>    def __str__(self):
>        return self.name
>
>
>class Book(models.Model):
>
>    title = models.CharField( max_length=32)
>    publishDate=models.DateField()
>    price=models.DecimalField(max_digits=5,decimal_places=2)
>
>    publisher=models.ForeignKey(to="Publish")
>    authors=models.ManyToManyField(to='Author')
>
>    def __str__(self):
>        return self.title
>```





### admin的定制

>
>
>在admin中只需要将Model中的某个类注册，即可在Admin中实现增删改查的功能，如：
>
>```python
>admin.site.register(models.UserInfo)
>```
>
>但是这种方式比较简单，如果想进行更多的定制操作，需要利用ModelAdmin进行操作，
>
>如：
>
>```python
>方式一：
>    class UserAdmin(admin.ModelAdmin):
>        list_display = ('user', 'pwd',)
> 
>    admin.site.register(models.UserInfo, UserAdmin) # 第一个参数可以是列表
>     
> 
>方式二：
>    @admin.register(models.UserInfo)                # 第一个参数可以是列表
>    class UserAdmin(admin.ModelAdmin):
>        list_display = ('user', 'pwd',)
>```
>
>ModelAdmin中提供了大量的可定制功能，如：
>
>1. list_display，列表时，定制显示的列。
>
>```
>@admin.register(models.UserInfo)
>class UserAdmin(admin.ModelAdmin):
>    list_display = ('user', 'pwd', 'xxxxx')
> 
>    def xxxxx(self, obj):
>        return "xxxxx"
>```
>
>2. list_display_links，列表时，定制列可以点击跳转。
>
>```
>@admin.register(models.UserInfo)
>class UserAdmin(admin.ModelAdmin):
>    list_display = ('user', 'pwd', 'xxxxx')
>    list_display_links = ('pwd',)
>```
>
>3. list_filter，列表时，定制右侧快速筛选。
>
>4. list_select_related，列表时，连表查询是否自动select_related
>
>5. list_editable，列表时，可以编辑的列 
>
>```
>@admin.register(models.UserInfo)
>class UserAdmin(admin.ModelAdmin):
>    list_display = ('user', 'pwd','ug',)
>    list_editable = ('ug',)
>```
>
>6. search_fields，列表时，模糊搜索的功能
>
>```
>@admin.register(models.UserInfo)
>class UserAdmin(admin.ModelAdmin):
>     
>    search_fields = ('user', 'pwd')
>```
>
>7. date_hierarchy，列表时，对Date和DateTime类型进行搜索
>
>```
>@admin.register(models.UserInfo)
>class UserAdmin(admin.ModelAdmin):
> 
>    date_hierarchy = 'ctime'
>```
>
>8  inlines，详细页面，如果有其他表和当前表做FK，那么详细页面可以进行动态增加和删除
>
>```
>class UserInfoInline(admin.StackedInline): # TabularInline
>    extra = 0
>    model = models.UserInfo
> 
> 
>class GroupAdminMode(admin.ModelAdmin):
>    list_display = ('id', 'title',)
>    inlines = [UserInfoInline, ]
>```
>
>9 action，列表时，定制action中的操作
>
>```
>@admin.register(models.UserInfo)
>class UserAdmin(admin.ModelAdmin):
> 
>    # 定制Action行为具体方法
>    def func(self, request, queryset):
>        print(self, request, queryset)
>        print(request.POST.getlist('_selected_action'))
> 
>    func.short_description = "中文显示自定义Actions"
>    actions = [func, ]
> 
>    # Action选项都是在页面上方显示
>    actions_on_top = True
>    # Action选项都是在页面下方显示
>    actions_on_bottom = False
> 
>    # 是否显示选择个数
>    actions_selection_counter = True
>```
>
>10 定制HTML模板
>
>```
>add_form_template = None
>change_form_template = None
>change_list_template = None
>delete_confirmation_template = None
>delete_selected_confirmation_template = None
>object_history_template = None
>```
>
>11 raw_id_fields，详细页面，针对FK和M2M字段变成以Input框形式
>
>```
>@admin.register(models.UserInfo)
>class UserAdmin(admin.ModelAdmin):
> 
>    raw_id_fields = ('FK字段', 'M2M字段',)
>```
>
>12  fields，详细页面时，显示字段的字段
>
>```
>@admin.register(models.UserInfo)
>class UserAdmin(admin.ModelAdmin):
>    fields = ('user',)
>```
>
>13 exclude，详细页面时，排除的字段
>
>```
>@admin.register(models.UserInfo)
>class UserAdmin(admin.ModelAdmin):
>    exclude = ('user',)
>```
>
>14  readonly_fields，详细页面时，只读字段
>
>```
>@admin.register(models.UserInfo)
>class UserAdmin(admin.ModelAdmin):
>    readonly_fields = ('user',)
>```
>
>15 fieldsets，详细页面时，使用fieldsets标签对数据进行分割显示
>
>```
>@admin.register(models.UserInfo)
>class UserAdmin(admin.ModelAdmin):
>    fieldsets = (
>        ('基本数据', {
>            'fields': ('user', 'pwd', 'ctime',)
>        }),
>        ('其他', {
>            'classes': ('collapse', 'wide', 'extrapretty'),  # 'collapse','wide', 'extrapretty'
>            'fields': ('user', 'pwd'),
>        }),
>    )
>```
>
>16 详细页面时，M2M显示时，数据移动选择（方向：上下和左右）
>
>```
>@admin.register(models.UserInfo)
>class UserAdmin(admin.ModelAdmin):
>    filter_vertical = ("m2m字段",) # 或filter_horizontal = ("m2m字段",)
>```
>
>17 ordering，列表时，数据排序规则
>
>```
>@admin.register(models.UserInfo)
>class UserAdmin(admin.ModelAdmin):
>    ordering = ('-id',)
>    或
>    def get_ordering(self, request):
>        return ['-id', ]
>```
>
>\18. radio_fields，详细页面时，使用radio显示选项（FK默认使用select）
>
>```
>radio_fields = {"ug": admin.VERTICAL} # 或admin.HORIZONTAL
>```
>
>19 form = ModelForm，用于定制用户请求时候表单验证
>
>```
>from app01 import models
>from django.forms import ModelForm
>from django.forms import fields
> 
> 
>class MyForm(ModelForm):
>    others = fields.CharField()
> 
>    class Meta:
>        model = models = models.UserInfo
>        fields = "__all__"
> 
>@admin.register(models.UserInfo)
>class UserAdmin(admin.ModelAdmin):
> 
>    form = MyForm
>```
>
>20 empty_value_display = "列数据为空时，显示默认值"
>
>```
>@admin.register(models.UserInfo)
>class UserAdmin(admin.ModelAdmin):
>    empty_value_display = "列数据为空时，默认显示"
> 
>    list_display = ('user','pwd','up')
> 
>    def up(self,obj):
>        return obj.user
>    up.empty_value_display = "指定列数据为空时，默认显示"
>```
>
>例子：
>
>```python
>from django.contrib import admin
>
># Register your models here.
>
>from .models import *
>
>
>
>
>class BookInline(admin.StackedInline): # TabularInline
>    extra = 0
>    model = Book
>
>class BookAdmin(admin.ModelAdmin):
>
>    list_display = ("title",'publishDate', 'price',"foo","publisher")
>    list_display_links = ('publishDate',"price")
>    list_filter = ('price',)
>    list_editable=("title","publisher")
>    search_fields = ('title',)
>    date_hierarchy = 'publishDate'
>    preserve_filters=False
>
>    def foo(self,obj):
>
>        return obj.title+str(obj.price)
>
>
>
>    # 定制Action行为具体方法
>    def func(self, request, queryset):
>        print(self, request, queryset)
>        print(request.POST.getlist('_selected_action'))
>
>    func.short_description = "中文显示自定义Actions"
>    actions = [func, ]
>    # Action选项都是在页面上方显示
>    actions_on_top = True
>    # Action选项都是在页面下方显示
>    actions_on_bottom = False
>
>    # 是否显示选择个数
>    actions_selection_counter = True
>
>
>
>    change_list_template="my_change_list_template.html"
>
>
>
>class PublishAdmin(admin.ModelAdmin):
>     list_display = ('name', 'email',)
>     inlines = [BookInline, ]
>
>
>
>admin.site.register(Book, BookAdmin) # 第一个参数可以是列表
>admin.site.register(Publish,PublishAdmin)
>admin.site.register(Author)
>```
>
>

# admin源码解析

### 单例模式

>
>
>- 单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式主要目的是确保
>
>  某一个类只有一个实例存在。当我们希望在整个系统中，某个类只能出现一个实例
>
>  时，单例对象就能派上用场。
>
>  - 比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个APPConfig
>
>    的类来读取配置文件的信息。如果在程序运行期间，有很多地方需要使用配置文
>
>    件的内容，也就是说，很多地方都需要APPConfig的实例对象，而这样会严重浪费
>
>    内存资源，尤其是在配置文件内容很多的情况下。事实上，类似AppConfig这样的
>
>    类，我们希望在程序运行期间只存在一个实例对象。
>
>  - 在python中，我们可以用很多种方式来实现单例模式：
>
>    - 使用模块（模块的导入）
>    - 使用\__new__
>    - 使用装饰器（decorator）
>    - 使用元类（metaclass）
>
>    #### （1）使用\__new__
>
>    为了使类只能出现一个实例，我们可以使用\__new__来控制实例的创建过程，代码
>
>    如下：
>
>    ```python
>    class Singleton(object):
>        _instance = None
>        def __new__(cls, *args, **kw):
>            if not cls._instance:
>                cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)  
>            return cls._instance  
>    
>    class MyClass(Singleton):  
>        a = 1
>    ```
>
>    在上面的代码中，我们将类的实例和一个类变量_instance关联起来，如果cls._instance为None则创
>
>    建实例，否则直接返回cls._instance
>
>    执行情况：
>
>    ```python
>    >>> one = MyClass()
>    >>> two = MyClass()
>    >>> one == two
>    True
>    >>> one is two
>    True
>    >>> id(one), id(two)
>    (4303862608, 4303862608)
>    ```
>
>    #### (2)使用模块
>
>    其实，**Python 的模块就是天然的单例模式**，因为模块在第一次导入时，会生成 `.pyc` 文件，当
>
>    第二次导入时，就会直接加载 `.pyc` 文件，而不会再次执行模块代码。因此，我们只需把相关的
>
>    函数和数据定义在一个模块中，就可以获得一个单例对象了。如果我们真的想要一个单例类，可
>
>    以考虑这样做：
>
>    ```python
>    # mysingleton.py
>    class My_Singleton(object):
>        def foo(self):
>            pass
>     
>    my_singleton = My_Singleton()
>    ```
>
>    将上面的代码保存在文件 `mysingleton.py` 中，然后这样使用：
>
>    ```python
>    from mysingleton import my_singleton
>     
>    my_singleton.foo()
>    ```

### admin执行流程

>
>
>###### <1>循环加载执行所有已经注册的app中的admin.py文件
>
>```python
>def autodiscover():
>    autodiscover_modules('admin', register_to=site)
>```
>
>###### <2>执行代码
>
>```python
>＃admin.py
>
>class BookAdmin(admin.ModelAdmin):
>    list_display = ("title",'publishDate', 'price')
>
>admin.site.register(Book, BookAdmin) 
>admin.site.register(Publish)
>```
>
>###### <3>admin.site
>
>```python
>class AdminSite(object):...
>    
>
># This global object represents the default admin site, for the common case.
># You can instantiate AdminSite in your own code to create a custom admin site.
>site = AdminSite()
>```
>
>这里应用的是一个单例模式，对于AdminSite类的一个单例模式，执行的每一个app中的每一个admin.site
>
>都是一个对象。
>
>###### <4>执行register方法
>
>```python
>admin.site.register(Book, BookAdmin) 
>admin.site.register(Publish)
>
>class ModelAdmin(BaseModelAdmin):pass
>
>def register(self, model_or_iterable, admin_class=None, **options):
>    if not admin_class:
>            admin_class = ModelAdmin
>    # Instantiate the admin class to save in the registry
>    self._registry[model] = admin_class(model, self)
>
>```
>
>```python
># 思考：在每一个app的admin .py中加上
>
>print(admin.site._registry)   ＃ 执行结果？
>```
>
> 到这里，注册结束！
>
>###### <5>admin的URL配置
>
>```python
>urlpatterns = [
>    url(r'^admin/', admin.site.urls),
>]
>```
>
>```python
>class AdminSite(object):
>    
>     def get_urls(self):
>        from django.conf.urls import url, include
>      
>        urlpatterns = []
>
>        # Add in each model's views, and create a list of valid URLS for the
>        # app_index
>        valid_app_labels = []
>        for model, model_admin in self._registry.items():
>            urlpatterns += [
>                url(r'^%s/%s/' % (model._meta.app_label, model._meta.model_name), include(model_admin.urls)),
>            ]
>            if model._meta.app_label not in valid_app_labels:
>                valid_app_labels.append(model._meta.app_label)
>
>      
>        return urlpatterns
>
>    @property
>    def urls(self):
>        return self.get_urls(), 'admin', self.name
>```
>
>###### <6>url方法的扩展应用
>
>```python
>from django.shortcuts import HttpResponse
>def test01(request):
>    return HttpResponse("test01")
>
>def test02(request):
>    return HttpResponse("test02")
>
>urlpatterns = [
>    url(r'^admin/', admin.site.urls),
>    url(r'^ward/', ([
>                    url(r'^test01/', test01),
>                    url(r'^test02/', test02),
>
>                    ],None,None)),
>
>]
>```
>
>扩展优化
>
>```python
>from django.conf.urls import url,include
>from django.contrib import admin
>
>from django.shortcuts import HttpResponse
>
>def change_list_view(request):
>    return HttpResponse("change_list_view")
>def add_view(request):
>    return HttpResponse("add_view")
>def delete_view(request):
>    return HttpResponse("delete_view")
>def change_view(request):
>    return HttpResponse("change_view")
>
>def get_urls():
>
>    temp=[
>        url(r"^$".format(app_name,model_name),change_list_view),
>        url(r"^add/$".format(app_name,model_name),add_view),
>        url(r"^\d+/del/$".format(app_name,model_name),delete_view),
>        url(r"^\d+/change/$".format(app_name,model_name),change_view),
>    ]
>
>    return temp
>
>
>url_list=[]
>
>for model_class,obj in admin.site._registry.items():
>
>    model_name=model_class._meta.model_name
>    app_name=model_class._meta.app_label
>
>    # temp=url(r"{0}/{1}/".format(app_name,model_name),(get_urls(),None,None))
>    temp=url(r"{0}/{1}/".format(app_name,model_name),include(get_urls()))
>    url_list.append(temp)
>
>urlpatterns = [
>    url(r'^admin/', admin.site.urls),
>    url(r'^ward/', (url_list,None,None)),
>]
>```
>
>
>
>



