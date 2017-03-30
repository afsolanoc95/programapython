import random
import sys



def Cartas():
    return 4*["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    
    
def Usuario(usuario,baraja):
    
    usuario.append( baraja.pop(0))
    usuario.append( baraja.pop(0))
    print("Tu mano es:")
    print (usuario)
    return usuario

def Maquina(maquina, baraja):
    maquina.append(baraja.pop(0))
    maquina.append(baraja.pop(0))
    return maquina


def JQK (mano,numero):   
    mano.append(numero)
    if mano[0]!=0:
       if mano[0]== "J" or mano[0]=="Q" or mano[0]== "K":
            mano.pop(0)
            return JQK(mano, 10)
       elif mano[0]== "A":
             if(mano[0]=="A" and mano[1]=="A"):
                 mano.pop(0)
                 JQK(mano,1)
             mano.pop(0)
             return JQK(mano, 11)  
       else:
          return JQK(mano, mano.pop(0))
    else:
        mano.pop(0)
        return mano

def comprobarA (mano,numero):
    mano.append(numero)  
    if(mano[0]!=0):
        if mano[0]==11 or mano[0]=="A":
            mano.pop(0)
            return comprobarA(mano,1)
        else:
            return comprobarA(mano,mano.pop(0))    
    else:
        mano.pop(0)
        return mano 

def RobarCarta(suma,baraja):
    if sumaCartas(suma,0)<=21:
        print ("\nLa carta repartida es: ")
        print baraja[0]
        suma.append(baraja.pop(0))
        print ("La nueva mano es: ")
        print suma
        JQK(suma,0)
        
def sumaCartas(lista,numero):
        lista.append(numero)
        if lista[0]!=0 : 
           return lista[0]+sumaCartas(lista,lista.pop(0))
        else:
            lista.pop(0) 
            return 0
        


def compararSumas(maquina,mano,Quedarse,baraja):
    print "La suma de tu mano:"
    print (sumaCartas(mano,0))
    
    if(sumaCartas(mano,0)<=21 and sumaCartas(maquina,0)<=21):
        if(Quedarse!=True and input("\n1. Pedir carta\n2. Plantarse\n\nIngrese la opcion:")==1 ):
            RobarCarta(mano,baraja)
            compararSumas(maquina,mano,False,baraja)
        elif (sumaCartas(mano,0)>sumaCartas(maquina,0) and sumaCartas(maquina,0)<21):
            RobarCarta(maquina,baraja)
            compararSumas(maquina,mano,True,baraja)
        elif (sumaCartas(mano,0)<sumaCartas(maquina,0) or sumaCartas(mano,0)==sumaCartas(maquina,0)):
            print("La mano de la maquina es:  ")
            print (maquina)
            print "La suma de la mano del pc es:"
            print (sumaCartas(maquina,0))
            print("Perdiste D:")                   
    else:
        if (sumaCartas(maquina,0)<21):
            if (sumaCartas(comprobarA(mano,0),0)<21):
              compararSumas(maquina,mano,False,baraja)
            else:
                print("La mano de la maquina es:  ")
                print (maquina)
                print "La suma de la mano del pc es:"
                print (sumaCartas(maquina,0))
                print("Perdiste D:")
        else:    
            if(sumaCartas(comprobarA(maquina,0),0)<21):
                compararSumas(maquina,mano,True,baraja)
            else:
                print("La mano de la maquina es:  ")
                print (maquina)
                print "La suma de la mano del pc es:"
                print (sumaCartas(maquina,0))
                print ("GANASTE :D")


def main(baraja):
    random.shuffle(baraja)
    compararSumas(JQK(Maquina([],baraja),0),JQK(Usuario([],baraja),0),False,baraja)
    sys.exit(0)
    main(baraja)
    
main(Cartas())

