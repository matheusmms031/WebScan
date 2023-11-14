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
    
    
def wordpressplugins(url,soup:BeautifulSoup):
    
    plugins = {}
    for link in soup.find_all("link"):
        href = link["href"]
        if f"https://{url}/wp-content/plugins/" in href:
            href_older = href # href sem subtituição, usado exclusivamente para decorar os links relacionados ao plugin X
            href = href.replace(f"https://{url}/wp-content/plugins/","") # href sem a parte primordial
            locate = href.find('/') 
            name_plugin = href[:locate] # Subtituindo por completo tudo que não é o nome do plugin
            if name_plugin in plugins.keys():
                plugins[name_plugin]['links'].append(href_older)
            else:
                plugins[name_plugin] = {}
                plugins[name_plugin]['links'] = []
                plugins[name_plugin]['links'].append(href_older)
            