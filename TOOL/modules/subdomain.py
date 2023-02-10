# Imports:

from requests           import ConnectionError,Session
from requests.adapters  import HTTPAdapter
from urllib3.util.retry import Retry
from time               import sleep


# Definition:

def Discover_Subdomains(domain,CYAN,BLUE,RESET,RED,GREEN) :

    file = open("modules/subdomains.txt")
    session = Session()
    retry = Retry(connect=3,backoff_factor=0.5)
    adaptor = HTTPAdapter(max_retries=retry)
    session.mount("http://",adaptor)
    session.mount("https://",adaptor)

    content=file.read()

    subdomains = content.splitlines()
    discovered_Subdomains = []
    count = content.count('\n')+1
    i = 0

    for subdomain in subdomains :

        url = f"http://{subdomain}.{domain}"
        urls = f"https://{subdomain}.{domain}"
        
        try :
            session.get(urls)
            i += 1
            sleep(1)

        except ConnectionError :
            try :
                session.get(url)
                i += 1
                sleep(1)

            except ConnectionError :
                i += 1
                print(f"{RED}[{i}/{count}] {url} Not found!{RESET}")
            else :
                print(f"{GREEN}[{i}/{count}] {BLUE} Discovered Subdomain : {CYAN} {url}{RESET}" )
                discovered_Subdomains.append(url)

                with open(f"results/subdomains/{domain}.txt","w") as f :
                    for subdomain in discovered_Subdomains :
                        print(subdomain,file=f)     

        else :
            print(f"{GREEN}[{i}/{count}] {BLUE} Discovered Subdomain : {CYAN} {urls}{RESET}" )
            discovered_Subdomains.append(urls)

            with open(f"results/subdomains/{domain}.txt","w") as f :
                for subdomain1 in discovered_Subdomains :
                    print(subdomain1,file=f)

########################### END ###########################