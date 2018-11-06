# Django-model进阶

## 目录：

>- QuerySet
>- 中介模型
>- 查询优化
>- extra
>- 整体插入



# QuerySet

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
>
>>```
>>exists：
>>简单的使用if语句进行判断也会完全执行整个queryset并且把数据放入cache，虽然你并不需要这些 数
>>据！为了避免这个，可以用exists()方法来检查是否有数据：
>>
>> if queryResult.exists():
>>    #SELECT (1) AS "a" FROM "blog_article" LIMIT 1; args=()
>>        print("exists...")
>>```
>>
>>```
>>iterator:
>>当queryset非常巨大时，cache会成为问题。
>>
>>处理成千上万的记录时，将它们一次装入内存是很浪费的。更糟糕的是，巨大的queryset可能会锁住系统 
>>进程，让你的程序濒临崩溃。要避免在遍历数据的同时产生queryset cache，可以使用iterator()方法
>>来获取数据，处理完数据就将其丢弃。
>>
>>objs = Book.objects.all().iterator()
>># iterator()可以一次只从数据库获取少量数据，这样可以节省内存
>>for obj in objs:
>>    print(obj.title)
>>#BUT,再次遍历没有打印,因为迭代器已经在上一次遍历(next)到最后一次了,没得遍历了
>>for obj in objs:
>>    print(obj.title)
>>
>>当然，使用iterator()方法来防止生成cache，意味着遍历同一个queryset时会重复执行查询。所以使
>>#用iterator()的时候要当心，确保你的代码在操作一个大的queryset时没有重复执行查询。
>>
>>```
>>
>>总结:
>>
>>queryset的cache是用于减少程序对数据库的查询，在通常的使用下会保证只有在需要的时候才会查
>>
>>询数据库。 使用exists()和iterator()方法可以优化程序对内存的使用。不过，由于它们并不会生成
>>
>>queryset cache，可能 会造成额外的数据库查询。
>
># 中介模型
>
>>```
>>处理类似搭配 pizza 和 topping 这样简单的多对多关系时，使用标准的ManyToManyField  就可以
>>了。但是，有时你可能需要关联数据到两个模型之间的关系上。
>>
>>例如，有这样一个应用，它记录音乐家所属的音乐小组。我们可以用一个ManyToManyField 表示小组和成员之间的多对多关系。但是，有时你可能想知道更多成员关系的细节，比如成员是何时加入小组的。
>>
>>对于这些情况，Django 允许你指定一个中介模型来定义多对多关系。 你可以将其他字段放在中介模型里
>>面。源模型的ManyToManyField 字段将使用through 参数指向中介模型。对于上面的音乐小组的例子，
>>代码如下：
>>
>>from django.db import models
>> 
>>class Person(models.Model):
>>    name = models.CharField(max_length=128)
>> 
>>    def __str__(self):              # __unicode__ on Python 2
>>        return self.name
>> 
>>class Group(models.Model):
>>    name = models.CharField(max_length=128)
>>    members = models.ManyToManyField(Person, through='Membership')
>> 
>>    def __str__(self):              # __unicode__ on Python 2
>>        return self.name
>> 
>>class Membership(models.Model):
>>    person = models.ForeignKey(Person)
>>    group = models.ForeignKey(Group)
>>    date_joined = models.DateField()
>>    invite_reason = models.CharField(max_length=64)
>>既然你已经设置好ManyToManyField 来使用中介模型（在这个例子中就是Membership），接下来你要开
>>始创建多对多关系。你要做的就是创建中介模型的实例：
>>
>>
>>>>> ringo = Person.objects.create(name="Ringo Starr")
>>>>> paul = Person.objects.create(name="Paul McCartney")
>>>>> beatles = Group.objects.create(name="The Beatles")
>>>>> m1 = Membership(person=ringo, group=beatles,
>>...     date_joined=date(1962, 8, 16),
>>...     invite_reason="Needed a new drummer.")
>>>>> m1.save()
>>>>> beatles.members.all()
>>[<Person: Ringo Starr>]
>>>>> ringo.group_set.all()
>>[<Group: The Beatles>]
>>>>> m2 = Membership.objects.create(person=paul, group=beatles,
>>...     date_joined=date(1960, 8, 1),
>>...     invite_reason="Wanted to form a band.")
>>>>> beatles.members.all()
>>[<Person: Ringo Starr>, <Person: Paul McCartney>]
>>与普通的多对多字段不同，你不能使用add、 create和赋值语句（比如，beatles.members = [...]）来创建关系：
>>
>>
>># THIS WILL NOT WORK
>>>>> beatles.members.add(john)
>># NEITHER WILL THIS
>>>>> beatles.members.create(name="George Harrison")
>># AND NEITHER WILL THIS
>>>>> beatles.members = [john, paul, ringo, george]
>>为什么不能这样做？ 这是因为你不能只创建 Person和 Group之间的关联关系，你还要指定 Membership模型中所需要的所有信息；而简单的add、create 和赋值语句是做不到这一点的。所以它们
>>不能在使用中介模型的多对多关系中使用。此时，唯一的办法就是创建中介模型的实例。
>>
>> remove()方法被禁用也是出于同样的原因。但是clear() 方法却是可用的。它可以清空某个实例所有的
>> 多对多关系：
>>
>>
>>>>> # Beatles have broken up
>>>>> beatles.members.clear()
>>>>> # Note that this deletes the intermediate model instances
>>>>> Membership.objects.all()
>>
>>```
>>
>>

