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
		for i in range(k+1,len_a):
			if i != k:
				a.ix[i,j] -= a.ix[k,j]*a.ix[i,k]

ans = []
ans.append(a.ix[len_a-1,len_a])

for k in range((len_a-1)-1,(0)-1,-1):
	xk = a.ix[k,len_a]
	for x,j in zip(ans,range(k+1,len_a)):
		xk -= a.ix[k,j]*x
	ans.insert(0,xk)

print(ans)
