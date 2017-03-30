def numeroFibonacci(numero):
   if numero==1 or numero==2:
       return 1
   else:
       return numeroFibonacci(numero-1)+numeroFibonacci(numero-2)
   
print(numeroFibonacci(9))