#include <stdio.h>

void __cyg_profile_func_enter (void *func,  void *caller)
{
      printf("Entry %p\n", func);
 //       tracepoint(lttng_ust_cyg_profile, func_entry, func, caller);
}

void __cyg_profile_func_exit (void *func, void *caller)
{

     printf("Exit %p\n", func);
//        tracepoint(lttng_ust_cyg_profile, func_exit, func, caller);
}

