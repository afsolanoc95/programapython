class nodoArbol():
    def __init__(self, valor):
        self.valor=valor
        self.hijos=[]
        
def busqueda(arbol, letra):
    if arbol.valor == letra:
        return arbol
    return busqueda_hijos(arbol.hijos,letra)

def busqueda_hijos(hijos,valor):
    if hijos==[]:
        return False
    return busqueda(hijos[0],valor) or busqueda_hijos(hijos[1:],valor)
    
def busquedaAdentro(arbol):
    imprimir(arbol.valor)
    for hijo in arbol.hijos:
        busquedaAdentro (hijo)
        
def agregarLetra(letra, letraPadre, arbol ):
    busqueda(arbol, letraPadre).hijos.append(nodoArbol(letra)); 
    
def escogerLetra(valor):
    if valor==arbol.hijos[0].valor or reducir(valor)==arbol.hijos[0].valor:
        agregarLetra(valor,a[1],arbol)
    if valor==arbol.hijos[1].valor or reducir(valor)==arbol.hijos[1].valor:
        agregarLetra(valor,a[2],arbol)
     
def reducir(valor):
    if valor==arbol.hijos[0].valor or valor==arbol.hijos[1].valor:
        return valor
    else:
        return reducir(valor[:len(valor)-1])
   
def imprimir(valor):
    print valor
a=['a','ab','ac','abel','abeta','abalia','acacia']

arbol = nodoArbol(a[0])
print(arbol.hijos)
agregarLetra(a[1],a[0],arbol)
agregarLetra(a[2],a[0],arbol)
escogerLetra(a[6])
escogerLetra(a[4])
escogerLetra(a[3])
escogerLetra(a[5])
busquedaAdentro(arbol)