
1、互联网两台机器之间通行：ip、端口、协议
	- 协议
		- HTTP  （80）
		- HTTPS  (443) 

2、浏览器输入URL一回车返回页面发生了什么？
	- 域名 -> DNS解析 -->ip地址 -> 找到服务端 ->服务端返回消息 -> 浏览器
	- 浏览器 <-> 服务器
	- 服务器把 写好的HTML页面，返回给浏览器，浏览器按照HTML格式渲染

3、请求和相应
	- HTTP协议的特点：
		- 浏览器给服务端发消息的过程叫请求（request）
		- 服务器给浏览器回复消息的过程叫响应（response）
		
	- 请求和相应的消息都必须遵循一个固定的格式

4、python中Web框架分类
	- a、收发socket消息，按照HTTP协议解析消息		Web服务程序	wsgiref、gunicorn、uWSGI
	- b、字符串替换								
	- c、业务逻辑处理							Web应用程序

	1- 自己实现abc的
		- Tronado
	2- 自己实现bc使用别人的a
		- Django
	3- 自己实现c使用别人的ab
		- Flask
5、Web服务程序  <-  WSGI协议  -> Web应用程序


6、创建第一个Django项目
	- 1、命令行  Django-admin startproject first_Django
	- 2、Pycharm创建
		- file -> new Project ->右侧选Django -> 选好路径 ->选好环境 -> 名字app -> 在新的窗口打开文件
	- 3、启动项目
		- 命令行启动
			- python manage.py runserver 127.0.0.1:8090(改端口这样指定)
		- pycharm启动
			- 框中选项为项目名->让后点击启动按钮（右上角）（如果想改就在旁边点编辑-就可以改端口等）

	- 目录介绍
		- 和项目名一样的是根目录
		- 
	---------------------
	- 先来一份自己的理解
		- 1、（与我们所创建文件名一致的目录）根目录
			- manage.py 
				- 这是启动文件，程序入口。
			- settings.py
				- 包含了项目的一些设置，包括数据库信息、调试标志以及其他的一些工作的变量。
			- urls.py
				- 路径与视图函数的映射关系


		- 2、templates - 这个文件夹存放的是HTML文件
		- 3、static - 这个文件夹是存放静态文件，需要自己配置，用的时候的导入时用 
		     /static/.. 来引入所用的静态文件
		     	# Static files (CSS, JavaScript, Images)
				# https://docs.djangoproject.com/en/1.11/howto/static-files/

				# 这个static就代表了下面的路径 （寻找的时候就是去static下面的路径中挨个找）
				STATIC_URL = '/static/'  # 起别名， HTML中找静态文件都要以这个别名开始  (找到别名后就去这个别名的配置比文件中找对应的文件)

				# 这个常量是固定格式
				STATICFILES_DIRS = [
				    os.path.join(BASE_DIR, 'static'),
				]
	

其他：
	- from django.shortcuts import HttpResponse, render
		- HttpResponse (封装了协议头等-有待商议)
		- render （渲染）

	- 文件的上传（form表单的提交， 必须用POST）
		def index(request):
		    print(request.GET)
		    print(request.POST)
		    print(request.FILES)

		    for item in request.FILES:
		        fileobj = request.FILES.get(item)
		        f = open('upload/%s' % fileobj.name, 'wb')
		        item_file = fileobj.chunks()
		        for line in item_file:
		            f.write(line)
		        f.close()

		    return HttpResponse("成功")
 	- form表单上传文件时需要注意的事情
 		- action 最后加 /  或者 修改settings:APPEND_SLASH=False
 		- method 必须为post 
 		- enctype = “multipart/form-data” 必须写

 	- 指定IP登录
 		默认IP和端口
		    python manage.py runserver
		指定端口：
		    python manage.py runserver 192.168.12.12:8080
		此时会报错，我们需要修改配置文件：
		修改settings.py，将192.168.12.12添加到ALLOWED_HOSTS中
		ALLOWED_HOSTS=['172.31.169.182','127.0.0.1','192.168.1.50','192.168.1.115']
		也可以将ALLOWED_HOSTS改成通配符 *
		ALLOWED_HOSTS = ["*"]
















