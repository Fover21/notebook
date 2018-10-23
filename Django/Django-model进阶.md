# Django-model进阶

## 目录：

>- QuerySet
>- 中介模型
>- 查询优化
>- extra
>- 整体插入

#### QuerySet

>
>
>1、可切片
>
>>```
>>使用Python 的切片语法来限制查询集记录的数目 。它等同于SQL 的LIMIT 和OFFSET 子句。
>>>>> Entry.objects.all()[:5]      # (LIMIT 5)
>>>>> Entry.objects.all()[5:10]    # (OFFSET 5 LIMIT 5)
>>不支持负的索引（例如Entry.objects.all()[-1]）。
>>通常，查询集 的切片返回一个新的查询集 —— 它不会执行查询。
>>```
>
>2、可迭代
>
>>```
>>articleList=models.Article.objects.all()
>>
>>for article in articleList:
>>    print(article.title)
>>```
>
>3、惰性查询
>
>>```
>>查询集 是惰性执行的 —— 创建查询集不会带来任何数据库的访问。你可以将过滤器保持一整天，直到查询集 需要求值时，Django 才会真正运行这个查询。
>>
>>queryResult=models.Article.objects.all() # not hits database
>> 
>>print(queryResult) # hits database
>> 
>>for article in queryResult:
>>    print(article.title)    # hits database
>> 
>> 一般来说，只有在“请求”查询集 的结果时才会到数据库中去获取它们。当你确实需要结果时，查询集 通过访问数据库来求值。
>>```
>
>4、缓存机制
>
>>```
>>每个查询集都包含一个缓存来最小化对数据库的访问。理解它是如何工作的将让你编写最高效的代码。
>>
>>在一个新创建的查询集中，缓存为空。首次对查询集进行求值 —— 同时发生数据库查询 ——Django 将保存查询的结果到查询集的缓存中并返回明确请求的结果（例如，如果正在迭代查询集，则返回下一个结果）。接下来对该查询集 的求值将重用缓存的结果。
>>
>>请牢记这个缓存行为，因为对查询集使用不当的话，它会坑你的。例如，下面的语句创建两个查询集，对它们求值，然后扔掉它们：
>>
>>print([a.title for a in models.Article.objects.all()])
>>print([a.create_time for a in models.Article.objects.all()])
>>这意味着相同的数据库查询将执行两次，显然倍增了你的数据库负载。同时，还有可能两个结果列表并不包含相同的数据库记录，因为在两次请求期间有可能有Article被添加进来或删除掉。为了避免这个问题，只需保存查询集并重新使用它：
>>
>>queryResult=models.Article.objects.all()
>>print([a.title for a in queryResult])
>>print([a.create_time for a in queryResult])
>>何时查询集不会被缓存?
>>查询集不会永远缓存它们的结果。当只对查询集的部分进行求值时会检查缓存， 如果这个部分不在缓存中，那么接下来查询返回的记录都将不会被缓存。所以，这意味着使用切片或索引来限制查询集将不会填充缓存。
>>
>>例如，重复获取查询集对象中一个特定的索引将每次都查询数据库：
>>
>>>>> queryset = Entry.objects.all()
>>>>> print queryset[5] # Queries the database
>>>>> print queryset[5] # Queries the database again
>>然而，如果已经对全部查询集求值过，则将检查缓存：
>>
>>>>> queryset = Entry.objects.all()
>>>>> [entry for entry in queryset] # Queries the database
>>>>> print queryset[5] # Uses cache
>>>>> print queryset[5] # Uses cache
>>下面是一些其它例子，它们会使得全部的查询集被求值并填充到缓存中：
>>
>>>>> [entry for entry in queryset]
>>>>> bool(queryset)
>>>>> entry in queryset
>>>>> list(queryset)
>>注：简单地打印查询集不会填充缓存。
>>
>>queryResult=models.Article.objects.all()
>>print(queryResult) #  hits database
>>print(queryResult) #  hits database
>>```
>>
>>
>
>5、exists()与iterator()方法