# 缓存

>由于Django是动态网站，所有每次请求均会去数据进行相应的操作，当程序访问量大时，耗时必然会更加
>
>明显，最简单解决方式是使用：缓存，缓存将一个某个views的返回值保存至内存或者memcache中，5分
>
>钟内再有人来访问时，则不再去执行view中的操作，而是直接从内存或者Redis中之前缓存的内容拿到，并
>
>返回。
>
>Django中提供了6种缓存方式：
>
>- 开发调试
>- 内存
>- 文件
>- 数据库
>- Memcache缓存（python-memcached模块）
>- Memcache缓存（pylibmc模块）
>
>>- 配置
>>
>>  ```
>>  CACHES = {
>>  	'default': {
>>  	'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
>>  	'LOCATION': 'unique-snowflake',
>>  	'TIMEOUT': 300,  # 缓存超时时间（默认300，None表示永不过期，0表示立即过期）
>>  	'OPTIONS': {
>>  		'MAX_ENTRIES': 300,  # 最大缓存个数（默认300）
>>  		'CULL_FREQUENCY': 3,  # 缓存到达最大个数之后，剔除缓存个数的比例，即1/CULL_FREQUENCY（默认3）
>>  		},
>>  	}
>>  }
>>  ```
>>
>>  redis
>>
>>  ​	django-redis
>>
>>- 应用
>>
>>
>>  ```
>>  应用到视图上： 粒度适中
>>  from django.views.decorators.cache import cache_page
>>  @cache_page(15)
>>  def user_list(request):
>>      print('user_list')
>>      users = models.User.objects.all()
>>      return render(request, 'user_list.html', {'users': users})
>>  ```
>>
>>  		全站应用： 粒度最大
>>  			MIDDLEWARE = [
>>  				'django.middleware.cache.UpdateCacheMiddleware',
>>  				# 其他中间件...
>>  				'django.middleware.cache.FetchFromCacheMiddleware',
>>  			]
>>  ```
>>  局部视图：粒度最细
>>  
>>  a. 引入TemplateTag
>>  
>>  {% load cache %}
>>  
>>  b. 使用缓存
>>  
>>  {% cache 5000 缓存key %}
>>  缓存内容
>>  {% endcache %}
>>  ```

# 序列化

>
>
>		json  pickle
>		
>		- 自定义序列化
>		
>		class JsonCustomEncoder(json.JSONEncoder):
>	
>			def default(self, field):
>				
>				if isinstance(field, datetime):
>					return field.strftime('%Y-%m-%d %H:%M:%S')
>				elif isinstance(field, date):
>					return field.strftime('%Y-%m-%d')
>				else:
>					return json.JSONEncoder.default(self, field)
>	
>		print(json.dumps(data,cls=JsonCustomEncoder))

# 信号

>
>
>- 信号
>   问题：
>   ​		数据库增加一条数据的时候，记录一条日志。
>   ​		
>   	内置信号	
>   	Model signals
>   		pre_init                    # django的model执行其构造方法前，自动触发
>   		post_init                   # django的model执行其构造方法后，自动触发
>   		pre_save                    # django的model对象保存前，自动触发
>   		post_save                   # django的model对象保存后，自动触发
>   		pre_delete                  # django的model对象删除前，自动触发
>   		post_delete                 # django的model对象删除后，自动触发
>   		m2m_changed                 # django的model中使用m2m字段操作第三张表（add,remove,clear）前后，自动触发
>   		class_prepared              # 程序启动时，检测已注册的app中modal类，对于每一个类，自动触发
>   	Management signals
>   		pre_migrate                 # 执行migrate命令前，自动触发
>   		post_migrate                # 执行migrate命令后，自动触发
>   	Request/response signals
>   		request_started             # 请求到来前，自动触发
>   		request_finished            # 请求结束后，自动触发
>   		got_request_exception       # 请求异常后，自动触发
>   	Test signals
>   		setting_changed             # 使用test测试修改配置文件时，自动触发
>   		template_rendered           # 使用test测试渲染模板时，自动触发
>   	Database Wrappers
>   		connection_created          # 创建数据库连接时，自动触发
>
>
>   ​	
>   	注册信号
>   		# 方法一
>   		def callback(sender, **kwargs):
>   			print("xxoo_callback")
>   			print(sender, kwargs)
>
>
>			post_save.connect(callback)
>
>
>			# 方法二
>	
>			@receiver(post_save)
>			def my_callback(sender, **kwargs):
>				print("xxoo_callback")
>				print(sender, kwargs)
>			
>	- ORM性能相关
>	
>		1. 	[{} ]
>			all_users = models.User.objects.all().values('name','age','role__name')
>			
>		2. [ 对象 ]
>			all_users = models.User.objects.all()
>			用的时候注意，只拿自己表中的字段，别跨表
>		3. select_related  （外键、一对一）
>			all_users = models.User.objects.all().select_related('role')
>			
>		4. prefetch_related （role）
>			all_users = models.User.objects.all().prefetch_related('role')
>			
>		5. only
>			all_users = models.User.objects.all().only('name')
>			用的时候注意，只拿自己指定的字段
>		6. defer
>			all_users = models.User.objects.all().defer('name')
>
># 验证码
>
>	- 验证码
>		from PIL import Image, ImageDraw, ImageFont
>		import random
>
>
>		def random_color():
>			return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
>
>
>		def v_code(request):
>			img_obj = Image.new('RGB', (250, 35), random_color())
>			
>			# 在该图片对象上生成一个画笔对象
>			draw_obj = ImageDraw.Draw(img_obj)
>			
>			font_obj = ImageFont.truetype('static/font/kumo.ttf', 28)
>			
>			temp = []
>			for i in range(5):
>				l = chr(random.randint(97, 122))  # 小写字母
>				b = chr(random.randint(65, 90))  # 大写字母
>				n = str(random.randint(0, 9))
>				
>				t = random.choice([l, b, n])
>				temp.append(t)
>				
>				draw_obj.text((i * 40 + 35, 0), t, fill=random_color(), font=font_obj)
>			
>			from io import BytesIO
>			f1 = BytesIO()
>			img_obj.save(f1, format="PNG")
>			img_data = f1.getvalue()
>			
>			return HttpResponse(img_data, content_type='image/png')
>
>
>​	
>​	
>​	