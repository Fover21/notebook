- 创建app应用与ORM操作

	- Django项目project
		- app（应用） -> 不同的功能放在不同的app中
			- 命令 ：
				- 创建app  
					python manage.py startapp app(应用名)	
				- 告诉Django创建了app
					在settings中的 INSTALLED_APPS 添加新创建的app（app名.apps.apps中的类）
						# 我这个项目有哪些app
						INSTALLED_APPS = [
						    'django.contrib.admin',
						    'django.contrib.auth',
						    'django.contrib.contenttypes',
						    'django.contrib.sessions',
						    'django.contrib.messages',
						    'django.contrib.staticfiles', 
						    'app.apps.AppConfig',  # 告诉Django我创建了一个app  # 以上都是系统自带的
						]
	- Django中ORM使用
		- 用处：
			- 操作数据表
			- 操作数据行
		- 使用
			- 手动创建数据库（数据库需要自己创建）
			- 告诉Django连那个数据库
				- settings中配置DATABASES
				DATABASES = {
				    'default': {
				        'ENGINE': 'django.db.backends.mysql',  # 链接数据库的类型
				        'NAME': 'db',  # 链接数据库的名字
				        'HOST': '127.0.0.1',  # 数据库主机地址
				        'PORT': 3306,  # 数据库端口
				        'USER': 'root',  # 数据库用户名
				        'PASSWORD': '123456',  # 数据库密码
				    }
				}

			- 用什么链接数据库？
				- 利用第三方包 pymysql 和 MySQLdb(py2中)
				- 告诉Django用pymysql模块代替默认的MySQLdb链接MySQL数据库
					和settings.py同级的__init__.py文件，写上
					import pymysql
					pymysql.install_as_MySQLdb()

			- 在app/models.py的文件中创建类
				类必须继承models.Model

					from django.db import models
					# Create your models here.
					# 类名就是表名，属性就是字段，一个对象就是一行数据
					class User(models.Model):
					    id = models.AutoField(primary_key=True)  # 创建一个自增的id列作为主键
					    email = models.CharField(max_length=32)  # varchar(32)
					    pwd = models.CharField(max_length=32)  # varchar(32)

			- 两个命令
				- 类在models中建好之后执行以下操作
				- python manage.py makemigrations
				  -> 相当于拿个小本本把models.py的变更记录下来（存放在app目录下的migrations目录中）
				- python manage.py migrate 
				  -> 把上面的变更记录翻译成sql语句，去数据库执行

			- ORM查询
				User.object.filter(email='', pwd='')



- 网站输入url提交表单流程：
	- 刚开始是get请求，服务器给响应返回一个页面
	- 输入数据提交表单，这个时候就会提交到form表单对应的action所指的url
	- 这个时候Django收到后就在urls.py文件中urlpatterns列表中找匹配的url
	- 找到后去匹配的url后找对应的视图函数
	- 在视图函数中写业务逻辑（必须有一个request参数，它存放的是表单的数据）
		- 可以通过request.method方法来进行条件判断
		- return redirect('/homework/')  # 返回的是url
		- return render(request, 'loginhtml', {'error_msg': error_msg}) 
			 # 返回的是html文件  最后的参数是html文件中的变量 俗称：模板语言  键是html文件中的变量（俗称模板语言）
		- return HttpResponse("成功")  #直接给页面返回信息




