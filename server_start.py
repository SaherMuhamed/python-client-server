import socket
from twilio.rest import Client

MY_EMAIL = "smtblibserver@gmail.com"
# MY_PASSWORD = "*0123456789*"
MY_PASSWORD = "soyrsfvxdjeoqaue"

account_sid = "AC2ca1a3f853bc2b84ffa601fe670496f7"
auth_token = "cd7fe6f1605e248d1a24814b49aafbcf"


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

                if float(incoming_data) <= 30:
                    client = Client(account_sid, auth_token)
                    message = client.messages.create(
                         body="From Saher.. Warning, the distance is very close.",
                         from_='+13464722818',
                         to='+201278144852'
                    )
                    print(message.status)
                # print(f"\r[*] Received from ESP8266 ==> {incoming_data} cm.", end="")
                # print(type(incoming_data))
                # Enter your processing function here.
        except KeyboardInterrupt:
            self.connection.close()
            print("\n[-] Detected ctrl + c Pressed, Connection Terminated.\n")
            exit()
