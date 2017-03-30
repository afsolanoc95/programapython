def binDecimal(num,n):
    if int(num)==1:
        return int(pow(2,n))
    else:
        return  int(binDecimal(num[:-1],n+1))+(int(num[len(num)-1])*pow(2,n))
print (binDecimal("1011101",0))