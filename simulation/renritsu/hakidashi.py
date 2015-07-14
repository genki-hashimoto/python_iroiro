import numpy as np
import pandas as pd

A = pd.read_csv("A1000.csv",header = None)
b = pd.read_csv("b1000.csv",header=None)
a = pd.concat([A,b],axis= 1)
len_a = len(a)

a.index = [np.arange(len_a)]
a.columns = [np.arange(len_a+1)]

for k in range(len_a):
	for j in range(k+1,len_a+1):
		a.ix[k,j] /= a.ix[k,k]
		for i in range(len_a):
			if i != k:
				a.ix[i,j] -= a.ix[k,j]*a.ix[i,k]

ans = list(a[len_a])
print(ans)
