import babeltrace.reader
import sys


# get the trace path from the first command line argument
trace_path = sys.argv[1]

#print path:
print (trace_path);

trace_collection = babeltrace.reader.TraceCollection()

trace_collection.add_trace(trace_path, 'ctf')

for event in trace_collection.events:
    print(event.name)