def invertirLista(lista):
    if len(lista) == 1:       
        return lista 
    else:
        return invertirLista(lista[1:]) + [lista[0]]

print (invertirLista([1,8,47,96,85,45]))