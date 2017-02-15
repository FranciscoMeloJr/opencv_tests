#!/bin/bash

# Display tracing:
STRING="Display tracing test"
echo $STRING

lttng create
lttng enable-event --userspace -all
lttng start

./test1/make_test

lttng stop
lttng destroy

