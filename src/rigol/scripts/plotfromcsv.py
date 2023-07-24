import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt(
    '/Users/mat/Documents/TeXDocs/RIGOL/python/test.csv', delimiter=',' , dtype='float',
    skiprows=1, usecols=[0, 1])
print(a)

plt.scatter(a[0],a[1])
plt.plot(a[0],a[1])
plt.xlabel('time[s]')
plt.ylabel('CH1 voltage [V]')
plt.show()