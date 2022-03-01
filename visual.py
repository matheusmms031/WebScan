

def ViewList(lista,colunas):
    saida = "\033[1;31m"
    i = 0
    for c in lista:
        i += 1
        if i % colunas == 0:
            saida += f"{c}\t\n"
        else:
            saida += f"{c}\t"
    return saida