# 查询优化

>表数据
>
>>```
>>class UserInfo(AbstractUser):
>>    """
>>    用户信息
>>    """
>>    nid = models.BigAutoField(primary_key=True)
>>    nickname = models.CharField(verbose_name='昵称', max_length=32)
>>    telephone = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
>>    avatar = models.FileField(verbose_name='头像',upload_to = 'avatar/',default="/avatar/default.png")
>>    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
>> 
>>    fans = models.ManyToManyField(verbose_name='粉丝们',
>>                                  to='UserInfo',
>>                                  through='UserFans',
>>                                  related_name='f',
>>                                  through_fields=('user', 'follower'))
>> 
>>    def __str__(self):
>>        return self.username
>> 
>>class UserFans(models.Model):
>>    """
>>    互粉关系表
>>    """
>>    nid = models.AutoField(primary_key=True)
>>    user = models.ForeignKey(verbose_name='博主', to='UserInfo', to_field='nid', related_name='users')
>>    follower = models.ForeignKey(verbose_name='粉丝', to='UserInfo', to_field='nid', related_name='followers')
>> 
>>class Blog(models.Model):
>> 
>>    """
>>    博客信息
>>    """
>>    nid = models.BigAutoField(primary_key=True)
>>    title = models.CharField(verbose_name='个人博客标题', max_length=64)
>>    site = models.CharField(verbose_name='个人博客后缀', max_length=32, unique=True)
>>    theme = models.CharField(verbose_name='博客主题', max_length=32)
>>    user = models.OneToOneField(to='UserInfo', to_field='nid')
>>    def __str__(self):
>>        return self.title
>> 
>>class Category(models.Model):
>>    """
>>    博主个人文章分类表
>>    """
>>    nid = models.AutoField(primary_key=True)
>>    title = models.CharField(verbose_name='分类标题', max_length=32)
>> 
>>    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid')
>> 
>>class Article(models.Model):
>> 
>>    nid = models.BigAutoField(primary_key=True)
>>    title = models.CharField(max_length=50, verbose_name='文章标题')
>>    desc = models.CharField(max_length=255, verbose_name='文章描述')
>>    read_count = models.IntegerField(default=0)
>>    comment_count= models.IntegerField(default=0)
>>    up_count = models.IntegerField(default=0)
>>    down_count = models.IntegerField(default=0)
>>    category = models.ForeignKey(verbose_name='文章类型', to='Category', to_field='nid', null=True)
>>    create_time = models.DateField(verbose_name='创建时间')
>>    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid')
>>    tags = models.ManyToManyField(
>>        to="Tag",
>>        through='Article2Tag',
>>        through_fields=('article', 'tag'),
>>)
>> 
>> 
>>class ArticleDetail(models.Model):
>>    """
>>    文章详细表
>>    """
>>    nid = models.AutoField(primary_key=True)
>>    content = models.TextField(verbose_name='文章内容', )
>> 
>>    article = models.OneToOneField(verbose_name='所属文章', to='Article', to_field='nid')
>> 
>> 
>>class Comment(models.Model):
>>    """
>>    评论表
>>    """
>>    nid = models.BigAutoField(primary_key=True)
>>    article = models.ForeignKey(verbose_name='评论文章', to='Article', to_field='nid')
>>    content = models.CharField(verbose_name='评论内容', max_length=255)
>>    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
>> 
>>    parent_comment = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')
>>    user = models.ForeignKey(verbose_name='评论者', to='UserInfo', to_field='nid')
>> 
>>    up_count = models.IntegerField(default=0)
>> 
>>    def __str__(self):
>>        return self.content
>> 
>>class ArticleUpDown(models.Model):
>>    """
>>    点赞表
>>    """
>>    nid = models.AutoField(primary_key=True)
>>    user = models.ForeignKey('UserInfo', null=True)
>>    article = models.ForeignKey("Article", null=True)
>>    models.BooleanField(verbose_name='是否赞')
>> 
>>class CommentUp(models.Model):
>>    """
>>    点赞表
>>    """
>>    nid = models.AutoField(primary_key=True)
>>    user = models.ForeignKey('UserInfo', null=True)
>>    comment = models.ForeignKey("Comment", null=True)
>> 
>> 
>>class Tag(models.Model):
>>    nid = models.AutoField(primary_key=True)
>>    title = models.CharField(verbose_name='标签名称', max_length=32)
>>    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid')
>> 
>> 
>> 
>>class Article2Tag(models.Model):
>>    nid = models.AutoField(primary_key=True)
>>    article = models.ForeignKey(verbose_name='文章', to="Article", to_field='nid')
>>    tag = models.ForeignKey(verbose_name='标签', to="Tag", to_field='nid')
>>```
>
>select_related
>
>>简单使用
>>
>>>```
>>>对于一对一字段（OneToOneField）和外键字段（ForeignKey），可以使用select_related 来对
>>>QuerySet进行优化。
>>>
>>>select_related 返回一个QuerySet，当执行它的查询时它沿着外键关系查询关联的对象的数据。它
>>>会生成一个复杂的查询并引起性能的损耗，但是在以后使用外键关系时将不需要数据库查询。
>>>
>>>简单说，在对QuerySet使用select_related()函数后，Django会获取相应外键对应的对象，从而在
>>>之后需要的时候不必再查询数据库了。
>>>
>>>下面的例子解释了普通查询和select_related() 查询的区别。
>>>
>>>查询id=2的文章的分类名称,下面是一个标准的查询：
>>># Hits the database.
>>>article=models.Article.objects.get(nid=2)
>>> 
>>># Hits the database again to get the related Blog object.
>>>print(article.category.title)
>>>
>>>'''
>>> 
>>>SELECT
>>>    "blog_article"."nid",
>>>    "blog_article"."title",
>>>    "blog_article"."desc",
>>>    "blog_article"."read_count",
>>>    "blog_article"."comment_count",
>>>    "blog_article"."up_count",
>>>    "blog_article"."down_count",
>>>    "blog_article"."category_id",
>>>    "blog_article"."create_time",
>>>     "blog_article"."blog_id",
>>>     "blog_article"."article_type_id"
>>>             FROM "blog_article"
>>>             WHERE "blog_article"."nid" = 2; args=(2,)
>>> 
>>>SELECT
>>>     "blog_category"."nid",
>>>     "blog_category"."title",
>>>     "blog_category"."blog_id"
>>>              FROM "blog_category"
>>>              WHERE "blog_category"."nid" = 4; args=(4,)
>>> 
>>> 
>>>'''
>>>```
>>>
>>> 如果我们使用select_related()函数：
>>>
>>>```
>>>articleList=models.Article.objects.select_related("category").all()
>>> 
>>> 
>>>    for article_obj in articleList:
>>>        #  Doesn't hit the database, because article_obj.category
>>>        #  has been prepopulated in the previous query.
>>>        print(article_obj.category.title)
>>>
>>>SELECT
>>>     "blog_article"."nid",
>>>     "blog_article"."title",
>>>     "blog_article"."desc",
>>>     "blog_article"."read_count",
>>>     "blog_article"."comment_count",
>>>     "blog_article"."up_count",
>>>     "blog_article"."down_count",
>>>     "blog_article"."category_id",
>>>     "blog_article"."create_time",
>>>     "blog_article"."blog_id",
>>>     "blog_article"."article_type_id",
>>> 
>>>     "blog_category"."nid",
>>>     "blog_category"."title",
>>>     "blog_category"."blog_id"
>>> 
>>>FROM "blog_article"
>>>LEFT OUTER JOIN "blog_category" ON ("blog_article"."category_id" = "blog_category"."nid");
>>>```
>>
>>多外键使用
>>
>>>```
>>>这是针对category的外键查询，如果是另外一个外键呢？让我们一起看下：
>>>
>>>article=models.Article.objects.select_related("category").get(nid=1)
>>>print(article.articledetail)
>>> 观察logging结果，发现依然需要查询两次，所以需要改为：
>>>article=models.Article.objects.select_related("category","articledetail").get(nid=1)
>>>print(article.articledetail)
>>> 或者：
>>>
>>>article=models.Article.objects
>>>　　　　　　　　　　　　　.select_related("category")
>>>　　　　　　　　　　　　　.select_related("articledetail")
>>>　　　　　　　　　　　　　.get(nid=1)  # django 1.7 支持链式操作
>>>print(article.articledetail)
>>> 
>>>
>>>
>>>SELECT
>>> 
>>>    "blog_article"."nid",
>>>    "blog_article"."title",
>>>    ......
>>> 
>>>    "blog_category"."nid",
>>>    "blog_category"."title",
>>>    "blog_category"."blog_id",
>>> 
>>>    "blog_articledetail"."nid",
>>>    "blog_articledetail"."content",
>>>    "blog_articledetail"."article_id"
>>> 
>>>   FROM "blog_article"
>>>   LEFT OUTER JOIN "blog_category" ON ("blog_article"."category_id" = "blog_category"."nid")
>>>   LEFT OUTER JOIN "blog_articledetail" ON ("blog_article"."nid" = "blog_articledetail"."article_id")
>>>   WHERE "blog_article"."nid" = 1; args=(1,)
>>>```
>>
>>深层查询
>>
>>>```
>>># 查询id=1的文章的用户姓名
>>>    article=models.Article.objects.select_related("blog").get(nid=1)
>>>    print(article.blog.user.username)
>>> 依然需要查询两次：
>>>
>>>
>>>SELECT
>>>    "blog_article"."nid",
>>>    "blog_article"."title",
>>>    ......
>>> 
>>>     "blog_blog"."nid",
>>>     "blog_blog"."title",
>>> 
>>>   FROM "blog_article" INNER JOIN "blog_blog" ON ("blog_article"."blog_id" = "blog_blog"."nid")
>>>   WHERE "blog_article"."nid" = 1;
>>> 
>>> 
>>> 
>>> 
>>>SELECT
>>>    "blog_userinfo"."password",
>>>    "blog_userinfo"."last_login",
>>>    ......
>>> 
>>>FROM "blog_userinfo"
>>>WHERE "blog_userinfo"."nid" = 1;
>>>
>>>
>>>
>>> 这是因为第一次查询没有query到userInfo表，所以，修改如下：
>>>
>>>article=models.Article.objects.select_related("blog__user").get(nid=1)
>>>print(article.blog.user.username)
>>>
>>>
>>>SELECT
>>> 
>>>"blog_article"."nid", "blog_article"."title",
>>>......
>>> 
>>> "blog_blog"."nid", "blog_blog"."title",
>>>......
>>> 
>>> "blog_userinfo"."password", "blog_userinfo"."last_login",
>>>......
>>> 
>>>FROM "blog_article"
>>> 
>>>INNER JOIN "blog_blog" ON ("blog_article"."blog_id" = "blog_blog"."nid")
>>> 
>>>INNER JOIN "blog_userinfo" ON ("blog_blog"."user_id" = "blog_userinfo"."nid")
>>>WHERE "blog_article"."nid" = 1;
>>>```
>>
>>总结：
>>
>>1. select_related主要针一对一和多对一关系进行优化。
>>
>>2. select_related使用SQL的JOIN语句进行优化，通过减少SQL查询的次数来进行优化、提高性能。
>>
>>3. 可以通过可变长参数指定需要select_related的字段名。也可以通过使用双下划线“__”连接字段名
>>
>>   来实现指定的递归查询。
>>
>>4. 没有指定的字段不会缓存，没有指定的深度不会缓存，如果要访问的话Django会再次进行SQL查询。
>>
>>5. 也可以通过depth参数指定递归的深度，Django会自动缓存指定深度内所有的字段。如果要访问指定深度外的字段，Django会再次进行SQL查询。
>>
>>6. 也接受无参数的调用，Django会尽可能深的递归查询所有的字段。但注意有Django递归的限制和性能的浪费。
>>
>>7. Django >= 1.7，链式调用的select_related相当于使用可变长参数。Django < 1.7，链式调用会导致前边的select_related失效，只保留最后一个。
>
>perfetch_related()
>
>>```
>>对于多对多字段（ManyToManyField）和一对多字段，可以使用prefetch_related()来进行优化。
>>
>>prefetch_related()和select_related()的设计目的很相似，都是为了减少SQL查询的数量，但是实现的方式不一样。后者是通过JOIN语句，在SQL查询内解决问题。但是对于多对多关系，使用SQL语句解决就显得有些不太明智，因为JOIN得到的表将会很长，会导致SQL语句运行时间的增加和内存占用的增加。若有n个对象，每个对象的多对多字段对应Mi条，就会生成Σ(n)Mi 行的结果表。
>>
>>prefetch_related()的解决方法是，分别查询每个表，然后用Python处理他们之间的关系。
>>
>>
>># 查询所有文章关联的所有标签
>>    article_obj=models.Article.objects.all()
>>    for i in article_obj:
>> 
>>        print(i.tags.all())  #4篇文章: hits database 5
>>改为prefetch_related：
>>
>>
>># 查询所有文章关联的所有标签
>>    article_obj=models.Article.objects.prefetch_related("tags").all()
>>    for i in article_obj:
>> 
>>        print(i.tags.all())  #4篇文章: hits database 2
>>
>>
>>SELECT "blog_article"."nid",
>>               "blog_article"."title",
>>               ......
>> 
>>FROM "blog_article";
>> 
>> 
>> 
>>SELECT
>>  ("blog_article2tag"."article_id") AS "_prefetch_related_val_article_id",
>>  "blog_tag"."nid",
>>  "blog_tag"."title",
>>  "blog_tag"."blog_id"
>>   FROM "blog_tag"
>>  INNER JOIN "blog_article2tag" ON ("blog_tag"."nid" = "blog_article2tag"."tag_id")
>>  WHERE "blog_article2tag"."article_id" IN (1, 2, 3, 4);
>>```

