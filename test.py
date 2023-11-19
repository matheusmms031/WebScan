import requests

url = 'http://www.chromos.com.br/avaliacao'

# Realiza a solicitação GET com redirecionamentos automáticos
response = requests.get(url, allow_redirects=True,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"})

# Exibe o conteúdo da página final (após todos os redirecionamentos)
print('Conteúdo da Página:', response.text)