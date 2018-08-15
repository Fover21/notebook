解决方案

# 我们可以借助一个模块，这个模块可以把要发送的数据长度转换成固定长度的字节。这样客户端每次接
# 收消息之前只要先接受这个固定长度字节的内容看一看接下来要接收的信息大小，那么最终接受的数据
# 要达到这个值就停止，就能刚好不多不少的接收完整的数据了。

# import json,struct
# #假设通过客户端上传1T:1073741824000的文件a.txt

# #为避免粘包,必须自定制报头
# header={'file_size':1073741824000,'file_name':'/a/b/c/d/e/a.txt','md5':'8f6fbf8347faa4924a76856701edb0f3'} #1T数据,文件路径和md5值

# #为了该报头能传送,需要序列化并且转为bytes
# head_bytes=bytes(json.dumps(header),encoding='utf-8') #序列化并转成bytes,用于传输

# #为了让客户端知道报头的长度,用struck将报头长度这个数字转成固定长度:4个字节
# head_len_bytes=struct.pack('i',len(head_bytes)) #这4个字节里只包含了一个数字,该数字是报头的长度

# #客户端开始发送
# conn.send(head_len_bytes) #先发报头的长度,4个bytes
# conn.send(head_bytes) #再发报头的字节格式
# conn.sendall(文件内容) #然后发真实内容的字节格式

# #服务端开始接收
# head_len_bytes=s.recv(4) #先收报头4个bytes,得到报头长度的字节格式
# x=struct.unpack('i',head_len_bytes)[0] #提取报头的长度

# head_bytes=s.recv(x) #按照报头长度x,收取报头的bytes格式
# header=json.loads(json.dumps(header)) #提取报头

# #最后根据报头的内容提取真实的数据,比如
# real_data_len=s.recv(header['file_size'])
# s.recv(real_data_len)


# 我们还可以把报头做成字典，字典里包含将要发送的真实数据的详细信息，然后json序列化，
# 然后用struck将序列化后的数据长度打包成4个字节（4个自己足够用了）

# 	发送时							接收时
# 先发报头的长度 			先收报头长度，用struct取出来
# 再编码报头内容然后发送		根据取出的长度收取报头内容，然后解码，反序列化
# 最后发真实内容			从反序列化的结果中取出待取数据的详细信息，然后去取真实的数据内容

#例子：
#server端
import socket, struct, json
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 就是它，在bind前加

phone.bind(('127.0.0.1', 8080))

phone.listen(5)

while True:
    conn, addr = phone.accept()
    while True:
        cmd = conn.recv(1024)
        if not cmd: break
        print('cmd: %s' % cmd)

        res = subprocess.Popen(cmd.decode('utf-8'),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        err = res.stderr.read()
        print(err)
        if err:
            back_msg = err
        else:
            back_msg = res.stdout.read()

        conn.send(struct.pack('i', len(back_msg)))  # 先发back_msg的长度
        conn.sendall(back_msg)  # 在发真实的内容

    conn.close()


#client端
import socket, struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = s.connect_ex(('127.0.0.1', 8080))

while True:
    msg = input('>>: ').strip()
    if len(msg) == 0: continue
    if msg == 'quit': break

    s.send(msg.encode('utf-8'))

    l = s.recv(4)
    x = struct.unpack('i', l)[0]
    print(type(x), x)
    # print(struct.unpack('I',l))
    r_s = 0
    data = b''
    while r_s < x:
        r_d = s.recv(1024)
        data += r_d
        r_s += len(r_d)

    print(data.decode('utf-8'))
    # print(data.decode('gbk')) #windows默认gbk编码
