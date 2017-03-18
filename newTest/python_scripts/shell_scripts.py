#Shell function:
import subprocess

#This function does the kernel tracing, replacing the bash scripts:
def kernel_trace(i):
    season_name = "my-kernel-session"
    if(i > 0):

        subprocess.check_call("lttng create "+ season_name + " --output=/tmp/my-kernel-trace", shell=True)
        #subprocess.check_call("lttng enable-event -k -a", shell=True)
        subprocess.check_call("lttng enable-event -k kmem_cache_alloc", shell=True)
        subprocess.check_call("lttng start", shell=True)
    else:
        subprocess.check_call("lttng stop " + season_name , shell=True)
        subprocess.check_call("lttng destroy "+ season_name, shell=True)


#This function does the tracing, replacing the bash scripts:
def trace(id, program, input, counter_list):
    season_name = " y "
    image = input #image = "../data/500x500.jpg"
    print(input)
    i = 10
    output = "--output=/tmp/ust-traces-python-" + str(id)
    output_run = -1
    max = len(counter_list)
    input = str(input)
    #do the process:
    pre1 = "LD_PRELOAD=/usr/local/lib/liblttng-ust-cyg-profile.so "
    pre2 = "LD_PRELOAD=/usr/local/lib/liblttng-ust-fork.so "
    subprocess.check_call("lttng create"+ season_name + output, shell=True)
    subprocess.check_call(["lttng enable-event -u -a"], shell=True)
    #subprocess.check_call(["lttng enable-event -u sched_switch"], shell=True)
    #subprocess.check_call(["lttng enable-event -u procname"], shell=True)
    j = 0
    while (j < max):
        subprocess.check_call(["lttng add-context -u -t " + counter_list[j]], shell=True)
        j= j+1


    subprocess.check_call("lttng start" + season_name, shell=True)

    try:
        # program execution:
        try:
            output_run = subprocess.check_output(pre1 + program +" "+ input , shell=True)
        except ValueError:
            print ("error")
        subprocess.check_call("lttng stop", shell=True)
        subprocess.check_call(["lttng destroy", str(i)], shell=True)
        subprocess.check_call(["echo", str(i)], shell=True)

    #exception treatment:
    except subprocess.CalledProcessError as e:
        print ("Error on the program")
        subprocess.check_call("lttng stop", shell=True)
        subprocess.check_call(["lttng destroy", str(i)], shell=True)
        subprocess.check_call(["echo", str(i)], shell=True)
        #in case of execption, it will return -1:
        output = -1

    print(output_run)
    return output

#execute the program:
def exec_program(input_value):
    input = str(input_value)
    program = "../program_to_load_program "
    pre1 = "LD_PRELOAD=/usr/lib/liblttng-ust-cyg-profile.so "
    pre2 =  "LD_PRELOAD=/usr/local/lib/liblttng-ust-fork.so "
    subprocess.check_call(pre1 + program + input, shell=True)

#execute the program:
def exec_reading(file):
    subprocess.check_call("libreoffice " + file, shell=True)

#calling the function
def run_cases(id, flag):
    trace_data = 0
    ret = 0
    if(id == 500):
        trace_data = "../data/500x500.jpg"
        if(flag):
            print (trace_data)
        ret = trace(trace_data, 3)
    if(id == 600):
        trace_data = "../data/600x600.jpg"
        ret = trace(trace_data, 3)
    if(id == 700):
        trace_data = "../data/700x700.jpg"
        ret = trace(trace_data, 3)

    if(id == 10):
        # run(500)
        i = 0
        while (i < 10):
            exec_program()
            i += 1
    return ret

#calling the function
def run_opencv(flag, file, program, counter_list):
    trace_data = 0
    ret = -1

    init = "../data/"
    init+=file
    if(flag):
        print (init)
    image_name = init
    trace_season = 3
    ret = trace(trace_season, program, image_name, counter_list)

    return ret

