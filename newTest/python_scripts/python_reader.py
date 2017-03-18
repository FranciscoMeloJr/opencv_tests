# This module calls the reading module
import babeltrace.reader
import sys

#Calculte the elapse for each metric:
def read(trace_path, info, print_flag):
    print("Reading ", info);
    print (trace_path);
    info_data = -1
    elapsed = -1
    trace_collection = babeltrace.reader.TraceCollection()

    trace_collection.add_trace(trace_path, 'ctf')

    ret = -1
    for event in trace_collection.events:
        if (event.name == 'hello_world:my_first_tracepoint'):
            print("event name: %s timestamp %d." % (event.name, event.timestamp))
            if(elapsed is -1):
                print ("elapsed")
                elapsed = event.timestamp
            else:
                if (info is "elapsed"):
                    return (event.timestamp - elapsed)
            for k, v in event.items():
                field = event._field(k)
                if (field.name == info):
                    print (info , field.name, field.value, info_data)
                    if(((str(info) is "my_integer_field")) or ((str(info) is "my_string_field"))):
                        return field.value
                    if (info_data is -1):
                        info_data = field.value
                    else:
                        print (info , info_data, field.value)
                        ret = (int(field.value) - int(info_data))

    print (ret)
    return ret

#Take a list of metrics and run read for each one:
def readList(trace_path, info, print_flag, arg1):
    list_result  = []
    list_result.append(arg1)
    for each in info:
        ret = read(trace_path, each, print_flag)
        print (ret)
        if(ret is not -1):
            list_result.append(ret)

    print (list_result)
    return list_result

readList("/tmp/ust-traces-python-3/ust/uid/1000/64-bit", ['my_string_field', 'my_integer_field','elapsed', 'perf_thread_page_fault', 'perf_thread_cache_misses', 'perf_thread_instructions', 'perf_thread_page_fault', 'perf_thread_cache_misses', 'perf_thread_instructions', 'perf_thread_cpu_cycles', 'perf_thread_cycles', 'perf_thread_context_switches'], True, 100)
#['my_string_field', 'my_integer_field', 'elapsed', 'perf_thread_page_fault', 'perf_thread_cache_misses', 'perf_thread_instructions']
