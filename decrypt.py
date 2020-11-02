

def dechiffrement(lc, n, d):
    m = len(lc)
    ld = []
    for i in range (0,m):
        j = pow(lc[i],d,n)
        ld.append(j)
    return(ld)



def message_decrypter(lc, n, d):
    ls=[]
    ld = dechiffrement(lc, n, d)
    m = len(ld)
    for i in range(0,m):
        ls.append(chr(ld[i]))
    return("".join(ls))


