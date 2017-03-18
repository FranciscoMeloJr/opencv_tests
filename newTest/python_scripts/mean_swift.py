#!/usr/bin/env python
#calls the reading
#module to read from the xml_parser
import sys

import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
import numpy

x = [1,1,5,6,1,5,10,22,23,23,50,51,51,52,100,112,130,500,512,600,12000,12230]

def calculate(x):
    X = np.array(zip(x, np.zeros(len(x))), dtype=np.int)
    bandwidth = estimate_bandwidth(X, quantile=0.1)
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(X)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

    for k in range(n_clusters_):
        my_members = labels == k
        print "cluster {0}: {1}".format(k, X[my_members, 0])


def coef(list1, list2):
    numpy.corrcoef(list1, list2)[0, 1]


if(len(sys.argv)> 2):
    print("not default execution")
    print(sys.argv[1])
    calculate(sys.argv[1])

else:
    calculate(x)