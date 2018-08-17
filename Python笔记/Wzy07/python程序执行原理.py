
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

opcode    oparg    opcode    opcode    oparg    …
1 byte    2 bytes    1 byte    1 byte    2 bytes
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