- 创建项目到创建应用流程
	- 创建项目
		- Django-admin startproject first_Django（项目名）
	- 创建app  
		- python manage.py startapp app(应用名)	
			- 告诉Django创建了app
				在settings中的 INSTALLED_APPS 添加新创建的app（app名.apps.apps中的类）
					# 我这个项目有哪些app
					INSTALLED_APPS = [
					    'django.contrib.admin',
					    'django.contrib.auth',
					    'django.contrib.contenttypes',
					    'django.contrib.sessions',
					    'django.contrib.messages',
					    'django.contrib.staticfiles', 
					    'app.apps.AppConfig',  # 告诉Django我创建了一个app  # 以上都是系统自带的
					]

	- Django中ORM使用
		- 用处：
			- 操作数据表
			- 操作数据行
		- 使用
			- 手动创建数据库
			- 告诉Django连那个数据库
				- settings中配置DATABASES
				DATABASES = {
				    'default': {
				        'ENGINE': 'django.db.backends.mysql',  # 链接数据库的类型
				        'NAME': 'db',  # 链接数据库的名字
				        'HOST': '127.0.0.1',  # 数据库主机地址
				        'PORT': 3306,  # 数据库端口
				        'USER': 'root',  # 数据库用户名
				        'PASSWORD': '123456',  # 数据库密码
				    }
				}

			- 用什么链接数据库？
				- 利用第三方包 pymysql 和 MySQLdb(py2中)
				- 告诉Django用pymysql模块代替默认的MySQLdb链接MySQL数据库
					和settings.py同级的__init__.py文件，写上
					import pymysql
					pymysql.install_as_MySQLdb()

			- 在app/models.py的文件中创建类
				类必须继承models.Model

			- 两个命令
				- python manage.py makemigrations -> 相当于拿个小本本把models.py的变更记录下来
				- python manage.py migrate -> 把上面的变更记录翻译成sql语句，去数据库执行

			- ORM查询
				User.object.filter(email='', pwd='')
				
	- 启动项目
		- 命令行启动(切换到项目的根目录)
			- python manage.py runserver 127.0.0.1:8090(改端口这样指定)   


