import random
jugador1=[[0,0,0],[0,0,0]]
jugador2=[[0,0,0],[0,0,0]]
jugador3=[[0,0,0],[0,0,0]]
for c in range (3):
    jugador1[0][c]=input("apostar jugada jugador1 ")
    jugador2[0][c]=input("apostar jugada jugador2 ")
    jugador3[0][c]=input("apostar jugada jugador3 ")

listas=map(lambda n,m,f:[n,m,f],jugador1[0],jugador2[0],jugador3[0])
x=random.choice(listas[0])
y=random.choice(listas[1])
z=random.choice(listas[2])
ganadores=[filter(lambda n:n==x,listas[0]),filter(lambda n:n==y,listas[1]),filter(lambda n:n==z,listas[2])]
ganancia1=reduce(lambda n,m:n+m,listas[0])-x
ganancia2=reduce(lambda n,m:n+m,listas[1])-y
ganancia3=reduce(lambda n,m:n+m,listas[2])-z
for i in range (3):
    for d in range (3):
        if listas[i][d]==ganadores[i][0]:
            if d==0:
                if i==0:
                    jugador1[1][i]=ganancia1
                if i==1:
                    jugador1[1][i]=ganancia2
                if i==2:
                    jugador1[1][i]=ganancia3
            if d==1:
                if i==0:
                    jugador2[1][i]=ganancia1
                if i==1:
                    jugador2[1][i]=ganancia2
                if i==2:
                    jugador2[1][i]=ganancia3
            if d==2:
                if i==0:
                    jugador3[1][i]=ganancia1
                if i==1:
                    jugador3[1][i]=ganancia2
                if i==2:
                    jugador3[1][i]=ganancia3
print jugador1
print jugador2
print jugador3
promedio=(reduce(lambda n,m:n+m,listas[0])+reduce(lambda n,m:n+m,listas[1])+reduce(lambda n,m:n+m,listas[2]))/9
print promedio