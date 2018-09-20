模块

1.模块定义
	用来从逻辑上组织python代码（变量，函数，类，逻辑：实现一个功能），本质上就是.py结尾python文件

	分类：内置模块（又称标准库）执行 help('modules')查看所有python自带模块列表
		 第三方开源模块，可通过 pip install 模块名   联网安装
		 自定义模块


2.导入模块
	本质：导入模块的本质就是把python文件解释一遍，
		 导入包的本质就是把包文件下面的init.py文件运行一遍。

		 1）同目录下模块的导入
		 	#同级目录下模块的导入

		 	import module_name   #直接导入模块
		 	import module1_name,module2_name  #导入多个模块  使用：模块名.函数名
		 	from modeule_name import * #导入模块中所有函数和变量等。。。不推荐使用
		 	from modeule_name import m1,m2,m3 #只导入模块中函数m1,m2,m3 使用：直接使用m1,m2,m3就可以
		 	from modeule_name import m1 as m #导入module_name模块中函数m1并且将函数重新复制给m 使用：直接用调用m

		 2）不同目录下模块的导入
		 	#不同目录下模块的导入  当前文件main.py

		 	#目录结构
			# ├── Credit_card
			# │
			# ├── core  
			# │   ├── __init__.py
			# │   └── main.py  # 当前文件
			# ├── conf  
			# │   ├── __init__.py
			# │   └── setting.py
			# │   └── lzl.py
			
			import sys,os
			#获取当前目录的上上级目录绝对路径，也就是Credit_card
			credit_card_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
			#把Credit_card目录加入到系统路径
			sys.path.insert(0,credit_card_path)

			#查看系统环境路径
			print(sys.path)

			例子：
				如果main文件夹要用conf文件夹下的setting文件，直接导入是不行的
				应该：
					fron conf import setting
					setting.函数名()  #这样执行setting模块中的函数

		3）不同目录下模块连环导入
			#不同目录多个模块之间互相导入

			#目录结构
			# ├── Credit_card
			# │
			# ├── core  
			# │   ├── __init__.py
			# │   └── main.py  # 当前文件
			# ├── conf  
			# │   ├── __init__.py
			# │   └── setting.py
			# │   └── lzl.py

			如果在setting文件中调用模块lzl.py，可以用语句 import lzl,但是如果这样，
			我们在main.py文件中调用setting文件时，就会报错#ImportError: No module named 'lzl'
			这个时候我们需要将 import lzl  换为  from . import lzl 
			然后main.py文件中调用setting文件时，才可以正常执行。

		4）不同目录多个模块相互导入，用相对路径

			Root
			    ├── Credit_card
			            ├── README.md
			            ├── core 
			            │   ├── __init__.py
			            │   └── main.py 
			            ├── conf 
			            │   ├── __init__.py
			            │   └── setting.py
			            │   └── lzl.py     


			lzl.py文件内容：   
					def name():
    					print("name is lzl")

    		setting.py文件内容：
    				#当前文件settings，调用lzl.py模块  相对路径
					from . import lzl       #通过相对路径导入模块lzl
					def set():
					    print("in the settings")
					    lzl.name()   #运行lzl模块下的函数

					set()  #执行函数set

			Core目录下的文件中的mian.py文件内容：
					#不同目录之间连环import 当前文件main.py  相对路径

					from Root.Credit_card.conf import settings
					settings.set()   #执行settings下的函数


			注意：
				lzl.py以及settings.py文件未变，main.py文件去掉了繁杂的sys.path添加的过程，
				直接执行from Root.Credit_card.conf import settings，使用相对路径，更加
				简洁方便！















