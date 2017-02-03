#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"

#include <iostream>

//Tests
#define DECLARE_TIMING(s)	int64 timeStart_##s; int64 timeDiff_##s; int64 timeTally_##s = 0; int64 countTally_##s = 0
#define START_TIMING(s)		timeStart_##s = cvGetTickCount()
#define STOP_TIMING(s)		timeDiff_##s = (cvGetTickCount() - timeStart_##s); timeTally_##s += timeDiff_##s; countTally_##s++
#define GET_TIMING(s)		(double)(0.001 * ( (double)timeDiff_##s / (double)cvGetTickFrequency() ))
#define GET_AVERAGE_TIMING(s)	(double)(countTally_##s ? 0.001 * ( (double)timeTally_##s / ((double)countTally_##s * cvGetTickFrequency()) ) : 0)
#define GET_TIMING_COUNT(s)	(int)(countTally_##s)
#define CLEAR_AVERAGE_TIMING(s)	timeTally_##s = 0; countTally_##s = 0
#define SHOW_TIMING(s, msg)	printf("%s time: \t %dms \t (%dms average across %d runs).\n", msg, cvRound(GET_TIMING(s)), cvRound(GET_AVERAGE_TIMING(s)), GET_TIMING_COUNT(s) )


using namespace cv;
using namespace std;

static void help()
{
    cout << "\nThis program demonstrates line finding with the Hough transform.\n"
            "Usage:\n"
            "./houghlines <image_name>, Default is ../data/pic1.png\n" << endl;
}

int main(int argc, char** argv)
{
    cv::CommandLineParser parser(argc, argv,
        "{help h||}{@image|../data/pic1.png|}"
    );
    if (parser.has("help"))
    {
        help();
        return 0;
    }
    string filename = parser.get<string>("@image");
    if (filename.empty())
    {
        help();
        cout << "no image_name provided" << endl;
        return -1;
    }
    Mat src = imread(filename, 0);
    if(src.empty())
    {
        help();
        cout << "can not open " << filename << endl;
        return -1;
    }
    
    //change:
    DECLARE_TIMING(wholeCode);

    Mat dst, cdst;
    Canny(src, dst, 50, 200, 3);
    cvtColor(dst, cdst, COLOR_GRAY2BGR);

#if 0
    vector<Vec2f> lines;
    HoughLines(dst, lines, 1, CV_PI/180, 100, 0, 0 );
    for( size_t i = 0; i < lines.size(); i++ )
    {
        float rho = lines[i][0], theta = lines[i][1];
        Point pt1, pt2;
        double a = cos(theta), b = sin(theta);
        double x0 = a*rho, y0 = b*rho;
        pt1.x = cvRound(x0 + 1000*(-b));
        pt1.y = cvRound(y0 + 1000*(a));
        pt2.x = cvRound(x0 - 1000*(-b));
        pt2.y = cvRound(y0 - 1000*(a));
        line( cdst, pt1, pt2, Scalar(0,0,255), 3, CV_AA);
    }
#else
    vector<Vec4i> lines;
    HoughLinesP(dst, lines, 1, CV_PI/180, 50, 50, 10 );
    for( size_t i = 0; i < lines.size(); i++ )
    {
        Vec4i l = lines[i];
        line( cdst, Point(l[0], l[1]), Point(l[2], l[3]), Scalar(0,0,255), 3, LINE_AA);
    }
#endif
    imshow("source", src);
    imshow("detected lines", cdst);

    STOP_TIMING(wholeCode);

    waitKey();
    SHOW_TIMING(wholeCode, "Whole operation");

        
    return 0;
}
