#include "/home/frank/Desktop/opencv/include/opencv2/opencv.hpp"
//#include <opencv2/core/core.hpp>
//#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <ctime>
#include <fstream>

using namespace cv;
using namespace std;


//Display:
std::clock_t display(String filename){
    Mat image;
    image = imread(filename, CV_LOAD_IMAGE_COLOR);   // Read the file

    if(! image.data )                              // Check for invalid input
    {
        cout <<  "Could not open or find the image" << std::endl ;
        return NULL;
    }

    namedWindow( "Display window", WINDOW_AUTOSIZE );// Create a window for display.
    std::clock_t start;
    imshow( "Display window", image );
    clock_t end = (std::clock() - start);

    return end;
}

//Hough Lines:
std::clock_t houghlines(String filename)
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
//Help:
void help(){

        cout <<" Help " << endl;
        cout <<" Usage: <command_name> <filename.jpg>" << endl;
        cout <<" Usage: <display_image>" << endl;
        cout <<" Usage: <hough_lines>" << endl;
        cout <<" Usage: <face_detection>" << endl;
        cout <<" Usage: <version>" << endl;
        return;

}
//Detect and Draw:
double detectFace( Mat& img, CascadeClassifier& cascade, CascadeClassifier& nestedCascade,
                    double scale )
{
    double t = 0;
    vector<Rect> faces;
    const static Scalar colors[] =
    {
        Scalar(255,0,0),
        Scalar(255,128,0),
        Scalar(255,255,0),
        Scalar(0,255,0),
        Scalar(0,128,255),
        Scalar(0,255,255),
        Scalar(0,0,255),
        Scalar(255,0,255)
    };
    Mat gray, smallImg;

    cvtColor( img, gray, COLOR_BGR2GRAY );
    double fx = 1 / scale;
    resize( gray, smallImg, Size(), fx, fx, INTER_LINEAR );
    equalizeHist( smallImg, smallImg );

    t = (double)getTickCount();
    cascade.detectMultiScale( smallImg, faces,
        1.1, 2, 0
        //|CASCADE_FIND_BIGGEST_OBJECT
        //|CASCADE_DO_ROUGH_SEARCH
        |CASCADE_SCALE_IMAGE,
        Size(30, 30) );
    t = (double)getTickCount() - t;
    cout << "detection time = "<< t*1000/getTickFrequency()<<"ms\n" ;
    for ( size_t i = 0; i < faces.size(); i++ )
    {
        Rect r = faces[i];
        Mat smallImgROI;
        vector<Rect> nestedObjects;
        Point center;
        Scalar color = colors[i%8];
        int radius;

        double aspect_ratio = (double)r.width/r.height;
        if( 0.75 < aspect_ratio && aspect_ratio < 1.3 )
        {
            center.x = cvRound((r.x + r.width*0.5)*scale);
            center.y = cvRound((r.y + r.height*0.5)*scale);
            radius = cvRound((r.width + r.height)*0.25*scale);
            circle( img, center, radius, color, 3, 8, 0 );
        }
        else
            rectangle( img, cvPoint(cvRound(r.x*scale), cvRound(r.y*scale)),
                       cvPoint(cvRound((r.x + r.width-1)*scale), cvRound((r.y + r.height-1)*scale)),
                       color, 3, 8, 0);
        if( nestedCascade.empty() )
            continue;
        smallImgROI = smallImg( r );
        nestedCascade.detectMultiScale( smallImgROI, nestedObjects,
            1.1, 2, 0
            //|CASCADE_FIND_BIGGEST_OBJECT
            //|CASCADE_DO_ROUGH_SEARCH
            //|CASCADE_DO_CANNY_PRUNING
            |CASCADE_SCALE_IMAGE,
            Size(30, 30) );
        for ( size_t j = 0; j < nestedObjects.size(); j++ )
        {
            Rect nr = nestedObjects[j];
            center.x = cvRound((r.x + nr.x + nr.width*0.5)*scale);
            center.y = cvRound((r.y + nr.y + nr.height*0.5)*scale);
            radius = cvRound((nr.width + nr.height)*0.25*scale);
            circle( img, center, radius, color, 3, 8, 0 );
        }
    }
    return t;
}
//Face Detection:
std::clock_t face_detection(String filename)
{
    Mat src = imread(filename, 1);
    if(src.empty())
    {
        cout << "can not open " << filename << endl;
        return NULL;
    }

    Mat dst, cdst;
    Canny(src, dst, 50, 200, 3);
    cvtColor(dst, cdst, COLOR_GRAY2BGR);

    CascadeClassifier cascade, nestedCascade;
    string cascadeName = "../data/haarcascades/haarcascade_frontalface_alt.xml";
    string nestedCascadeName = "../data/haarcascades/haarcascade_eye_tree_eyeglasses.xml";

    double scale = 1;
    clock_t start = std::clock();
    if ( !nestedCascade.load( nestedCascadeName ) )
        cerr << "WARNING: Could not load classifier cascade for nested objects" << endl;
    if( !cascade.load( cascadeName ) )
    {
        cerr << "ERROR: Could not load classifier cascade" << endl;
        help();
        return -1;
    }
    cout << "Detecting face(s) in " << filename << endl;
    if( !src.empty() )
    {
        detectFace( src, cascade, nestedCascade, scale );
    }

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

//Keys:
const char* keys =
{
    "{help h||}{@command c |version|command}{@image i|../data/obama.jpg|input image file}{@counter n| 100 |number of times to run}{@output o| null |save to a file}"

};
//Select command:
static std::clock_t execute_command(string command = "version", String filename = "../data/obama.jpg", int counter = 100, bool output = false)
{
    clock_t elapsed_time = NULL;
    std::ostringstream oss;

    if(command.compare("display_image") == 0 ){
            cout << "<display_image>" << endl;
            for(int i = 0 ; i < counter; i++){
                elapsed_time = display(filename);
                std::cout << command << " elapsed time: " << elapsed_time << " ns in " << counter << " times "<< std::endl;
                oss << elapsed_time << "\n";
            }
    }
    if(command.compare("hough_lines") == 0 ){
            cout <<"<hough_lines>" << endl;
            cout << filename << endl;
            for(int i = 0 ; i < counter; i++){
                elapsed_time = houghlines(filename);
                std::cout << command << " elapsed time: " << elapsed_time << " ns in " << counter << " times "<< std::endl;
                oss <<  elapsed_time << "\n";
            }
    }

    if(command.compare("face_detection") == 0 ){
            cout <<"<face_detection>" << endl;
            for(int i = 0 ; i < counter; i++){
                elapsed_time = face_detection(filename);
                std::cout << command << " elapsed time: " << elapsed_time << " ns in " << counter << " times "<< std::endl;
                oss << elapsed_time << "\n";
            }
    }
    if(command.compare("version") == 0 ){
        cout << "\tUsing OpenCV version " << CV_VERSION << "\n" << endl;
    }
    if(command.size() == 0 ){
        cout << command << " use a command or help" << endl;
        return 0;
    }

    if(output)
    {
        std::string intro = "\tUsing OpenCV version ";
        std::string s = CV_VERSION;
        intro.append(s + "\n");
        std::string content = oss.str();
        write_file( intro +" "+content);
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

        String inputCommand = parser.get<String>(0);
        String inputImage = parser.get<String>(1);
        int inputTimes = parser.get<int>(2);
        bool output = parser.get<bool>(3);

        if (!parser.check())
        {
                parser.printErrors();
                return -1;
        }
        execute_command(inputCommand,inputImage,inputTimes, output);

    }
    catch (int e)
     {
        cout << "An exception occurred. Exception Nr. " << e << '\n';
     }

    return 0;
}


