from socket import *
msg = b'\r\n I love computer networks!'
endmsg = b'\r\n.\r\n'
# Choose a mail server(e.g. Google mail server) amd call it mailserver
mailserver = "163mx02.mxmail.netease.com" 
# Create socket called clientSocket and establish a TCP connection with mailserver
# start 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
# end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO aommand and print server response.
heloCommand = b'HELO hhj\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response
# start 
mfCommand = b'MAIL FROM: <a15095132619@163.com>'
clientSocket.send(mfCommand)
recv2 = clientSocket.recv(1024).decode()
#print(recv2)
if recv2[:3] != '250':
    print('MAIL FROM 250 reply not received from server.')
# end

# Send RCPT TO command and print server response
# start 
rtCommand = b'RCPT TO: <1291536750@qq.com>'
clientSocket.send(rtCommand)
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('RCPT TO 250 reply not received from server.')
# end

# Send DATA command and print server response
# start 
dataCommand = b'DATA'
clientSocket.send(dataCommand)
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('DATA 354 reply not received from server.')
# end

# Send message data.
# start
clientSocket.send(msg)
# end

# Message ends with a single period.
# start 
clientSocket.send(endmsg)
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('. 250 reply not received from server.')
# end 

# Send QUIT command and get server respinse
# start 
quitCommand = b'QUIT'
clientSocket.send(quitCommand)
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '221':
    print('QUIT 221 reply not received from server.')
# end
