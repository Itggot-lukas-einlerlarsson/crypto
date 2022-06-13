# anteckningar från föreläsning:
# välj primtal p o q
# n = p*q
# g E Z_n^2 -- hitta ett bra g som inte har ord(phi), gärna lägre
# k = ord_n^2(g)
# lambd = lcm(p-1,q-1)
# my = L(g^lambd mod n^2)^-1 mod n
# där L = floor((x-1)/n)
# privat nyckel: (lambd, my)
# publik nyckel: (g, n)

import random
import math

def main():
    print("pallier test:")
    text = "tjenixen"
    p = 10000001969 #blocklängd: p-2?
    q = 10000000799
    m = heltalsblock(text)
    print("m talet:", m)
    n, g, k, lambd, my = pallier(p, q) # private_key, public_key
    print("n:", n, "\ng:", g, "\nk:", k, "\nlambda:", lambd, "\nmy", my )
    c = encrypt(m, g, n)
    print("c tal", c)
    m = decrypt(c, lambd, my, n)
    print("m talet:", m)
    text = heltalsblock(m, "v->s")
    print("text:", text)


# används för att gå från text till tal eller tvärtom
def heltalsblock(s, mode = "s->v"): #s = string, v = value
    if mode == "v->s":
        x = []
        q = s
        while q > 0:
            r = q % 256
            q = (q-r)//256
            x.insert(0,r)
        text = ""
        for value in x:
            text += chr(value)
        return text
    else:
        lst = []
        for letter in s:
            lst.append(ord(letter))
        exponent = len(lst)-1
        number = 0
        for value in lst:
            number += 256**exponent * value
            exponent -= 1
        return number

# bestämmer blocklängden
def blocklength(n):
    return math.floor(math.log(n, 256))

# pallier kryptering
def encrypt(m, g, n, x = 0):
    if x == 0:
        while math.gcd(x,n) != 1:
            x = random.randint(2, n)
    c =pow(pow(g, m, n**2)* pow(x, n, n**2), 1, n**2)
    return c

# pallier dekryptering
def decrypt(c, lambd, my, n):
    m = pow(L(pow(c, lambd, n**2), n)*my,1, n)
    return m

# palliers L-funktion
def L(x, n):
    return (x-1)//n

# generering av nycklar
def pallier(p, q):
    n = p * q
    g = n
    while math.gcd(g, n**2) != 1:
        g = random.randint(3, n)
    k = (p**2-p)*(q**2-q) #phi atm not the least but works.
    lambd = math.lcm(p-1,q-1)
    my = pow(L(pow(g, lambd, n**2), n), -1, n)
    private_key = [lambd, my, n]
    public_key = [g, n]
    return n, g, k, lambd, my#private_key, public_key



# --- UPPG 2 ----
def uppg_2():
    (g, n) = (449351979529, 1348055938589)
    (lambd, my) = (337013404056, 855990458218)
    klartext = "Shine On You Crazy Diamond"
    c = [273556253247361873874628, 1154100605855994198119516]
    Th = [372, 369, 381, 395, 365, 378, 402, 373, 374, 380, 377] #temperaturer*10
    uppg_a(n)
    uppg_b(klartext, g, n, lambd, my)
    uppg_c(c, g, n, lambd, my)
    uppg_d(Th, g, n, lambd, my)




def uppg_a(n):
    print("\n\nUppgift a):")
    print("Blocklength:", blocklength(n)) #n?

def uppg_b(text, g, n, lambd, my):
    print("\nUppgift b):")
    bl = blocklength(n) #9
    m = []
    for i in range(0, len(text), bl):
        m.append(heltalsblock(text[i:i+bl]))
    x = 2022
    c = []
    for value in m:
        c.append(encrypt(value, g, n, x))
        x += 1
    str = ""
    for value in c:
        str += heltalsblock(decrypt(value, lambd, my, n), "v->s")
    print("klartext i block:", m)
    print("klartext krypterad:", c)
    print("åter dekrypterad:", str)

def uppg_c(c, g, n, lambd, my):
    print("\nUppgift c):")
    str = ""
    for value in c:
        str += heltalsblock(decrypt(value, lambd, my, n), "v->s")
    print("dekrypterad text:", str)

def uppg_d(Th, g, n, lambd, my):
    print("\nUppgift d):")
    #forskare vill: för alla temperaturer i T ta fram dess medelvärde, får inte veta krypterade värden:
    sum = 0
    sample_length = len(Th)
    for value in Th:
        sum += value
    medelvärde = sum/sample_length
    print("okrypterad summa:", sum)
    print("okrypterat medelvärde:", medelvärde)
    c = []
    for value in Th:
        c.append(encrypt(value, g, n))
    C = 1
    for value in c:
        C *= value % n**2 # multiplicera ihop alla krypterade temperaturer
    krypterad_summa = decrypt(C, lambd, my, n) #krypterade produktern
    print("krypterad summa:", krypterad_summa)
    krypterat_medelvärde = (krypterad_summa/sample_length) % n
    print("Medelvärde framtaget ur krypterad information:", krypterat_medelvärde)

main()
uppg_2()
