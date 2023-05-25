# client.py
import time, socket, sys

print("\nChat Room \n")
# create a socket object 
s = socket.socket()
# retrieve the hostname and IP address 
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
print(host, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("\nEnter your name: "))
port = 1234
s.connect((host, port))
print("Connected.\n")
s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")
while True:
    message = s.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        s.send(message.encode())
        print("\n")
        break
    s.send(message.encode())
