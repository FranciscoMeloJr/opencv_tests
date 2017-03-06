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

import sys

#module to read from the xml_parser
import sys

#w = white
#b = black

#function to take all metrics:
def take_all_metrics(trace_path, print_flag, counters_list, case, path):
    extended_path = "/ust/uid/1000/64-bit"
    if extended_path not in trace_path:
        trace_path+=path

    print (trace_path, counters_list, print_flag, case)
    counters_list = ['my_string_field', 'my_integer_field', 'elapsed', 'perf_thread_page_fault', 'perf_thread_cache_misses', 'perf_thread_instructions']
    return python_reader.readList(trace_path, counters_list, print_flag, case)

#this function executes the program and takes its results as a list:
def executeProgram(caseSelection, flag, letter, counters, ext_path, type_of_file, program):
    case = caseSelection
    #execution(True, "black/b100.jpg")
    file_name = letter
    file_name += str(caseSelection)
    file_name += type_of_file
    tracePath = shell_scripts.execution(flag, file_name, program)

    # This module calls the reading module
    # trace_path1 = "/tmp/test1/data/500x500.jpg-pf-1/ust/uid/1000/64-bit"
    # trace_path2 = "/tmp/ust-traces--pf-9/ust/uid/1000/64-bit"

    listResults = []
    if (tracePath is not -1):
        print(tracePath)
        print_flag = flag
        # This module calls the reading module to read all the info:
        counters_list = counters

        #counters_list = ["my_string_field", "my_integer_field","elapsed", "perf_thread_page_fault", "perf_thread_cache_misses", "perf_thread_instructions"]

        listResults = take_all_metrics(tracePath, print_flag, counters_list, case, ext_path)

    else:
        print("Error on the tracing")

    return listResults

#this function writes to a csv file:
def write(flag, listAllResults, case, FILE):
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
        print (writer_path)
        csv_module.write_to_csv(writer_path, list, True)

def all_exe(flag, list, qtd, letter, counters, FILE, ext_path, type_of_file, program):
    # This call the module to run the shell scripts:

    j = 1
    listAllResults = []
    case = -1
    if(flag):
        print (list)
    for eachElement in list:
        case = eachElement
        i = 0
        if (flag):
            print (case)
        while i < qtd:
            j +=1
            listResults = executeProgram(case, flag, letter, counters, ext_path, type_of_file, program)
            if(len(listResults)> 0):
                listAllResults.append(listResults)
                i+=1
        print (j)
    if(case != -1):
        write(flag, listAllResults, case, FILE)
        return 1
    else:
        print("Error on the tracing")
        return -1

def run(xml, flag):
    list = []
    k = 1
    max = 11
    letter = "white/w"
    times = 1000
    xml_file = xml
    counters = xml_parser.read_metrics(xml_file)
    max = int(xml_parser.read_max(xml_file)[0])
    times = int(xml_parser.read_times(xml_file)[0])
    FILE = xml_parser.read_file(xml_file)[0]
    ext_path = xml_parser.read_ext(xml_file)[0]
    type_of_file = xml_parser.read_type(xml_file)[0]
    program = xml_parser.read_program(xml_file)[0]

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
    shell_scripts.exec_reading('/home/frank/Desktop/Research/OpenCV/' + FILE[6:])

#This function does the analysis:
def analysis(csv):
    list = csv_module.read_from_csv(csv, False)
    cla.create_runs(list, True)
    return 1

def call_analysis():
    csv = "/home/frank/Desktop/Research/OpenCV/python_results.csv"
    return analysis(csv)

# run( '../../data/metrics.xml',True)
call_analysis()
