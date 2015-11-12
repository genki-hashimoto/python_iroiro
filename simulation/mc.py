import numpy as np

np.random.seed(1145141919)


i = 0
In = 0
All = 0
while True:
	a = np.random.rand()
	b = np.random.rand()
	All += 1
	if np.hypot(a,b) <= 1:
		In += 1
	if i % 10000000 == 0:
		print(i,":",(4*In)/All)
	i += 1
