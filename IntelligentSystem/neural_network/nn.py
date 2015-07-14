import numpy as np
import sympy as sp

x = sp.Symbol("x")
x1 = sp.Symbol("x1")
x2 = sp.Symbol("x2")

w = [\
    [\
     [1.077001,1.076606],\
     [-1.502847,-1.509075]\
    ],\
    [-2.125039,-2.071516]\
    ]
off = [1.674558,-0.572590,-1.034925]

insignal = [[0,0],[0,1],[1,0],[1,1]]
f = 1 / (1+sp.exp(-4*x))
xb = w[0][0][0]*x1 + w[0][0][1]*x2 -off[0]
xc = w[0][1][0]*x1 + w[0][1][1]*x2 -off[1]

for i in insignal:
    XB = xb.subs([(x1,i[0]),(x2,i[1])])
    XC = xc.subs([(x1,i[0]),(x2,i[1])])
    b = f.subs([(x,XB)])
    c = f.subs([(x,XC)])

    xa = w[1][0]*b + w[1][1]*c -off[2]


    a = f.subs([(x,xa)])

    print(b,c,a)
