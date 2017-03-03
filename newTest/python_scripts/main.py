#calls the reading
import python_reader
import sys
# This module calls the reading module
trace_path1 = "/tmp/test1/data/500x500.jpg-pf-1/ust/uid/1000/64-bit"
trace_path2 = "/tmp/ust-traces--pf-9/ust/uid/1000/64-bit"

python_reader.read(trace_path2, "perf_thread_page_fault")
python_reader.read(trace_path2, "perf_thread_cache_misses")
python_reader.read(trace_path2, "perf_thread_instructions")