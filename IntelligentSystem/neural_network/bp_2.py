import numpy as np
import pandas as pd
import random
import time

def init_weight(weight):
	random.seed(15)
	for i in range(len(weight)):
		for j in range(len(weight[i])):
			for k in range(len(weight[i][j])):
				weight[i][j][k] = (random.random()-0.5)*2*0.3
	return weight

def sigmoid(x,sigma):
	return 1.0 / (1.0 + np.exp(-1.0*sigma*x))

def front(weight,inO,sigma):
	newron = []
	O = list(inO)
	for i in range(len(weight)):
		line = []
		for j in range(len(weight[i])):
			O.append(1)
			X = 0
			for k in range(len(weight[i][j])):
				X += weight[i][j][k]*O[k]
			line.append(sigmoid(X,sigma))
		newron.append(line)
		O = list(newron[i])

	return newron

def back_propagation(weight, outsig, insig, teacher_sig, sigma, eta):
	delta = []
	for i in range((len(weight)-1),-1,-1):
		for j in range(len(weight[i])):
			if i == len(weight)-1:
				delta_k = (outsig[i][j]-teacher_sig)* sigma * (1 - outsig[i][j]) * outsig[i][j]
				delta.append(delta_k)
			else :
				delta_j = 0
				for d in range(len(delta)):
					delta_j += delta[d] * weight[i+1][d][j] * sigma * (1-outsig[i][j]) * outsig[i][j]
			for k in range(len(weight[i][j])):
				if i == len(weight)-1:
					if k == len(weight[i][j]) -1:
						weight[i][j][k] -= eta * delta_k * 1
					else:
						weight[i][j][k] -= eta * delta_k * outsig[i-1][k]
				else :
					if k == len(weight[i][j])-1:
						weight[i][j][k] -= eta * delta_j * 1
					elif i == 0:
						weight[i][j][k] -= eta * delta_j * insig[k]
					else:
						weight[i][j][k] -= eta * delta_j * outsig[i-1][k]
	return weight

eta = 0.1
sigma = 4.0
weight = [[[1.0,1.0,1.0],[1.0,1.0,1.0]],\
					[[1.0,1.0,1.0]]]
weight = init_weight(weight)
#print("weight:",weight)
newron = []
#insignal = np.loadtxt("signal.csv", delimiter = ",")
t_sig = [0,1,1,0]
insignal = [[0,0],[0,1],[1,0],[1,1]]

gosa_tmp = 0
i = 0
while True:
	i += 1
	#print("##########",i,"#########")
	gosa = 0

	for (insig,t) in zip(insignal,t_sig):
		insig = list(insig)
		#print(weight)
		newron = list(front(weight, insig,sigma))
		#print(newron[1][0])

		#print("NEWRON:",newron)
		gosa += ((newron[1][0]-t)**2)/2
		weight = back_propagation(weight, newron,insig, t, sigma, eta)
	print(gosa)
	if i > 1000:
		break;
	#time.sleep(0.3)
print(i)
for insig in insignal:
	insig = list(insig)
	newron = list(front(weight, insig, sigma))
	print(newron[1])
