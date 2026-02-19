
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
list = []

#for i in randn(100):
#    list.append(i)
#    if i >
#print (list)

x = np.random.randn(100000)
print(x)

plt.hist(x)
plt.show()