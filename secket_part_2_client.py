import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("connecting......")
sock.connect((socket.gethostname(), 5555))
# complete_messge = ""
print("server is typing something!")
while True:
    message = sock.recv(2048)
    print(message.decode("utf-8"))
    if message.decode("utf-8") == "quit":
        print("Connection has been terminated!")
        break
    # sock.close()
    # if len(message) <= 0:
    #     break
    # else:
    #     complete_messge += message.decode("utf-8")
    # print(complete_messge)
