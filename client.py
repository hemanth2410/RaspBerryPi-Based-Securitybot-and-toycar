import socket
s = socket.socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##host = socket.gethostbyname("DESKTOP-HC36K46") !My windows pc name
port = 1122
EndNumber = 255
i = 100
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
    elif(data == "b's'"):
        print("S")
    elif(data == "b'a'"):
        print("A")
    elif(data == "b'd'"):
        print("D")
    elif(data == "b'wa'"):
        print("WA")
    elif(data == "b'wd'"):
        print("WD")
    elif(data == "b'sa'"):
        print("SA")
    elif(data == "b'sd'"):
        print("SD")



### replace "DESKTOP-HC36K46" with your server name
