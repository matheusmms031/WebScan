import requests

from bs4 import BeautifulSoup 



def wordpressdirectories(url,header,wordpresslist):
    
    response = requests.get(f"https://{url}/wp-admin",headers=header)
    if response.status_code == 200:
        directories = []
        for diretorios in wordpresslist:
            response = requests.get(f"https://{url}/{diretorios}",headers=header)
            if response.status_code == 200:
                directories.append(diretorios)
        return [True , directories]
    else:
        return [False, None]
    
def wordpressplugins(soup:BeautifulSoup):
    for link in soup.find_all("link"):
        print(link.get("href"))