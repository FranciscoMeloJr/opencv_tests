#Shell function:
import subprocess

#This function does the tracing, replacing the bash scripts:
def trace(image_name, id):
    season_name = " x "
    image = image_name #image = "../data/500x500.jpg"
    print(image_name)
    i = 10
    output = "--output=/tmp/ust-traces-python-" + str(id)

    #do the process:
    subprocess.check_call("lttng create"+season_name + output, shell=True)
    subprocess.check_call(["lttng enable-event -u -a", str(i)], shell=True)
    subprocess.check_call(["lttng enable-event -u sched_switch", str(i)], shell=True)
    subprocess.check_call(["lttng add-context -u -t perf:thread:page-fault", str(i)], shell=True)
    subprocess.check_call(["lttng add-context -u -t perf:thread:cache-misses", str(i)], shell=True)
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

#execute the program:
def exec_program():
    image = "../data/500x500.jpg"
    subprocess.check_call("LD_PRELOAD=/usr/local/lib/liblttng-ust-fork.so ../opencv " + image, shell=True)

#calling the function
def run(id, flag):
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
def run_png(id, flag, letter):
    trace_data = 0
    ret = -1

    init = "../data/"
    init+=letter
    init+=str(id)
    init+="x"
    init += str(id)
    init+=".png"
    if(flag):
        print (init)
    trace_data = init
    ret = trace(trace_data, 3)

    if(id == 10):
        # run(500)
        i = 0
        while (i < 10):
            exec_program()
            i += 1
    return ret

def execution(exe, flag, letter):
    # execute a test calling the exec_program
    if(flag):
        print (execution)
    ret = run_png(exe, flag, letter)
    if (ret is not -1):
        print("Open the file: ", ret[9:])
        return ret[9:]
    else:
        print("An error just occured")
        return -1











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