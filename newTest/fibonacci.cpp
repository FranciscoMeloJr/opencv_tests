#include <iostream>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main ( int argc, char *argv[] )
{
   int nextTerm = 0;
    if ( argc != 2 ) // argc should be 2 for correct execution
       // We print argv[0] assuming it is the program name
       cout<<"usage: "<< argv[0] <<" <n series>\n";
    else {
         int n, t1 = 0, t2 = 1;

 	    //cout << "Enter the number of terms: ";
	    //cin >> n;
	    n = atoi(argv[1]);
	
	    //cout << "Fibonacci Series: ";
	
	    for (int i = 1; i <= n; ++i)
	    {
	        // Prints the first two terms.
	        if(i == 1)
	        {
	            //cout << " " << t1;
	            continue;
	        }
	        if(i == 2)
	        {
	            //cout << t2 << " ";
	            continue;
	        }
	        nextTerm = t1 + t2;
	        t1 = t2;
	        t2 = nextTerm;
	        
	        //cout << nextTerm << " ";
    		}
    }	
   //cout << nextTerm;   
   fflush(stdout);
   return nextTerm;
}
