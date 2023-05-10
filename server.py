import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)
print('UDP server is running on {}:{}'.format(*server_address))

while True:
    data, client_address = server_socket.recvfrom(4096)
    print('Received message from {}: {}'. format(client_address,data.decode()))
    message = 'Hello, I am the UDP server!'.encode('utf-8')
    server_socket.sendto(message, client_address)
    