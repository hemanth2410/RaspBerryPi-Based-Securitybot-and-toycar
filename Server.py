import socket
from directkeys import PressKey,W,A,S,D
import time
from getkeys import key_check
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('starting server on pc')
print(socket.gethostname())
print('Please enter the following code from raspberry pi')
host = socket.gethostbyname("DESKTOP-HC36K46")
port = 1122
print("Socket successfully created")
s.bind((host,port))
s.listen(300)
print("waiting for clients")
c,addr = s.accept()
print("connection from "+str(addr))
while True:
    time.sleep(0.2)
    keys = key_check()
    if 'W' in keys and 'A' in keys:
        c.send(b'wa')
    elif 'W' in keys and 'D' in keys:
        c.send(b'wd')
    elif 'S' in keys and 'A' in keys:
        c.send(b'sa')
    elif 'S' in keys and 'D' in keys:
        c.send(b'sd')
    elif 'W' in keys:
        c.send(b'w')
    elif 'S' in keys:
        c.send(b's')
    elif 'A' in keys:
        c.send(b'a')
    elif 'D' in keys:
        c.send(b'd')


### THIS NEEDS TO BE RUNNING ON WINDOWS PC OR LINUX PC(please avoid lenovo laptop network programming is not properly working on them)
