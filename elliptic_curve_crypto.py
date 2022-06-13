# från lektionsanteckningar:
# låt p vara ett primtal större än 3
# låt A och B vara element i Z_p sådana att 4A^3+27B !≡ 0 (mod p) U {O}
# Elliptisk kurva över Z_p E {(x, y) ∈ Z^2_p : y^2 ≡ x^3 + Ax + B (mod p)}, O ≡ oändlighetspunkten ≡ 0, inte (x, y)
# EX:
# P ≡ 23  -> y^2≡x^3 + 2x + 14 (mod 23)
# # NOTE: 4A^3 + 27B^2 ≡ 11 ≡! 0 (mod 23)
# # NOTE: om x ≡ 0 -> y^2≡ 14 (mod 23) som saknar lösning -> ingen kordinat där x ≡ 0
# om x ≡ 2 -> y^ ≡ 2^3 + 2 * 2 + 14 ≡ 3 (mod 23)
# -> y_1= 7 o y_2 = 16
# -> punkterna (2, 7) och  (2, 16) ∈ E där E är en punkt i det elliptiska systemet
# studerar vi alla 23 värden (0..23) -> E = {O, (2, 7), (2, 16), (3, 1), (3, 22), (6, 9), (6, 14), (7, 7), (7, 16), (8, 6), (8, 17), (9, 5), (9, 18), (12, 8), (12, 15), (13, 11), (13, 12), (14, 7), (14, 16), (16, 5), (16, 18), (17, 4), (17, 19), (20, 2), (20, 21), (21, 5), (21, 18)}
# -> |E| = 27, antalet element är alltså 27 i E
# -> alltså desto högre primatal p -> desto mer punkter i systemet

# låt punkten P vara ett element i systemet E, där P != O -> P= (x, y)
# -> speglingen av P blir då P' = -P = (x, - y) ≡ (x, p-y) (mod p), ex: P + Q' = P - Q
# associativitet, kommutativ, identitet och invers: addition

import random #
import math
from sympy import legendre_symbol

class Point():
    def __init__(self, x, y, z = 1):
        self.x = x
        self.y = y
        self.z = z
    def print_P(self):
        s = "x:" + str(self.x) + "    y:" + str(self.y) + "    z:" + str(self.z)
        return s

def heltalsblock(s, mode = "s->v"): #s = string, v = value
    if mode == "v->s":
        x = []
        q = s
        r = 1
        while q > 0:
            r = q %256
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

def verify_curve(p, A, B):
    return (4*A**3 + 27*B**2) % p != 0

def inE(P, E): #E = [p, A, B]
    p = E[0]
    A = E[1]
    B = E[2]
    if P.y**2 % p == (P.x**3 + A*P.x+ B) % p:
        return True
    else:
        return False

def addE(P, Q, E): #elliptic_sum
    p = E[0]
    A = E[1]
    if P.x == 0 and P.y == 1 and P.z == 0: #Point(0, 1, 0):
        S = Q
    elif Q.x == 0 and Q.y == 1 and Q.z == 0: #Point(0, 1, 0):#
        S = P
    elif P.x == Q.x and P.y == p-Q.y and P.z == Q.z: # -Q ska vara -P?
        S = Point(0, 1, 0)
    else:
        if P.x == Q.x and P.y == Q.y and P.z == Q.z or P.x == Q.x or P.y == Q.y:
            lambd =((3* P.x**2+A) * pow(2*P.y, -1, p)) % p #pow ska vara power_mod
        else:
            lambd =((Q.y - P.y) * pow(Q.x-P.x, -1, p)) % p #pow ska vara power_mod
        x_3 = (lambd**2 - P.x - Q.x) % p
        y_3 = (lambd * (P.x - x_3) - P.y) % p
        S = Point(x_3, y_3)
    return S

# from "An introduction to Mathematical Cyrptography, Springer", sida 313
def potE(n, P, E): #E = [p, A, B]
    p = E[0]
    A = E[1]
    B = E[2]
    Q = P #Point(P.x, P.y)
    R = Point(0, 1, 0)
    while n > 0:
        if n % 2 == 1:
            R = addE(R, Q, E)#elliptic_sum(R, Q, A, p)# addE(R, Q, E)
        Q = addE(Q, Q, E) # tror att dett fungerar.
        n = n//2
    return R

