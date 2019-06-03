import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket has been successfully created")
sock.bind((socket.gethostname(), 5555))
print("Socket has been successfully binded")
sock.listen(5)
while True:
    client_socket, ip_address = sock.accept()
    print("Connection from {0} has been establish!".format(ip_address))
    while True:
        message = input("Please enter the text that you want to send: ")
        client_socket.send(bytes(message, "utf-8"))
        if message == "quit":
            break
    break
print("Connection has been terminated!")
client_socket.close()
