Django之模板继承

模板继承
    - 目的是：减少代码的冗余
    - 语法：
        {% block classinfo %}
        
        {% endblock %}
    - 具体步骤
        1）创建一个base.html文件
        2）把要显示的页面的内容写在这里面，也就是html要在浏览器显示的内容
        3）在right里面写个盒子
            {% block classinfo %}
            
            {% engblock %}
            在这里面写个空盒子，以后谁来扩展就在这个盒子里面添加相应的内容就行
        4) 然后再创建一个.html文件，让这个继承base.html文件
            {% extends "base.html" %}    #必须是在文件的第一行
        　　 在基板里面添加内容
        　　 {% block classinfo %}
        　　 　　<h2>首页</h2>
        　　 　　<h2>学生信息</h2>
        　　 　　<h3>{{ class_id }}班</h3>
        　　 {% endblock%}
            5）也可以写好多盒子，
　　              在left中写个盒子
　　　　            {% block menu %}
　　　　　　              <p>I see you you</p>
　　　　            {% endblock %}

            注意：
　　            盒子里面可以有默认的内容，如果有默认的时候你不扩展就走默认的，如果你扩展了，就替换了，
               那么不替换直接追加可以嘛？可以的，那就用下面的方式。
               {% block.super %}

                例如：
                    {% block menu %}

                    　　{{ block.super }}

                    　　<p>！！！</p>       #先继承父类的，后插入数据

                    {% endblock %}


总结：

1、模板继承围绕两点：继承和扩展
　　　　　　　　　　你有什么继承什么，
　　　　　　　　　　扩展的是盒子，
2、模板中设置的盒子越多越好，因为这样你想扩展的时候就容易了。我想扩展就扩展了。不扩展就不扩展了
3、为了更好的可读性，你也可以给你的 {% endblock %} 标签一个 名字 。例如：

{% block content %}
...
{% endblock content %}
4、如果你发现你自己在大量的模版中复制内容，那可能意味着你应该把内容移动到父模版中的一个 {% block %} 中。

最后，请注意你并不能在一个模版中定义多个相同名字的 block 标签。这个限制的存在是因为block标签的作用是“双向”的。
这个意思是，block标签不仅提供了一个坑去填，它还在 _父模版_中定义了填坑的内容。如果在一个模版中有两个名字一样的
block 标签，模版的父模版将不知道使用哪个block的内容。



具体例子说明

urls.py

urlpatterns = [
               url(r'^admin/', admin.site.urls),
               url(r'^text/(\d+)', views.text),
               ]
views.py


from django.shortcuts import render,redirect

# Create your views here.

def text(request,class_id):
    # 班级变量
    print(class_id)  #拿到的是你在路径里输入的几就是几
    # 数据库查询
        return render(request, "text.html", {"class_id": class_id})



templaite / base.html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width">
    <link rel="stylesheet" href="/static/bootstrap-3.3.7-dist/css/bootstrap.min.css">
    <title>Title</title>
    <style>
        .right {
            height: 400px;
            background-color: silver;
    }
    </style>
</head>
<body>
{#导航条#}
<nav class="navbar navbar-primary navbar-inverse">
    <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">Brand</a>
        </div>
        
        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
                <li><a href="#">Link</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                        aria-expanded="false">Dropdown <span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="#">Action</a></li>
                        <li><a href="#">Another action</a></li>
                        <li><a href="#">Something else here</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">Separated link</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">One more separated link</a></li>
                    </ul>
            </li>
    </ul>
        </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
</nav>
{#内容#}
<div class="containers">
    <div class="row">
        <div class="col-md-11 col-lg-offset-1">
            {#            左侧#}
            <div class="left col-md-3">
                {% block menu %}
                    <div class="list-group">
                        <a href="#" class="list-group-item active">
                            学生班级
                        </a>
                        <a href="/text/6" class="list-group-item">s6</a>
                        <a href="/text/7" class="list-group-item">s7</a>
                        <a href="/text/8" class="list-group-item">s8</a>
                        <a href="/text/9" class="list-group-item">s9</a>
                    </div>
                {% endblock %}
            </div>
            {#            右侧#}
            <div class="right col-md-8">
                {#                定义一个盒子#}
                {% block classinfo %}
                
                {% endblock %}
            </div>
    </div>
    </div>
</div>
{#底部#}

</body>
</html>



template /text.py   继承上面的文件


{% extends "base.html" %}


{% block classinfo %}
    <h1>学生信息</h1>
    <h3>{{ class_id }}班级</h3>
{% endblock %}


{#追加#}
{% block menu %}
    {{ block.super }}
    <a href="">学生信息</a>
{% endblock %}


