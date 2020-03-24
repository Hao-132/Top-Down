from socket import *
serverName = "192.168.1.105"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("Input Lowercase sentence:")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("From Server: \n", modifiedSentence.decode())
clientSocket.close()
