#!/usr/bin/env python
#calls the reading
import python_reader
#calls the sheel creator
import shell_scripts

#module to write csv:
import csv_module

#module to parse xml:
import xml_parser

import cla

import time

#module to read from the xml_parser
import sys

#w = white
#b = black

#function to take all metrics:
def take_all_metrics(trace_path, print_flag, counters_list, case, path):
    extended_path = "/ust/uid/1000/64-bit"
    if extended_path not in trace_path:
        trace_path+=path

    counters_list = to_string(counters_list)
    counters_list = ['my_string_field', 'my_integer_field', 'elapsed', 'perf_thread_page_fault', 'perf_thread_cache_misses', 'perf_thread_instructions', 'perf_thread_cpu_cycles', 'perf_thread_cycles', 'perf_thread_context_switches']
    return python_reader.readList(trace_path, counters_list, print_flag, case)

def to_string(list_non_strings):
    list_strings = []
    for each in list_non_strings:
        list_strings.append(str(each))
    return list_strings

#this function executes the OpenCV program and takes its results as a list:
def executeProgramCV(caseSelection, flag, letter, counters, ext_path, type_of_file, program):
    case = caseSelection
    #execution(True, "black/b100.jpg")
    file_name = letter
    file_name += str(caseSelection)
    file_name += type_of_file
    tracePath = shell_scripts.execution_cv(flag, program, file_name)

    # This module calls the reading module
    # trace_path1 = "/tmp/test1/data/500x500.jpg-pf-1/ust/uid/1000/64-bit"
    # trace_path2 = "/tmp/ust-traces--pf-9/ust/uid/1000/64-bit"

    listResults = []
    if (tracePath is not -1):
        print(tracePath)
        print_flag = flag
        # This module calls the reading module to read all the info:
        counters_list = counters
        print (counters_list)
        counters_list = ["my_string_field", "my_integer_field","elapsed", "perf_thread_page_fault", "perf_thread_cache_misses", "perf_thread_instructions"]

        listResults = take_all_metrics(tracePath, print_flag, counters_list, case, ext_path)

    else:
        print("Error on the tracing")

    return listResults

#this function executes the OpenCV program and takes its results as a list:
def executeProgramFib(flag, counters, input_value, program, ext_path):
    #execution(True, "black/b100.jpg")
    tracePath = -1
    while tracePath is -1:
        tracePath = shell_scripts.execution_fib(flag, program, input_value)

    # This module calls the reading module
    # trace_path1 = "/tmp/test1/data/500x500.jpg-pf-1/ust/uid/1000/64-bit"

    listResults = []
    if (tracePath is not -1):
        print(tracePath)
        print_flag = flag
        # This module calls the reading module to read all the info:
        counters_list = counters

        counters_list = ["my_string_field", "my_integer_field","elapsed", "perf_thread_page_fault", "perf_thread_cache_misses", "perf_thread_instructions", "perf_thread_cpu_cycles", "perf_thread_cycles","perf_thread_context_switches"]

        listResults = take_all_metrics(tracePath, print_flag, counters_list, input_value, ext_path)

    else:
        print("Error on the tracing")

    return listResults

#this function writes to a csv file:
def write(flag, list_to_write, FILE, mode):
    if (len(list_to_write) > 0):
        list = []
        # first_line = ["workload:", "version", "perf_thread_page_fault", "perf_thread_cache_misses", "perf_thread_instructions"]
        list.append(list_to_write)

        writer_path = FILE
        print (writer_path)
        csv_module.write_to_csv(writer_path, list, True, mode)

def all_exe(flag, list, qtd, letter, counters, FILE, ext_path, type_of_file, program):
    # This call the module to run the shell scripts:

    j = 1
    case = -1
    if(flag):
        print (list)

    metrics = ["workload", "function", "version", "elapsed_time", "perf_thread_page_fault", "perf_thread_cache_misses",
               "perf_thread_instructions", "perf:thread:cpu-cycles", "perf:thread:cycles",
               "perf:thread:context-switches"]
    write(flag, metrics, FILE, "w")
    for eachElement in list:
        case = eachElement
        i = 0
        if (flag):
            print (case)
        while i < qtd:
            j +=1
            listResults = executeProgramCV(case, flag, letter, counters, ext_path, type_of_file, program)
            if(len(listResults)> 0):
                write(flag, listResults, FILE, "a")
                i+=1
        print (j)
    if(case != -1):
        print("OK")
        return 1
    else:
        print("Error on the tracing")
        return -1

