# Imports:

import functions
from modules import whoiis,ddns,google_map,subdomain,portscanner
from modules import plugins,admin_finder,website_information,http_header
from random  import randint
from os      import system
from time    import sleep
from pprint  import pprint

# Definition:

def clear() :
    try :
        system('cls')
    except :
        system('clear')

def banner_options() :
    clear()
    STYLE
    functions.Tools.banner()
    functions.Tools.options()

# Colors:

STYLE=functions.STYLE
GREEN,LIGHTGREEN,BLUE,MAGENTA,RED=functions.GREEN,functions.LIGHTGREEN,functions.BLUE,functions.MAGENTA,functions.RED
YELLOW,CYAN,LIGHTCYAN,WHITE,RESET=functions.YELLOW,functions.CYAN,functions.LIGHTCYAN,functions.WHITE,functions.RESET

# Main:

banner_options()

while True :
    try:
        num=input(f" {STYLE}{RED} [+] {WHITE}Enter a number from the list : {LIGHTGREEN}")

        if num == '1' : #==> Whois

            clear()
            domain = input(f" {RED} [1] {WHITE}Enter a Domain : {LIGHTGREEN}")
            whois = whoiis.Information(num)
            res_Domain = whois.Domain_info(domain)
            res_Server = whois.Server_info(domain)
            print(f"{RED}Result of Domain : {CYAN}\n")
            pprint(res_Domain)
            print(f"\n{RED}Result of Server : {CYAN}\n")
            pprint(res_Server)
            input(f"\n{MAGENTA}Press Enter to continue : {RESET}")
            banner_options()

        elif num == '2' : #==> Dns Checker

            clear()
            domain = input(f" {RED} [2] {WHITE}Enter a Domain : {LIGHTGREEN}")
            Dns=ddns.Dns_Checker(domain)
            Dns.options()
            num = input(f" {RED} [2] {WHITE}Enter a Number from the list : {LIGHTGREEN}")

            if num == '1' :

                res = Dns.A_record()
                print(f"\n {RED} [+] {WHITE}IP{RED} ==> {CYAN}{res}{RESET}")
                input(f"\n{MAGENTA}Press Enter to continue : {RESET}")
                banner_options()

            elif num == '2' :

                res = Dns.Cname()
                print(f"\n {RED} [+] {BLUE}Domain{RED} ==> {CYAN}{domain}{WHITE} , {GREEN}C Name{RED} ==> {CYAN}{res}{RESET}")
                input(f"\n{MAGENTA}Press Enter to continue : {RESET}")
                banner_options()

            elif num == '3' :

                res = Dns.MX_record()
                print(f" {RED} Host {CYAN}{res.exchange}{RED} has preference {CYAN}{res.preference}{RESET}")
                input(f"\n{MAGENTA}Press Enter to continue : {RESET}")
                banner_options()

            elif num ==  '00' :
                banner_options()
                continue

        elif num == '3' : #==> Ip location

            google_map.generate()
        
        elif num == '4' : #==> Sub Domains

            clear()
            domain = input(f" {RED} [4] {WHITE}Enter a Domain : {LIGHTGREEN}")
            print('\n')
            subdomain.Discover_Subdomains(domain,CYAN,BLUE,RESET,RED,GREEN)
            print(f"\n{RED}Discover Ended !{RESET}")
            input(f"\n{MAGENTA}Press Enter to continue : {RESET}")
            banner_options()

        elif num == '5' : #==> WordPress Plugin

            clear()
            domain = input(f" {RED} [5] {WHITE}Enter a Domain : {LIGHTGREEN}")
            print('\n')
            plugins.Discover_Plugins(domain,CYAN,BLUE,RESET,RED,GREEN)
            print(f"\n{RED}Discover Ended !{RESET}")
            input(f"\n{MAGENTA}Press Enter to continue : {RESET}")
            banner_options()

        elif num == '6' : #==> Admin Finder

            clear()
            domain = input(f" {RED} [6] {WHITE}Enter a Domain : {LIGHTGREEN}")
            time_sleep = input(f" {RED} [6] {WHITE}Enter time interval between two requests  : {LIGHTGREEN}")
            print('\n')
            admin_finder.Admin_finder(domain,time_sleep,CYAN,RED,GREEN,BLUE,RESET)
            print(f"\n{RED}Discover Ended !{RESET}")
            input(f"\n{MAGENTA}Press Enter to continue : {RESET}")
            banner_options() 

        elif num == '7' : #==> Website Information

            clear()
            domain = input(f" {RED} [7] {WHITE}Enter a Domain : {LIGHTGREEN}")
            print('\n')
            website_information.Fetch_info(domain,CYAN,RESET)
            input(f"\n{MAGENTA}Press Enter to continue : {RESET}")
            banner_options() 

        elif num == '8' : #==> Port Scanner

            clear()
            ip = input(f" {RED} [*] {WHITE}Enter an IP (default ==> localhost): {LIGHTGREEN}")
            rrange = input(f" {RED} [*] {WHITE}Enter a range of port [for example ==> 2-500] (default ==> all ==> 1-65535)  : {LIGHTGREEN}")
            port_scanner = portscanner.Portscanner(GREEN,RED,RESET,ip,rrange)
            while True :
                _license = input(f" {RED} [*] {WHITE} Which option [ all ports ==> 1 ] or [ open ports ==> 2 ] (default ==> all ==> 2): {LIGHTGREEN}")
                print('\n')
                
                if _license == '1' : 
                    print('\n')
                    portscanner.Portscanner.Scan(port_scanner)
                    break
                elif _license == '2' or _license == '' :
                    print('\n')
                    portscanner.Portscanner.Scan_o(port_scanner)
                    break
                else :
                    print(f"{RED} please correct the option ! {RESET}")
            input(f"\n{MAGENTA}Press Enter to continue : {RESET}")
            banner_options() 

        elif num == '9' : #==> HTTP Header

            clear()
            domain = input(f" {RED} [9] {WHITE}Enter a Domain : {LIGHTGREEN}")
            print('\n')
            res = http_header.http_header(domain)
            print(f"{RED} Results : \n{CYAN}")
            pprint(f"{res}")
            print(RESET)
            input(f"\n{MAGENTA}Press Enter to continue : {RESET}")
            banner_options() 

        elif num == '00' or num == '0' : #==> Exit
            for i in range(randint(1,4)) :
                clear()
                print(f'{YELLOW}closing progress .{RESET}')
                sleep(0.4)
                clear()
                print(f'{YELLOW}closing progress . .{RESET}')
                sleep(0.4)
                clear()
                print(f'{YELLOW}closing progress . . .{RESET}')
                sleep(0.4)
            clear()
            exit()
        
        else :
            raise ValueError(f'{RED}You must to enter number of list !{RESET}')
        
    except Exception as e:
        print(f"\n{RED}Error : {e}")
        input(f"\n{MAGENTA}Press Enter to continue : {RESET}")
        banner_options()
        continue

########################### END ###########################