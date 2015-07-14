import numpy as np
import pandas as pd

def sigmoid(x):
	return 1 / (1 + np.exp(-4*x))

def front(weight,inO):
	newron = []
	O = inO
	for i in range(len(weight)):
		line = []
		for j in range(len(weight[i])):
			O.append(1)
			X = 0
			for k in range(len(weight[i][j])):
				X += weight[i][j][k]*O[k]
			line.append(sigmoid(X))
		newron.append(line)
		O = list(newron[i])

	return newron

def back_propagation():
	return 0


weight = [[[1.077001,1.076606,-1.674558],[-1.502847,-1.509075,0.572590]],\
					[[-2.125039,-2.071516,1.034925]]]
newron = []
insignal = [[0,0],[0,1],[1,0],[1,1]]

for insig in insignal:
	newron = list(front(weight, insig))
	print(newron)
