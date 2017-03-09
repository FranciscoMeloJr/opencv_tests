import numpy

def create_runs(list, flag):
    list_runs = []
    for each in list:
        if (flag):
            print (each)
        a = Run(each)
        list_runs.append(a)

    if(flag):
        print (len(list_runs))
        print (list_runs[1].show())

    return list_runs[1:]

def take_metrics_1(list_runs, flag):
    list_metrics1 = []
    for each in list_runs:
        if(flag):
            print (each.get_metrics_1())
        list_metrics1.append(each.get_metrics_1())

    return list_metrics1

def take_metrics_index(list_runs, index, flag):
    list_metrics_index = []
    for each in list_runs:
        if(flag):
            print (each.get_metrics_index(index))
        list_metrics_index.append(each.get_metrics_index(index))

    return list_metrics_index

def correlation(list1, list2):
    print (list1)
    print (list2)
    result = numpy.corrcoef(list1, list2)[0, 1]
    print (result)

#Class used for classification:
class Run:
    """A simple example class"""
    id = -1
    metrics = -1

    def __init__(self, list):
        ...
        self.metrics = list

    def show(self):
        print (self.metrics)
        return

    def get_metrics_1(self):
        return self.metrics[0]

    def get_metrics_index(self, index):
        return self.metrics[index]