# extra

>```
>extra(select=None, where=None, params=None, 
>      tables=None, order_by=None, select_params=None)
>```
>
>有些情况下，Django的查询语法难以简单的表达复杂的 `WHERE` 子句，对于这种情况, Django 提供了 
>
>`extra()` `QuerySet`修改机制 — 它能在 `QuerySet`生成的SQL从句中注入新子句
>
>extra可以指定一个或多个 `参数`,例如 `select`, `where` or `tables`. 这些参数都不是必须的，但是你至
>
>少要使用一个!要注意这些额外的方式对不同的数据库引擎可能存在移植性问题.(因为你在显式的书写SQ
>
>L语句),除非万不得已,尽量避免这样做
>
>### 参数之select
>
>The `select` 参数可以让你在 `SELECT` 从句中添加其他字段信息，它应该是一个字典，存放着属性名到
>
> SQL 从句的映射。
>
>```
>queryResult=models.Article
>　　　　　　　　　　　.objects.extra(select={'is_recent': "create_time > '2017-09-05'"})
>```
>
>结果集中每个 Entry 对象都有一个额外的属性is_recent, 它是一个布尔值，表示 Article对象的
>
>create_time 是否晚于2017-09-05.
>
>练习：
>
>```
># in sqlite:
>    article_obj=models.Article.objects
>　　　　　　　　　　　　　　.filter(nid=1)
>　　　　　　　　　　　　　　.extra(select={"standard_time":"strftime('%%Y-%%m-%%d',create_time)"})
>　　　　　　　　　　　　　　.values("standard_time","nid","title")
>    print(article_obj)
>    # <QuerySet [{'title': 'MongoDb 入门教程', 'standard_time': '2017-09-03', 'nid': 1}]>
>```
>
>
>
>### 参数之`where` / `tables`
>
>您可以使用`where`定义显式SQL `WHERE`子句 - 也许执行非显式连接。您可以使用`tables`手动将表添加
>
>到SQL `FROM`子句。
>
>`where`和`tables`都接受字符串列表。所有`where`参数均为“与”任何其他搜索条件。
>
>举例来讲：
>
>```
>queryResult=models.Article
>　　　　　　　　　　　.objects.extra(where=['nid in (1,3) OR title like "py%" ','nid>2'])
>```

# 整体插入

创建对象时，尽可能使用bulk_create()来减少SQL查询的数量。例如：

```
Entry.objects.bulk_create([
    Entry(headline="Python 3.0 Released"),
    Entry(headline="Python 3.1 Planned")
])
```

...更优于：

```
Entry.objects.create(headline="Python 3.0 Released")
Entry.objects.create(headline="Python 3.1 Planned")
```

注意该方法有很多注意事项，所以确保它适用于你的情况。

这也可以用在ManyToManyFields中，所以：

```
my_band.members.add(me, my_friend)
```

...更优于：

```
my_band.members.add(me)
my_band.members.add(my_friend)
```

...其中Bands和Artists具有多对多关联。

