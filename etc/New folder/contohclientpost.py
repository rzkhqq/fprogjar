__author__ = 'zq'

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("localhost",8080))


s.send("POST / HTTP/1.0\r\nHost: localhost:80\n\n")
content = ""
while True:
        resp = s.recv(1024)
        if resp == "": break
        print resp
        content += resp
        #file.write(resp)

s.close()
print content
#print "Content : " + content
temporarySplit = content.split('\r\n\r\n')
responseHeader = temporarySplit[0]

#print responseHeader