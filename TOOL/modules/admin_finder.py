# Imports:

from urllib3.util.retry import Retry
from requests           import Session
from requests.adapters  import HTTPAdapter
from time               import sleep
from os                 import system

# Definition:

def Admin_finder (domain,time_sleep,CYAN,RED,GREEN,BLUE,RESET) :
    urls = f"https://{domain}"
    url = f"http://{domain}"

    session = Session()
    retry = Retry(connect=3,backoff_factor=0.5)
    adaptor = HTTPAdapter(max_retries=retry)
    session.mount("http://",adaptor)
    session.mount("https://",adaptor)

    pages = open("modules/admins.txt","r").read()
    i = 0
    count = pages.count("\n")+1
    pages = pages.splitlines()

    for page in pages :

        sleep(int(time_sleep))

        try:
            full_address = f"{urls}/{page}"
            status = session.get(full_address,timeout=15).status_code
        except :
            full_address = f"{url}/{page}"
            status = session.get(full_address,timeout=15).status_code

        i += 1


        if status != 406 :


            if status == 200 :

                system(f"touch results/admin_pages/{domain}.txt")
                with open(f"results/admin_pages/{domain}.txt") as file :
                    res = file.read().splitlines()
                    if full_address not in res :
                        f = open(f"results/admin_pages/{domain}.txt","a")
                        f.write(full_address+"\n")
                        f.close()
                
                print(f"{GREEN}[{i}/{count}] {CYAN}{full_address}{GREEN} is Exsists ===> {status}{RESET}")
                
            elif status == 429 :

                system(f"touch results/admin_pages/{domain}.txt")
                with open(f"results/admin_pages/{domain}.txt") as file :
                    res = file.read().splitlines()
                    if full_address not in res :
                        f = open(f"results/admin_pages/{domain}.txt","a")
                        f.write(full_address+"\n")
                        f.close()
                
                print(f"{GREEN}[{i}/{count}] {CYAN}{full_address}{GREEN} is Exsists {RED}But to many requests! {GREEN}===> {status}{RESET}")
                
            elif status == 403 :

                f = open(f"results/admin_pages/{domain}.txt","w")
                f.close()
                with open(f"results/admin_pages/{domain}.txt") as file :
                    res = file.read().splitlines()
                    if full_address not in res :
                        f = open(f"results/admin_pages/{domain}.txt","a")
                        f.write(full_address+" Forbidden"+"\n")
                        f.close()

                print(f"{GREEN}[{i}/{count}] {CYAN} {full_address}{RED} is Exsists But Forbidden ! ===> {status}{RESET}")

            else :

                print(f"{RED}[{i}/{count}] [{full_address}] is Not Exsists ! ===> {status}{RESET}")

        else :
            raise ConnectionRefusedError (f"{RED}[{domain}] Say : permision Denied !!{RESET}")