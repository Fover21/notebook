#序列化模块
#what
#什么叫序列化--将原本的字典、列表等内容转换成一个字符串的过程叫做序列化。
#why
#序列化的目的
##1.以某种存储形式使自定义对象持久化
##2.将对象从一个地方传递到另一个地方
##3.使程序更具有维护性

#str-------------反序列化-------->>>数据结构
#数据结构<<<-------序列化-------------str

#json
#json模块提供了四个功能：dumps,dump,loads,load

#loads 和 dumps  ****************

import json

dic0 = {'k1':'v1', 'k2':'v2'}
str_dic = json.dumps(dic0)  #序列化：将一个字典转换成一个字符串
print(str_dic, type(str_dic))#{"k1": "v1", "k2": "v2"} <class 'str'>
#注意：要用json转换完的字符串类型的字典中的字符串是由""表示的

dic1 = json.loads(str_dic)  #反序列化：将一个字符串格式的字典转换为一个字典
#注意：要用json的loads功能处理的字符串类型的字典中的字符串必须由""表示
print(dic1, type(dic1))#{'k1': 'v1', 'k2': 'v2'} <class 'dict'>

list_dic = [1,['a','b','c'],3,{'k1':'v1','k2':'v2'}]
str_dic = json.dumps(list_dic) #也可以处理嵌套的数据类型 
print(type(str_dic),str_dic) #<class 'str'> [1, ["a", "b", "c"], 3, {"k1": "v1", "k2": "v2"}]
list_dic2 = json.loads(str_dic)
print(type(list_dic2),list_dic2) #<class 'list'> [1, ['a', 'b', 'c'], 3, {'k1': 'v1', 'k2': 'v2'}]

#load 和 dump    ******************

import json

f = open('json_file','w')
dic0 = {'k1':'v1', 'k2':'v2'}
json.dump(dic0,f)	#dump方法接收一个文件句柄，直接将字典转为json字符串写入文件
f.close()

f = open('json_file', 'r')
dic1 = json.load(f)	#load方法接收一个文件句柄，直接将文件中的json字符串转换成数据结构返回
f.close()
print(dic1, type(dic1))#{'k1': 'v1', 'k2': 'v2'} <class 'dict'>

#ensure_ascii关键字参数  ********

import json

f = open('file.txt','w',encoding='utf-8')
ret = json.dumps({'国籍':'美国'},ensure_ascii=False)
f.write(ret+'\n')
f.close()

#其他参数说明

# 1.Serialize obj to a JSON formatted str.(字符串表示的json对象) 
# 2.Skipkeys：默认值是False，如果dict的keys内的数据不是python的基本类型(str,unicode,int,long,float,bool,None)，设置为False时，就会报TypeError的错误。此时设置成True，则会跳过这类key 
# 3.ensure_ascii:，当它为True的时候，所有非ASCII码字符显示为\uXXXX序列，只需在dump时将ensure_ascii设置为False即可，此时存入json的中文即可正常显示。) 
# If check_circular is false, then the circular reference check for container types will be skipped and a circular reference will result in an OverflowError (or worse). 
# If allow_nan is false, then it will be a ValueError to serialize out of range float values (nan, inf, -inf) in strict compliance of the JSON specification, instead of using the JavaScript equivalents (NaN, Infinity, -Infinity). 
# 4.indent：应该是一个非负的整型，如果是0就是顶格分行显示，如果为空就是一行最紧凑显示，否则会换行且按照indent的数值显示前面的空白分行显示，这样打印出来的json数据也叫pretty-printed json 
# 5.separators：分隔符，实际上是(item_separator, dict_separator)的一个元组，默认的就是(‘,’,’:’)；这表示dictionary内keys之间用“,”隔开，而KEY和value之间用“：”隔开。 
# 6.default(obj) is a function that should return a serializable version of obj or raise TypeError. The default simply raises TypeError. 
# 7.sort_keys：将数据根据keys的值进行排序。 
# To use a custom JSONEncoder subclass (e.g. one that overrides the .default() method to serialize additional types), specify it with the cls kwarg; otherwise JSONEncoder is used.

#json的格式化输出

