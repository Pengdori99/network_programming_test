#TCP Echo Sever Program
from socket import *

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))#종단점과 소켓 결합. ' 임의 주소'
sock.listen(1)
conn, (remotehost, remoteport) = sock.accept()
print('connected by', remotehost, remoteport)
while True:
    data = conn.recv(BUFSIZE)
    if not data: #''이면 종료, ''는 False
        break
    print("Received message: ", data.decode())
    conn.send(data)
conn.close()
