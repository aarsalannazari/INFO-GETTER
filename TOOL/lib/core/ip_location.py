# Imports:

from colorama import Fore
from pprint   import pprint
from ipapi    import location

# Colors:

GREEN,LIGHTGREEN,BLUE,MAGENTA,RED=Fore.GREEN,Fore.LIGHTGREEN_EX,Fore.BLUE,Fore.MAGENTA,Fore.RED
YELLOW,CYAN,LIGHTCYAN,WHITE,RESET=Fore.YELLOW,Fore.CYAN,Fore.LIGHTCYAN_EX,Fore.WHITE,Fore.RESET

# Definition:

def info(ip) :
    result = location(ip)
    print(f'{CYAN}')
    pprint(result)
    print({RESET})

if __name__ == '__main__' :
    info('')

########################### END ###########################