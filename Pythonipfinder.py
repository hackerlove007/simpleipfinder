
import socket

host = input("write")
ip = socket.gethostbyname(host)
print(ip)
