import socket
from directkeys import PressKey,ReleaseKey,W,A,S,D
s = socket.socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##host = socket.gethostbyname("DESKTOP-HC36K46") !My windows pc name
port = 1122
EndNumber = 255
i = 100 
## really depends on your router (mine starts from 192.168.0.100) 
##yours may start from 192.168.0.1 if thats the case change  i = 100 to i = 1 and EndNumber to something Less like 20
## because at max home router can handle 8-16 devices at max
host = 'WWW'
while i < EndNumber:
    ip = "192.168.0."+str(i)
    i = i+1
    print(ip)
    try:
        hostname = socket.gethostbyaddr(str(ip))
        print(hostname)
        computerName = hostname[0]
        print(computerName)
        Server = computerName.split('.')
        print(Server[0])
        if(str(Server[0]) == "DESKTOP-HC36K46"):## finding my server's ip address
            host = str(ip)
            print(ip)
            break
    except:
        pass
s.connect((host,port))
print("CONNECTED TO SERVER")
while True:
    data = s.recv(2)
    print(str(data))
    data = str(data)
    if(data == "b'w'"):
        print("W")
        PressKey(W)
        ReleaseKey(S)
        ReleaseKey(A)
        ReleaseKey(D)
    elif(data == "b's'"):
        print("S")
        PressKey(S)
        ReleaseKey(W)
        ReleaseKey(A)
        ReleaseKey(D)
    elif(data == "b'a'"):
        print("A")
        PressKey(A)
        ReleaseKey(W)
        ReleaseKey(S)
        ReleaseKey(D)
    elif(data == "b'd'"):
        print("D")
        PressKey(D)
        ReleaseKey(W)
        ReleaseKey(S)
        ReleaseKey(A)
    elif(data == "b'wa'"):
        PressKey(A)
        pressKey(W)
        ReleaseKey(S)
        ReleaseKey(D)
    elif(data == "b'wd'"):
        print("WD")
        PressKey(D)
        pressKey(W)
        ReleaseKey(S)
        ReleaseKey(A)
    elif(data == "b'sa'"):
        print("SA")
        PressKey(A)
        pressKey(S)
        ReleaseKey(W)
        ReleaseKey(D)
    elif(data == "b'sd'"):
        print("SD")
        PressKey(D)
        pressKey(S)
        ReleaseKey(W)
        ReleaseKey(A)



### replace "DESKTOP-HC36K46" with your server name
