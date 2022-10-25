import socket
import sys


class Client:

    def __init__(self, client_ip, client_port):
        self.connection = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.connection.connect((client_ip, client_port))
        self.print_format()
        print("[+] Connection Established Successfully.\n"
              "----------------------------------------------------------")
        self.print_settings()

    def print_format(self):
        print('''   
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |   C:\>_         |  |  |     |         |      |
     |  |                 |  |  |/----|`---=    |      |
     |  |       by        |  |  |   ,/|==== ooo |      ;
     |  |      Saher      |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
''')

    def print_settings(self):
        print("                    [Setting Screen]                      ")
        print("----------------------------------------------------------")
        print("[1] Calculator.")
        print("[2] BMI Calculator.")
        print("[3] Circle Area.")
        print("[4] Fahrenheit to Celsius Converter.")
        print("[5] Network Connectivity.")

    def run(self):
        while True:
            input_data = input("\nsaher@root~# ")
            self.connection.send(input_data.encode("UTF-8"))
            if input_data == "exit":
                self.connection.close()
                sys.exit()


client_1 = Client(client_ip="127.0.0.1", client_port=7878)
client_1.run()
