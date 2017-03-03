import babeltrace.reader
import sys

#print path:
def read(trace_path):
    print("Read");
    print (trace_path);

    trace_collection = babeltrace.reader.TraceCollection()

    trace_collection.add_trace(trace_path, 'ctf')

    for event in trace_collection.events:
        if(event.name == 'hello_world:my_first_tracepoint'):
            print("event name: %s timestamp %d." % (event.name, event.timestamp, event.))