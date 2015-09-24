import socket
import threading
import os
from os.path import isfile, join,isdir

path='/home/aravind/'

def Retfile(name,sock):
    files = []
    fi = search_file(path,files)
    for filename in fi:
        if os.path.getsize(filename) != 0:
            data = sock.recv(1024)
            if os.path.isfile(filename):
                client_file = filename.split('/')[-1]
                sock.send(client_file)
                sock.recv(1024)
                sock.send("Exist" + str(os.path.getsize(filename)))
                userRes = sock.recv(1024)
                if userRes[:2] == 'OK':
                    with open(filename,'rb') as f:
                        bytesToSend = f.read(1024)
                        sock.send(bytesToSend)
                        while bytesToSend != '':
                            bytesToSend = f.read(1024)
                            sock.send(bytesToSend)
            else:
                pass
    data = sock.recv(1024)  
    if data =='complete':
        sock.send("DownloadComplete")

def search_file(path,files):
    if isdir(path):
        print "searching ...."
        for f in os.listdir(path):
            if isfile(join(path, f)):
                path_f = path+f
                files.append(path_f)
            else:
                temp_path = join(path, f) + '/'
                temp_file = search_file(temp_path,files)
    return files    

HOST = '192.168.1.16'   
PORT = 8888 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
print "listening"
while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    t=threading.Thread(target=Retfile,args=("Thread1",conn))
    t.start()

       

        


