# This module calls the reading module
import babeltrace.reader
import sys

#Calculte the elapse for each metric:
def read(trace_path, info, print_flag):
    print("Reading ", info);
    print (trace_path);
    info_data = []
    info_data2 = []
    version = 0
    trace_collection = babeltrace.reader.TraceCollection()

    trace_collection.add_trace(trace_path, 'ctf')

    for event in trace_collection.events:
        if(event.name == 'hello_world:my_first_tracepoint'):
            if (print_flag):
                print("event name: %s timestamp %d." % (event.name, event.timestamp))
                info_data2.append(event.timestamp)
            fields = dict()
            i = 0
            for k, v in event.items():
                field = event._field(k)
                if (print_flag):
                    print("field name", field.name);
                if(field.name == info):
                    if(print_flag):
                        print("field ", info, field.value);
                    info_data.append(field.value)
                    if (print_flag):
                        print("elapsed %s", info, info_data);
                    if(field.name == "my_integer_field"): #this will take the version
                        version = field.value
                        return version
                    if (field.name == "my_string_field"):  # this will take the function
                        function = field.value
                        return function
                i = i + 1

    # shows the information:
    delta2 = -1
    if (len(info_data2) > 1):
        delta2 = info_data2[1] - info_data2[0]
        if (print_flag):
            print("Delta time stamp", delta2)

    if(info == "elapsed"):
        return delta2

    #shows the information:
    if(len(info_data) > 1):
        delta = info_data[1] - info_data[0]
        if (print_flag):
            print("Delta", delta)
        return delta
    else:
        if (print_flag):
            print("Length < 1")
        return -1

#Take a list of metrics and run read for each one:
def readList(trace_path, info, print_flag, arg1):
    list_result  = []
    list_result.append(arg1)
    for each in info:
        ret = read(trace_path, each, print_flag)
        if(ret is not -1):
            list_result.append(ret)

    return list_result
