import numpy as np
import sklearn
import sklearn.datasets
import matplotlib.pyplot as plt


X , y = sklearn.datasets.make_moons(200 , noise = 0.20)
plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)


