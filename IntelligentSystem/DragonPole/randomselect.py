import numpy as np
import matplotlib.pyplot as plt
import sys

def toBinary2(decimal):
	if decimal == 0: return [0]
	bin = []
	while decimal > 0:
		bin.append(decimal % 2)
		decimal >>= 1
	return bin[::-1]

argvs = sys.argv
argc = len(argvs)

if argc != 2:
	print("arg ERROR")
	quit()

filename = argvs[1]
f = open(filename, 'r')

data = []
i = 0
for line in f:
	d = []
	if i == 0:
		limit = int(line.split("=")[1])
	elif i != 1 :
		tmp = line.split(",")

		d.append(int(tmp[1]))
		d.append(int(tmp[2]))
		data.append(d)
	i += 1
f.close()

biggest = 0
num_max = 2**len(data)
plot_data = []
for i in range(10000):
	selection = toBinary2(np.random.randint(0,num_max))
	while len(selection) < len(data):
		selection.insert(0,0)
	weight = 0
	money = 0
	for s,d in zip(selection,data):
		if s == 1:
			weight += d[0]
			money += d[1]
	if limit < weight:
		money = 5
	plot_data.append[]
	if money > biggest:
		biggest = money
		print(i,selection)
		print(money)
