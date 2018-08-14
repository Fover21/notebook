#udp聊天交互
#****server端
import socket
sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8050))
while 1:
    msg, addr = sk.recvfrom(1024)
    
    print(msg.decode('utf-8'))
    
    msg_f = input('>>>')
    
    sk.sendto(msg_f.encode('utf-8'), addr)
sk.close()

#****client端

import socket
sk = socket.socket(type = socket.SOCK_DGRAM)
while 1:
    msg = input('>>>')
    sk.sendto(msg.encode('utf-8'),('127.0.0.1', 8050))
    smsg , addr = sk.recvfrom(1024)
    print(smsg.decode('utf-8'))
sk.close()
