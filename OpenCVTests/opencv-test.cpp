#include "/home/frank/Desktop/opencv/include/opencv2/opencv.hpp"
//#include <opencv2/core/core.hpp>
//#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <ctime>

using namespace cv;
using namespace std;


//Display:
std::clock_t display(String filename, int counter = 100){
    Mat image;
    image = imread(filename, CV_LOAD_IMAGE_COLOR);   // Read the file

    if(! image.data )                              // Check for invalid input
    {
        cout <<  "Could not open or find the image" << std::endl ;
        return NULL;
    }

    namedWindow( "Display window", WINDOW_AUTOSIZE );// Create a window for display.
    clock_t acc = 0;
    for(int i = 0; i< counter; i++){
        std::clock_t start;
        imshow( "Display window", image );
        clock_t end = (std::clock() - start);
        acc+=end;
    }
    acc/=counter;
    return acc;
}

//Hough Lines:
std::clock_t houghlines(String filename, int counter = 100)
{
    Mat src = imread(filename, 0);
    if(src.empty())
    {
        cout << "can not open " << filename << endl;
        return NULL;
    }

    Mat dst, cdst;
    Canny(src, dst, 50, 200, 3);
    cvtColor(dst, cdst, COLOR_GRAY2BGR);

    vector<Vec4i> lines;
    clock_t start = std::clock();
    HoughLinesP(dst, lines, 1, CV_PI/180, 50, 50, 10 );
    clock_t end = (std::clock() - start);
    return end;
}

//Face Detection:
std::clock_t face_detection(String filename, int counter = 100)
{
    Mat src = imread(filename, 0);
    if(src.empty())
    {
        cout << "can not open " << filename << endl;
        return NULL;
    }

    Mat dst, cdst;
    Canny(src, dst, 50, 200, 3);
    cvtColor(dst, cdst, COLOR_GRAY2BGR);

    vector<Vec4i> lines;
    clock_t start = std::clock();

    /*cout << "Detecting face(s) in " << inputName << endl;
            if( !image.empty() )
            {
                detectAndDraw( image, cascade, nestedCascade, scale, tryflip );
                waitKey(0);
            }

    */
    clock_t end = (std::clock() - start);
    return end;
}

int main( int argc, char** argv )
{
    if( argc <= 2)
    {
        cout <<" Usage: <command_name> <filename.jog>" << endl;
        cout <<" Usage: <display_image>" << endl;
        cout <<" Usage: <hough_lines>" << endl;
        cout <<" Usage: <face_detection>" << endl;
        return 0;
    }

    String command = argv[1];
    String filename = argv[2];
    int counter = NULL;
    if(argv[3]!=NULL){
        counter = atoi(argv[3]);
    }
    clock_t elapsed_time = NULL;

    if(command.compare("display_image") == 0 ){
            cout << "<display_image>" << endl;
            elapsed_time = display(filename, counter);
    }
    if(command.compare("hough_lines") == 0 ){
            cout <<"<hough_lines>" << endl;
            elapsed_time = houghlines(filename, counter);
    }

    if(command.compare("face_detection") == 0 ){
            cout <<"<face_detection>" << endl;
            elapsed_time = face_detection(filename, counter);
    }
    if(command.size() == 0 ){
        cout << command << " command not found" << endl;
        return 0;
    }
    if(counter != NULL){
        std::cout << command << " elapsed time: " << elapsed_time << " ns in" << counter << " times "<< std::endl;
    }
    else{
        std::cout << command << " elapsed time: " << elapsed_time << " ns in 100 times" << std::endl;
    }

    return 0;
}


