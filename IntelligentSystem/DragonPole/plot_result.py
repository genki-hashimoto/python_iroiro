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

selection = np.zeros(len(data))
biggest = 0
biggest2 = 0
num_max = 2**len(data)
plot_data = []
plot_data2 =[]
for i in range(100):
	selection2 = toBinary2(i)
	while len(selection2) < len(data):
		selection2.insert(0,0)
	for j in range(len(selection)):
		selection[j] = np.random.randint(2)
	weight = weight2 = 0
	money = money2 = 0
	for s,s2,d in zip(selection,selection2,data):
		if s == 1:
			weight += d[0]
			money += d[1]
		if s2 == 1:
			weight2 += d[0]
			money2 += d[1]
	if limit < weight:
		money = 5
	if limit < weight2:
		money2 = 5
	if money > biggest:
		biggest = money
	if money2 > biggest2:
		biggest2 = money2
	plot_data.append(biggest)
	plot_data2.append(biggest2)


plt.plot(plot_data,"r-")
plt.plot(plot_data2,"b-")

plt.show()
