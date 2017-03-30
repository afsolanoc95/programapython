def mcd(numero1,numero2):
	if numero2 == 0:
		return numero1
	return mcd(numero2, numero1 % numero2)
print(mcd(30,20))