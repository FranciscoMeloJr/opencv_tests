#calls the reading
import python_reader
#calls the sheel creator
import shell_scripts

#module to write csv:
import csv_module

import sys

#function to take all metrics:
def take_all_metrics(trace_path, print_flag):
    extended_path = "/ust/uid/1000/64-bit"
    if extended_path not in trace_path:
        trace_path+=extended_path

    counters_list = ["perf_thread_page_fault", "perf_thread_cache_misses", "perf_thread_instructions"]
    return python_reader.readList(trace_path, counters_list, print_flag)



#This call the module to run the shell scripts:
trace_path = shell_scripts.execution()

# This module calls the reading module
trace_path1 = "/tmp/test1/data/500x500.jpg-pf-1/ust/uid/1000/64-bit"
trace_path2 = "/tmp/ust-traces--pf-9/ust/uid/1000/64-bit"

if(trace_path is not -1):
    print (trace_path)
    print_flag = False
    ret = take_all_metrics(trace_path, print_flag)
else:
    print("Error on the tracing")

if(len(ret)> 1):
    csv_module.write_to_csv("results.csv", ret)