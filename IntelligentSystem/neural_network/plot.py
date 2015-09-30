import numpy as np
import matplotlib.pyplot as plt

fishA = []
fishB = []
for line in open("fishA.train", "r"):
	items = line.split()
	fishA.append([float(items[0]),float(items[1])])
for line in open("fishB.train", "r"):
	items = line.split()
	fishB.append([float(items[0]),float(items[1])])

for a in fishA:
	plt.plot(a[0],a[1],"ro")

for b in fishB:
	plt.plot(b[0],b[1],"bo")

plt.show()
