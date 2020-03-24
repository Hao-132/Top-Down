# UDPing

用`try`和`except`可以在报错的时候，捉住bug。

用`settimeout`可以设置`socket.socket.recvfrom()`接收报文的超时时间，当接收超时时，会报错，这时就可以用`try`和`except`来处理这种情况。