def generate_factors(p): # kan ta långt tid.
    A = 0
    B = 0
    while (4*A**3 + 27*B**2) % p == 0 :
        A = random.randint(1, p)
        B = random.randint(1, p)
    return A, B


def generate_point(A, B, p):
    y = 3
    x = 2
    while y**2 % p != (x**3 + A*x+ B) % p:
        y = random.randint(1, p)
        x = random.randint(1, p)
    return Point(x, y, 1)

def negE(P, E): #E = [p, A, B]
    p = E[0]
    return Point(P.x, p - P.y)

def koblitz(m, kappa, E): #E = [p, A, B]
    p = E[0]
    A = E[1]
    B = E[2]
    P = Point(0, 1, 0)
    for j in range(1, kappa) :
        x = m * kappa + j
        a = (x^3 + A * x + B) % p
        if legendre_symbol(a, p) == 1 : #kronecker(a, p)
            y = math.ceil(math.sqrt(a % p)) #lift
            M = Point(x, y, 1)
            break
    return M


#koblitz method
def code_text(M, kappa, E):
    p = E[0]
    A = E[1]
    B = E[2]
    for j in range(2, kappa):
        y = j**2
        x = M*kappa+j
        if y**2 % p == (x^3 + A*x +B) % p:
            break
    return Point(x, y, 1)

def main():
    print("\n\nUppgift 3!")
    print("_" * 10)
    p = 1299689
    A = 790384
    B = 410135
    P = Point(779301, 1245564, 1)
    Q = Point(70859, 130938, 1)
    o = 1300731     # ordningen för Pcd Do  n
    OP = Point(0, 1, 0)  # oändlighetspunkten
    uppg_a(p, A, B)
    uppg_b(p, A, B)
    uppg_c(p, A, B, P, Q)
    uppg_d_e(p, A, B, P, Q)
    uppg_f_g(p, A, B, P, Q)
    uppg_h(p, A, B, P, Q, o)
    uppg_i(p, A, B, P, Q)
    yojimbo_ps = uppg_j(p, A, B, P, Q)
    uppg_k(p, A, B, P, Q, yojimbo_ps)
    uppg_l(p, A, B, P, Q, yojimbo_ps)

    #lenstras
    print("\n\nscuffed Lenstras method, n = 26754:")
    d = lenstras(26754, A)
    print(d)




def uppg_a(p, A, B):
    print("\nUppgift a)")
    print("Elliptic curve:", verify_curve(p, A, B))

def uppg_b(p, A, B):
    print("\nUppgift b)")
    # test_P = generate_point(A, B, p) #can take a long time
    test_P = Point(834730, 257765)
    print("Test point: ", end = "")
    print(test_P.print_P())
    E = [p, A, B]
    print("Point is on curve:", inE(test_P, E))

def uppg_c(p, A, B, P, Q):
    print("\nUppgift c)")
    E = [p, A, B]
    print("Point is on curve, A:", inE(P, E))
    print("Point is on curve, B:", inE(Q, E))
    print("Point is on curve, (123,456):", inE(Point(123,456), E))

def uppg_d_e(p, A, B, P, Q):
    print("\nUppgift d, e)")
    E = [p, A, B]
    OP = Point(0, 1, 0)  # oändlighetspunkten
    print("OP +  P = ", addE(OP, P, E).print_P(), "   Point is on curve:", inE(addE(OP, P, E), E))
    print("P +  P = ", addE(P, P, E).print_P(), "   Point is on curve:", inE(addE(P, P, E), E))
    print("P +  Q = ", addE(P, Q, E).print_P(), "   Point is on curve:", inE(addE(P, Q, E), E))
    print("123456P = ", potE(123456, P, E).print_P() , "   Point is on curve:", inE(potE(123456, P, E), E))
    print("987P +  654Q = ", addE(potE(987,P, E), potE(654, Q, E), E).print_P(), "   Point is on curve:", inE(addE(potE(987,P, E), potE(654, Q, E), E), E))

def uppg_f_g(p, A, B, P, Q):
    print("\nUppgift f, g)")
    E = [p, A, B]
    print(P.print_P(), "\n", negE(P,E).print_P())
    print("P  -  P = ", addE(P, negE(P, E), E).print_P())
    print("P  -  Q = ", addE(P, negE(Q, E), E).print_P())
    print("987P -  654Q = ", addE(potE(987,P, E), negE(potE(654, Q, E), E), E).print_P())

