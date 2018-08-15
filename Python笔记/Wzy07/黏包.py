********黏包********

****黏包现象****

基于tcp先制作一个远程执行命令的程序（命令 ls -l ; |||; pwd）

res=subprocess.Popen(cmd.decode('utf-8'),
shell=True,
stderr=subprocess.PIPE,
stdout=subprocess.PIPE)

的结果的编码是以当前所在的系统为准的，如果是windows，那么res.stdout.read()读出
的就是GBK编码的，在接收端需要用GBK解码。
且只能从管道里读一次结果

r = subprocess.Popen('ls',
shell=True,
stdout=subprocess.PIPE,
stderr=subprocess.PIPE)
# subprocess.Popen(cmd,shell=True,subprocess.stdout,subprocess.stderr)
# cmd : 代表系统命令
# shell = True   代表这条命令是 系统命令,告诉操作系统,将cmd当成系统命令去执行
# stdout   是执行完系统命令之后,用于保存结果的一个管道
# stderr   是执行完系统命令之后,用于保存错误结果的一个管道
print(r.stdout.read().decode('gbk'))
print(r.stderr.read().decode('gbk'))
#因为只能从管道中读一次结果，如果我我们想多次使用，可以拿一个变量接收一下。

what？    黏包

同时执行多条命令之后，得到的结果很可能只有一部分，在执行其他命令的时候又接收到
之前执行的另一部分结果，这种现象就是黏包。

**基于tcp协议实现的黏包

#server端
import socket
import subprocess
ip_port = ('127.0.0.1', 8080)
BUFSIZE = 1024
tcp_socket_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
tcp_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_socket_server.bind(ip_port)
tcp_socket_server.listen(4)
while 1:
    conn, addr = tcp_socket_server.accept()
    print('客户端', addr)
    while 1:
        cmd = conn.recv(BUFSIZE)
        res = subprocess.Popen(cmd.decode('utf-8'),shell=True,
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE)
        stdeer = res.stderr.read()
        stdout = res.stdout.read()
        conn.send(stdeer)
        conn.send(stdout)


#client端
import socket
BUFSIZZE = 1024
ip_port = ('127.0.0.1', 8080)
s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
res = s.connect_ex(ip_port)
while 1:
    msg = input('>>>:').strip()
    if len(msg)==0:continue
    if msg =='q':break
    s.send(msg.encode('utf-8'))
    act_res = s.recv(BUFSIZZE)

    print(act_res.decode('utf-8'))


**基于udp协议实现以上代码---（发现：只有TCP有黏包现象，UDP永远不会黏包）

#server端
import socket
import subprocess
ip_port = ('127.0.0.1', 8080)
BUFSIZE = 1024
udp_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udp_server.bind(ip_port)
while 1:
    cmd, addr = udp_server.recvfrom(BUFSIZE)
    print('命令--->', cmd)
    res = subprocess.Popen(cmd.decode('utf-8'),
                           shell=True,
                           stderr=subprocess.PIPE,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE)
    stdeer = res.stderr.read()
    stdout = res.stdout.read()
    udp_server.sendto(stdeer, addr)
    udp_server.sendto(stdout, addr)
udp_server.close()

#client端
import socket
ip_port = ('127.0.0.1', 8080)
BUFSIZE = 1024
udp_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
while 1:
    msg = input(">>>>").strip()
    udp_client.sendto(msg.encode('utf-8'), ip_port)
    err, addr = udp_client.recvfrom(BUFSIZE)
    out, addr = udp_client.recvfrom(BUFSIZE)
    if err:
        print('error: %s ' % (err.decode('utf-8')), end='')

    if out:
        print(out.decode('utf-8'), end='')

**************只有TCP有黏包现象，UDP永远不会黏包


why?   黏包

****TCP协议中的数据传输

**tcp协议中拆包机制
当发送端缓冲区的长度大于网卡的MTU时间，tcp会将这次发送的数据拆成几个数据包发送出去。
MTU是Maximum Transmission Unit的缩写，意识是网络上传送的最大数据包。
MTU的单位是字节。大部分网络设备的MTU都是1500.如果本机的MTU不网关的MTU大，
大的数据包就会被拆开来传送，这样会产生很多数据包碎片，增加丢包率，降低网络速度。

**面向流的通信特点和Nagle算法
TCP（transport control protocol，传输控制协议）是面向连接的，面向流的，提供高可靠性服务。
收发两端（客户端和服务器端）都要有一一成对的socket，因此，发送端为了将多个发往接收端的包，
更有效的发到对方，使用了优化方法（Nagle算法），将多次间隔较小且数据量小的数据，合并成一个大
的数据块，然后进行封包。这样，接收端，就难于分辨出来了，必须提供科学的拆包机制。 即面向流的通
信是无消息保护边界的。 对于空消息：tcp是基于数据流的，于是收发的消息不能为空，这就需要在客户
端和服务端都添加空消息的处理机制，防止程序卡住，而udp是基于数据报的，即便是你输入的是空内容（直接回车），
也可以被发送，udp协议会帮你封装上消息头发送过去。 可靠黏包的tcp协议：tcp的协议数据不会丢，没有收完包，
下次接收，会继续上次继续接收，己端总是在收到ack时才会清除缓冲区内容。数据是可靠的，但是会粘包

