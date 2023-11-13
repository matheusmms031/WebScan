import requests





class WebScan():
    
    def __init__(self,url) -> None:
        self.url = url
        self.directories = []
        self.text = """
        +-------------------+
        |                   |
        |    \033[1;31mDiretórios\033[m     |
        |                   |
        +-------------------+
        """
        self.wordpresslist = ["index.php","license.txt","readme.html","wp-activate.php","wp-blog-header.php","wp-comments-post.php","wp-config-sample.php","wp-cron.php","wp-links-opml.php","wp-load.php","wp-login.php","wp-mail.php","wp-settings.php","wp-signup.php","wp-trackback.php","xmlrpc.php"]
        self.header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

    
    def wordpressdirectories(self):
        response = requests.get(f"https://{self.url}/wp-admin.php",headers=self.header.update({"host":self.url}))
        if response.status_code == 200:
            for diretorios in self.wordpresslist:
                response = requests.get(f"https://{self.url}/{diretorios}",headers=self.header.update({"host":self.url}))
                if response.status_code == 200:
                    self.directories.append(diretorios)
            return True
        else:
            return False
        
    def robots(self):
        response = requests.get(f"https://{self.url}/robots.txt",headers=self.header.update({"host":self.url}))
        if response.status_code == 200:
            elementos = []
            reais = []
            for c in response.text.replace('\r', '').split("\n"):
                elementos.append(c.split(':'))
            for elemento in elementos:
                if len(elemento) == 2:
                    self.directories.append(elemento[1])
            return True
        else:
            return False


    def scan_directories(self):
        print(self.text)
        self.robots()
        self.wordpressdirectories()
        if self.directories != False:
            saida = ""
            i = 0
            for diretorio in self.directories:
                i += 1
                saida += f'\t\033[1;34m {diretorio}\033[m\t'
                if i % 4 == 0:
                    saida+= '\n'
            print(saida)