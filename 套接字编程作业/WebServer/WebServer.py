from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
# start
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
# end
while True:
    print("Ready to server...")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # start
        connectionSocket.send("Connection: close/r/n".decode())
        connectionSocket.send("Content-Length: %d/r/n".format(len(outputdata)).decode())
        connectionSocket.send("Content-Type: text//html/r/n".decode())
        # end
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()

    except IOError:
        # start
        connectionSocket.send("404 Not Found!".decode())
        # end
        # start
        connectionSocket.close()
        # end

serverSocket.close()
    