def all_exe_fib(flag, list, qtd, counters, FILE, ext_path, program):
    # This call the module to run the shell scripts:

    j = 1
    case = -1
    if(flag):
        print (list)
    metrics = ["workload", "function", "version", "elapsed_time", "perf_thread_page_fault", "perf_thread_cache_misses",
               "perf_thread_instructions", "perf:thread:cpu-cycles", "perf:thread:cycles",
               "perf:thread:context-switches"]
    write(flag, metrics, FILE, "w")
    for eachElement in list:
        each_input = eachElement
        i = 0
        if (flag):
            print (each_input)
        while i < qtd:
            j +=1
            listResults = executeProgramFib(flag, counters, each_input, program, ext_path)
            if(len(listResults)> 0):
                write(flag, listResults, FILE, "a")
                i+=1
        print (j)
    case = each_input
    if(case != -1):
        print("Ok")
        return 1
    else:
        print("Error on the tracing")
        return -1

def run_cv(xml, flag):
    list = []
    k = 1
    xml_file = xml
    letter = xml_parser.read_to_data(xml_file)[0]
    counters = xml_parser.read_metrics(xml_file)
    max = int(xml_parser.read_max(xml_file)[0])
    times = int(xml_parser.read_times(xml_file)[0])
    FILE = xml_parser.read_file(xml_file)[0]
    ext_path = xml_parser.read_ext(xml_file)[0]
    type_of_file = xml_parser.read_type(xml_file)[0]
    program = xml_parser.read_program(xml_file)[0]
    current_path = '/home/frank/Desktop/Research/OpenCV/'
    if(flag):
        print ("counters ", counters)
        print ("max ", max)
        print ("times ", times)
        print ("file ", FILE)
        print ("ext path", ext_path)
        print ("type of file", type_of_file)

    while k <= int(max):
        list.append((k*100))
        k= k+1
    if(flag):
        list
    all_exe(flag, list, times, letter, counters, FILE, ext_path, type_of_file, program)

    time.sleep(5)
    #reading:
    shell_scripts.exec_reading(current_path + FILE[6:])
    shell_scripts.exec_analysis(current_path + FILE[6:])

def run_fib(xml, flag):
    list = []
    k = 1
    times = 1000
    xml_file = xml
    counters = xml_parser.read_metrics(xml_file)
    max = int(xml_parser.read_max(xml_file)[0])
    times = int(xml_parser.read_times(xml_file)[0])
    FILE = xml_parser.read_file(xml_file)[0]
    ext_path = xml_parser.read_ext(xml_file)[0]
    program = xml_parser.read_program(xml_file)[0]
    current_path = '/home/frank/Desktop/Research/OpenCV/'
    if(flag):
        print ("counters ", counters)
        print ("max ", max)
        print ("times ", times)
        print ("file ", FILE)
        print ("ext path", ext_path)

    while k <= int(max):
        list.append((k))
        k= k+1
    if(flag):
        list
    all_exe_fib(flag, list, times, counters, FILE, ext_path, program)

    time.sleep(5)
    #reading:
    shell_scripts.exec_reading(current_path + FILE[6:])
    shell_scripts.exec_analysis(current_path + FILE[6:] )

#This function does the analysis:
def analysis(csv):
    list = csv_module.read_from_csv(csv, False)
    list_runs = cla.create_runs(list, False)
    i = 0
    results = []
    while (i < 5):
        results.append(cla.take_metrics_index(list_runs, i, False))
        i = i+1

    cla.correlation(sorted(results[0]), sorted(results[3]))
    return True

def call_analysis():
    csv = "/home/frank/Desktop/Research/OpenCV/python_results.csv"
    return analysis(csv)

def run(xml):
    print(xml)
    xml_file = xml
    program = xml_parser.read_program(xml_file)
    program = str(program)
    if ("fib" in str(program)):
        run_fib(xml, True)

    if ('program_to_load_program' in program):
        run_cv(xml, True)

    if ('parallel_preorder' in program):
        run_fib(xml, True)

if(len(sys.argv)> 2):
    print("not default execution")
    print(sys.argv[1])
    run(sys.argv[1])

else:
    print ("default execution")
    #shell_scripts.kernel_trace(1)
    run('../../data/metrics.xml')
    #shell_scripts.kernel_trace(-1)
    # run_cv( '../../data/metrics.xml',True)
    # call_analysis()