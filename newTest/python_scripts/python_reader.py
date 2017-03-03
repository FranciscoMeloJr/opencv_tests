# This module calls the reading module
import babeltrace.reader
import sys

#Calculte the elapse for each metric:
def read(trace_path, info):
    print("Read");
    print (trace_path);
    info_data = []
    trace_collection = babeltrace.reader.TraceCollection()

    trace_collection.add_trace(trace_path, 'ctf')

    for event in trace_collection.events:
        if(event.name == 'hello_world:my_first_tracepoint'):
            print("event name: %s timestamp %d." % (event.name, event.timestamp))

            fields = dict()
            i = 0
            for k, v in event.items():
                field = event._field(k)
                if(field.name == info):
                    #print("field %s %s", info, field.value);
                    info_data.append(field.value)
                    print("elapsed %s", info, info_data);
                i = i + 1

    #shows the information:
    print(info_data[1]- info_data[0])

