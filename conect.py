import socket
import sys
import json
 
# Set up a TCP/IP server
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
server_address = ('192.168.194.80', 8080)
tcp_socket.bind(server_address)
 
# Listen on port 8080 
tcp_socket.listen(1)
 
while True:
    print("Waiting for connection")
    connection, client = tcp_socket.accept()
 
    try:
        print("Connected to client IP: {}".format(client))
         
        # Receive and print data 32 bytes at a time, as long as the client is sending something
        while True:
            data = connection.recv(130)
            dataJson = json.loads(data)
             
            # printing all elements of dictionary
            print("Dictionary after parsing: ", dataJson)

            print("Timestamp: ", dataJson['accelerometer']['timestamp'])
            print("X: ", dataJson['accelerometer']['value'][0])
            print("Y: ", dataJson['accelerometer']['value'][1])
            print("G: ", dataJson['accelerometer']['value'][2])
 
            if not data:
                break
 
    finally:
        connection.close()