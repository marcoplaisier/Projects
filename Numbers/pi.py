from decimal import Decimal, getcontext
import math

__author__ = 'marco'

def pi_generator():
    #http://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm
    getcontext().prec = 240
    a = Decimal(1.0)
    b = Decimal(1.0 / math.sqrt(2))
    t = Decimal(1.0/4)
    p = Decimal(1)

    while True:
        an = (a + b) / 2
        bn = (a * b).sqrt()
        tn = t - p * (a - an)*(a - an)
        pn = 2*p

        pi = ((an + bn)*(an + bn)) / (4*tn)
        yield pi
        a, b, t, p = an, bn, tn, pn

if __name__ == '__main__':
    pigen = pi_generator()
    for i in range(100):
        print(next(pigen))

#3.140
#3.14159264
#3.1415926535897932382