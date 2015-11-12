import numpy as np

data = [[7,1,2,10],\
				[1,8,3,8],\
				[2,3,9,6]]

data = [[2,3,4,6],\
				[3,5,2,5],\
				[4,3,30,32]]

data = np.loadtxt("Ab_for_python", delimiter = ",")


ans = []
for i in range(len(data)) :
	ans.append(0)

print(ans)
while True:
	before_ans = list(ans)
	ans_tmp = list(ans)
	for i in range(len(data)):
		tmp = 0
		for j in range(len(data[i])):
			if i == j:
				div = data[i][j]
			elif j == len(data[i])-1:
				tmp += data[i][j]
			else :
				tmp -= data[i][j]*ans_tmp[j]
		ans[i] = tmp / div
	print(ans)
	flg = True
	for a,b_a in zip(ans,before_ans):
		if np.abs(a-b_a) > 10**-7:
			flg = False
	if flg:
		break
