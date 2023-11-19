import argparse
from src import WebScanTT
import time
from writefile import writefilescans 


parser = argparse.ArgumentParser(description='Web Scan para identificar vulnerabilidades e versões de frameworks',prog='TeteScan')
parser.add_argument('-url', action='store',required=True,dest='url',help='Url alvo')
parser.add_argument('-o', action='store',required=False, dest='output',help='Nome do arquivo para salvamento da sáida das linhas')
arguments = parser.parse_args()

webscan = WebScanTT(arguments.url, arguments.output)
print(f"""
----------------------------------------------------------------------------     
      
 \033[34m######   ######   ######   ######    #####    ####     ####    ##  ##
   ##     ##         ##     ##       ##       ##  ##   ##  ##   ### ##
   ##     #####      ##     #####     ####    ##       ######   ######
   ##     ##         ##     ##           ##   ##  ##   ##  ##   ## ###
   ##     ######     ##     ######   #####     ####    ##  ##   ##  ##\033[m
   
                    Created by: \033[33mMatheus Magalhães M.S\033[m
                            Version: 1.0.0

-----------------------------------------------------------------------------

Alvo : \033[1;31m{arguments.url}\033[m
""")
print("\033[31m This may take a while \033[m")

webscan.scan()

writefilescans(webscan.url, webscan.frameworks, webscan.directories, "teste")