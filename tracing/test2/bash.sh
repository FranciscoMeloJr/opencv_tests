lttng create
lttng enable-event -u -a
lttng start
./opencv_test1 
lttng stop
lttng destroy