def uppg_h(p, A, B, P, Q, o):
    print("\nUppgift h)") #1 300 731
    E = [p, A, B]
    OP = Point(0, 1, 0)  # oändlighetspunkten
    print(potE(o, P, E).print_P())

def uppg_i(p, A, B, P, Q):
    print("\nUppgift i)")
    E = [p, A, B]
    n = 1
    o = 1300731     # ordningen för Pcd Do  n
    print(Q.print_P())
    print(potE(n, P, E).print_P())
    R = potE(n, P, E)#addE(potE(n-1, P, E), P, E)
    while R.x != Q.x or R.y != Q.y or R.z != Q.z:
        R = potE(n, P, E)#addE(potE(n-1, P, E), P, E)
        n += 1
    print("n is:", n-1)

def uppg_j(p, A, B, P, Q):
    print("\nUppgift j)")
    text = "Yojimbo (1961)"
    E = [p, A, B]
    text_v = []
    for i in range(0, len(text), 1):
        text_v.append(heltalsblock(text[i:i+1]))
    print("text:", text_v)
    M = 256**2
    kappa = int(p//M)
    points = []
    for m in text_v:
        points.append(koblitz(m, kappa, E))
    print("\nPoints:")
    for p in points:
        print(p.print_P(), end = "\t")
        print(heltalsblock((p.x-1)//kappa, "v->s"))
    return points

def uppg_k(p, A, B, P, Q, yojimbo_ps):
    print("\nUppgift k)")
    k = [852, 4036, 73661, 84351, 445566, 13698, 602738]
    cipher = []
    for i in range(0, len(k)):
        cipher.append(encrypt(k[i], P, yojimbo_ps[i], Q, p, A, B))
    print("cipher:\t\t C: \t\t\t D:")
    for c in cipher:
        print(c[0].print_P(),"\t|" ,c[1].print_P())

def uppg_l(p, A, B, P, Q, yojimbo_ps):
    print("\nUppgift l)")
    kryptogram = [[Point(767251, 1077761, 1), Point(971380, 969630, 1)],
              [Point(1132186, 46936, 1), Point(564132, 407087, 1)],
              [Point(851976, 651432, 1), Point(775920, 613044, 1)],
              [Point(520670, 942916, 1), Point(955318, 1078696, 1)],
              [Point(562560, 462087, 1), Point(1193358, 1169142, 1)],
              [Point(675778, 567298, 1), Point(956248, 511009, 1)],
              [Point(955429, 287337, 1), Point(154265, 1066310, 1)],
              [Point(1006365, 85778, 1), Point(704913, 968189, 1)],
              [Point(1214214, 214247, 1), Point(791561, 178111, 1)]]
    n = 741
    text_v = []
    for value in kryptogram:
        print(value[0].print_P(), value[1].print_P())
        text_v.append(decrypt(value[0], value[1], n, p, A, B))
    print(text_v)
    text = ""
    for value in text_v:
        text += heltalsblock(value, "v->s")
    print("n:",n, "with secret text:",  text)

def encrypt(k, P, M, Q, p, A, B):
    E = [p, A, B]
    C = potE(k, P, E)
    D = addE(M, potE(k, Q, E), E)
    return C, D

def decrypt(C, D, n, p, A, B):
    E = [p, A, B]
    M = addE(D, negE(potE(n, C, E),E), E)
    m = 256**2
    kappa = p//m
    return (M.x-1)//kappa

def lenstras(n, A): # test
    #A, B = generate_factors(n)
    x = random.randint(0, n)
    y = random.randint(0, n)
    B = (y**2-x**3-A*x)%n
    d = math.gcd(4*A**3+27*B**2, n)
    E = [n, A, B]
    if d == 1 or d == n:
        P = Point(x, y, 1)
        Q_k1 = P
        for k in range(0, n//2+1): #should be for each prime i think
            try:
                Q_k = potE(n, Q_k1, E) #def potE(n, P, E):
            except Exception as e:
                d = Q_k1.y # maybe d = Q_k1.x
                return math.gcd(d, n)
    else:
        return d


if __name__ == '__main__':
    main()
