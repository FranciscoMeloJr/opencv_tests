/******************************
 *
 *	TimingTest for OpenCV's C++ interface by Shervin Emami, June 5th 2011 (www.shervinemami.info)
 *
 ******************************/

#include <iostream>

#include <cv.h>						// Include OpenCV (any version)
#include <highgui.h>					// Include HighGUI (any version)
//#include <opencv2/opencv.hpp>	// Include OpenCV & HighGUI (v2.2)
//#include <opencv2/highgui/highgui.hpp>	// Include OpenCV & HighGUI (v2.2)

using namespace std;
using namespace cv;


//------------------------------------------------------------------------------
// Timer functions
//------------------------------------------------------------------------------
// Record the execution time of some code, in milliseconds. By Shervin Emami, May 4th 2011.
// eg:
//	DECLARE_TIMING(myTimer);
//	START_TIMING(myTimer);
//	  printf("A slow calc = %f\n", 1.0/sqrt(2.0) );
//	STOP_TIMING(myTimer);
//	printf("Execution time: %f ms.\n", GET_TIMING(myTimer) );
//	printf("Average time: %f ms per iteration.\n", GET_AVERAGE_TIMING(myTimer) );
//  SHOW_TIMING(myTimer, "My Timer");
#define DECLARE_TIMING(s)		int64 timeStart_##s; int64 timeDiff_##s; int64 timeTally_##s = 0; int64 countTally_##s = 0
#define START_TIMING(s)			timeStart_##s = cvGetTickCount()
#define STOP_TIMING(s)			timeDiff_##s = (cvGetTickCount() - timeStart_##s); timeTally_##s += timeDiff_##s; countTally_##s++
#define GET_TIMING(s)			(double)(0.001 * ( (double)timeDiff_##s / (double)cvGetTickFrequency() ))
#define GET_AVERAGE_TIMING(s)	(double)(countTally_##s ? 0.001 * ( (double)timeTally_##s / ((double)countTally_##s * cvGetTickFrequency()) ) : 0)
#define GET_TIMING_COUNT(s)		(int)(countTally_##s)
#define CLEAR_AVERAGE_TIMING(s)	timeTally_##s = 0; countTally_##s = 0
#define SHOW_TIMING(s, msg)		printf("%s time: \t %dms \t (%dms average across %d runs).\n", msg, cvRound(GET_TIMING(s)), cvRound(GET_AVERAGE_TIMING(s)), GET_TIMING_COUNT(s) )



int main(int argc, const char *argv[])
{
	cout << "TimingTest (C++ version)." << endl;
	cout << "This program was compiled on " __TIMESTAMP__ << endl;
	cout << "OpenCV version: " << CV_VERSION << endl;

	const char* filename = argc > 1 ? argv[1] : "lena.jpg";

	namedWindow("Output", CV_WINDOW_AUTOSIZE);

	DECLARE_TIMING(wholeCode);
	DECLARE_TIMING(loadFile);
	DECLARE_TIMING(grayscale);
	DECLARE_TIMING(findEdges);
	DECLARE_TIMING(findLines);


	// Run a test many times, so we can get averaged results.
	int iterations = 100;
	START_TIMING(wholeCode);
	for (int iter=0; iter<iterations; iter++) {

		// Load the (same) image
		START_TIMING(loadFile);
		Mat img = imread( filename, CV_LOAD_IMAGE_COLOR );
		if (!img.data) {
			cerr << "Can't open image file: " << filename << endl;
			return 1;
		}
		STOP_TIMING(loadFile);

		// Convert to grayscale.
		START_TIMING(grayscale);
		Mat gray;
		cvtColor(img, gray, CV_BGR2GRAY);
		STOP_TIMING(grayscale);

		// Find edges.
		START_TIMING(findEdges);
		Mat edges;
		Canny(gray, edges, 50, 200);
		STOP_TIMING(findEdges);

		// Find lines.
		START_TIMING(findLines);
		vector<Vec4i> lines;
		HoughLinesP(edges, lines, 1, CV_PI/180, 50, 50, 10 );
		for( size_t i = 0; i < lines.size(); i++ )
		{
			Vec4i l = lines[i];
			line( edges, Point(l[0], l[1]), Point(l[2], l[3]), Scalar(200,200,200), 3, CV_AA);
		}
		STOP_TIMING(findLines);

		// Only show the output on the 1st iteration
		if (iter == 0) {
			imshow("Output", edges);
			waitKey(20);
		}

	}
	STOP_TIMING(wholeCode);

	// Show the timing results
	SHOW_TIMING(wholeCode, "Whole operation");
	SHOW_TIMING(loadFile, "Load image file");
	SHOW_TIMING(grayscale, "Grayscale conversion");
	SHOW_TIMING(findEdges, "Find edges");
	SHOW_TIMING(findLines, "Find lines");


	return 0;
}