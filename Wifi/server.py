#!/usr/bin/python3
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname() 
port = 444 

serversocket.bind(('192.168.137.1', port))
serversocket.listen(3)

while True:
    
    #Starting the connection 
    clientsocket,address = serversocket.accept()

    print("received connection from %s " % str(address))
    
    #Message sent to client after successful connection
    message=input("Enter:")
    
    #message = 'hello! Thank you for connecting to the server' + "\r\n"
    
    clientsocket.send(message.encode('ascii'))

clientsocket.close()