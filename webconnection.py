import requests


wordpresslist = ["index.php","license.txt","readme.html","wp-activate.php","wp-blog-header.php","wp-comments-post.php","wp-config-sample.php","wp-cron.php","wp-links-opml.php","wp-load.php","wp-login.php","wp-mail.php","wp-settings.php","wp-signup.php","wp-trackback.php","xmlrpc.php"]
header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}


def Robots(url):
    response = requests.get(f"https://{url}/robots.txt",headers=header.update({"host":url}))
    if response.status_code == 200:
        elementos = []
        reais = []
        for c in response.text.replace('\r', '').split("\n"):
            elementos.append(c.split(':'))
        for elemento in elementos:
            if len(elemento) == 2:
                reais.append(elemento[1])
        return(reais)
    else:
        return False

def wordpress(url):
    
    response = requests.get(f"https://{url}/wp-admin.php",headers=header.update({"host":url}))
    if response.status_code == 200:
        diretorios_ok = []
        for diretorios in wordpresslist:
            response = requests.get(f"https://{url}/{diretorios}",headers=header.update({"host":url}))
            if response.status_code == 200:
                diretorios_ok.append(diretorios)
        return diretorios_ok
    else:
        return False


