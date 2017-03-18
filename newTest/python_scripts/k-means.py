print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


from sklearn.cluster import KMeans

from matplotlib import style
style.use("ggplot")

X = np.array([[1,2],[5,8],[1.5,1.8],[1,0.6],[9,11], [9,15], [10,18]])

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

centroid = kmeans.cluster_centers_
labels = kmeans.labels_

print (centroid)
print(labels)

colors = ["g.","r.","c."]

for i in range(len(X)):
   print ("coordinate:" , X[i], "label:", labels[i])
   plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)

plt.scatter(centroid[:,0],centroid[:,1], marker = "x", s=150, linewidths = 5, zorder =10)

plt.show()
