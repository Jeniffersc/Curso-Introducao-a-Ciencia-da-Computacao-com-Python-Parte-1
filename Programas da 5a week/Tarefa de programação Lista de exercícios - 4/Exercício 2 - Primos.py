def éPrimo (k):
    i=3
    if k==3:
        primo = 3
        return primo
    else:
        while i<=k:
            if i%2!=0 and i%3!=0:
                primo = i
                i = i+1
            else:
                n_primo = i
                i = i+1
        return primo

def maior_primo (k):
    return éPrimo(k)
