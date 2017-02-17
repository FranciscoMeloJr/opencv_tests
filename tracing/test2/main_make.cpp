#include <iostream>
#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/core/version.hpp"
#include <stdlib.h>
#include <unistd.h> /* for fork */
#include <sys/types.h> /* for pid_t */
#include <sys/wait.h> /* for wait */
#include <ctime>
#include <stdio.h>
using namespace cv;
using namespace std;


int display(int argc, char ** argv){

  if( argc != 2)
    {
     cout <<" Usage: display_image ImageToLoadAndDisplay" << endl;
     return -1;
    }

    Mat image;
    image = imread(argv[1], CV_LOAD_IMAGE_COLOR);   // Read the file

    if(! image.data )                              // Check for invalid input
    {
        cout <<  "Could not open or find the image" << std::endl ;
        return -1;
    }

    namedWindow( "Display window", WINDOW_AUTOSIZE );// Create a window for display.
    imshow( "Display window", image );                   // Show our image inside it.

    waitKey(0);                                          // Wait for a keystroke in the window
    return 0;
}

int main(int argc, char ** argv)
{
  std::cout << "OpenCV version: "
			<< CV_MAJOR_VERSION << "." 
			<< CV_MINOR_VERSION << "."
			<< CV_SUBMINOR_VERSION
			<< std::endl;
  int ret = 0;
  ret = display(argc, argv);
  return ret;
}