#calling the function
def run_fib(flag, program, input, counter_list):
    trace_data = 0
    ret = -1

    if(flag):
        print (input)
    trace_season = 5
    ret = trace(trace_season, program, str(input), counter_list)

    return ret

def execution_fib(flag, program, input):
    # execute a test calling the exec_program
    counter_list = ["perf:thread:page-fault",
                    "perf:thread:cache-misses",
                    "perf:thread:instructions",
                    "perf:thread:cpu-cycles",
                    "perf:thread:cycles",
                    "perf:thread:context-switches"]
    if(flag):
        print (execution_cv)
    ret = run_fib(flag, program, input, counter_list)
    if (ret is not -1):
        print("Open the file: ", ret[9:])
        return ret[9:]
    else:
        print("An error just occured")
        return -1

def execution_cv(flag, program, file):
    # execute a test calling the exec_program
    counter_list = ["perf:thread:page-fault",
                    "perf:thread:cache-misses",
                    "perf:thread:instructions",
                    "perf:thread:cpu-cycles",
                    "perf:thread:cycles",
                    "perf:thread:context-switches"]
    if(flag):
        print (execution_cv)
    ret = run_opencv(flag, file, program, counter_list)
    if (ret is not -1):
        print("Open the file: ", ret[9:])
        return ret[9:]
    else:
        print("An error just occured")
        return -1

#execution(True, "black/b100.jpg")
#exec_program()

#This function does the tracing, replacing the bash scripts:
def trace_selected(image_name, id, list):
    season_name = " x "
    image = image_name #image = "../data/500x500.jpg"
    print(image_name)
    i = 10
    output = "--output=/tmp/ust-traces-python-" + str(id)

    #do the process:
    subprocess.check_call("lttng create"+season_name + output, shell=True)
    subprocess.check_call(["lttng enable-event -u -a", str(i)], shell=True)
    subprocess.check_call(["lttng enable-event -u sched_switch", str(i)], shell=True)
    if("pg" in list):
        subprocess.check_call(["lttng add-context -u -t perf:thread:page-fault", str(i)], shell=True)

    if ("cm" in list):
        subprocess.check_call(["lttng add-context -u -t perf:thread:cache-misses", str(i)], shell=True)

    if ("inst" in list):
        subprocess.check_call(["lttng add-context -u -t perf:thread:instructions", str(i)], shell=True)

    subprocess.check_call("lttng start" + season_name, shell=True)

    try:
        # program execution:
        subprocess.check_output("LD_PRELOAD=/usr/local/lib/liblttng-ust-fork.so ../opencv "+ image , shell=True)
        subprocess.check_call("lttng stop", shell=True)
        subprocess.check_call(["lttng destroy", str(i)], shell=True)
        subprocess.check_call(["echo", str(i)], shell=True)

    #exception treatment:
    except subprocess.CalledProcessError as e:
        print ("Error on the program")
        subprocess.check_call("lttng stop", shell=True)
        subprocess.check_call(["lttng destroy", str(i)], shell=True)
        subprocess.check_call(["echo", str(i)], shell=True)
        #in case of execption, it will return -1:
        output = -1

    return output

# execute the program:
def exec_tbb(input_value):
   input = str(input_value)
   program = "LD_PRELOAD=/usr/local/lib/liblttng-ust-fork.so /home/frank/Desktop/Research/tbb/examples/parallel_do/parallel_preorder/parallel_preorder "
   subprocess.check_call(program + input, shell=True)

# execute the program:
def exec_program(program, input_value):
   input = str(input_value)
   subprocess.check_call(program + input, shell=True)

# execute the program:
def exec_analysis(input_value):
   input = str(input_value)
   program = "python multiple_regression.py "
   subprocess.check_call(program + input, shell=True)

#execution_fib(True, "../program_to_load_program", 5)

#exec_tbb(8)
trace("x", "/home/frank/Desktop/Research/tbb/examples/parallel_do/parallel_preorder/parallel_preorder", 1, [])
#exec_program("/home/frank/Desktop/Research/OpenCV/newTest/demo")