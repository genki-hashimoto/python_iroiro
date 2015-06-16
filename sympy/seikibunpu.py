import numpy as np
import matplotlib.pyplot as plt

mean = 85.3
sd = 11.58

x = np.arange(0,100,1)
y = (1. / np.sqrt(2 * np.pi * sd)) * np.exp(-(x - mean)**2/(2*sd))
print(y)
add = 0
for a in y:
    add += a
print(add)
plt.plot(x,y)
plt.show()
