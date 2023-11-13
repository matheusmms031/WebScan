import argparse
import webconnection as wb
import visual as vs
import scanlib as sc
import time


parser = argparse.ArgumentParser(description='Web Scan para identificar vulnerabilidades e versões de frameworks',prog='TeteScan')
parser.add_argument('-url', action='store',required=True,dest='url',help='Url alvo')
parser.add_argument('-o', action='store',required=False, dest='output',help='Nome do arquivo para salvamento da sáida das linhas')
arguments = parser.parse_args()

webscan = sc.WebScan(arguments.url)

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


webscan.scan_directories()