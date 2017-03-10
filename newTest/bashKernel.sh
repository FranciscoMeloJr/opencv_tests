
lttng create $1 --$e
lttng enable-event -u -a
#./opencv_example 
lttng enable-event -u sched_switch
lttng add-context -u -t perf:thread:page-fault
#lttng add-context -u -t perf:thread:cache-misses 
#lttng add-context -u -t perf:thread:instructions 

lttng start

python3 python

lttng stop
lttng destroy

