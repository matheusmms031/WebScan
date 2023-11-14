import requests
import argparse
from .utils.wpscan import wordpressdirectories, wordpressplugins
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
        A Classe necessita da url, porém o `output_name_file` é argumento
        que se não for colocado as respostas dos scans não serão salvas em
        arquivos .txt, apenas receberá as respostas como `WebScanTT object`. 
        
        [ Arguments ]
        
        - URL
        - OUTPUT_NAME_FILE
        
        """
        self.url = url
        self.directories = []
        self.robots = None
        self.output_name = output_name_file
        self.wp_response_scan = None
        self.robots_response_scan = None
        self.frameworks = {"wordpress":{"version":None,"exist":None,"plugins":[],"themes":[]}} # Serve para dizer os detalhes de cada framework, O WORDPRESS É BUSCA PADRÃO
        self.scans = {"wordpress":{"plugins":["https://{url}/wp-content/plugins/"],"themes":["https://{url}/wp-content/themes/"]}} # Serve para dizer as funções quais query's utilizar na tentativa de buscar plugins e temas 
        self.wordpresslist = ["index.php","license.txt","readme.html","wp-activate.php","wp-blog-header.php","wp-comments-post.php","wp-config-sample.php","wp-cron.php","wp-links-opml.php","wp-load.php","wp-login.php","wp-mail.php","wp-settings.php","wp-signup.php","wp-trackback.php","xmlrpc.php"]
        self.header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
        response = requests.get(f"https://{url}",headers=self.header.update({"host":url}))
        self.response = {"object":response, "text":response.text,"soup":BeautifulSoup(response.text,"html.parser")}

    def scan(self:object):
        """
        Função que serve apenas para realizar todas as scans do módulo `.utils`
        """
        
        # self.wp_response_scan = wordpressdirectories(self.url,self.header,self.wordpresslist)
        # self.robots_response_scan = robotsscan(self.url,self.header)
        wordpressplugins(self.url,self.response["soup"])
        # print(self.robots_response_scan)
        # print(self.wp_response_scan)
    
    # def versionframeworks(self): AINDA PRECISA SER ACABADO
    
