import numpy as np
import sympy as sym
import math

print("a:")
a = float(input())
print("b:")
b = float(input())

x  = sym.Symbol("x")
f = x**2 - 2

ans = 0

while True:
    f_a = f.subs([(x,a)])
    f_b = f.subs([(x,b)])
    w = (a*f_b - b*f_a) / (f_b - f_a)
    f_w = f.subs([(x,w)])
    print("fa:",f_a)
    print("fb:",f_b)
    print("fw:",f_w)
    if f_a == 0:
        ans = a
        break
    elif f_b == 0:
        ans = b
        break
    elif f_a * f_b > 0 : #f_aとf_bの符号が同じ→適用不可
        print("sry, pls reset a and b:(")
        quit()
    else:
        if math.fabs(f_w) < 0.000000001:
            ans = w
            break
        elif f_w < 0:
            if f_a < 0:
                a = w
            else:
                b = w
        else :
            if f_a > 0:
                a = w
            else:
                b = w

print(ans)
