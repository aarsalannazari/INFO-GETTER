#Import Librarys:

from colorama import Fore,Style

#Colors:

STYLE = Style.BRIGHT
GREEN,LIGHTGREEN,BLUE,MAGENTA,RED=Fore.GREEN,Fore.LIGHTGREEN_EX,Fore.BLUE,Fore.MAGENTA,Fore.RED
YELLOW,CYAN,LIGHTCYAN,WHITE,RESET=Fore.YELLOW,Fore.CYAN,Fore.LIGHTCYAN_EX,Fore.WHITE,Fore.RESET

# Definition:

class Tools :

    def banner(self=None):
        print(f"""{STYLE}{BLUE}
 __  .__   __.  _______   ______        _______  _______ .___________.___________. _______ .______      
|  | |  \ |  | |   ____| /  __  \      /  _____||   ____||           |           ||   ____||   _  \    
|  | |   \|  | |  |__   |  |  |  |    |  |  __  |  |__   `---|  |----`---|  |----`|  |__   |  |_)  |   
|  | |  . `  | |   __|  |  |  |  |    |  | |_ | |   __|      |  |        |  |     |   __|  |      /    
|  | |  |\   | |  |     |  `--'  |    |  |__| | |  |____     |  |        |  |     |  |____ |  |\  \    
|__| |__| \__| |__|      \______/      \______| |_______|    |__|        |__|     |_______||__| \__\                                                                                                 
                        {CYAN}    
                                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                ~  Coded By  : Amir Arsalan Nazari         ~
                                ~  WebSite   : (None)                      ~
                                ~  Telegram  : (None)                      ~
                                ~  Instagram : aarsalannazari              ~
                                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        {RESET}""")

    def options(self=None):
        print(f"""{YELLOW}
    OPTIONS:
    {RED}
    [ 1 ]  -  Whois
    [ 2 ]  -  Dns Checker
    [ 3 ]  -  Ip Loacation
    [ 4 ]  -  Sub Domains
    [ 5 ]  -  WordPress Plugins
    [ 6 ]  -  Admin Page Finder
    [ 7 ]  -  WebSite Information
    [ 8 ]  -  IP Scanner
    [ 9 ]  -  Port Scanner
    [ 10 ] -  Show HTTP Header
      00   -  Exit 
    {RESET}  
        """)

########################### END ###########################
