#时间模块
import time

#常用方法
#time.sleep(secs)#(线程)推迟指定的时间运行。单位为秒

#print(time.time())#获取当前时间戳

#表示时间的三种方式
#在python中，通常有三种方式来表示时间：时间戳，元组(结构化时间)，格式化的时间字符串：
#1.时间戳（timestamp）：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量，是一个float类型

#2.格式化的时间字符串（Format String）:‘1972-1-2’
#python中时间日期格式化符号：
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

#3.元组（struct_time）：struct_time元组共有9个元素（年，月，日，使，分，秒，一年中第几周，一年中第几天，是否是夏令时）
# 索引（Index）	属性（Attribute）			值（Values）
# 0				tm_year（年）			比如2011
# 1				tm_mon（月）				1 - 12
# 2				tm_mday（日）			1 - 31
# 3				tm_hour（时）			0 - 23
# 4				tm_min（分）				0 - 59
# 5				tm_sec（秒）				0 - 60
# 6				tm_wday（weekday）		0 - 6（0表示周一）
# 7				tm_yday（一年中的第几天）	1 - 366
# 8				tm_isdst（是否是夏令时）	默认为0


#时间戳
print(time.time)

#时间字符串
print(time.strftime('%Y-%m-%d'))
print(time.strftime('%Y-%m-%d %H:%M:%S'))

#时间元组：localtime()将一个时间戳转换为当前时区的struct_time
print(time.localtime())

# 结果：
# 2018-08-08
# 2018-08-08 16:13:36
# time.struct_time(tm_year=2018, tm_mon=8, tm_mday=8, tm_hour=16, tm_min=13, tm_sec=36, tm_wday=2, tm_yday=220, tm_isdst=0)

#注：时间戳是计算机能够识别的时间；时间字符串是人能够看懂的时间；元组则是用来操作时间的

#几种格式之间的转换

#1.时间戳-->结构化时间
#time.gmtime(时间戳) #UTC时间，与英国伦敦当地时间一致
#time.localtime(时间戳) #当地时间。我们是北京是啊金，与UTC时间相差8小时

print(time.gmtime(12000000000))
#结果：
#time.struct_time(tm_year=2350, tm_mon=4, tm_mday=7, tm_hour=21, tm_min=20, tm_sec=0, tm_wday=4, tm_yday=97, tm_isdst=0)

print(time.localtime(12000000000))
#结果：
#time.struct_time(tm_year=2350, tm_mon=4, tm_mday=8, tm_hour=5, tm_min=20, tm_sec=0, tm_wday=5, tm_yday=98, tm_isdst=0)

#2.结构化时间--->时间戳
#time.mktime(结构化时间)

time_tuple = time.localtime(12000000000)
print(time.mktime(time_tuple))
#结果：
#12000000000.0

#3.结构时间--->字符串时间
#time.strftime('格式定义','结构化时间') 结构化时间参数若不传，则实现当前时间

print(time.strftime('%Y-%m-%d'))
print(time.strftime('%Y-%m-%d', time.localtime(12000000000)))
#结果：
#2018-08-08
#2350-04-08
#4.字符串时间--->结构化时间
#time.strptime('时间字符串','字符串对应格式')

print(time.strptime('2020-1-1', '%Y-%m-%d'))
print(time.strptime('2020/1/2', '%Y/%m/%d'))
#结果：
#time.struct_time(tm_year=2020, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=1, tm_isdst=-1)
#time.struct_time(tm_year=2020, tm_mon=1, tm_mday=2, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=2, tm_isdst=-1)

#5.结构化时间---> %a %b %d %H:%M:%Y串
#time.asctime(结构化时间) 如果不传参数，直接返回当前时间的格式化串

print(time.asctime())
print(time.asctime(time.localtime(12000000000)))
#结果：
#Wed Aug  8 16:42:30 2018
#Sat Apr  8 05:20:00 2350

#6.时间戳--->%a %b %d %H:%M:%Y串
#time.ctime(时间戳) 如果不传参数，直接返回当前时间的格式化串
print(time.ctime())
print(time.ctime(12000000000))

#结果：
# Wed Aug  8 16:44:31 2018
# Sat Apr  8 05:20:00 2350

#其他方法
print(time.clock())#计算cpu执行时间





