#!/usr/bin/python
import sys
import csv

import numpy as np
import statsmodels.api as sm

import numpy as np
 
from sklearn import linear_model


def read_csv(flag, file_to_open):
    print file_to_open
    f = open(file_to_open, 'rb')
    list_runs = []
    reader = csv.reader(f)
    for row in reader:
        if(flag):
            print row
        list_runs.append(row)

    list_runs = list_runs[1:]
    print len(list_runs)
    f.close()
    return list_runs[0:]

def simulation():
    y = [1,2,3,4,3,4,5,4,5,5,4,5,4,5,4,5,6,5,4,5,4,3,4]

    x = [
         [4,2,3,4,5,4,5,6,7,4,8,9,8,8,6,6,5,5,5,5,5,5,5],
         [4,1,2,3,4,5,6,7,5,8,7,8,7,8,7,8,7,7,7,7,7,6,5],
         [4,1,2,5,6,7,8,9,7,8,7,8,7,7,7,7,7,7,6,6,4,4,4]
         ]
    print reg_m(y, x).summary()
    
def reg_m(y, x):
    ones = np.ones(len(x[0]))
    X = sm.add_constant(np.column_stack((x[0], ones)))
    for ele in x[1:]:
        X = sm.add_constant(np.column_stack((ele, X)))
    results = sm.OLS(y, X).fit()
    return results

def take_y(list, flag):
    return take(list, flag, 3)

def take(list, flag, i):
    list_y = []
    for each in list:
        if(flag):
            print each[i]
        list_y.append(each[i])

    list_y = np.array(list_y).astype(np.float)
    return list_y

def take_x(list, flag):
    list_x1 = []
    list_x2 = []
    list_x3 = []

    list_x1 =  take(list, flag, 0)
    list_x2 =  take(list, flag, 5)
    list_x3 =  take(list, flag, 6)

    x = []
    x.append(list_x1)
    x.append(list_x2)
    x.append(list_x3)
    
    return x
        
def run(file_to_open):
    flag = True
    result = read_csv(flag, file_to_open)
    y = take_y(result, flag)
    x = take_x(result, flag)
    print len(y)
    print len(x[0])

    print reg_m(y, x).summary()
    
    
#clf = linear_model.LinearRegression()
#clf.fit([[getattr(t, 'x%d' % i) for i in range(1, 8)] for t in texts],
#        [t.y for t in texts])


print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

if(len(sys.argv)> 2):
    run(sys.argv[1])
else:
    run("/home/frank/Desktop/Research/OpenCV/python_resultsFib.csv")
