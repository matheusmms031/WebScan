import requests





class WebScan():
    """
WebScanTT
~~~~~~~~~~~~~~~

Biblioteca de Python para scan de sites WEB

:copyright: (c) 2023 by Matheus Magalhães.
:license: Apache 2.0, see LICENSE for more details.
    """
    
    
    def __init__(self,url:str,output_name_file:str) -> None:
        """ 
        É necessário colocar a url e o output_name_file pois
        é parte principal de tudo...
        
        [Arguments]
        
        - URL
        - OUTPUT_NAME_FILE
        
        """
        self.url = url
        self.directories = []
        self.robots = None
        self.output_name = output_name_file
        self.frameworks = {"wordpress":{"version":None,"exist":None}} # Ainda precisa ser acabado
        self.pluginswordpress = {} # Ainda precisa ser acabado
        self.wordpresslist = ["index.php","license.txt","readme.html","wp-activate.php","wp-blog-header.php","wp-comments-post.php","wp-config-sample.php","wp-cron.php","wp-links-opml.php","wp-load.php","wp-login.php","wp-mail.php","wp-settings.php","wp-signup.php","wp-trackback.php","xmlrpc.php"]
        self.header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
        self.response = requests.get(f"https://{self.url}",headers=self.header.update({"host":self.url}))
        
    def wordpressdirectories(self):
        
        response = requests.get(f"https://{self.url}/wp-admin",headers=self.header.update({"host":self.url}))
        if response.status_code == 200:
            for diretorios in self.wordpresslist:
                response = requests.get(f"https://{self.url}/{diretorios}",headers=self.header.update({"host":self.url}))
                if response.status_code == 200:
                    self.directories.append(diretorios)
            return True
        else:
            return False
        
    def robotsscan(self):
        
        response = requests.get(f"https://{self.url}/robots.txt",headers=self.header.update({"host":self.url}))
        if response.status_code == 200:
            elements = []
            for c in response.text.replace('\r', '').split("\n"):
                elements.append(c.split(':'))
            for element in elements:
                if len(element) == 2:
                    self.directories.append(element[1])
            return True
        else:
            return False


    def scan(self):
        """
        Função que serve apenas para realizar todas as scans da classe `WebScan`
        """
        
        self.robots = self.robotsscan()
        self.wordpressdirectories()
        # print(self.directories)
    
    # def versionframeworks(self): AINDA PRECISA SER ACABADO
        