import json
data = {'username':['李大爷','二大爷'],'sex':'male','age':16}
json_dic2 = json.dumps(data,sort_keys=True,indent=2,separators=(',',':'),ensure_ascii=False)
print(json_dic2)


#总结：
#1.json格式的key必须是字符串数据类型，json格式中的字符串必须是”“双引号
#2.如果数字是key，那么dump之后会强行转为字符串类型
#3.json对元组做value的字典会把元组强行转为列表，json对元组做key，不支持，会报错
#4.中文格式在文件中dumps和dump有关键字参数ensure_ascii
#5.json的其他参数 sort_keys,indent,separators
#6.不允许存set数据类型，set不能被dump和dumps
#7.不可以多次dunp


#pickle
# 用于序列化的两个模块

# json，用于字符串 和 python数据类型间进行转换
# pickle，用于python特有的类型 和 python的数据类型间进行转换

# pickle模块提供了四个功能：dumps、dump(序列化，存）、loads（反序列化，读）、load  （不仅可以序列化字典，列表...可以把python中任意的数据类型序列化

import pickle
dic = {'k1':'v1','k2':'v2','k3':'v3'}
str_dic = pickle.dumps(dic)
print(str_dic)  #一串二进制内容

dic2 = pickle.loads(str_dic)
print(dic2)    #字典

import time
struct_time  = time.localtime(1000000000)
print(struct_time)
f = open('pickle_file','wb')
pickle.dump(struct_time,f)
f.close()

f = open('pickle_file','rb')
struct_time2 = pickle.load(f)
print(struct_time2.tm_year)

# 这时候机智的你又要说了，既然pickle如此强大，为什么还要学json呢？
# 这里我们要说明一下，json是一种所有的语言都可以识别的数据结构。
# 如果我们将一个字典或者序列化成了一个json存在文件里，那么java代码或者js代码也可以拿来用。
# 但是如果我们用pickle进行序列化，其他语言就不能读懂这是什么了～
# 所以，如果你序列化的内容是列表或者字典，我们非常推荐你使用json模块
# 但如果出于某种原因你不得不序列化其他的数据类型，而未来你还会用python对这个数据进行反序列化的话，那么就可以使用pickle

#总结：
#1.dump的结果是bytes，dunp用的文件句柄需要wb，load需要用rb
#2.支持几乎所有对象的序列化，对应对象的序列化需要这个对象对应的类在内存中
#3.可以多次dump   while i: try: picle.load(f) excepe EOFError: break

#shelve

# shelve也是python提供给我们的序列化工具，比pickle用起来更简单一些。
# shelve只提供给我们一个open方法，是用key来访问的，使用起来和字典类似。

import shelve
f = shelve.open('shelve_file')
f['key'] = {'int':10, 'float':9.5, 'string':'Sample data'}  #直接对文件句柄操作，就可以存入数据
f.close()

import shelve
f1 = shelve.open('shelve_file')
existing = f1['key']  #取出数据的时候也只需要直接用key获取即可，但是如果key不存在会报错
f1.close()
print(existing)

# 这个模块有个限制，它不支持多个应用同一时间往同一个DB进行写操作。
#所以当我们知道我们的应用如果只进行读操作，我们可以让shelve通过只读方式打开DB

f = shelve.open('shelve_file', flag='r')
existing = f['key']
f.close()
print(existing)

# 由于shelve在默认情况下是不会记录待持久化对象的任何修改的，
#所以我们在shelve.open()时候需要修改默认参数，否则对象的修改不会保存。

import shelve
f1 = shelve.open('shelve_file')
print(f1['key'])
f1['key']['new_value'] = 'this was not here before'
f1.close()

f2 = shelve.open('shelve_file', writeback=True)
print(f2['key'])
f2['key']['new_value'] = 'this was not here before'
f2.close()

# writeback方式有优点也有缺点。
#优点是减少了我们出错的概率，并且让对象的持久化对用户更加的透明了；
#但这种方式并不是所有的情况下都需要，首先，使用writeback以后，
#shelf在open()的时候会增加额外的内存消耗，并且当DB在close()
#的时候会将缓存中的每一个对象都写入到DB，这也会带来额外的等待时间。
#因为shelve没有办法知道缓存中哪些对象修改了，哪些对象没有修改，
#因此所有的对象都会被写入

