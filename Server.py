import socket
import threading
from Parser import Parser
from struct import *

class Server(object):
    def __init__(self, host, port, timeout):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(self.timeout)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        print ("New connection from " + address[0] + ".")
        while True:
            try:
                data = client.recv(size)
                if data:
                    data = str(data.decode()).replace('\x00', '')
                    print('Message from  ' + address[0] + ':')
                    print(data)
                    parser = Parser(data)
                    response = parser.Parse()

                    if response != None:
                        print('Response to  ' + address[0] + ':')
                        print(response)
                        client.send(bytearray(response, 'utf-8'))
                else:
                   raise error('Client disconnected')
            except:
                print ('Connection from ' + address[0] + ' is over.')
                client.close()
                return False

    {"ID": "UPDATE_ROOM", "rID": "2", "user1": "KJ", "user2": "JJ", "user3": "AA", "user4": "BC", "user5": "AS"}

    def mysend(self, msg, client):
        totalsent = 0
        while totalsent < 1024:
            sent = client.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("Socket error")
            totalsent = totalsent + sent

if __name__ == "__main__":
    port_num = 1236
    Server('192.168.140.101', int(port_num), 120).listen()