# Imports:

from socket import socket,AF_INET,SOCK_STREAM,gaierror

# Definition:

class Portscanner :

    def __init__(self,GREEN:str,RED :str,RESET: str,ip: str,rrange) :

        self.ip,self.range = ip,rrange
        self.GREEN,self.RED,self.RESET = GREEN,RED,RESET

    def Scan(self) :

        if self.ip == '' :
            self.ip = 'localhost'
        rrange = self.range.split("-")
        if rrange == [''] :
            rrange = ['1','65535']
            
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

        if rrange == [''] :
            rrange = ['1','65535']

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

if __name__ == '__main__' :

    from colorama import *
    print(f'{Fore.BLUE}this is a demo of this module ')
    print('if you dont see any ports it may be your host does not any open ports')
    print(f'its a test from localhost ports{Fore.RESET}')
    test = Portscanner(Fore.GREEN,Fore.RED,Fore.RESET,'127.0.0.1','1-65535')
    test.Scan_o()
            
########################### END ###########################