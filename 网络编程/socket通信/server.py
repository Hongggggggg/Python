import socket
import subprocess

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
            conn.send(stdout + stderr)
        except ConnectionResetError as e:
            print(e)
            break
    #关闭连接
    conn.close()
tcp_socket.close()