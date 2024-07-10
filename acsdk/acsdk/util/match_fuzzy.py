from urllib.parse import urljoin, urlparse

def match_fuzzy(url1, url2):
    url1 = url1 if url1.endswith("/") else url1 + "/"
    url2 = url2 if url2.endswith("/") else url2 + "/"

    url1 = urlparse(url1) if urlparse(url1).hostname != None else urlparse("//" + url1)
    url2 = urlparse(url2) if urlparse(url2).hostname != None else urlparse("//" + url2)

    if (urljoin("//" + url1.hostname, url1.path) == urljoin("//" + url2.hostname, url2.path)):
        return True
    
    return False
