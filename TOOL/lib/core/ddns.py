# Imports:

from dns            import resolver
from colorama       import Fore

# Colors:

GREEN,LIGHTGREEN,BLUE,MAGENTA,RED=Fore.GREEN,Fore.LIGHTGREEN_EX,Fore.BLUE,Fore.MAGENTA,Fore.RED
YELLOW,CYAN,LIGHTCYAN,WHITE,RESET=Fore.YELLOW,Fore.CYAN,Fore.LIGHTCYAN_EX,Fore.WHITE,Fore.RESET

# Definition:

class Dns_Checker :
    
    def __init__(self,domain) :
        self.domain=domain

    def options(self=None) :
        print(f"""{YELLOW}
        OPTIONS:
        {RED}
        1  -  A Record
        2  -  C Name
        3  -  MX Record
        00 -  Return to Main Menu

        {RESET}""")

    def A_record (self,type='A') :
        result = resolver.query(self.domain,type)
        for ip in result :
            return ip

    def MX_record(self,type='MX') :
        answers = resolver.query(self.domain,type)
        for rdata in answers:
            return rdata
    
    def Cname(self,type='CNAME') :
        result = resolver.query(self.domain,type)
        for cname in result :
            return cname.target

########################### END ###########################