# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 23:40:52 2023

@author: lucas
"""

import socket

# 初始化
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 3000))
server_socket.listen(1)

print("等待連接...")

# 等待客戶端連接
conn,addr= server_socket.accept()
print(f"已連接到 {addr}")

# 接收回音(echo)和發送回音
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"接收到的資料：{data.decode()}")
    conn.send(data)

# 關閉連接
conn.close()
server_socket.close()

