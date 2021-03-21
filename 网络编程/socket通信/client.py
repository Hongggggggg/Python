import socket
import struct
import json

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#连接
tcp_socket.connect(('127.0.0.1', 8081))

#发、收消息
while True:
    cmd = input(">>").strip()
    if cmd:
        tcp_socket.send(cmd.encode('utf-8'))
        #第一步，先手报头长度
        obj = tcp_socket.recv(4)
        header_size = struct.unpack('i', obj)[0]
        print('header_size:', header_size)

        #第二步，收报头具体内容
        header_bytes = tcp_socket.recv(header_size)
        
        #第三步，从报头中解析数据描述信息
        header_json = header_bytes.decode('utf-8')
        print('=====' + header_json)
        header_dic = json.loads(header_json)
        print(header_dic)
        total_size = header_dic['total_size']

        #第四步，收取真实数据
        recv_size = 0
        recv_data = b''
        while recv_size < total_size:
            res = tcp_socket.recv(1024)
            recv_data += res
            recv_size += len(res)

        print(recv_data.decode('utf-8'))

tcp_socket.close()