#calls the reading
import python_reader
#calls the sheel creator
import shell_scripts

#module to write csv:
import csv_module

#module to parse xml:
import xml_parser

#module to read from the xml_parser
import sys

#w = white
#b = black
FILE = "../../python_resultsPNG-w.csv"

#function to take all metrics:
def take_all_metrics(trace_path, print_flag, counters_list, case):
    extended_path = "/ust/uid/1000/64-bit"
    if extended_path not in trace_path:
        trace_path+=extended_path

    return python_reader.readList(trace_path, counters_list, print_flag, case)

#this function executes the program and takes its results as a list:
def executeProgram(caseSelection, flag, letter):
    case = caseSelection
    tracePath = shell_scripts.execution(case, flag, letter)

    # This module calls the reading module
    # trace_path1 = "/tmp/test1/data/500x500.jpg-pf-1/ust/uid/1000/64-bit"
    # trace_path2 = "/tmp/ust-traces--pf-9/ust/uid/1000/64-bit"

    listResults = []
    if (tracePath is not -1):
        print(tracePath)
        print_flag = flag
        # This module calls the reading module to read all the info:
        counters_list = xml_parser.read('../../data/metrics.xml')
        #counters_list = ["my_string_field", "my_integer_field","elapsed", "perf_thread_page_fault", "perf_thread_cache_misses", "perf_thread_instructions"]

        listResults = take_all_metrics(tracePath, print_flag, counters_list, case)

    else:
        print("Error on the tracing")

    return listResults

#this function writes to a csv file:
def write(flag, listAllResults, case):
    if (len(listAllResults) > 0):
        list = []
        data = case
        metrics = ["workload","function", "version","elapsed time","perf_thread_page_fault", "perf_thread_cache_misses", "perf_thread_instructions"]
        # first_line = ["workload:", "version", "perf_thread_page_fault", "perf_thread_cache_misses", "perf_thread_instructions"]
        list.append(metrics)

        if(flag):
            print(listAllResults)

        if (len(listAllResults) > 0):
            if (flag):
                for eachList in listAllResults:
                    if(len(eachList) > 0):
                        list.append(eachList)

        writer_path = FILE
        csv_module.write_to_csv(writer_path, list, True)

def all_exe(flag, list, qtd, letter):
    # This call the module to run the shell scripts:

    j = 1
    listAllResults = []
    for eachElement in list:
        case = eachElement
        i = 0
        if (flag):
            print (case)
        while i < qtd:
            j +=1
            listResults = executeProgram(case, flag, letter)
            if(len(listResults)> 0):
                listAllResults.append(listResults)
                i+=1
        print (j)

    write(flag, listAllResults, case)

def run(flag):
    list = []
    k = 1
    max = 10
    letter = "w"
    times = 100
    while k <max:
        list.append((k*100))
        k= k+1
    if(flag):
        list
    all_exe(flag, list, times, letter)

run(True)