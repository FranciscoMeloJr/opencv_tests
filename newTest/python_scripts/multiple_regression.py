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
        if(each[i] is not None):
            if(flag):
                print each[i]
            list_y.append(each[i])

    list_y = np.array(list_y).astype(np.float)
    return list_y

def take_x(list, flag, list_x):

    x = []
    i = 0
    while i < len(list_x):
        x.append(take(list, flag, list_x[i]))
        i = i + 1
    
    return x
        
def run(file_to_open, list_x):
    flag = False
    result = read_csv(flag, file_to_open)
    y = take_y(result, flag)
    x = take_x(result, flag, list_x)
    print len(y)
    print len(x[0])

    print reg_m(y, x).summary()
    
    
#clf = linear_model.LinearRegression()
#clf.fit([[getattr(t, 'x%d' % i) for i in range(1, 8)] for t in texts],
#        [t.y for t in texts])


print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

if(len(sys.argv)> 2):
    if (len(sys.argv) == 2):
        list_x = [0,5,6,7]
        run(sys.argv[1],list_x)
    if (len(sys.argv) > 2):
        run(sys.argv[1], sys.argv[1])
else:
    list_x = [0,5,6,7]
    run("/home/frank/Desktop/Research/OpenCV/python_resultsFace.csv",list_x)
