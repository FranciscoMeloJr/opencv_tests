#Shell function:
import subprocess

#This function does the tracing, replacing the bash scripts:
def trace(image_name, id, program):
    season_name = " x "
    image = image_name #image = "../data/500x500.jpg"
    print(image_name)
    i = 10
    output = "--output=/tmp/ust-traces-python-" + str(id)

    #do the process:
    subprocess.check_call("lttng create"+ season_name + output, shell=True)
    subprocess.check_call(["lttng enable-event -u -a"], shell=True)
    subprocess.check_call(["lttng enable-event -u sched_switch"], shell=True)
    subprocess.check_call(["lttng add-context -u -t perf:thread:page-fault"], shell=True)
    subprocess.check_call(["lttng add-context -u -t perf:thread:cache-misses"], shell=True)
    subprocess.check_call(["lttng add-context -u -t perf:thread:instructions"], shell=True)

    subprocess.check_call("lttng start" + season_name, shell=True)

    try:
        # program execution:
        subprocess.check_output("LD_PRELOAD=/usr/local/lib/liblttng-ust-fork.so "+ program +" "+ image , shell=True)
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

#execute the program:
def exec_program():
    image = "../data/black/b500.jpg"
    subprocess.check_call("LD_PRELOAD=/usr/local/lib/liblttng-ust-fork.so ../opencv " + image, shell=True)

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
def run(flag, file, program):
    trace_data = 0
    ret = -1

    init = "../data/"
    init+=file
    if(flag):
        print (init)
    image_name = init
    trace_season = 3
    ret = trace(image_name, trace_season, program)

    return ret

def execution(flag, file, program):
    # execute a test calling the exec_program
    if(flag):
        print (execution)
    ret = run(flag, file, program)
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