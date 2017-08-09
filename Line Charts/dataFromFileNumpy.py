import matplotlib.pyplot as plt
import numpy as np

x,y = np.loadtxt('example.txt',delimiter=',', unpack = True)
plt.plot(x,y,label = 'loaded data from file')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('loading data from file using numpy and then visualizing it')
plt.legend()

plt.show()