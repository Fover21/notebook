。
操作系统

Json vs pickle
JSON（转为字符串类型）
优点：跨语言。体积小
缺点：只能支持 int\str\list\tuple\dict
Pickle（转为bytes类型）
优点：专为python设计，支持python所有数据类型
缺点：只能在python中使用，存储数据占空间大

架构：
      C/S架构：充分发挥PC机的性能
      B/S架构：统一了应用接口，隶属于C/S架构
    物理地址：mac，全球唯一，类似于一个身份证
    ip地址：四位点分十进制
    （要求：二进制，十六进制，十进制）
    arp协议：通过目标ip地址，获取目标mac地址
    OSI五层模型：
       应用层          http协议，ftp协议，https协议，py文件
       传输层          tcp/udp协议
       网络层          ip协议
       数据链路层      arp协议
       物理层          传输电信号
     交换机的通信方式：
       单播：点对点
       组播：点对多（一组，不是指所有）
       广播：向多个pc端发送数据包（吼一嗓子）
     交换机的功能：
       组成局域网，经过内部处理解析数据，将数据以点对点，点对多的方式发送给目标
     路由器的功能：
       跨网段的数据传输，路由出网络传输的最佳路径


     TCP协议：面向连接的，面向字节流传输，可靠，
     UDP协议：无连接，面向数据包，不可靠，快
     TCP协议和UDP协议的区别：
        TCP有三次握手，四次挥手
           三次握手：第一次的请求一定是客户端先发起
             客户端向服务器发送一个连接请求
             服务器回复一个确认接收到请求，并要求连接客户端
             客户端回复服务器一个确认连接的消息
           四次挥手：谁先发起都可以
             客户端先发送一个断开连接的请求
             服务器回复一个确认收到
             服务器回复一个确认断开连接的请求
             客户端回复一个确认收到
        TCP可能会出现粘包情况
          粘包：在数据传输过程中，接收端接收数据时，不知道应该如何接收数据，造成的一个数据混乱的现象
          粘包的原因:
            一个是拆包机制
            一个是合包机制（Nagle算法）
            两个机制都是发生在发送端
        TCP本质上就是只允许在同一时间，一个服务器和一个客户端保持连接
        UDP允许一个服务器和多个客户端同时通信

    新模块：
        socket模块 ：套接字，网络传输数据，处于应用层和传输层之间的一个抽象层
        subprocess模块 ：Popen方法：执行操作系统命令的
        struct模块：pack和unpack方法 

总结：
     以下最重要，需要背过
     1 操作系统的目标：
         有效性：提高系统资源利用率。
         方便性：更加方便用户的使用。
         高内聚：内聚指模块内部各部分之间的紧密程度。
         低耦合：耦合指模块与模块之间的依赖程度。
      2 操作系统的作用
	1.封装所有硬件接口，让各种用户使用电脑更加方便
	2.是对计算机内所有资源进行合理的调度和分配

      3 计算机的五大硬件组成
	cpu，主板，存储，输入输出设备       控制器，运算器，存储器，输入设备，输出设备

      4 编程语言发展史
	机器语言，汇编语言（指令、命令形式的！），高级语言
      5 进程的概念
	是指在执行的程序
	是程序执行过程中的一次 指令，数据集等的集合
	也可以叫做程序的一次执行过程
	进程是一个动态过程
	 
	进程三大组成部分：代码段，数据段,PCB(进程管理控制 )

      6 进程的三大基本状态
	就绪状态：已经获得运行需要的所有资源，除CPU
	执行状态：已经获得了所有的资源包括CPU，处在正在运行
	阻塞状态：因为各种原因，进程放弃了CPU，导致进程无法继续执行，此时进程处于内存中，继续等待获取CPU进程的一个特殊状态
	挂起状态：是指因为各种原因，进程放弃了CPU，导致进程无法继续执行，此时进程被踢出内存。
	
	问题：用户写一个程序，如何让cpu帮你执行，中间经过了哪些步骤？
	
    进程由三部分组成：
        代码段，数据段，PCB（进程控制块）


