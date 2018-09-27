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
