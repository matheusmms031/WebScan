import requests

from bs4 import BeautifulSoup 



def wordpressdirectories(url,header,wordpresslist):
    """
    The function `wordpressdirectories` checks if a WordPress site is accessible and returns a list of
    directories that exist on the site.
    
    Args:
      url: The URL of the WordPress website you want to check.
      header: The `header` parameter is a dictionary that contains the headers to be included in the
    HTTP request. Headers are used to provide additional information to the server, such as
    authentication credentials or user agent information.
      wordpresslist: The `wordpresslist` parameter is a list of directories that you want to check for
    existence on a WordPress website. These directories can include common WordPress directories such as
    `wp-content`, `wp-includes`, `wp-admin`, etc.
    
    Returns:
      a list with two elements. The first element is a boolean value indicating whether the WordPress
    admin page was successfully accessed (True) or not (False). The second element is a list of
    directories that were successfully accessed on the WordPress site.
    """
    
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
    """
    The function `wordpressplugins` extracts the names and links of WordPress plugins from a given URL
    and BeautifulSoup object.
    
    Args:
      url: The `url` parameter is a string that represents the URL of the website you want to scrape for
    WordPress plugins.
      soup (BeautifulSoup): The parameter `soup` is of type `BeautifulSoup`, which is a Python library
    used for web scraping. It is used to parse the HTML content of a webpage and extract information
    from it. In this case, it is used to parse the HTML content of a webpage and find all the `<link
    """
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
            