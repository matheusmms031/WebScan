import argparse
import webconnection as wb
import visual as vs
import time


parser = argparse.ArgumentParser(description='Web Scan para identificar vulnerabilidades e versões de frameworks')
parser.add_argument('-url', action='store',required=True,dest='url',help='Url alvo')
parser.add_argument('-o', action='store',required=False,dest='output',help='Nome do arquivo para salvamento da sáida das linhas')
arguments = parser.parse_args()


diretorios = wb.Robots(arguments.url)
print("Starting WebScan 1.0 at ")
print(f"""
+------------------------+
|                        |
|        WebScan         |
|   \033[1;32mMatheus Magalhães\033[m    |
|                        |
+------------------------+

Alvo : \033[1;31m{arguments.url}\033[m

""")
print("""
    +-------------------+
    |                   |
    |    \033[1;31mDiretórios\033[m     |
    |                   |
    +-------------------+
    """)
if diretorios != False:
    saida = ""
    i = 0
    for diretorio in diretorios:
        i += 1
        saida += f'\t\033[1;34m {diretorio}\033[m\t'
        if i % 4 == 0:
            saida+= '\n'
    print(saida)

else:
    print("Não foi encontrado o ROBOTS.TXT")