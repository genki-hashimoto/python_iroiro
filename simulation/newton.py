import numpy as np
import sympy as sym
import math

x = sym.Symbol("x")

#f = x**2 - 2
f = 3*sym.atan(x-1) + x/4
df = sym.diff(f)

X  = 2.55
ans = 0

i = 1
while True :
    f_x = f.subs( [(x,X)] )
    df_x = df.subs([(x,X)])
    print("###",i,"###",f_x,",",X)
    if np.abs(f_x) < 0.000000000001:
        break
    elif df_x == 0 :
        print("df(X) == 0 you cant found ans. pls reset x0.")
        exit()
    else :
        X = X - f_x / df_x

    i += 1


print (X)