2 进程的两种开启方法
      (1) p = Process(target=None,args(,))
      (2) 自定义类，继承Process父类

    3 进程的常用方法
      （1） start()  开启一个子进程
      （2） join()   异步变同步（就是让父进程停留在join这句话，等待子进程执行结束，父进程再继续执行）
      （3） is_alive() 判断进程是否活着
      （4） terminate()   杀死进程
    4 进程的常用属性
       （1） p.name =    给p进程一个名字
       （2） p.pid       返回p进程的pid
       （3） p.daemon = True   将p进程设置为守护进程。（True为守护进程，False为普通进程）
           守护进程的两个特点：
              守护进程会随着父进程的代码执行结束而结束
              守护进程不能再创建子进程（不能要孩子）
		必须在start之前



    dos系统：      单用户单任务
    windows系统：  单用户多任务（早期的windows）
    unix系统：     多用户多任务

       什么是并行和并发？
		并行：两件或多件事情在同一时间点同时执行     两者同时执行（多个cpu）
		并发：两件或多件事情在同一时间间隔内同时执行  在资源有限的情况下，两者交替轮流使用
       什么是阻塞和非阻塞？
		阻塞：等
		非阻塞：不等
       什么是同步和异步？
		同步：不管在那条路上始终只有一辆车开       按顺序执行  从头开到尾
		异步：同一时间不同的路上两辆车在同时开
       multiprocessing包，Process模块，自己创建一个子进程让其工作

from multiprocessing import Process

import time


def fuc(arg1, arg2):
    print('$' * arg1)
    time.sleep(3)
    print('$' * arg2)


P = Process(target=fuc, args=(10, 20))
P.start()
print('完')







    并行 ： 两个进程在同一时间点发生
    并发 ： 两个进程在同一时间间隔内运行
    同步 ： 某一个任务的执行必须依赖于另一个任务的返回结果
    异步 ： 某一个任务的执行，不需要依赖于另一个任务的返回，只需要告诉另一个任务一声
    阻塞 ： 程序因为类似于IO等待、等待事件等导致无法继续执行。
    非阻塞：程序遇到类似于IO操作时，不再阻塞等待，如果没有及时的处理IO，就报错或者跳过等其他操作

进程的方法和属性：
    方法：start（）  开启一个子进程
          join       异步变同步，让父进程等待子进程的执行结束，再继续执行
          is_alive， 判断进程是否活着
          terminate  杀死进程
    属性：
          name   子进程的名字
          pid    子进程的pid
          daemon  设置进程为守护进程，给一个True代表为守护进程，默认为False，不是守护进程
守护进程
    特点：
        随着父进程的代码执行完毕才结束
        守护进程不能创建子进程
        守护进程必须要在start之前设置


IPC -- inter process Communication  进程间通信
今天内容：
    学习锁机制
        l = Lock()
        一把锁配一把钥匙
        拿钥匙，锁门  l.acquire()
        还钥匙，开门  l.release()
    学习信号机制
        sem = Semaphore(n)
        n : 是指初始化一把锁配几把钥匙，一个int型
        拿钥匙，锁门  l.acquire()
        还钥匙，开门  l.release()
        信号量机制比锁机制多了一个计数器，这个计数器是用来记录当前剩余几把钥匙的。
        当计数器为0时，表示没有钥匙了，此时acquire()处于阻塞。
        对于计数器来说，每acquire一次，计数器内部就减1，release一次，计数器就加1

    学习事件机制
        e = Event()
        # e.set()    #将is_set()设为True
        # e.clear()  # 将is_set()设为False
        # e.wait()   #判断is_set的bool值，如果bool为True，则非阻塞，bool值为False，则阻塞
        # e.is_set() # 标识
        # 事件是通过is_set()的bool值，去标识e.wait() 的阻塞状态
        # 当is_set()的bool值为False时，e.wait()是阻塞状态
        # 当is_set()的bool值为True时，e.wait()是非阻塞状态
        # 当使用set()时，是把is_set的bool变为True
        # 当使用clear()时，是把is_set的bool变为False

    学习生产者消费者模型
        主要用于解耦（耦合度）





课程回顾：
    并发：在同一个时间段内多个任务同时进行
    并行：在同一个事件点上多个任务同时进行
    进程的三大基本状态：
      就绪状态：所有进程需要的资源都获取到了，除了CPU
      执行状态：获取到了所有资源包括CPU，进程处于运行状态
      阻塞状态：进程停滞不再运行，放弃了CPU，进程此时处于内存里
    什么叫进程？
      正在运行的程序。
      由代码段，数据段，PCB（进程控制块）
    进程是资源分配的基本单位。

    进程之间能不能直接通信？
        正常情况下，多进程之间是无法直接进行通信的。因为每个进程都有自己独立的内存空间。


    锁。为了多进程通信时，保护数据的安全性
       一把锁配一把钥匙
       l = Lock（）
       l.acquire()
       l.release()
    信号量。
       一把锁配多把钥匙
       sem = Semaphore（num）
       num代表的是几把钥匙
    事件。
       e = Event()
       e.is_set()返回一个bool值
       e.wait()  阻塞和非阻塞
       e.set()   把is_set的bool值变为True
       e.clear() 把is_set的bool值变为False


