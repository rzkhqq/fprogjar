import socket

# create socket and connect to server
server_address = ('localhost', 8080)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)
# send string to server and close socket
client_socket.send('Hi ... ')
resp=client_socket.recv(1024)
print resp 
client_socket.close()