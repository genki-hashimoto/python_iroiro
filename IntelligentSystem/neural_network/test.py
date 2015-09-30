weight = [[[0.33,0.8, 1.6],[0.5,0.8,-0.2]],\
					[[0.05,0.3,-1.1]]]
for i in range(len(weight)-1,-1,-1):
	for j in range(len(weight[i])):
		for k in range(len(weight[i][j])):
			print(i,j,k)
