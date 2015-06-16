import numpy as np
from matplotlib import pyplot as plt

sigmas = [0.2, 1.0, 5.0, 0.5]
myus = [0, 0, 0, -2]

x = np.arange(-5., 5., 0.001)
for v in zip(sigmas,myus):
    y = (1./np.sqrt(2*np.pi*v[0])) * np.exp(-(x - v[1])**2/2/v[0])
    plt.plot(x, y)

plt.show()
