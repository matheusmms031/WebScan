import requests
import argparse
from .utils.wpscan import wordpressdirectories, wordpressplugins, wordpressthemes
from .utils.robots import robotsscan
from bs4 import BeautifulSoup

class WebScanTT():
    """
WebScanTT
~~~~~~~~~~~~~~~

Biblioteca de Python para scan de sites WEB

:copyright: (c) 2023 by Matheus Magalhães.
:license: Apache 2.0, see LICENSE for more details.
    """
    
    
    def __init__(self,url:str,output_name_file:str | None = None) -> None:
        """
        This is the initialization function for a class that scans a given URL for information about the
        WordPress framework and other details.
        
        Args:
          url (str): The URL of the website you want to scan. It should be a string.
          output_name_file (str | None): The `output_name_file` parameter is a string that represents
        the name of the output file where the results of the code will be saved. It is an optional
        parameter and can be set to `None` if no output file name is specified.
        """
        
        self.url = url
        self.directories = []
        self.robots = None
        self.output_name = output_name_file
        self.wp_response_scan = None
        self.robots_response_scan = None
        self.frameworks = {"wordpress":{"version":None,"exist":None,"plugins":None,"themes":None}} # Serve para dizer os detalhes de cada framework, O WORDPRESS É BUSCA PADRÃO
        self.wordpresslist = ["index.php","license.txt","readme.html","wp-activate.php","wp-blog-header.php","wp-comments-post.php","wp-config-sample.php","wp-cron.php","wp-links-opml.php","wp-load.php","wp-login.php","wp-mail.php","wp-settings.php","wp-signup.php","wp-trackback.php","xmlrpc.php"]
        self.header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
        response = requests.get(f"https://{url}",headers=self.header.update({"host":url}))
        self.response = {"object":response, "text":response.text,"soup":BeautifulSoup(response.text,"html.parser")}

    def scan(self:object):
        """
        The function "scan" calls the "wordpressplugins" function with the given URL and response soup.
        
        Args:
          self (object): The "self" parameter refers to the instance of the class that the method
        belongs to. It is used to access the attributes and methods of the class.
        """
        
        self.wp_response_scan = wordpressdirectories(self.url,self.header,self.wordpresslist)
        self.robots_response_scan = robotsscan(self.url,self.header)
        self.robots = self.robots_response_scan[0] # Atualiza o robots
        self.directories += self.wp_response_scan[1] # Adiciona na lista de diretorios o que foi achado no scan
        self.directories += self.robots_response_scan[1]
        self.frameworks['wordpress']['exist'] = self.wp_response_scan[0] # Seta se wordpress realmente existe no site
        self.robots_response_scan = robotsscan(self.url,self.header) 
        self.frameworks['wordpress']['plugins'] = wordpressplugins(self.url,self.response["soup"])
        self.frameworks['wordpress']['themes'] = wordpressthemes(self.url, self.response["soup"])
    
    # def versionframeworks(self): AINDA PRECISA SER ACABADO
    
