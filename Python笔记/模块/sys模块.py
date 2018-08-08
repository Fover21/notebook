#sys模块是与python解释器交互的一个接口
import sys

print(sys.argv) #命令行参数list，第一个元素是程序本身路径
#（第一个元素就是执行文件的时候，写在python命令后的第一个值，之后的元素在执行
#python的启动的时候可以写多个值，这些值都会依次添加到列表中）

#sys.exit() #t退出程序，正常退出时exit(0),错误退出sys.exit(1)

print(sys.version)#获取python解释器程序的版本信息

print(sys.path)#返回模板的搜索路径，初始化的时候使用PYTHONPATH环境变量的值

print(sys.platform) #返回操作系统平台名称（不怎么准确）

print(sys.maxsize) #返回最大的int值

print(sys.modules) #返回加载到内存中的模块名称及地址