- ORM一些总结与注意事项
	- 创建数据库表
		- 类必须要继承models.Model
		- 自增id可以不写，默认会有自增id
	- ORM数据库表的单表查询
		- 添加表记录
			- # 方式一：实例化对象就是一条表记录
				- Frank_obj = models.Student(name ="海东",course="python",birth="2000-9-9",fenshu=80)
    			- Frank_obj.save()
    		- # 方式二：
    			- models.Student.objects.create(name ="海燕",course="python",birth="1995-5-9",fenshu=88)
	
    	- 查询表记录
    		- 查询相关API
    			- all():查看所有

    			- filter():可以实现且关系，但是或关系需要借助Q查询实现。。。查不到的时候不会报错

    			- get():如果找不到会报错，如果多个值，也会报错，只能拿到一个值

    			- exclude():排除条件

    			- values():是QuerySet的一个方法（把对象转换成字典的形式）

    			- values_list():是QuerySet的一个方法(把对象转换成元组的形式)

    			- order_by():排序

    			-reverse():倒序

    			- distinct():去重（只要结果里面有重复的）

    			- count():查看几条记录

    			- first():

    			- last():

    			- esits():查看有没有记录，如果有返回True，没有返回False，并不需要判断所有数据

    		- 双下划线之表单查询
    			
    			models.Tb1.objects.filter(id__lt=10, id__gt=1)   # 获取id小于1 且 大于10的值
				models.Tb1.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
				models.Tb1.objects.exclude(id__in=[11, 22, 33])  # not in
				models.Tb1.objects.filter(name__contains="ven")  #包括ven的
				models.Tb1.objects.filter(name__icontains="ven") # icontains大小写不敏感
				models.Tb1.objects.filter(id__range=[1, 2])      # 范围bettwen and
				 
				startswith，istartswith, endswith, iendswith

				注：
				对象可以调用自己的属性，用一个点就可以
				还可以通过双下划线。。。
				    models.Book.objects.filter(price__gt=100)   价格大于100的书
				    models.Book.objects.filter(author__startwith= "张")    查看作者的名字是以张开头的
				    主键大于5的且小于2
				    price__gte=99大于等于
				publishDate__year =2017,publishDate__month = 10   查看2017年10月份的数据




		- 修改表记录
			- #方式一
				- author = Author.objects.get(id=5)
				- author.name = 'ward'
				- author.save()
			- #方式二
				- Author.objects.fillter(id=2).updata(name='ward')(注意：不能有get(id=2))

			- 注意：
				<1> 第二种方式修改不能用get的原因是：update是QuerySet对象的方法，get返回的是一个model对象，它没有update方法，
				而filter返回的是一个QuerySet对象(filter里面的条件可能有多个条件符合，比如name＝'alvin',可能有两个name＝'alvin'的行数据)。
				<2>我们有提到模型的save()方法，这个方法会更新一行里的所有列。 而某些情况下，我们只需要更新行里的某几列。
 
				此外，update()方法对于任何结果集（QuerySet）均有效，这意味着你可以同时更新多条记录update()方法会返回一个整型数值，表示受影响的记录条数。
				注意，这里因为update返回的是一个整形，所以没法用query属性；对于每次创建一个对象，想显示对应的raw sql，需要在settings加上日志记录部分


		- 删除表记录
			- 删除方法就是 delete()。它运行时立即删除对象而不返回任何值。
				- 例如：e.delete()
					def delstudent(request,id):
			    	# 删除数据
			    	models.Student.objects.filter(nid=id).delete()
			    		return redirect("/test/")
				你也可以一次性删除多个对象。每个 QuerySet 都有一个 delete() 方法，它一次性删除 QuerySet 中所有的对象。
					- 例如，下面的代码将删除 pub_date 是2005年的 Entry 对象：
						Entry.objects.filter(pub_date__year=2005).delete()
				- 要牢记这一点：无论在什么情况下，QuerySet 中的 delete() 方法都只使用一条 SQL 语句一次性删除所有对象，而并不是分别删除每个对象。
				如果你想使用在 model 中自定义的 delete() 方法，就要自行调用每个对象的delete 方法。(例如，遍历 QuerySet，在每个对象上调用 
				delete()方法)，而不是使用 QuerySet 中的 delete()方法。

				- 在 Django 删除对象时，会模仿 SQL 约束 ON DELETE CASCADE 的行为，换句话说，删除一个对象时也会删除与它相关联的外键对象。
					- 例如：
						b = Blog.objects.get(pk=1)
						# This will delete the Blog and all of its Entry objects.
						b.delete()
					要注意的是： delete() 方法是 QuerySet 上的方法，但并不适用于 Manager 本身。
					这是一种保护机制，是为了避免意外地调用 Entry.objects.delete() 方法导致所有的 
					记录被误删除。如果你确认要删除所有的对象，那么你必须显式地调用：
					Entry.objects.all().delete()


		- 编辑表格中的内容涉及到的语法
		- 编辑操作涉及到的语法

			- 分析：
			    1、点击编辑，让跳转到另一个页面，拿到我点击的那一行
			    两种取id值的方式
			    方式一：
			        利用数据传参数（作为数据参数传过去了）
			        <a href="/edit/?book_id = {{book_obj.nid}}"></a>  #相当于发了一个键值对
			        url里面就不用写匹配的路径了，
			        id = request.GET.get("book_id")  #取值 
			    
			    方式二：
			        利用路径传参，得在url里面加上（\d+）,就得给函数传个参数，无名分组从参数里面取值
			        <a href="/{{book_obj.nid}}"></a>
			    
			    2、拿到id，然后在做筛选
			        id = request.GET.get("book_id")
			        book_obj = models.Book.objects.filter(nid=id)  #拿到的是一个列表对象
			        注意：
			            1.取[0]就拿到对象了，，然后对象.属性就可以取到值了
			            2.用get，你取出来的数据必须只有一条的时候，，如果有多条用get就会报错，，，但是用get就不用加[0]了
			        book_obj = models.Book.objects.filter(nid=id)[0]    
			        
			    3、当点击编辑的时候怎么让input框里显示文本内容
			        value = "{{book_obj.title}}"
			    4、改完数据后重新提交
			        当提交的时候走action...../edit/}
			        隐藏一个input,
			        <input type="hidden" name = "book_id" value="{{book_obj.nid}}">
			        判断post的时候：
			            修改数据 
			                方式一：save（这种方式效率是非常低的，不推荐使用，了解就行了）
			                    修改的前提是先取(拿到要编辑的id值)
			                    id = request.POST.get("book_id")
			                    bk_obj = models.Book.objects.filter(nid=id)[0]
			                    bk_obj.title = "hhhhhh"  #这是写死了，不能都像这样写死了
			                    bk_obj.save()  只要是用对象的这种都要.save
			                方式二：update
			                title = request.POST.get("title")
			                models.Book.objects.filter(nid=id).update(title=title,......)
			            跳转到index
            
            
            
			- 如果是post请求的时候怎么找到id呢，
				一、如果是数据传参：(也就是get请求的时候)
				    可以通过一个隐藏的input框，给这个框给一个name属性，value属性。通过request.POST.get("键")，，就可以得到id的值
				二、如果是路径传参
				    可以通过传参的形式，当正则表达式写一个(\d+)的时候，就给函数传一个id,可通过这个id知道id.




	- ORM数据库表的跨表操作 
		- 创建表
			- 书籍模型： 书籍有书名和出版日期，一本书可能会有多个作者，一个作者也可以写多本书，所以作者和书籍的关系就是多对多的关联关系(many-to-many);

		　　 - 一本书只应该由一个出版商出版，所以出版商和书籍是一对多关联关系(one-to-many)。

		    -- 创建一对一的关系：OneToOne("要绑定关系的表名")
		    -- 创建一对多的关系：ForeignKey("要绑定关系的表名")
		    -- 创建多对多的关系：ManyToMany("要绑定关系的表名")  会自动创建第三张表


		    	
		    	class Book(models.Model):
				    nid = models.AutoField(primary_key=True)  # 自增id(可以不写，默认会有自增id)
				    title = models.CharField(max_length=32)
				    publishDdata = models.DateField()  # 出版日期
				    price = models.DecimalField(max_digits=5, decimal_places=2)  # 一共5位，保留两位小数
				    
				    #一个出版社有多本书，关联字段要写在多的一方
				    # 不用命名为publish_id，因为django为我们自动就加上了_id
				    publish = models.ForeignKey("Publish")  #foreignkey（表名）建立的一对多关系
				    # publish是实例对象关联的出版社对象
				    authorlist = models.ManyToManyField("Author")  #建立的多对多的关系
				    def __str__(self):  #__str__方法使用来吧对象转换成字符串的，你返回啥内容就打印啥
				        return self.title
				class Publish(models.Model):
				    #不写id的时候数据库会自动给你增加自增id
				    name =models.CharField(max_length=32)
				    addr = models.CharField(max_length=32)
				    
				    def __str__(self):
				        return self.name
				class Author(models.Model):
				    name = models.CharField(max_length=32)
				    age = models.IntegerField()

				class AuthorDeital(models.Model):
				    tel = models.IntegerField()
				    addr = models.CharField(max_length=32)
				    author = models.OneToOneField("Author")  #建立的一对一的关系

		- 添加记录
			- 一对多添加记录
		        # 一对多的添加

		        # 方式一:如果是这样直接指定publish_id字段去添加值，前提是你的主表里面必须有数据
		        # 主表：没有被关联的（因为book表是要依赖于publish这个表的）也就是publish表
		        # 子表：关联的表
		        models.Book.objects.create(title="追风筝的人",publishDdata="2015-5-8",price="111",publish_id=1)

		        # 方式二:推荐
		        pub_obj = models.Publish.objects.filter(name="人民出版社")[0]
		        print(pub_obj)
		        models.Book.objects.create(title = "简爱",publishDdata="2000-6-6",price="222",publish=pub_obj)
		        
		        # 方式三：save
		        pubObj= models.Publish.objects.get(name="人民出版社") #只有一个的时候用get,拿到的直接就是一个对象
		        bookObj = models.Book(title = "真正的勇士",publishDdata="2015-9-9",price="50",publish=pubObj)
		        bookObj.save()


		    - 多对多添加记录
		    	书和作者是多对多的关系：一本书可以有多个作者，一个作者可以出版多本书
		    	步骤：
		    		先找到书对象
		    		再找到需要的作者对象
		    		给书对象绑定作者对象（用add方法），也就是绑定多对多的关系。

		    	# 多对多的添加的两种方式
		    	# 方式一：
		    		# 先创建一本书
		    			pub_obj=models.Publish.objects.filter(name="万能出版社").first()
        				book_obj = models.Book.objects.create(title="醉玲珑",publishDdata="2015-4-10",price="222",publish=pub_obj)
		    		# 通过作者的名字django默认找到id
		    			haiyan_obj = models.Author.objects.filter(name="haiyan")[0]
        				jack_obj = models.Author.objects.filter(name="jack")[0]
        				tom_obj = models.Author.objects.filter(name="tom")[0]
		    		# 绑定对对多的关系
		    			book_obj.authorlist.add(haiyan_obj, jack_obj, tom_obj)

		    	# 方式二：
		    		#查出所有的作者
			    		pub_obj = models.Publish.objects.filter(name="万能出版社").first()
	       				book_obj = models.Book.objects.create(title="醉玲珑", publishDdata="2015-4-10", price="222", publish=pub_obj)
	        			authers = models.Author.objects.all()
	        		# 绑定多对多的关系
	        			book_obj.authorlist.add(*authers)

	        		- 解除绑定：remove：将某个特定的对象从被关联对象集合中去除  ======   book_obj.authors.remove(*[]) 
	        			# 解除多对多的关系（remove）
	        				book_obj=models.Book.objects.filter(title="醉玲珑").last() #找到书对象
				            authers=models.Author.objects.filter(id__lt=3)  #找到符合条件的作者对象
				            book_obj.authorlist.remove(*authers) #因为清除的是多条，得加个*

				    - 清除绑定：clear # 清空别关联对象集合
				    	#清除关系方法：（clear）
				    	book_obj= models.Book.objects.filter(title="红楼梦")
			            for book_obj_item in book_obj:#把所有红楼梦的都给清空了
			                book_obj_item.authorlist.clear()

			        	- 总结：remove和clear的区别
			        		- remove：得把你要清除的数据筛选出来，然后移除
			        		- clear：不用查，直接就把数据清空了
			        		各有各的应用场景



	    - 基于对象的查询记录（相当于sql语句的where子查询）
	    	- 一对一查询记录：author和authordeital是一对一的关系
	    		- 正向查询（按字段author）
	    		- 反向查询（按子弹authordeital）：因为是一对一的关系，就不用_set了
	    			# 一对一的查询
		            # 正向查询：手机号为13245的作者的姓名
		            deital_obj = models.AuthorDeital.objects.filter(tel="13245").first()
		            print(deital_obj.author.name)
		            # 反向查询：查询jack的手机号
		            jack_obj = models.Author.objects.filter(name="jack").first()
		            print(jack_obj.authordeital.tel)

		    - 一对多记录查询
		    	- 正向查询（按字段：publish）
		    	- 反向查询（按表名：book_set）
		    		# 正向查询：查询《真正的勇士》这本书的出版社的地址
		            book_obj = models.Book.objects.filter(title="真正的勇士")[0]  # 找对象
		            print("======", book_obj.publish)  # 拿到的是关联出版社的对象
		            print(book_obj.publish.addr)

		            # 反向查询：查询人民出版社出版过的所有的书的价格和名字
		            pub_obj = models.Publish.objects.filter(name="人民出版社")[0]
		            book_dic = pub_obj.book_set.all().values("price", "title")[0]
		            print(book_dic)
		            print(book_dic["price"])

		            # 查询 人民出版社出版过的所有书籍
		            publish=models.Publish.objects.get(name="人民出版社")   #get得到的直接是一个对象，不过get只能查看有一条记录的
		            book_list=publish.book_set.all()  # 与人民出版社关联的所有书籍对象集合
		                for book_obj in book_list:
		                    print(book_obj.title)
		            注意这里用for循环或是用values,vauleslist都是可以的。

		    - 多对多查询记录
		    	- 正向查询（按字段：authorlist）
		    	- 方向查询（按表名：book_set）
		    		# 多对多的查询

		            # 正向查询：查询追风筝的人的这本书的所有的作者的姓名和年龄
		            book_obj = models.Book.objects.filter(title="追风筝的人")[0]
		            print(book_obj.authorlist.all().values("name", "age"))  # 这本书关联的所有作者对象的集合

		            # 反向查询：查询作者是haiyan的这个人出了哪几本书的信息
		            haiyan_obj = models.Author.objects.filter(name="haiyan")[0]
		            print("bookinfo====", haiyan_obj.book_set.all().first().title)  # 与该作者关联的所有书对象的集合
		            return HttpResponse("ok")

		                可以通过在 ForeignKey() 和ManyToManyField的定义中设置 related_name 的值来覆写 FOO_set 的名称。
		                例如，如果 Article model 中做一下更改： publish = ForeignKey(Blog, related_name='bookList')，
		                那么接下来就会如我们看到这般：
		                    # 查询 人民出版社出版过的所有书籍
		                    publish=Publish.objects.get(name="人民出版社")
		                    book_list=publish.bookList.all()  # 与人民出版社关联的所有书籍对象集合



		- 基于双下划线的跨表查询
			Django 还提供了一种直观而高效的方式在查询(lookups)中表示关联关系，它能自动确认 SQL JOIN 联系。要做跨关系查询，
    		就使用两个下划线来链接模型(model)间关联字段的名称，直到最终链接到你想要的 model 为止。(相当于用sql语句用join
    		连接的方式，可以在settings里面设置，可查看sql语句)

    		- 举例：
    			一对多查询：

					练习1、查询人民出版社出版过的所有的书的价格和名字


					    # 基于双下划线的方式查询1================一对多
					    # 第一种查法
					    ret = models.Publish.objects.filter(name="人民出版社").values("book__price","book__title")
					    print(ret)
					    # 第二种查法
					    ret2 = models.Book.objects.filter(publish__name="人民出版社").values("price","title")
					    print(ret2)

					练习2、查询linux这本书的出版社的地址:filer先过滤，，values显示要求的字段
					    
					    第一种查法
					    ret = models.Book.objects.filter(title="linux").values("publish__addr")
					    print(ret)
					    第二种查法
					    ret2 = models.Publish.objects.filter(book__title="linux").values("addr")
					    print(ret2)

				- 多对多查询：

					练习1、查询jack出过的所有书的名字
					    
					    #方式一
					    ret = models.Author.objects.filter(name="jack").values("book__title")
					    print(ret)
					    #方式二：两种方式也就是逻辑不一样
					    ret2 = models.Book.objects.filter(authorlist__name="jack").values("title")
					    print(ret2)


					练习2、查询手机号以151开头的作者出版过的所有书的名称以及出版社的名称
					    
					    # 方式一：
					    author_obj = models.AuthorDeital.objects.filter(tel__startswith="151").first()
					    print(author_obj.author.book_set.all().values("title","publish__name"))
					    # 方式二：
					    ret = models.Book.objects.filter(authorlist__author_deital__tel__startswith="151").values("title","publish__name")
					    print(ret)



		- 聚合查询与分组查询（很重要 ***** ）

			- 聚合查询：aggregate(*args, **kwargs)，只对一个组进行聚合

				from django.db.models import Avg,Sum,Count,Max,Min
				# 1、查询所有图书的平均价格
				print(models.Book.objects.all().aggregate(Avg("price")))
				aggregate()是QuerySet 的一个终止子句（也就是返回的不再是一个QuerySet集合的时候），意思是说，它返回一个包含一些键值对的字典。键的名称是聚合值的标识符，值是计算出来的聚合值。键的名称是按照字段和聚合函数的名称自动生成出来的。如果你想要为聚合值指定一个名称，可以向聚合子句提供它。

				from django.db.models import Avg,Sum,Count,Max,Min
				# 1、查询所有图书的平均价格
				print(models.Book.objects.all().aggregate(avgprice = Avg("price")))
				如果你希望生成不止一个聚合，你可以向aggregate()子句中添加另一个参数。所以，如果你也想知道所有图书价格的最大值和最小值，可以这样查询：

				print(models.Book.objects.all().aggregate(Avg("price"),Max("price"),Min("price")))
				#打印的结果是：  {'price__avg': 174.33333333333334, 'price__max': Decimal('366.00'), 'price__min': Decimal('12.00')}

			- 分组查询 :annotate()：为QuerySet中每一个对象都生成一个独立的汇总值。
				    
				    是对分组完之后的结果进行的聚合

				1、统计每一本书的作者个数
				    
				    # 方式一：
				    print(models.Book.objects.all().annotate(authorNum = Count("authorlist__name")).values("authorNum"))
				    # 方式二：
				    booklist =models.Book.objects.all().annotate(authorNum=Count("authorlist__name"))
				    for book_obj in booklist:
				        print(book_obj.title,book_obj.authorNum)

				2、统计每一个出版社最便宜的书

				    # 2、统计每一个出版社的最便宜的书
				    # 方式一：
				    print(models.Book.objects.values("publish__name").annotate(nMinPrice=Min('price')))  注意：values内的字段即group by的字段，，也就是分组条件
				    # 方式二：
				    print(models.Publish.objects.all().annotate(minprice=Min("book__price")).values("name","minprice"))
				    # 方式三
				    publishlist = models.Publish.objects.annotate(minprice = Min("book__price"))
				    for publish_obj in publishlist:
				        print(publish_obj.name,publish_obj.minprice)

				3、统计每一本以py开头的书籍的作者个数：
				print(models.Book.objects.filter(title__startswith="py").annotate(authNum = Count("authorlist__name")).values("authNum"))


				(4)统计不止一个作者的图书：
				print(models.Book.objects.annotate(num_authors=Count('authorlist__name')).filter(num_authors__gt=1).values("title","num_authors"))
				(5)根据一本图书作者数量的多少对查询集QuerySet进行排序:
				print(models.Book.objects.all().annotate(authorsNum=Count("authorlist__name")).order_by("authorsNum"))


				(6)查询各个作者出的书的总价格:
				    # 方式一
				    print(models.Author.objects.all().annotate(priceSum = Sum("book__price")).values("name","priceSum"))
				    # 方式二
				    print(models.Book.objects.values("authorlist__name").annotate(priceSum=Sum("price")).values("authorlist__name","priceSum"))
				

		- F查询和Q查询

			- F查询：
				在上面所有的例子中，我们构造的过滤器都只是将字段值与某个常量做比较。如果我们要对两个字段的值做比较，那该怎么做呢？

				Django 提供 F() 来做这样的比较。F() 的实例可以在查询中引用字段，来比较同一个 model 实例中两个不同字段的值。

				1、查看评论数大于阅读数的书
				    from django.db.models import F,Q
				        print(models.Book.objects.filter(commentNum__gt=F("readNum")))
				2、修改操作也可以使用F函数,比如将id大于1的所有的书的价格涨价100元
				print(models.Book.objects.filter(nid__gt=1).update(price=F("price")+100))


				3、Django 支持 F() 对象之间以及 F() 对象和常数之间的加减乘除和取模的操作。
				    # 查询评论数大于收藏数2倍的书籍
				    models.Book.objects.filter(commnetNum__lt=F('keepNum')*2)
			- Q查询：
				filter() 等方法中的关键字参数查询都是一起进行“AND” 的。 如果你需要执行更复杂的查询（例如OR 语句），你可以使用Q 对象。

				1、查询id大于1并且评论数大于100的书
				    print(models.Book.objects.filter(nid__gt=1,commentNum__gt=100))
				    print(models.Book.objects.filter(nid__gt=1).filter(commentNum__gt=100))
				    print(models.Book.objects.filter(Q(nid__gt=1)&Q(commentNum__gt=100)))
				2、查询评论数大于100或者阅读数小于200的书
				print(models.Book.objects.filter(Q(commentNum__gt=100)|Q(readNum__lt=200)))
				Q 对象可以使用& 和| 操作符组合起来。当一个操作符在两个Q 对象上使用时，它产生一个新的Q 对象。
				3、查询年份等于2017年或者价格大于200的书
				    print(models.Book.objects.filter(Q(publishDdata__year=2017)|Q(price__gt=200)))
				4、查询年份不是2017年或者价格大于200的书
				print(models.Book.objects.filter(~Q(publishDdata__year=2017)&Q(price__gt=200)))
				注意：

				查询函数可以混合使用Q 对象和关键字参数。所有提供给查询函数的参数（关键字参数或Q 对象）都将"AND”在一起。但是，如果出现Q 对象，它必须位于所有关键字参数的前面。例如：

				    bookList=models.Book.objects.filter(Q(publishDate__year=2016) | Q(publishDate__year=2017),
				                                        title__icontains="python"
				                                        )


