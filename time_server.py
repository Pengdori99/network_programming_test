#time_Server.py
import socket # 소켓 모듈을 불러온다
import time

#TCP 소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('', 5000)#''=임의 주소, 포트 번호=5000
s.bind(address)
s.listen(5)

while True:
    client, addr = s.accept()
    print("Connection Requested from ", addr)
    client.send(time.ctime(time.time()).encode())
    client.close()