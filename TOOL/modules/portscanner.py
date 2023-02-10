# Imports:

from socket import socket,AF_INET,SOCK_STREAM,gaierror

# Definition:

class Portscanner :

    def __init__(self,ip: str,rrange: str,GREEN: str,RED :str,RESET: str) :

        self.ip,self.range = ip,rrange
        self.GREEN,self.RED,self.RESET = GREEN,RED,RESET

    def Scan(self) :

        rrange = self.range.split("-")

        try:
            for port in range(int(rrange[0]),int(rrange[1])+1) :

                s = socket(AF_INET,SOCK_STREAM)
                result = s.connect_ex((self.ip,port))
                if result == 0 :
                    print(f"{self.GREEN} [+] Port {port} is Open{self.RESET}")

                else :
                    print(f"{self.RED} [-] Port {port} is Closed !{self.RESET}")

        except gaierror :
            print(f"{self.RED}Server {self.ip} is Not Available !{self.RESET}")
        
        finally :
            print(f"{self.RED} job finished ! {self.RESET}")


    def Scan_o(self) :

        rrange = self.range.split("-",2)

        try:
            for port in range(int(rrange[0]),int(rrange[1])+1) :

                s = socket(AF_INET,SOCK_STREAM)
                result = s.connect_ex((self.ip,port))
                if result == 0 :
                    print(f"{self.GREEN} [+] Port {port} is Open{self.RESET}")

        except gaierror :
            print(f"{self.RED}Server {self.ip} is Not Available !{self.RESET}")

        finally :
            print(f"{self.RED} job finished ! {self.RESET}")
            
########################### END ###########################