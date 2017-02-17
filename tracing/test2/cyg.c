#include <stdio.h>
#include <time.h>
#include <dlfcn.h>
#include <sys/types.h>

#define TRACEPOINT_DEFINE
#define TRACEPOINT_CREATE_PROBES

#include <cyg.h>

void __attribute__ ((constructor)) trace_begin (void)
{
}
 
void __attribute__ ((destructor)) trace_end (void)
{
	// printf("func_count = %lu\n", func_count);
}

void __cyg_profile_func_enter (void *func,  void *caller)
{
	printf("Entry %p\n", func);
        tracepoint(lttng_ust_cyg_profile, func_entry, func, caller);
	//func_count++;
        

}
 
void __cyg_profile_func_exit (void *func, void *caller)
{

	printf("Exit %p\n", func);
        tracepoint(lttng_ust_cyg_profile, func_exit, func, caller);
	//func_count++;
}
