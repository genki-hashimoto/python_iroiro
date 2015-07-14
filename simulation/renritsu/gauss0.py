import numpy as np
import pandas as pd

a = pd.read_csv("data.csv",header = None)

len_a = len(a)


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
