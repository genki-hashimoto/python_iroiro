import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import math

x = sym.Symbol("x")
e = sym.Symbol("e")

#f = 1 / (1 + sym.exp(-e * x))
#f = 3* sym.atan(x-1) + x / 4
f = 1 / sym.sqrt(2 * sym.pi * 11.2) * sy
#df = sym.diff(f)

#matplotlibによるプロット機能もありますxlimだけでなく表題や軸の設定なども引数で設定できる
#sym.plotting.plot(f.subs([(e,1)]),(x,-10,10))
sym.plotting.plot(f,color = "b")
