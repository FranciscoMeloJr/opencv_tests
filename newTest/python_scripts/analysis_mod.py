import json
from pprint import pprint
from sklearn.cluster import KMeans
import numpy as np


#Class of execution
class Execution:
    'Common base class for all employees'
    id = -1
    a = 0
    b = 0
    d = 0
    e = 0
    def __init__(self, id):
        self.id = id

    def __init__(self, id, a, b):
        self.id = id
        self.a = a
        self.b = b

    def getA(self):
        return self.a

    def displayExecution(self):
        print
        "Id : ", self.id, ", A: ", self.a

# this display all the executions
def get_duration_list(list_exe):
    duration = []
    for each in list_exe:
        duration.append(each.getA())

    return duration

#This function reads the json
def read():
    with open('/var/www/html/siteTest/data/open1001.json') as data_file:
        data = json.load(data_file)
    return data

#This creates all the executions in a list of class
def create_executions(data):
    list_e = []
    i = 0
    while i < len(data["executions"]):
        Exe = Execution(i, data["executions"][i]['a'], data["executions"][i]['b'])
        list_e.append(Exe)
        i = i + 1

    return list_e

#this display all the executions
def print_executions(data):
    i = 0
    while i < len(data["executions"]):
        print (data["executions"][i])
        i = i + 1

#this function gets the timestamp:
def get_timestamp(data):
    i = 0
    timestamp = []
    while i < len(data["executions"]):
        timestamp.append(data["executions"][i]['b'])
        i = i + 1

    return timestamp

#this funciton gets the duration:
def get_duration(data):
    i = 0
    duration = []
    while i < len(data["executions"]):
        duration.append(data["executions"][i]['a'])
        i = i + 1

    return duration

#this function gets the max value
def max(list_unk):
    max = list_unk[0]
    for each in list_unk:
        if (each > max):
            max = each
    return max

#function main:
def main():
    data = read()
    #pprint(data)
    #print_executions(data)
    list_exe = create_executions(data)
    duration = get_duration_list(list_exe)
    order_duration = sorted(duration)
    print (order_duration)

main()


#"masks": {       "id": "valore"     },     "om_points": "value",    "parameters": {         "id": "valore"     } }
#data["maps"][0]["id"]