一些小栗子：

	- 多对对的正反向查询
		- 
			class Class(models.Model):
			    name= models.CharField(max_length=32,verbose_name="班级名")
			    course = models.CharField(verbose_name="课程",max_length=32)
			    def __str__(self):
			        return self.name

			class Teacher(models.Model):
			    name= models.CharField(max_length=23,verbose_name="姓名")
			    classes = models.ManyToManyField(verbose_name="所属班级",to="Class")
			    def __str__(self):
			        return self.name
			查找登登老师所带的班级
			# 方式一：基于对象的查找
			        obj = models.Teacher.objects.filter(name="登登").first()
			        print(obj.classes.all())
			        print("登登老师带的班级",obj.classes.values("name"))
			       
			 # 方式二：基于双下划线的查找
			        obj_cls = models.Teacher.objects.filter(name="登登").values("classes__name")
			        print("登登老师带的班级",obj_cls)

			注意：
				- 要说明的是多对多的查询用.all，，查单个的时候用.values或者values_list，不要用obj.classes.name，
				这样查到的会是None，反向查询也是如此。我就是犯了这样的错，引以为戒。。
			总结：
				- 不管是一对多，还是多对多，要是查询多得一方就得用all()

		例子：
			-  例子
				- 表结构
				from django.db import models

				# Create your models here.
				# 一个学生有一个班级，一个班级可以有好多学生，所以是
				# 一对多的关系，关联字段放在多的一方
				class Student(models.Model):
				    name = models.CharField(max_length=32,verbose_name="姓名")
				    age = models.IntegerField(verbose_name="年龄")
				    classes = models.ForeignKey(to="Class",verbose_name="所属班级")
				    def __str__(self):
				        return self.name

				class Class(models.Model):
				    name = models.CharField(max_length=32,verbose_name="班级名")
				    course = models.CharField(verbose_name="课程",max_length=32)
				    def __str__(self):
				        return self.name

				class Teacher(models.Model):
				    name = models.CharField(max_length=23,verbose_name="姓名")
				    classes = models.ManyToManyField(verbose_name="所属班级",to="Class")
				    def __str__(self):
				        return self.name

				问题：
				- 查询海燕所在哪个班级
				    # 方式一：
						- print("海燕所在的班级",models.Student.objects.filter(name="海燕").values("classes__name"))
				    # 方式二：
						- obj_cls = models.Student.objects.filter(name="海燕").first()
						- print("海燕所在的班级",obj_cls.classes.name)

				- 查询海燕所在班级老师的名字
					# 方式一：
				        print("海燕所在的班级",models.Student.objects.filter(name="海燕").values("classes__name"))
				    # 方式二：
				        obj_cls = models.Student.objects.filter(name="海燕").first()
				        print("海燕所在的班级",obj_cls.classes.name)
				- 查询海燕所在班的老师的姓名
					print("海燕所在班的老师的姓名",models.Student.objects.filter(name="海燕").values("classes__teacher__name"))

				- 查询软件1班的所有学生的姓名
					- print("软件1班的所有学生的姓名",models.Class.objects.filter(name="软件1班").values("student__name"))
					- obj = models.Class.objects.filter(name="软件1班").first()
					- # print("软件1班的所有学生的姓名",obj.student_set.name)  #这样打印的结果是None
					- print("软件1班的所有学生的姓名",obj.student_set.all().values("name"))






















