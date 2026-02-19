import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt


N=1000000
counter = 0
list = []
for i in randn(N):
    if i >= -1 and i <=1:
        counter += 1
    list.append(i)
print(np.mean(list))
media_teorica = counter/N
print("counter is: ", counter)
print(media_teorica)


