import socket
import subprocess
import json
import struct

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #可重复使用端口
#tcp_socket

#设置IP和端口号
tcp_socket.bind(('127.0.0.1', 8081))

#设置最大链接数
tcp_socket.listen(5)
while True:
    #等待接受数据
    conn, client_addr = tcp_socket.accept()

    #收发数据
    while True:
        try:
            cmd = conn.recv(1024)#一次最多接收1024字节
            if not cmd: break

            obj = subprocess.Popen( cmd.decode('utf-8'), shell = True,
                                    stdout = subprocess.PIPE,
                                    stderr = subprocess.PIPE,)

            print('rcv cmd:' + cmd.decode('utf-8'))
            stdout=obj.stdout.read()
            stderr=obj.stderr.read()

            print(stdout + stderr)

            #第一步制定报头
            header_dir = {
                "filename": "tcp.txt",
                "md5": 123456,
                "total_size": len(stdout) + len(stderr)
            }
            header_json = json.dumps(header_dir) #先转成json格式的字符串
            header_bytes = header_json.encode('utf-8') #再将json字符串转成byte类型 

            #第二步，先发送报头的长度
            header_size = struct.pack('i', len(header_bytes))
            conn.send(header_size)

            #第三步，发送报头
            conn.send(header_bytes)

            #第四步，发送payload
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionResetError as e:
            print(e)
            break
    #关闭连接
    conn.close()
tcp_socket.close()