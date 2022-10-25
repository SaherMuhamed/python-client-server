import socket
from twilio.rest import Client


class Server:

    def __init__(self, server_ip, server_port):
        listener = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            listener.bind((server_ip, server_port))
        except socket.error as error:
            print(f"[-] {str(error)}")
        listener.listen(1)
        self.printing_format()
        print("[+] Waiting for Incoming Connections ...")
        self.connection, self.address = listener.accept()
        if self.connection:
            print(f"[+] Got a Connection from {self.address}\n"
                  "-------------------------------------------------")

    def printing_format(self):
        print('''
░██████╗███████╗██████╗░██╗░░░██╗███████╗██████╗░
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗
╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝
░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗
██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
             By Saher Muhamed v1.0
''')

    def receive_data(self):
        """Already decoded"""
        return self.connection.recv(4096).decode("UTF-8")

    def run(self):
        try:
            while True:
                incoming_data = self.receive_data()
                print(f"[*] Received from ESP8266 ==> {incoming_data} cm.")
                # print(f"\r[*] Received from ESP8266 ==> {incoming_data} cm.", end="")
                # print(type(incoming_data))
                # Enter your processing function here.
        except KeyboardInterrupt:
            self.connection.close()
            print("\n[-] Detected ctrl + c Pressed, Connection Terminated.\n")
            exit()
