import time



p = int(input("donnez un entier naturel premier appelé p"))
q = int(input("donnez un autre entier naturel premier appelé q"))


def pgcd(a,b) :
    a,b=max(a, b),min(a, b)
    if (b==0) :
        return(a)
    else :
        r=a%b
        return(pgcd(b,r))



def trouver_e (p, q, phi) :
    e = max(p,q) + 1
    while pgcd(e, phi) != 1 :
        e = e + 1
    return(e)



def coefficients_de_bezout(a, b):
    if a == 0 and b == 0:
        return (0, 0)
    if b == 0:
        return(a/abs(a), 0)
    (u, v) = coefficients_de_bezout(b, a%b)
    return(v, (u - v*(a//b)))

def inverse_modulaire(x, y):
    (u, _) = coefficients_de_bezout(x, y)
    return(int(u%abs(y)))
   


phi = (p-1)*(q-1)
e = trouver_e (p, q, phi)
n = p * q 
d = inverse_modulaire(e, phi)

 
def public_key ():
    return(n, e)


def private_key () :
    return (n, d)


print('la clef publique est :', public_key ())
print('la clef privée est :', private_key ())


s = list(input("donnez une phrase à crypter"))

t1 = time.clock()

def string_en_chiffre(s):
    ld=[]
    ls=list(s)
    n=len(ls)
    for i in range(0,n):
        ld.append(ord(ls[i]))
    return(ld)


ld = string_en_chiffre(s)


def chiffrement (ld, e ,n) :
    m=len(ld)
    lc=[]
    for i in range(0,m):
        j=pow(ld[i],e,n)
        lc.append(j)
    return(lc)


print('le message crypté est :' , chiffrement(ld, e, n))

t2 = time.clock()

print("temps d'éxécution pour le cryptage (de la phrase seulement)", t2 - t1)