今日内容：

生产者 消费者模型


from multiprocessing import Process, JoinableQueue


def consumer(q, name):
	while 1:
		info = q.get()
		print('%s吃了'%name + info)
		q.task_done()

def producer(q, name):
	for I in range(10):
		info = ‘%s生产了%s号包子’ % (name, i)
		q.put(info)
	q.join()

Q = JoinableQueue()
Pro = Process(target = producer, arget = (q, 'Tom')).start()
Con0 = consumer(target = consumer, arget = (q, 'Jake')).start()
Con1 = consumer(target = consumer, arget = (q, 'Jason')).start()
Con0.daemon = True
Con1,daemon = True  #有几个消费者就有几个守护进程
Pro.join()



    1 生产者消费者模型
       主要是为解耦
       借助队列来实现生产者消费者模型

       栈：先进后出（First In Last Out       简称 FILO）
       队列： 先进先出（First In First Out   简称 FIFO）


    import queue  # 不能进行多进程之间的数据传输
    （1）from multiprocessing import Queue   借助Queue解决生产者消费者模型
       队列是安全的。
       q = Queue(num)
       num ： 队列的最大长度
       q.get()# 阻塞等待获取数据，如果有数据直接获取，如果没有数据，阻塞等待
       q.put()# 阻塞，如果可以继续往队列中放数据，就直接放，不能放就阻塞等待

       q.get_nowait()# 不阻塞，如果有数据直接获取，没有数据就报错
       q.put_nowait()# 不阻塞，如果可以继续往队列中放数据，就直接放，不能放就报错

    （2）from multiprocessing import JoinableQueue#可连接的队列
       JoinableQueue是继承Queue，所以可以使用Queue中的方法
       并且JoinableQueue又多了两个方法
       q.join()# 用于生产者。等待 q.task_done的返回结果，通过返回结果，生产者就能获得消费者当前消费了多少个数据
       q.task_done() # 用于消费者，是指每消费队列中一个数据，就给join返回一个标识。

     2 管道(了解)
         from multiprocessing import Pipe
         con1,con2 = Pipe()
         管道是不安全的。
         管道是用于多进程之间通信的一种方式。
         如果在单进程中使用管道，那么就是con1收数据，就是con2发数据。
                                 如果是con1发数据，就是con2收数据

         如果在多进程中使用管道，那么就必须是父进程使用con1收，子进程就必须使用con2发
                                             父进程使用con1发，子进程就必须使用con2收
                                             父进程使用con2收，子进程就必须使用con1发
                                             父进程使用con2发，子进程就必须使用con1收
         在管道中有一个著名的错误叫做EOFError。是指，父进程中如果关闭了发送端，子进程还继续接收数据，那么就会引发EOFError。

     3 进程之间的共享内存
       from multiprocessing import Manager,Value
       m = Manager()
       num = m.dict({键 : 值})
       num = m.list([1,2,3])

     4 进程池
       进程池：一个池子，里边有固定数量的进程。这些进程一直处于待命状态，一旦有任务来，马上就有进程去处理。
       因为在实际业务中，任务量是有多有少的，如果任务量特别的多，不可能要开对应那么多的进程数
       开启那么多进程首先就需要消耗大量的时间让操作系统来为你管理它。其次还需要消耗大量时间让
       cpu帮你调度它。
       进程池还会帮程序员去管理池中的进程。
       from multiprocessing import Pool
       p = Pool(os.cpu_count() + 1)

       进程池有三个方法：
         map(func,iterable)
         func：进程池中的进程执行的任务函数
         iterable: 可迭代对象，是把可迭代对象中的每个元素依次传给任务函数当参数

         apply(func,args=())： 同步的效率，也就是说池中的进程一个一个的去执行任务
         func：进程池中的进程执行的任务函数
         args: 可迭代对象型的参数，是传给任务函数的参数
         同步处理任务时，不需要close和join
         同步处理任务时，进程池中的所有进程是普通进程（主进程需要等待其执行结束）

         apply_async(func,args=(),callback=None)： 异步的效率，也就是说池中的进程一次性都去执行任务
         func：进程池中的进程执行的任务函数
         args: 可迭代对象型的参数，是传给任务函数的参数
         callback: 回调函数，就是说每当进程池中有进程处理完任务了，返回的结果可以交给回调函数，由回调函数进行进一步的处理,回调函数只有异步才有，同步是没有的
         异步处理任务时，进程池中的所有进程是守护进程（主进程代码执行完毕守护进程就结束）
         异步处理任务时，必须要加上close和join

         回调函数的使用：
             进程的任务函数的返回值，被当成回调函数的形参接收到，以此进行进一步的处理操作
             回调函数是由主进程调用的，而不是子进程，子进程只负责把结果传递给回调函数


