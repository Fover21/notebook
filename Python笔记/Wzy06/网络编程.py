******socket概念******

图


****理解socket

Socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口。
在设计模式中，Socket其实就是一个门面模式，它把复杂的TCP/IP协议
族隐藏在Socket接口后面，对用户来说，一组简单的接口就是全部，让
Socket去组织数据，以符合指定的协议。

其实站在你的角度上看，socket就是一个模块。我们通过调用模块中已经
实现的方法建立两个进程之间的连接和通信。也有人将socket说成ip+port，
因为ip是用来标识互联网中的一台主机的位置，而port是用来标识这台机器
上的一个应用程序。所以我们只要确立了ip和port就能找到一个应用程序，
并且使用socket模块来与之通信。


******套接字（socket）的发展史

套接字起源于 20 世纪 70 年代加利福尼亚大学伯克利分校版本的 Unix,即人们所说的 BSD Unix。 
因此,有时人们也把套接字称为“伯克利套接字”或“BSD 套接字”。一开始,套接字被设计用在同 一台
主机上多个应用程序之间的通讯。这也被称进程间通讯,或 IPC。套接字有两种（或者称为有两个种族）
分别是基于文件型的和基于网络型的。 

**基于文件类型的套接字家族

套接字家族的名字：AF_UNIX

unix一切皆文件，基于文件的套接字调用的就是底层的文件系统来取数据，两个套接字进程运行在同
一机器，可以通过访问同一个文件系统间接完成通信

**基于网络类型的套接字家族

套接字家族的名字：AF_INET

(还有AF_INET6被用于ipv6，还有一些其他的地址家族，不过，他们要么是只用于某个平台，要么就
是已经被废弃，或者是很少被使用，或者是根本没有实现，所有地址家族中，AF_INET是使用最广泛的
一个，python支持很多种地址家族，但是由于我们只关心网络编程，所以大部分时候我么只使用AF_INET)

*******tcp协议和udp协议********

TCP（Transmission Control Protocol）可靠的、面向连接的协议（eg:打电话）、
传输效率低全双工通信（发送缓存&接收缓存）、面向字节流。使用TCP的应用：Web浏
览器；电子邮件、文件传输程序。

UDP（User Datagram Protocol）不可靠的、无连接的服务，传输效率高（发送前时延小）
，一对一、一对多、多对一、多对多、面向报文，尽最大努力服务，无拥塞控制。使用UDP的
应用：域名系统 (DNS)；视频流；IP语音(VoIP)。

图


******套接字（socket）初使用******

*****基于TCP协议的socket
tcp是基于链接的，必须先启动服务端，然后再启动客户端去链接服务端

**server端

import socket
sk = socket.socket()#创建服务的套接字
sk.bind(('127.0.0.1', 8080))#把地址绑定到套接字
sk.listen()#监听链接
conn, addr = sk.accept()#接收客户端链接
ret = conn.recv(1024)#接收客户端信息
print(ret)#打印客户端信息
conn.send(b'helli')#向客户端发送信息
conn.close()
sk.close()

**client端

import socket
sk = socket.socket()#创建客户端套接字
sk.connect(('127.0.0.1', 8080))#尝试链接服务器
sk.send(b'hi')
ret = sk.recv(1024)#对话（发送/接收）
print(ret)
sk.close()


*****基于UDP协议的socket
udp是无链接的，启动服务之后可以直接接受消息，不需要提前建立链接

**server端

import socket
udp_sk = socket.socket(type=socket.SOCK_DGRAM)   #创建一个服务器的套接字
udp_sk.bind(('127.0.0.1',8080))        #绑定服务器套接字
msg,addr = udp_sk.recvfrom(1024)
print(msg)
udp_sk.sendto(b'hi',addr)                 # 对话(接收与发送)
udp_sk.close()                         # 关闭服务器套接字

**client端

import socket
ip_port=('127.0.0.1',8080)
udp_sk=socket.socket(type=socket.SOCK_DGRAM)
udp_sk.sendto(b'hello',ip_port)
back_msg,addr=udp_sk.recvfrom(1024)
print(back_msg.decode('utf-8'),addr)


******socket参数的详解******

socket.socket(family=AF_INET,type=SOCK_STREAM,proto=0,fileno=None)

创建socket对象的参数说明：
family			地址系列应为AF_INET(默认值),AF_INET6,AF_UNIX,AF_CAN或AF_RDS。
				（AF_UNIX 域实际上是使用本地 socket 文件来通信）
type			套接字类型应为SOCK_STREAM(默认值),SOCK_DGRAM,SOCK_RAW或其他SOCK_常量之一。
SOCK_STREAM 	是基于TCP的，有保障的（即能保证数据正确传送到对方）面向连接的SOCKET，多用于资料传送。 
SOCK_DGRAM 		是基于UDP的，无保障的面向消息的socket，多用于在网络上发广播信息。
proto			协议号通常为零,可以省略,或者在地址族为AF_CAN的情况下,协议应为CAN_RAW或CAN_BCM之一。
fileno			如果指定了fileno,则其他参数将被忽略,导致带有指定文件描述符的套接字返回。
				与socket.fromfd()不同,fileno将返回相同的套接字,而不是重复的。
				这可能有助于使用socket.close()关闭一个独立的插座。


































