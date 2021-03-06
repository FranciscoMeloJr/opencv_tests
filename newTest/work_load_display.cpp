#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> /* for fork */
#include <sys/types.h> /* for pid_t */
#include <sys/wait.h> /* for wait */
#include <ctime>
#include <iostream>
#include "hello-tp.h" //for the tracing point

#define tic(start) clock_gettime(CLOCK_MONOTONIC, &start)
#define toc(end) clock_gettime(CLOCK_MONOTONIC, &end)
#define elapsed_nsec(start, end) (end.tv_nsec + 1E9 * end.tv_sec) - (start.tv_nsec + 1E9 * start.tv_sec)

using namespace std;

int main( int argc, char** argv )
{
    /*Spawn a child to run the program.*/
    
    if( argc != 2)
    {
     cout <<" Usage: program_to_test input_file" << endl;
     return -1;
    }

    
    struct timespec t_start, t_end;
    pid_t pid=fork();
    unsigned long int time_elapsed = 0;

    tic(t_start);//clock_t begin = clock();

    if (pid==0) { /* child process */
                
                tracepoint(hello_world, my_first_tracepoint, 3, "hough");
                execv("../Houghlines/HoughLines", argv); //../DisplayImage/DisplayProject
                tracepoint(hello_world, my_first_tracepoint, 3, "hough");
                exit(127); /* only if execv fails */
    }
    else { /* pid!=0; parent process */
                waitpid(pid,0,0); /* wait for child to exit */
    }
    toc(t_end);//clock_t end = clock();
    time_elapsed = elapsed_nsec(t_start, t_end); //double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    string s = argv[1];
    string result = s.substr (s.length()-7,3); 
    //string token = s.substr(0, s.find(delimiter));
    std::cout << "0"  <<"," << time_elapsed  << "," << result  <<"," << "hough" << endl;
       
    return 0;
}
