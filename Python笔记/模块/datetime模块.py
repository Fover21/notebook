datetime模块

datetime模块重新封装了time模块，提供更多接口，提供的类有：date,time,datetime,timedelta,tzinfo。

1、date类

datetime.date(year, month, day)

静态方法和字段

date.max、date.min：date对象所能表示的最大、最小日期；
date.resolution：date对象表示日期的最小单位。这里是天。
date.today()：返回一个表示当前本地日期的date对象；
date.fromtimestamp(timestamp)：根据给定的时间戮，返回一个date对象；

1 >>> import datetime
2 >>> datetime.date.max
3 datetime.date(9999, 12, 31)
4 >>> datetime.date.min
5 datetime.date(1, 1, 1)
6 >>> datetime.date.resolution
7 datetime.timedelta(1)
8 >>> datetime.date.today()
9 datetime.date(2017, 4, 8)
10 >>> datetime.date.fromtimestamp(time.time())
11 datetime.date(2017, 4, 8)

方法和属性

d1 = date(2017,4,8)  #date对象（年月日都不能是以0开头 (2017,04,08)错误 ）

>>> d1 = datetime.date(2017,4,8)
>>> d1
datetime.date(2017, 4, 8)
>>> d1.year
2017
>>> d1.month
4
>>> d1.day
8
>>>
d1.replace(year, month, day)：生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性。（原有对象仍保持不变）

>>> d2 = d1.replace(2017,3,20)
>>> d1
datetime.date(2017, 4, 8)
>>> d2
datetime.date(2017, 3, 20)
>>>
d1.timetuple()：返回日期对应的time.struct_time对象；

>>> d1.timetuple()
time.struct_time(tm_year=2017, tm_mon=4, tm_mday=8, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=98, tm_isdst=-1)
>>>
d1.weekday()：返回weekday，如果是星期一，返回0；如果是星期2，返回1，以此类推；

>>> d1.weekday()
5       #周六
>>>
d1.isoweekday()：返回weekday，如果是星期一，返回1；如果是星期2，返回2，以此类推；

>>> d1.isoweekday()
6      #周六   weekday镜像？
>>>
d1.isocalendar()：返回格式如(year，sum_week，day)的元组；

>>> d1
datetime.date(2017, 4, 8)
>>> d1.isocalendar()
(2017, 14, 6)          #第一个是2017年， 14是 当前为今年的第14周  6 表示 第14周结束后过了6天(当前是15周)
>>>
d1.isoformat()：返回格式如'YYYY-MM-DD’的字符串；

>>> d1.isoformat()
'2017-04-08'
>>>
d1.strftime(fmt)：和time模块format相同。

>>> d1.strftime('%Y-%m-%d')
'2017-04-08'
>>>



2、time类

datetime.time(hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] )

静态方法和字段

复制代码
time.min、time.max：time类所能表示的最小、最大时间

>>> import datetime
>>> datetime.time.min
datetime.time(0, 0)
>>> datetime.time.max
datetime.time(23, 59, 59, 999999)
>>>
time.resolution：时间的最小单位，这里是1微秒；

>>> datetime.time.resolution
datetime.timedelta(0, 0, 1)      #秒，毫秒，微秒
>>>

方法和属性

t1 = datetime.time(10,23,15)  #time对象 时，分，秒...
t1.hour、t1.minute、t1.second、t1.microsecond：时、分、秒、微秒；

>>> t = datetime.time(15,30,20)
>>> t
datetime.time(15, 30, 20)
>>> t.hour
15
>>> t.minute
30
>>> t.second
20
>>> t.microsecond
0
>>>
t1.tzinfo：时区信息；
t1.replace([ hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )：创建一个新的时间对象，用参数指定的时、分、秒、微秒代替原有对象中的属性（原有对象仍保持不变）；
t1.isoformat()：返回型如"HH:MM:SS"格式的字符串表示；
t1.strftime(fmt)：同time模块中的format；

3、datetime类

datetime相当于date和time结合起来。
datetime.datetime (year, month, day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )

静态方法和字段

datetime.today()：返回一个表示当前本地时间的datetime对象；
datetime.now([tz])：返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间；
datetime.utcnow()：返回一个当前utc时间的datetime对象；#格林威治时间
datetime.fromtimestamp(timestamp[, tz])：根据时间戮创建一个datetime对象，参数tz指定时区信息；
datetime.utcfromtimestamp(timestamp)：根据时间戮创建一个datetime对象；
datetime.combine(date, time)：根据date和time，创建一个datetime对象；
datetime.strptime(date_string, format)：将格式字符串转换为datetime对象；

方法和属性

dt=datetime.now()#datetime对象
dt.year、month、day、hour、minute、second、microsecond、tzinfo：
dt.date()：获取date对象；
dt.time()：获取time对象；
dt. replace ([ year[ , month[ , day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] ] ] ])：
dt. timetuple ()
dt. utctimetuple ()
dt. toordinal ()
dt. weekday ()
dt. isocalendar ()
dt. isoformat ([ sep] )
dt. ctime ()：返回一个日期时间的C格式字符串，等效于time.ctime(time.mktime(dt.timetuple()))；
dt. strftime (format)

4.timedelta类，时间加减

使用timedelta可以很方便的在日期上做天days，小时hour，分钟，秒，毫秒，微妙的时间计算，如果要计算月份则需要另外的办法。


1 >>> import datetime
2 >>> d = datetime.datetime.now()
3 >>> d
4 datetime.datetime(2017, 4, 8, 15, 42, 1, 656144) 8 >>> d1 = d + datetime.timedelta(days=-1)      #昨天
9 >>> d1
10 datetime.datetime(2017, 4, 7, 15, 42, 1, 656144)
11 >>> d2 = d - datetime.timedelta(days=1)      #昨天
12 >>> d2
13 datetime.datetime(2017, 4, 7, 15, 42, 1, 656144)
14 >>> d3 = d + datetime.timedelta(days=1)          #明天
15 >>> d3
16 datetime.datetime(2017, 4, 9, 15, 42, 1, 656144)
17 >>>

5、tzinfo时区类

from datetime import datetime, tzinfo,timedelta

"""
    tzinfo是关于时区信息的类
    tzinfo是一个抽象类，所以不能直接被实例化
    """
class UTC(tzinfo):
    """UTC"""
    def __init__(self,offset = 0):
        self._offset = offset
    
    def utcoffset(self, dt):
        return timedelta(hours=self._offset)
    
    def tzname(self, dt):
        return "UTC +%s" % self._offset
    
    def dst(self, dt):
        return timedelta(hours=self._offset)

#北京时间
beijing = datetime(2011,11,11,0,0,0,tzinfo = UTC(8))
print ("beijing time:",beijing)
#曼谷时间
bangkok = datetime(2011,11,11,0,0,0,tzinfo = UTC(7))
print ("bangkok time",bangkok)
#北京时间转成曼谷时间
print ("beijing-time to bangkok-time:",beijing.astimezone(UTC(7)))

#计算时间差时也会考虑时区的问题
timespan = beijing - bangkok
print ("时差:",timespan)

#Output==================
# beijing time: 2011-11-11 00:00:00+08:00
# bangkok time 2011-11-11 00:00:00+07:00
# beijing-time to bangkok-time: 2011-11-10 23:00:00+07:00
# 时差: -1 day, 23:00:00
