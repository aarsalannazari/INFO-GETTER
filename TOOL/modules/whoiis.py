# Imports:

from ipwhois import IPWhois
from socket  import gethostbyname
from whois   import query

# Definition:

class Information:
        
    def __init__(self,domain) :

        self.domain=domain

    def Get_ip(self,domain):
        ip = gethostbyname(domain)
        return ip
    def Domain_info(self,domain) :
        return query(domain).__dict__

    def Server_info(self,domain) :
        ip = Information.Get_ip(None,domain)
        info = IPWhois(ip)
        info = info.lookup_whois()
        return info

########################### END ###########################