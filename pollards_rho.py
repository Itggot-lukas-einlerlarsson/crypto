import math

def f(x,n):
    return (x**2 + 1)%n

def pollards_rho(n, x_0): #returns a divisor and iteration amount
    x_i = x_0 #turtle
    y_i = x_0 #hare
    i = 0
    while 1:
        i = i + 1
        x_i = f(x_i, n)
        y_i = f(f(y_i,n),n)
        d = math.gcd((x_i-y_i), n)
        if d > 1 and d < n:
            break
    return (d, i)

h = [708135681371, 1412536792680015997, 95270801418092775165121913281, 359211301308594647469531797189639, 14683859981444130204708927334356982829, 7528575712348838132721848826467242743143, 52315285858560849957648945390281417094685881389288399, 976446009728623913234119178855528065696691676752499533, 577048900428714995413742965756994328276447681053651695320078699419496386017830817112881, 98019457094851014537689242474466616941261641321201346560044633094007486512688945300826383626603]
def find_divisors():
    i = 0
    for value in h:
        d, c = pollards_rho(value, 2)
        if len(str(d)) > 10:
            print("tal:\t", str(value)[:4],"...\td: ", d, "\tantal iterationer: ", c)
        elif len(str(d)) < 3:
            print("tal:\t", str(value)[:4],"...\td: ", d, "\t\t\tantal iterationer: ", c)
        else:
            print("tal:\t", str(value)[:4],"...\td: ", d, "\t\tantal iterationer: ", c)
        i += 1
find_divisors()