**基于tcp协议特点的黏包现象成因
1.发送端可以是一K一K地发送数据，而接收端的应用程序可以两K两K地提走数据，
当然也有可能一次提走3K或6K数据，或者一次只提走几个字节的数据。也就是说，
应用程序所看到的数据是一个整体，或说是一个流（stream），一条消息有多少
字节对应用程序是不可见的，因此TCP协议是面向流的协议，这也是容易出现粘包问题的原因。
2.而UDP是面向消息的协议，每个UDP段都是一条消息，应用程序必须以消息为单位提取数据，
不能一次提取任意字节的数据，这一点和TCP是很不同的。
3.怎样定义消息呢？可以认为对方一次性write/send的数据为一个消息，需要明白的是当对
方send一条信息的时候，无论底层怎样分段分片，TCP协议层会把构成整条消息的数据段排序
完成后才呈现在内核缓冲区。

例如基于tcp的套接字客户端往服务端上传文件，发送时文件内容是按照一段一段的字节流发送的，
在接收方看了，根本不知道该文件的字节流从何处开始，在何处结束此外，发送方引起的粘包是由
TCP协议本身造成的，TCP为提高传输效率，发送方往往要收集到足够多的数据后才发送一个TCP段。
若连续几次需要send的数据都很少，通常TCP会根据优化算法把这些数据合成一个TCP段后一次发送
出去，这样接收方就收到了粘包数据。

****UDP不会发生黏包

**UDP（user datagram protocol，用户数据报协议）是无连接的，面向消息的，提供高效率服务。 
不会使用块的合并优化算法，, 由于UDP支持的是一对多的模式，所以接收端的skbuff(套接字缓冲区）
采用了链式结构来记录每一个到达的UDP包，在每个UDP包中就有了消息头（消息来源地址，端口等信息），
这样，对于接收端来说，就容易进行区分处理了。 即面向消息的通信是有消息保护边界的。 
**对于空消息：tcp是基于数据流的，于是收发的消息不能为空，这就需要在客户端和服务端都添加空消息的
处理机制，防止程序卡住，而udp是基于数据报的，即便是你输入的是空内容（直接回车），也可以被发送，
udp协议会帮你封装上消息头发送过去。 
**不可靠不黏包的udp协议：udp的recvfrom是阻塞的，一个recvfrom(x)必须对唯一一个sendinto(y),
收完了x个字节的数据就算完成,若是y;x数据就丢失，这意味着udp根本不会粘包，但是会丢数据，不可靠。


补充：

**用UDP协议发送时，用sendto函数最大能发送数据的长度为：65535- IP头(20) – UDP头(8)＝65507字节。
用sendto函数发送数据时，如果发送数据长度大于该值，则函数会返回错误。（丢弃这个包，不进行发送） 

**用TCP协议发送时，由于TCP是数据流协议，因此不存在包大小的限制（暂不考虑缓冲区的大小），这是指在
用send函数时，数据长度参数不受限制。而实际上，所指定的这段数据并不一定会一次性发送出去，如果这
段数据比较长，会被分段发送，如果比较短，可能会等待和下一次数据一起发送


******会发生黏包的两种情况******

****情况一 发送方的缓冲机制
发送端需要等缓冲区满才发送出去，造成黏包（）发送数据时间间隔很短，数据很小，会合到一起，产生黏包

例子：

#server端
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8888))
sk.listen()
conn, addr = sk.accept()
conn.send(b'hello')
conn.send(b'world')
conn.close()
sk.close()

#client端
import socket
sk = socket.socket()
sk.connect_ex(('127.0.0.1', 8888))
msg1 = sk.recv(1024)
print('msg1:', msg1)
msg2 = sk.recv(1024)
print('msg2:', msg2)
sk.close()


****情况二 接收方的缓冲机制
接收方不及时接收缓冲区的包，造成多个包接收（客户端发送了一段数据，服务端只收了一小部分，服务
端下次再收的时候还是从缓冲区拿上次遗留的数据，产生黏包）

例子：
#server端
import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 8888))
sk.listen()
conn, addr = sk.accept()
data1 = conn.recv(2)
data2 = conn.recv(10)
print(data1)
print(data2)
conn.close()
sk.close()

#client端
import socket

sk = socket.socket()
sk.connect_ex(('127.0.0.1', 8888))
sk.send('hello word'.encode('utf-8'))
sk.close()

总结：
黏包现象只发生在tcp协议中：
1.从表面上看，黏包问题主要是因为发送方和接收方的缓存机制、tcp协议面向流通信的特点
2.实际上，主要还是因为接收方不知道消息之间的界限，不知道一次性提取多少字节的数据所造成的。


********黏包解决方案*******





