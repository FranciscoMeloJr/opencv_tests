#include "/home/frank/Desktop/opencv/include/opencv2/opencv.hpp"
//#include <opencv2/core/core.hpp>
//#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <ctime>
#include <fstream>

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
    clock_t acc = 0;
    for(int i = 0; i< counter; i++){
        clock_t start = std::clock();
        HoughLinesP(dst, lines, 1, CV_PI/180, 50, 50, 10 );
        clock_t end = (std::clock() - start);
        acc+=end;
    }
    acc/=counter;
    return acc;
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

//Write to file:
int write_file (String content) {
  ofstream myfile;
  myfile.open("outputfile.txt");
  myfile << content;
  myfile.close();
  return 0;
}

//Help:
void help(){

        cout <<" Help " << endl;
        cout <<" Usage: <command_name> <filename.jog>" << endl;
        cout <<" Usage: <display_image>" << endl;
        cout <<" Usage: <hough_lines>" << endl;
        cout <<" Usage: <face_detection>" << endl;
        cout <<" Usage: <version>" << endl;
        return;

}
//Keys:
const char* keys =
{
    "{help h||}{@command|version|command}{@image|../data/obama.jpg|input image file}{@counter n| 100 |number of times to run}{@output w| null |save to a file}"

};
//Select command:
static std::clock_t execute_command(string command, String filename, int counter, String outputFile)
{
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
    if(command.compare("version") == 0 ){
        cout << "\tUsing OpenCV version " << CV_VERSION << "\n" << endl;
    }
    if(command.size() == 0 ){
        cout << command << " use a command or help" << endl;
        return 0;
    }

    return elapsed_time;
}

//Main:
int main( int argc, char** argv )
{
    try{

        cv::CommandLineParser parser(argc, argv, keys);
        parser.about("OpenCv Tests v1.0.0");

        if (parser.has("help"))
        {
            help();
            return 0;
        }

        String inputCommand = parser.get<String>("@command");
        String inputImage = parser.get<String>("@image");
        int inputTimes = parser.get<int>("@counter");
        String outputFile = parser.get<String>("@output");

        String command = inputCommand;

        std::clock_t elapsed_time = execute_command(inputCommand,inputImage,inputTimes, outputFile);
        std::cout << command << " elapsed time: " << elapsed_time << " ns in " << inputTimes << " times "<< std::endl;


    }
    catch (int e)
     {
        cout << "An exception occurred. Exception Nr. " << e << '\n';
     }

    return 0;
}