作业：
    0 整理博客
    1 必须会一个生产者消费者模型的编码
    2 使用Manager实现一下银行的存取款问题
    3 使用进程池去实现一下socket的tcp协议编码。允许一个服务器同时接受多个客户端的请求，
      客户端连接成功后，客户端发送一个数据，服务器把该数据转成大写发送回去就行。










总结|：
    你知道的IPC都有哪些？
       管道，队列，（锁，信号量，事件）





Python程序的执行原理

1. 过程概述
Python先把代码（.py文件）编译成字节码，交给字节码虚拟机，然后解释器一条一条执行字节码指令，从而完成程序的执行。

1.1python先把代码(.py文件)编译成字节码，交给字节码虚拟机，然后解释器会从编译得到的PyCodeObject对象中一条一条执行字节码指令，
并在当前的上下文环境中执行这条字节码指令，从而完成程序的执行。Python解释器实际上是在模拟操作中执行文件的过程。PyCodeObject对象
中包含了字节码指令以及程序的所有静态信息，但没有包含程序运行时的动态信息——执行环境（PyFrameObject)

2. 字节码
字节码在python解释器程序里对应的是PyCodeObject对象
.pyc文件是字节码在磁盘上的表现形式

2.1从整体上看：OS中执行程序离不开两个概念：进程和线程。python中模拟了这两个概念，模拟进程和线程的分别是PyInterpreterState和
PyTreadState。即：每个PyThreadState都对应着一个帧栈，python解释器在多个线程上切换。当python解释器开始执行时，它会先进行一
些初始化操作，最后进入PyEval_EvalFramEx函数，它的作用是不断读取编译好的字节码，并一条一条执行，类似CPU执行指令的过程。函数内部
主要是一个switch结构，根据字节码的不同执行不同的代码。

3. .pyc文件
PyCodeObject对象的创建时机是模块加载的时候，及import
Python test.py会对test.py进行编译成字节码并解释执行，但是不会生成test.pyc
如果test.py加载了其他模块，如import urlib2, Python会对urlib2.py进行编译成字节码，生成urlib2.pyc,然后对字节码进行解释
如果想生成test.pyc，我们可以使用Python内置模块py_compile来编译。
加载模块时，如果同时存在.py和pyc,Python会尝试使用.pyc，如果.pyc的编译时间早于.py的修改时间，则重新编译.py并更新.pyc。

4. PyCodeObject
Python代码的编译结果就是PyCodeObject对象

typedef struct {
    PyObject_HEAD
    int co_argcount;        /* 位置参数个数 */
    int co_nlocals;         /* 局部变量个数 */
    int co_stacksize;       /* 栈大小 */
    int co_flags;  
    PyObject *co_code;      /* 字节码指令序列 */
    PyObject *co_consts;    /* 所有常量集合 */
    PyObject *co_names;     /* 所有符号名称集合 */
    PyObject *co_varnames;  /* 局部变量名称集合 */
    PyObject *co_freevars;  /* 闭包用的的变量名集合 */
    PyObject *co_cellvars;  /* 内部嵌套函数引用的变量名集合 */
    /* The rest doesn’t count for hash/cmp */
    PyObject *co_filename;  /* 代码所在文件名 */
    PyObject *co_name;      /* 模块名|函数名|类名 */
    int co_firstlineno;     /* 代码块在文件中的起始行号 */
    PyObject *co_lnotab;    /* 字节码指令和行号的对应关系 */
    void *co_zombieframe;   /* for optimization only (see frameobject.c) */
} PyCodeObject;


5. .pyc文件格式
加载模块时，模块对应的PyCodeObject对象被写入.pyc文件

6.分析字节码

6.1解析PyCodeObject
Python提供了内置函数compile可以编译python代码和查看PyCodeObject对象

6.2指令序列co_code的格式

opcode	oparg	opcode	opcode	oparg	…
1 byte	2 bytes	1 byte	1 byte	2 bytes	 
Python内置的dis模块可以解析co_code

7. 执行字节码
Python解释器的原理就是模拟可执行程序再X86机器上的运行，X86的运行时栈帧如下图

https://images2015.cnblogs.com/blog/827237/201703/827237-20170321221026096-252405791.png

