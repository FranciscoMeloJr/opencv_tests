#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> /* for fork */
#include <sys/types.h> /* for pid_t */
#include <sys/wait.h> /* for wait */
#include <ctime>
#include <iostream>

int main()
{
    /*Spawn a child to run the program.*/
    int i =0;
       
    for(i=0;i<10;i++){
         
    	pid_t pid=fork();
        clock_t begin = clock();

    	if (pid==0) { /* child process */
                
        	static char *argv[]={"obama.jpg"};
                execv("DisplayImage3.0",argv);
        	exit(127); /* only if execv fails */
    	}
    	else { /* pid!=0; parent process */
        	waitpid(pid,0,0); /* wait for child to exit */
    	}
        clock_t end = clock();
        double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
        std::cout << elapsed_secs/10;
    }
    return 0;
}
