def decimalBinario(num):
    if num == 0:
        return ""
    else:
        return decimalBinario(num//2)+str(num % 2) 
print(decimalBinario(8))