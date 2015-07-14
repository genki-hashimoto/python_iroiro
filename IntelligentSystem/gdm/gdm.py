import numpy as np
import sys
import matplotlib.pyplot as plt
import sympy as sp


argvs = sys.argv
argc = len(argvs)

if argc != 3:
    print("ERROR")
    quit()

a = sp.Symbol("a")
f = (a-1)**2 * (a+1)**2
df = sp.diff(f)
eta = float(argvs[2])

i = 1
ans = []
ans.append(float(argvs[1]))
while True:
    print(ans[-1])
    ans.append(ans[-1] - eta* df.subs([(a,ans[-1])]))


    if ans[-1] == ans[-2]:
        break


print("kyokuti:",ans[-1])
print("kyokuti:",f.subs([(a,ans[-1])]))
