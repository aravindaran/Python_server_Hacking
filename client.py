import socket
import sys, string, select
 
HOST = '192.168.1.16'   
PORT = 8888 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (HOST,PORT)
s.connect(address)
print "connecting..."
s.send("start")
while 1:
    filename = s.recv(1024)
    if filename == 'DownloadComplete':
        print "--->>>>>>> DownloadComplete <<<<<<<<<<----"
        userdata=raw_input()
        break      
    s.send("got it")
    data = s.recv(1024)
    if data[:5] == 'Exist':
        filesize = long(data[5:])
        message = raw_input(filename + " file exists. " + str(filesize) + "bytes..download? (Y/N)? ->")
        if message =='Y' or message =='y':
            s.send("OK")
            f = open("new_" + filename, 'wb')
            data = s.recv(1024)
            totalRecv = len(data)
            f.write(data)
            while totalRecv < filesize:
                data = s.recv(1024)
                totalRecv += len(data)
                f.write(data)
                print "{0:.2f}".format((totalRecv/float(filesize))*100)+"Done"
            s.send("complete")
        else:
            break
    else:
        print "File doesn't exist"

                            		


	
 


