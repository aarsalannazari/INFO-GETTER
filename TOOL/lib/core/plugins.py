# Imports:

from requests           import Session
from requests.adapters  import HTTPAdapter
from urllib3.util.retry import Retry
from time               import sleep

# Definition:

def Discover_Plugins(domain,CYAN,BLUE,RESET,RED,GREEN) :

    file = open("TOOL/lib/plugins.txt")
    session = Session()
    retry = Retry(connect=3,backoff_factor=0.5)
    adaptor = HTTPAdapter(max_retries=retry)
    session.mount("http://",adaptor)
    session.mount("https://",adaptor)
    content=file.read()
    plugins = content.splitlines()
    count = content.count('\n')+1
    i = 0
    discovered_plugins = []
    
    sites = f"https://{domain}/wp-content/plugins/"
    site = f"http://{domain}/wp-content/plugins/"
    # try:

    response1 = session.get(sites)

    if response1.status_code == 200 or response1.status_code == 403 :

        for plugin in plugins :

            url = f"{sites}{plugin}"
            response2 = session.get(url)
            i += 1
            sleep(1)

            if response2.status_code == 200 or response2.status_code == 403 :

                print(f"{GREEN}[{i}/{count}] {BLUE} Discovered Plugin : {CYAN} {plugin}{RESET}" )
                discovered_plugins.append(url)
                
            else :

                print(f"{RED}[{i}/{count}] Not Found Plugin : {plugin}{RESET}" )

        with open(f"results/plugins/{domain}.txt","w") as f :
            for plugin in discovered_plugins :
                print(plugin,file=f)

    else :
        print(f"{RED} This site is Not make with WordPress CMS !{RESET}")
    # except ConnectionError :

    #     response1 = get(site)

    #     if response1.status_code == 200 or response1.status_code == 403 :

    #         for plugin in plugins :
    #             url = f"{site}{plugin}"
    #             response2 = get(url)
    #             i += 1
    #             sleep(1)

    #             if response2.status_code == 200 or response2.status_code == 403 :

    #                 print(f"{GREEN}[{i}/{count}] {BLUE} Discovered Plugin : {CYAN} {plugin}{RESET}" )
    #                 discovered_plugins.append(url)
                
    #             else :

    #                 print(f"{RED}[{i}/{count}] Not Found Plugin : {plugin}{RESET}" )

    #         with open(f"results/plugins/{domain}.txt","w") as f :
    #             for plugin in discovered_plugins :
    #                 print(plugin,file=f)

    # else :
    #     print(f"{RED} This site is Not make with WordPress CMS !{RESET}")

########################### END ###########################