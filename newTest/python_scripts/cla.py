def classify(list, flag):
    list_runs = []
    for each in list:
        print (each)
        a = Run(each)
        list_runs.append(a)

    print (len(list_runs))
    print (list_runs[1].get_metrics_1())

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