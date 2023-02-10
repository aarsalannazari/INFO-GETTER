# Imports:

from requests           import Session
from requests.adapters  import HTTPAdapter
from urllib3.util.retry import Retry

# Definition:

def http_header(domain) :

    session = Session()
    retry = Retry(connect=3,backoff_factor=0.5)
    adaptor = HTTPAdapter(max_retries=retry)
    session.mount("http://",adaptor)
    session.mount("https://",adaptor)
    urls = f"https://{domain}"
    url = f"http://{domain}"
    try:
        response = session.get(urls)
        # response = get(urls)
    except :
        response = session.get(url)
        # response = get(url)
    return response.headers

########################### END ###########################