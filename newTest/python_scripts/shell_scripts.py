#Shell function:
import subprocess

#This function does the tracing, replacing the bash scripts:
def trace(image_name):
    season_name = " x "
    image = image_name #image = "../data/500x500.jpg"
    i = 10
    subprocess.check_call("lttng create"+season_name, shell=True)
    subprocess.check_call(["lttng enable-event -u -a", str(i)], shell=True)
    subprocess.check_call(["lttng enable-event -u sched_switch", str(i)], shell=True)
    subprocess.check_call(["lttng add-context -u -t perf:thread:page-fault", str(i)], shell=True)
    subprocess.check_call(["lttng add-context -u -t perf:thread:cache-misses", str(i)], shell=True)
    subprocess.check_call(["lttng add-context -u -t perf:thread:instructions", str(i)], shell=True)

    subprocess.check_call("lttng start" + season_name, shell=True)

    subprocess.check_call("LD_PRELOAD=/usr/local/lib/liblttng-ust-fork.so ../opencv "+ image , shell=True)

    subprocess.check_call("lttng stop", shell=True)
    subprocess.check_call(["lttng destroy", str(i)], shell=True)
    subprocess.check_call(["echo", str(i)], shell=True)

#calling the function
def run():
    trace("../data/500x500.jpg")

run()