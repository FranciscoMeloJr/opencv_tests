lttng create
lttng enable-event -u -a
lttng start
#./opencv_example 
./main 
lttng stop
lttng destroy

