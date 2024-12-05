import socket 

HOST = "127.0.0.1"
PORT = 6432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    data = " " 
    while data != b"END":  
        data = s.recv(1024)
        print(f"Data sended from server:{data}")