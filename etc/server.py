import socket
import sys

server_address = ('localhost', 8080)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

print 'Serving HTTP on port %s ...' % server_address[1]

try:
    while True:
        client_socket, client_address = server_socket.accept()
        #print client_address
        data = client_socket.recv(4096)
        print data
        
        
        
        http_response = "Hello World\r\nHTTP/1.1\r\n\r\n"
        client_socket.sendall(http_response)
        client_socket.close()        
   
except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)