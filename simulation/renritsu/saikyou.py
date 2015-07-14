import numpy as np
import pandas as pd

NUM = 1000
A = pd.read_csv("A1000.csv",header=None)
b = pd.read_csv("b1000.csv",header=None)
#x = np.random.rand(NUM,1)
#b = np.dot(A,x)

from numpy.linalg import solve
xx = solve(A, b)

print(xx)
