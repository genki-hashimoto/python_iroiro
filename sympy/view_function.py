import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import math

x = sym.Symbol("x")
e = sym.Symbol("e")

f = 1 / (1 + sym.exp(-e * x))

#matplotlibによるプロット機能もありますxlimだけでなく表題や軸の設定なども引数で設定できる
sym.plotting.plot(f.subs([(e,1)]),(x,-10,10))

plt.show()
