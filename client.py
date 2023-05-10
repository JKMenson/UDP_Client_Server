import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
message = input("Write a message: ").encode('utf-8')
server_address =('localhost',12345)
client_socket.sendto(message, server_address)
data, server_address = client_socket.recvfrom(4096)
print("Received response from {}: {}". format(server_address,data.decode()))
client_socket.close()