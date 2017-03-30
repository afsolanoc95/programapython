import random
import math           
def mazo(mano,cartas,randomCartas,totalcartas):
    if(len(mano)<=40):
        if(len(cartas)>0 and totalcartas>1):
            mano.append(cartas[randomCartas])
            cartas.pop(randomCartas)
            mazo(mano,cartas,math.floor(random.randrange(0,totalcartas-1)),totalcartas-1)
    return mano
                                    
def jugador(mazo, mano):
    print("jugador", mano)    
    if(len(mano)<=1):
        
        jugador(mazo[2:],mano+[mazo[0]]+[mazo[1]])
    else:
        if(croupier(mano)<22):            
            if(croupier(mano)==21):
                print("victoria")                
            elif(input("otra carta?  ")==('s')):            
                print(len(mano))
                jugador(mazo[1:],mano+[mazo[0]])                
            else:
                print("jugador ", mano)
                print(croupier(mano))
        else:
            print(croupier(mano))
            print("derrota")
            
def croupier(juego):    
    if(juego==[]):
        return 0
    else:
        return juego[0] + croupier(juego[1:])
a=1

print ("bienvenido al juego de 21")+(jugador(mazo([],[a,a,a,a,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10],math.floor(random.randrange(0,40)),40),[]))

