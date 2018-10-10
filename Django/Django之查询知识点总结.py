========关于Django查询知识点总结=======

models.Book.objects.filter(**kwargs): querySet [obj1,obj2]
models.Book.objects.filter(**kwargs).values(*args) : querySet [{},{},{}]
models.Book.objects.filter(**kwargs).values_list(title) : querySet [(),(),()]

跨表查询总结
    - 创建表
        class Book(models.Model):
        　　title = models.CharField(max_length=32)
        　　publish=models.ForeignKey("Publish") # 创建一对多的外键字段
        　　authorList=models.ManyToManyField("Author") # 多对多的关系，自动创建关系表
        class Publish(models.Model):
        　　name = models.CharField(max_length=32)
        　　addr = models.CharField(max_length=32)
        class Author(models.Model):
        　　name=models.CharField(max_length=32)
        　　age=models.IntegerField()
        　　ad=models.models.OneToOneField("AuthorDetail") #创建一对一的关系
        class AuthorDetail(models.Model):
        　　tel=models.IntegerField()

    - 基于对象关联查询
        - 一对多查询（Book-Publish）
            - 正向查询，按字段
                - book_obj.publish:与这本书关联的出版社对象
                - book_obj.publish.addr:与这本书关联的出版社地址
            - 反向查询，按表名_set
                - publish_obj.book_set:与这个出版社关联的书籍对象集合
                - publish_obj.book_set.all():[obj1, obj2, ...]
        - 一对一查询（Author-AuthorDetail）
            - 正向查询，按字段
                - author_obj.ad:与这个作者关联的作者详细信息对象
            - 反向查询，按表名
                - author_detail_obj.author:与这个作者详细对象关联的作者对象
        - 多对多（Book-Author）
            - 正向查询，按字段
                - book_obj.authorList.all():与这本书关联的所有这作者对象的集合[obj1,obj2,...]
                - book_obj.authorList.all().values("name"):如果想查单个值得时候可以这样查
            - 反向查询，按表名_set
                - author_obj.book_set.all():与这个作者关联的所有书籍对象的集合
                - author_obj.book_set.all().values("name"):如果想查单个值得时候可以这样查

    - 基于双下滑线的跨表查询
        - 一对多查询（Book-Publish）
            - 正向查询，按字段
                - # 查询python这本书的出版社的名字
                - models.Book.objects.all().filter(title='python').values("publish__name")
            - 反向查询，按表名
                - #查询人民出版社出版过的所有书籍的名字
                －　models.Publish.objects.filter(name='人民出版社').values("book__title")
        - 一对一查询（Author-AuthorDetail）
            - 正向查询，按字段
                - #查询ward的手机号
                - models.Author.objects.filter(name='ward')values('ad__tel')
            - 反向查询，按表名
                - #查询手机号是10086的作者
                - models.AuthorDetail.objects.filter(tel='10086').values('author__name')
        - 多对多
            - 正向查询，按字段
                - #查询python这本书的作者的名字
                - models.Book.objects.filter(title="pytohon").values("authorList__name") [{},{},{},{},...]
            - 反向查询，按表名
                - #查询ward出版过的书的价格
                - models.Author.objects.filter(name='ward').values("book__price")

- 注意：

    publish=models.ForeignKey("Publish",related_name="bookList")
    authorlist=models.ManyToManyField("Author",related_name="bookList")
    ad=models.models.OneToOneField("AuthorDetail"，related_name="authorInfo")
    反向查询的时候都用：related_name的值

- 聚合查询
    querySet().aggregate(聚合函数)------返回的是一个字典，不再是一个querySet
    Book.objects.all().aggregate(average_price=Avg('price'))

- 分组查询
    querySet().annotate()　--- 返回的是querySet

    #统计每一个出版社中最便宜的书籍的价格

    sql:   select Min(price) from book group by publish_id;
    ORM:　　models.Book.objects.values("publish__name").annotate(Min("price"))






















