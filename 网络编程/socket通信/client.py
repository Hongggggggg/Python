import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#连接
tcp_socket.connect(('127.0.0.1', 8081))

#发、收消息
while True:
    data = input(">>").strip()
    if data:
        tcp_socket.send(data.encode('utf-8'))
        data = tcp_socket.recv(4096)
        print(data)

tcp_socket.close()