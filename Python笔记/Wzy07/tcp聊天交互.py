#tcp聊天交互
#****setver端
import socket
sk = socket.socket()
adress = ('127.0.0.1', 8032)
sk.bind(adress)
sk.listen(4)
while 1:
    conn, addr = sk.accept()
    while 1:
        res_s = conn.recv(1024).decode('utf-8')
        print(res_s)
        if res_s == 'q':
            break
        res_f = input('>>>>>')
        conn.send(res_f.encode('utf-8'))
        if res_f == 'q':
            break
    conn.close()
sk.close()

#****client端

import socket
sk = socket.socket()
adress = ('127.0.0.1', 8032)
sk.connect(adress)
while 1:
    meg = input('>>>')
    sk.send(meg.encode('utf-8'))
    if meg == 'q':
        break
    res_s = sk.recv(1024).decode('utf-8')
if res_s == 'q':
    break
    print(res_s)
sk.close()