Python解释器的原理就是模拟上述行为。当发生函数调用时，创建新的栈帧，对应Python的实现就是PyFrameObject对象。
PyFrameObject对象创建程序运行时的动态信息，即执行环境

7.1 PyFrameObject

typedef struct _frame{  
    PyObject_VAR_HEAD //"运行时栈"的大小是不确定的  
    struct _frame *f_back; //执行环境链上的前一个frame，很多个PyFrameObject连接起来形成执行环境链表  
    PyCodeObject *f_code; //PyCodeObject 对象，这个frame就是这个PyCodeObject对象的上下文环境  
    PyObject *f_builtins; //builtin名字空间  
    PyObject *f_globals;  //global名字空间  
    PyObject *f_locals;   //local名字空间  
    PyObject **f_valuestack; //"运行时栈"的栈底位置  
    PyObject **f_stacktop;   //"运行时栈"的栈顶位置  
    //...  
    int f_lasti;  //上一条字节码指令在f_code中的偏移位置  
    int f_lineno; //当前字节码对应的源代码行  
    //...  
      
    //动态内存，维护(局部变量+cell对象集合+free对象集合+运行时栈)所需要的空间  
    PyObject *f_localsplus[1];    
} PyFrameObject;

每一个 PyFrameObject对象都维护了一个 PyCodeObject对象，这表明每一个 PyFrameObject中的动态内存空间对象都和源代码中的一段Code相对应。


总结：

A. 其实Python是否保存成pyc文件和我们在设计缓存系统时是一样的，我们可以仔细想想，到底什么是值得扔在缓存里的，什么是不值得扔在缓存里的。

=========归根到底还是：pyc文件就是为了，模块的重用========

B. 在跑一个耗时的Python脚本时，我们如何能够稍微压榨一些程序的运行时间，就是将模块从主模块分开。（虽然往往这都不是瓶颈）

C. 在设计一个软件系统时，重用和非重用的东西是不是也应该分开来对待，这是软件设计原则的重要部分。

D. 在设计缓存系统（或者其他系统）时，我们如何来避免程序的过期，其实Python的解释器也为我们提供了一个特别常见而且有效的解决方案。














网络编程+并发编程

架构：B/S 和 C/S
	C/S:充分发挥PC机的性能
	B/S:统一了应用的接口，隶属于CS架构
	
	
OSI模型  七层
我们用五层

应用层	http协议   https协议   ftp协议
传输层	tcp udp 协议	（四层交换机）
网络层	IP协议	路由器（？）	（三次交换机）
数据链路层	arp协议，交换机  （二层交换机）
物理层	网卡，双绞线     （传输电信号）

Arp协议：通过目标ip地址获取目标mac地址
物理地址：mac地址全球唯一，每个电脑的网卡上
Ip地址：四位点分十进制			三十二位点分二进制

交换机的通信方式：
	单播：点对点
	组播：点对多
	广播：向多个pc端发送数据包

交换机和路由器的区别？
交换机是组织局域网的，经过内部处理解析数据，将数据已点对点，点对多的方式发送给目标
路由器是跨网段的数据传输，路由出网络传输的最佳路径



 socket 介于应用层和传输层的socket抽象层

socket类型：
	family = AF_UNIX：基于文件类型的套接字
	family = AF_INET：基于网络类型的套接字
tcp协议：  type = SOCK_STREAM
udp协议： type = SOCK_DGRAM

Tcp：面向连接的，双全工的  面向字节流的，安全可靠，会发生黏包，只可以一个客户端访问。 三次握手，四次挥手 
Udp：无连接的，面向数据报的，不安全，不可靠。可以同时和多个客户端通信

三次握手：（必须是客户点先发起）
1.客户端发起请求链接服务端
2.服务端收到请求，向客户端发送可以连接的请求
3.客服端收到连接，连接成功


四次挥手：（客户端和服务端都可以发起）

1.客户端发起断开连接的请求
2.服务端收到请求，然后准备断开连接的一些事物
3.服务端发送请求，我已经准备完毕，可以断开了
4.客户端收到请求，断开连接。

为什么会发生黏包：因为有缓存机制，连续发或者连续收。（在数据传输过程中，接收数据端接收数据时不知道该如何接收，造成的数据混乱现象）
合包机制：nagle算法 — 发数据的时候一点一点发，但是接收的时候会一次收到。 
拆包机制：发送的数据太大，分开发送，接收的时候，最后不能刚刚接完，就会发生黏包。
都是发生在发送端。 

如何解决黏包？

