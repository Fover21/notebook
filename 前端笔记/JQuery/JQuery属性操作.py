********JQuery属性相关的操作********

1、属性
    属性（如果你的选择器选出了多个对象，那么默认只会返回出第一个属性）、

        attr(属性名|属性值)
            - 一个参数是获取属性的值，两个参数是设置属性值
            - 点击加载图片示例
        removeAttr(属性名)
            -删除属性的值
        prop(属性名|属性值)
            - 属性的返回值的是布尔类型
            - 单选，反选，取消的例子
        removeProp(属性名)
            -删除属性的值

    循环：each（两种循环示例）
        - $.each(数组/对象, function(i, v){})
      - $("div").each(function(){})
    CSS类
        - addClass 添加类属性
        - removeClass 移除类属性
        - toggleClass 开关|切换（有就移除，没有就添加）
          灯泡的例子
    HTML代码/文本/值
        没有参数就是获取对应的值，
        有参数就设置对应的值
        - .html()  添加html标签    .html("<span>啦啦啦。</span>")
        - .text()  添加文本        .text("啦啦啦。")
        - .val()
            input :一个参数,获取的是input框里面的值
            checkbox :一个参数，获取的是value的值
            select :
                单选：获取值
                多选：得到的是一个数组，设置的时候也要是数组

2、jquery中的循环的两种方式

//    方式一
    li = [11,22,33];
    $.each(li,function (i,v) {
        console.log(i,v)// 0 11
                         // 1 22
                         // 2 33
    })
//    方式二
    $(".c1").each(function (i,v) {
        console.log(i,v)  //这里的v拿到的是标签
//         0 <div class="c1">hah</div>
//         1 <div class="c1">年</div>
//         2 <div class="c1">娃的</div>
        console.log(v.innerText)  //拿到文本
    })

