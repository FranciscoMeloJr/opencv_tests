#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> /* for fork */
#include <sys/types.h> /* for pid_t */
#include <sys/wait.h> /* for wait */
#include <ctime>
#include <iostream>
#include "hello-tp.h" //for the tracing point

static struct timespec ts_start, ts_end;
#define tic(start) clock_gettime(CLOCK_MONOTONIC, &start)
#define toc(end) clock_gettime(CLOCK_MONOTONIC, &end)
#define elapsed_nsec(start, end) (end.tv_nsec + 1E9 * end.tv_sec) - (start.tv_nsec + 1E9 * start.tv_sec)

using namespace std;

int main( int argc, char** argv )
{
    /*Spawn a child to run the program.*/
    int i =0;
    if( argc != 2)
    {
     cout <<" Usage: display_image ImageToLoadAndDisplay" << endl;
     return -1;
    }

    
    struct timespec t_start, t_end;
    pid_t pid=fork();
    unsigned long int time_elapsed = 0;

    tic(t_start);//clock_t begin = clock();

    if (pid==0) { /* child process */

                static char *argv[]={"obama.jpg"};
                tracepoint(hello_world, my_first_tracepoint, 3, "display");
                execv("DisplayImage3.0",argv);
                tracepoint(hello_world, my_first_tracepoint, 3, "display");
                exit(127); /* only if execv fails */
    }
    else { /* pid!=0; parent process */
                waitpid(pid,0,0); /* wait for child to exit */
    }
    toc(t_end);//clock_t end = clock();
    time_elapsed = elapsed_nsec(t_start, t_end); //double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    string s = argv[1];
    string result = s.substr (8,3); 
    //string token = s.substr(0, s.find(delimiter));
    std::cout << 0  <<"," << time_elapsed  << "," << result  <<"," << "Display" ;
    
    return 0;
}
