from time import *
from socket import *
serverName = "192.168.1.105"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
# 设置超时报错
clientSocket.settimeout(1) 
message = input("Input Lowercase sentence:")
for i in range(10):
    start = perf_counter()
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    # 用try语句，当recvfrom超时报错时，打印包丢失。
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    except timeout:
        print("Ping {0:d}: loss packet.".format(i))
        continue
    end = perf_counter()
    print("Ping {:d}: successful. the time is {:f}.".format(i, end - start))
    print("The message is " + modifiedMessage.decode())
clientSocket.close()