自定义表头：用struct模块，事先将要发送文件的大小存下来，发送 过去，然后按着指定数据开始接收。
Struct 模块  可以将一个整数，封装为一个指定（一般为4）字节数的数字，这样接收端就可以指定大小接收这个数字。

socketserver   （框架）

import socketserver

class Myserver(socketserver.BaseRequestHandler):
	def handle(self):
		pass

if __name__ == ‘__main__’:
	server = socketserver.ThreadingTCPServer((’127.0.0.1’, 8080), Myserver)
	server.serve_forever()


操作系统

Dos系统			#单用户单任务
Windows系统		#单用户多任务（早起的Windows）
Unix系统			#多用户多任务

操作系统的作用：1）封装接口，让用户方便使用 	2）对系统资源的分配与调度

计算机的五大组成部分：运算器。控制器。存储器。输入设备。输出设备。

编程语言发展史：机器语言，汇编语言，高级语言

并行：（两件事或者多件事）同一时间点，同时执行 （多个CPU）
并发：（两件事或者多件事）同一时间间隔，交替执行
阻塞：程序因为类似IO等待、等待时间等导致无法继续执行
非阻塞：程序遇到类似于IO操作时，不再阻塞等待，如果没有及时的处理IO，就会报错或者跳过等待其他操作，
同步：某一个任务的执行必须依赖另一个任务的返回结果
异步：一个任务的执行，不需要依赖另一个任务的返回，只需要告诉另一个任务一声

进程：cpu资源分配的最小单位    	进程由三部分组成：代码段，数据段，PCB（进程控制块）
线程：cpu资源调度的最小单位		线程由三部分组成：代码段，数据段，TCB（线程控制块）

进程的三大基本状态：
	就绪状态：已经获得运行所需的所有资源，除CPU
	执行状态：已经获得所有资源包括CPU，处于正在运行
	阻塞状态：因为各种原因，进程放弃了CPU，导致进程无法继续执行，此时进程处于内存中，继续等待获取CPU的一种状态。ß

进程学的东西： multiprocessing

1）Process模块
	线程的创建 	
	1）直接创建
	p = Process(target = func, args = (元组形式， 为func所传的参数)) #实例化进程对象	
	2）继承 （Process）

	多线程的开启	1）for循环		2）多个对象实例化
	方法：
		start()		#开启进程
		join()			#感知进程的结束，异步变同步
		is_alive()		#判断进程是否存活
		terminate()	#杀死一个进程
	属性：
		name			#获取进程名
		pid				#获取进程号
		daemon = True 	#守护进程    
		守护进程的特点：
			#当主进程代码结束后，守护进程随主进程结束
			#守护进程不能再创建子进程
			#守护进程必须在start之前			

2）	锁  		Lock模块			(互斥锁/同步锁)
		lock = Lock()	#实例化一个锁对象
		lock.acquire()	#上锁
		lock.release()	#解锁
			RLock模块		（递归锁）
		递归锁可以同时acquire多次，但是必须acquire几次就必须release几次。都在就会陷入死锁状态
			死锁
		典型的例子：科学家吃面    （一个人拿着面，一个人拿着叉子，到最后谁也吃不上面）

	信号量	Semaphore模块
		sem = Semaphore(int数据类型)	#可以指定有多少线程可以同时拿到锁
		sem.acquire()					#需要上锁将这些数据锁住
		sem.release()
	事件		Event模块
		e = Event()
		e.wait()	#根据is_set()的状态来决定，自身的阻塞状态  如果is_set()为False则为阻塞，如果is_set()为True则为非阻塞
		e.is_set()		#默认为False，
		e.set()		#将is_set()的状态变为True
		e.clear()		#将is_set()的状态变为False

	典型例子：红绿灯事件	

