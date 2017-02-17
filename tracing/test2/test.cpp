#include <stdio.h>

void __cyg_profile_func_enter (void *func,  void *caller)
{
      printf("Entry %d\n", 0);
 //       tracepoint(lttng_ust_cyg_profile, func_entry, func, caller);
}

void __cyg_profile_func_exit (void *func, void *caller)
{

      printf("Exit %d\n", 1);
//        tracepoint(lttng_ust_cyg_profile, func_exit, func, caller);
}

