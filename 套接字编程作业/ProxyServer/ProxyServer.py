from socket import *

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# start
tcpSerSock.bind(('', 12000))
tcpSerSock.listen(5)
# end
while 1:
    # Strat receiving data from the client 
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from: ', addr)
    message =  tcpCliSock.recv(4096).decode() # start
    print(message)
    # Extract the filename from the given message
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print(filename)
    fileExist = "false"
    fileouse = "/" + filename
    print(fileouse)
    try:
        # Check wether the dile exist in the cache
        f = open(fileouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a acahe hit and generates a response message
        """
        tcpCliSock.send(b" HTTP/1.1 200 OK\n")
        tcpCliSock.send(b"Content-Type: text/html\n")
        # start
        tcpCliSock.send("Content-Length: {0:d}\n\n".format(len(outputdata)).encode())
        """
        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i].encode())
        # end
        print('Read from cache')
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM) # start
            hostn = filename.replace("www.", "", 1)
            print(hostn)
            try:
                # Connect to the socket to port 80
                # start 
                c.connect(('', 80))
                # end
                # Create a temporary file on this socket and ask port 80
                # for the file requested by the client
                fileobj = c.makefile('r', 0)
                fileobj.write("GET" + "http://" + filename + "HTTP/1.1\n\n")
                # Read the response into buffer
                # start 
                outdata = c.recv(1024).decode()

                # end
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket
                # and the corresponding file in the cache
                tmpFile = open("./" + filename, "wb")
                # start 
                tmpFile.write(outdata)
                tmpFile.close()
                tcpCliSock.send(outdata.encode())
                # end
            except:
                print("Illegal request")
        else:
            # HTTP response message for file not found
            # start 
            tcpCliSock.send(b" HTTP/1.1 404 Found")
            # end
    # Close the client and the server sockets
    tcpCliSock.close()
tcpSerSock.close()



