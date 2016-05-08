import socket
import sys


def server():
    print("server")
    server = socket.socket()
    host = socket.gethostname()
    port = 4951
    s.bind((host, port))
    
    server.listen(5)
    while True:
        client, address = server.accept()
        print(address)
        client.send("Ground control to Major Tom")
        client.close()
   
    
def client():
    print("client")
    server = socket.socket()
    host = '98.146.149.203' #socket.gethostname()
    port = 4951
    
    server.connect((host, port))
    print(server.recv(1024))
    server.close()
    

if __name__ == '__main__':
    try: 
        if sys.argv[1] == 'server':
            server()
        else:
            client()
    except:
        pass