3）进程间通信（IPC）
	Queue模块		#队列     先进先出    First in first out
		q = Queue()	#创建队列对象（可以指定大小）
		q.put() 		#向队列中添加元素（如果队列以满处于阻塞状态，只有当队列不满才可以继续添加）
		q.get()		#取出队列中元素（如果队列中元素为空处于阻塞状态，只有对列中有元素才可以继续取出）
		q.full()		#判断一个对列是否 已满
		q.empty()		#判断一个对列是否为空
		q.qsize()		#返回队列大小
		q.put_nowait()	 #不阻塞，如果可以继续往队列中放数据就继续放，不能放就报错
		q.get_nowait()	 #不阻塞，如果有数据就直接获取，没有数据就报错
	JoinableQueue()模块
		q = JoinableQueue()
						#继承了Queue模块，但是新增了两个方法
		q.task_done()   	#统计对列q有多少个元素被拿走（拿走一个数据就给join返回一个结果），通常与q.get()在一起用  用于消费者
		q.join()			#感知一个对列的数据被全部执行完毕  与q.put()在一起用      用于生产者
	
	队列  =  管道  +  锁
		
	重点：生产者消费着模型
		
	Pipe模块			#管道   (本身是不安全的)         （双全工）
		p = Pipe()
		conn1, conn2  = Pipe()
	
		管道是不安全的
		管道是用于多进程之间通信的一种方式
		如果在单进程中使用管道，那么就是conn1收数据，conn2发数据
							如果是conn1发数据,那么conn2收数据
		如果在多进程中使用管道，那么就必须是父进程中用con1收，子进程中使用conn2发
									父进程使用conn1发，子进程中使用conn2收
									父进程使用conn2收,子进程中使用conn1发
									父进程使用conn2发，子进程中使用conn1收
		在管道中有一个著名的错误叫做EOFERrror。
		是指：父进程中如果关闭了发送端，子进程还继续接受数据，那么就会引发EOFError

4)数据共享	Manager模块    Value模块
	men = Manager()
	(1)
	m.list(列表数据)
	m.dict(字典数据)
	(2)
	with Manager() as m:
		……

5)进程池		Pool模块

	p = Pool(os.cup_count() +１)		＃开启多进程之后，每次处理数据只能指定个数个处理
	
	p.close()
	p.join()	#close在join之前

	方法：
		p.map(func, itreable)	#异步处理 itreable ，有返回值，返回值是，每一个func的返回值组成的列表， 自带close和join
		p.apply(func, args)	#同步处理		有返回值，返回值为func的返回值   不需要加close和join
		p.apply_async(func, args, callback)	#异步处理，有返回值，返回一个对象，这个对象有get方法，可以获取func的返回值
									#这个get只能一个一个获取，以我们一般处理完所有线程后再获取数据
									#func的返回值可以作为参数传给callback这个回调函数。回调函数在主进程中执行
		apply函数中的所有进程都为普通进程
		apply_async函数中的所有进程都为守护进程




线程学的东西：threading

GIL：全局解释器锁（只有CPython才有）
	锁的是线程：同一时间只允许一个线程访问CPU      #（没有真正的并行）

1）Thread模块

	线程的创建
	1）t = Thresd(target= func. args = (元组，为func所传的参数))   实例化线程对象
	2）继承
	
	多线程的创建
	1）for 循环
	2）直接实例化多个对象

2）	锁
		Lock		#互斥锁（同步锁）
		RLock 	#递归锁
		死锁		#死锁
	 
	信号量	Semaphore模块
		sem = Semaphore(int数据类型)	#可以指定有多少线程可以同时拿到锁
		sem.acquire()					#需要上锁将这些数据锁住
		sem.release()

	事件		Event模块
		e = Event()
		e.wait()	#根据is_set()的状态来决定，自身的阻塞状态  如果is_set()为False则为阻塞，如果is_set()为True则为非阻塞
		e.is_set()		#默认为False，
		e.set()		#将is_set()的状态变为True
		e.clear()		#将is_set()的状态变为False
3)多线程利器（queue模块）
	import queue
	q = 	queue.Queue()
	q.put() 		#向队列中添加元素（如果队列以满处于阻塞状态，只有当队列不满才可以继续添加）
	q.get()		#取出队列中元素（如果队列中元素为空处于阻塞状态，只有对列中有元素才可以继续取出）
	q.full()		#判断一个对列是否 已满
	q.empty()		#判断一个对列是否为空
	q.qsize()		#返回队列大小
	q.put_nowait()	 #不阻塞，如果可以继续往队列中放数据就继续放，不能放就报错
	q.get_nowait()	 #不阻塞，如果有数据就直接获取，没有数据就报错
	q.task_done()   	#统计对列q有多少个元素被拿走（拿走一个数据就给join返回一个结果），通常与q.get()在一起用  用于生产者
	q.join()			#感知一个对列的数据被全部执行完毕  与q.put()在一起用      用于消费着
	
	LifoQueue  		#栈
	PriorityQueue		#优先队列

	
4）条件	Condition模块
	
		条件是让程序员自行去调度线程的一个机制
		
		方法：
		acquire()
		release()
		wait()   #让线程阻塞住
		notify(int数据类型)	#是指给wait发一个信号，让wait变成不阻塞						#int数据类型，是指你要给多少wai发信号
	

5）定时器		Timer模块

		创建：Timer(time, func)
				#time：睡眠时间，以秒为单位
				#func：睡眠之后，需要执行的任务
		

