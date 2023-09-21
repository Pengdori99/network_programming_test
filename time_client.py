# time_client.py
import socket
import time

#TCP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("localhost", 5000)
sock.connect(address)

while True:
    time.sleep(1)
    print("현재시각: ", sock.recv(1024).decode())#수신내용을 문자열로 변환하여 출력