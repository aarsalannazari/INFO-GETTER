# Imports :

from socket import *

# Definition :

class IP_Scanner :

    def IP_Scanner_a(ip24 : str,time_out : float,RED,GREEN,RESET) :
        """
        NOTE : IP address must 24 first bit of address with out the . of 24th bit
        for timeout 0.7 second is good.
        """
        
        if not ip24 :

            ip24 = '192.168.1'

        if time_out == '' :

            time_out = 0.7

        for i in range(256) :
            
            ip = ip24 + '.' + str(i)

            try :

                inet_aton(ip)

                s = socket(AF_INET,SOCK_STREAM)
                s.settimeout(float(time_out))
                
                ports = []

                for port in range(65536) :

                    try :
                        s.connect((ip,port))
                        ports.append(port)
                        break

                    except : pass

                if not ports :

                    print(f"{RED} [-] {ip} is Not Found !{RESET}")

                else : 

                    print(f"{GREEN} [+] {ip} is Found {RESET}")

                s.close()

            except error as e : print(e)

        return

    """
    NOTE : This ipscanner scan with open ports 
            if some ips have not any open ports it say 'this ip is not Found!'
            Please be careful for this NOTE !
    """

    def IP_Scanner_o(ip24 : str,time_out,GREEN,RESET) :
        """
        NOTE : IP address must 24 first bit of address with out the . of 24th bit
        for timeout 0.7 second is good.
        """
        
        if not ip24 :
            ip24 = '192.168.1'

        if time_out == '' :
            time_out = 0.7

        for i in range(256) :
            
            ip = ip24 + '.' + str(i)

            try :

                inet_aton(ip)

                s = socket(AF_INET,SOCK_STREAM)
                s.settimeout(float(time_out))
                
                ports = []

                for port in range(65536) :

                    try :
                        s.connect((ip,port))
                        ports.append(port)
                        break

                    except : pass

                if not ports :pass

                else : 

                    print(f"{GREEN} [+] {ip} is Found {RESET}")

                s.close()

            except error as e : print(e)

        return

    """
    NOTE : This ipscanner scan with open ports 
            if some ips have not any open ports it say 'this ip is not Found!'
            Please be careful for this NOTE !
    """

if __name__ == '__main__' :

    from colorama import Fore
    print(f'{Fore.BLUE}this is a demo of this module ')
    print(f'its a test from range 192.168.1.0 to 192.168.1.255{Fore.RESET}')
    print('\n')
    IP_Scanner.IP_Scanner_a('192.168.1',0.7,Fore.RED,Fore.GREEN,Fore.RESET)



########################### END ###########################