6）线程池
Concurrent.futures模块提供了高度封装的异步调用接口
ThreadPoolExecutor:线程池，提供异步调用
ProcessPoolExecutor:进程池，提供异步调用


#submit(fn, *args, **kwargs)
异步提交任务

#map(func, *iterables, timeout=None, chunksize=1) 
取代for循环submit的操作

#shutdown(wait=True) 
相当于进程池的pool.close()+pool.join()操作
wait=True，等待池内所有任务执行完毕回收完资源后才继续
wait=False，立即返回，并不会等待池内的任务执行完毕
但不管wait参数为何值，整个程序都会等到所有任务执行完毕
submit和map必须在shutdown之前

#result(timeout=None)
取得结果

#add_done_callback(fn)
回调函数

 线程池中的回调函数是子线程调用的，和父线程没有关系
 进程池中的回调函数是父进程调用的，和子进程没有关系



进程与线程的区别：
	进程资源分配的基本单位，线程是cpu调度的基本单位。
	线程不可以自己独立拥有资源。线程的执行，必须依赖于所属进程中的资源。
	进程中必须至少应该有一个线程。
	线程上下文切换比进程上下文切换要快的多。
	通信
	守护进程和守护线程

线程和进程的比较：
	1）cpu切换进程比切换线程慢很多，在python中如果IO操作过多的话，使用线程最好
	2）在同一个进程内，所有线程共享这个进程pid，也就是说所有线程共享所属进程的所有资源和内存地址
	3）在同一个进程内，所有线程共享该进程中的全局变量
	4）因为GIL锁的存在，在CPython中，没有真正的线程并行。但是有真正的多进程并行
		当你的任务是计算密集的情况下，使用多进程好。
		总结：在CPython中，IO密集用多线程，计算密集用多线程。
	5）关于守护线程和守护进程的事情：（注意：代码执行结束，并不代表程序结束）
		守护进程：要么自己正常结束，要么根据父进程的代码执行结束而结束
		守护线程：要么自己正常结束，要么根据父线程的执行结束而结束（会等其余子线程运行结束）


协程：

为什么要有协程？
	因为想要在单线程内实现并发的效果。
	因为CPthon有GIL锁，限制了在同一个时间点，只能执行一个线程
	所以想要在执行一个线程的期间，充分的利用CPU的性能
	所以才有了想在单线程内实现并发的效果。

        并发：切换+保存状态
        cpu是为什么要切换？
           1 因为某个程序阻塞了
           2 因为某个程序用完了时间片
           很明显  解决1 这个问题才能提高效率
        所以想要实现单线程的并发，就要解决在单线程内，多个任务函数中，某个任务函数遇见IO操作，马上自动切换到其他任务函数去执行。

     协程：是一个比线程更加轻量级的单位，是组成线程的各个函数
       协程本身没有实体
     greenlet模块：能简单的实现函数与函数之间的切换，但是遇到IO操作，不能自动切换到其他函数中
        （1） 注册一下函数func，将函数注册成一个对象f1
              f1 = greenlet(func)
        （2） 调用func，使用f1.switch()，如果func需要传参，就在switch这里传即可

     gevent模块：可以实现在某函数内部遇到IO操作，就自动的切换到其他函数内部去执行
         g = gevent.spawn(func，参数) 注册一下函数func，返回一个对象g
         gevent.join(g) #等待g指向的函数func执行完毕，如果在执行过程中，遇到IO，就切换
         gevent.joinall([g1,g2,g3])#等待g1 g2 g3指向的函数func执行完毕

   大的总结：协程是由用户自己去调度的，
       面试题：
       已经学习过了进程，线程，协程
         计算密集用多进程，可以充分利用多核cpu的性能，
         IO密集用多线程（注意，协程是在单线程的）
       多线程和协程的区别是：
         线程是由操作系统调度，控制
         协程是由程序员自己调度，控制

     IO多路复用
        阻塞IO
        非阻塞IO
        多路复用IO
        异步IO python实现不了，但是有tornado框架，天生自带异步

     面试题：
       select  和    poll    和epoll的区别

      select和poll有一个共同的机制，都是采用轮训的方式去询问内核，有没有数据准备好了
      select有一个最大监听事件的限制，32位机限制1024，,6位机限制2048
      poll没有，理论上poll可以开启无限大，1G内存大概够你开10W个事件去监听

      epoll是最好的，采用的是回调机制，解决了select和poll共同存在的问题
      而且epoll理论上也可以开启无限多个监听事件



并发的本质：切换 + 保存状态



















