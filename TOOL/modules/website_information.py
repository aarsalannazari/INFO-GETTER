# Imports:

from builtwith import builtwith

# Definition:

def Fetch_info(domain,CYAN,RESET) :

    url = f"http://{domain}"
    urls = f"https://{domain}"

    try:
        res = builtwith(urls)
    except :
        res = builtwith(url)
        
    for info in res :
        print(f"{CYAN} {info} ==> {res[info]}{RESET}")
    
########################### END ###########################