/******************************
 *
 *	TimingTest for OpenCV's C interface, by Shervin Emami, June 5th 2011 (www.shervinemami.info)
 *
 ******************************/

#include <iostream>

#include <cv.h>								// Include OpenCV (any version)
#include <highgui.h>						// Include HighGUI (any version)
//#include <opencv2/highgui/highgui.hpp>	// Include OpenCV & HighGUI (v2.2)

using namespace std;


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
	cout << "TimingTest (C version)." << endl;
	cout << "This program was compiled on " __TIMESTAMP__ << endl;
	cout << "OpenCV version: " << CV_VERSION << endl;

	const char* filename = argc > 1 ? argv[1] : "lena.jpg";

	cvNamedWindow("Output");
	CvMemStorage* storage = cvCreateMemStorage(0);

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
		IplImage *img = cvLoadImage( filename, CV_LOAD_IMAGE_COLOR );
		if (!img) {
			cerr << "Can't open image file: " << filename << endl;
			return 1;
		}
		STOP_TIMING(loadFile);

		// Convert to grayscale
		START_TIMING(grayscale);
		IplImage *gray = cvCreateImage(cvGetSize(img), 8, 1);
		cvCvtColor(img, gray, CV_BGR2GRAY);
		STOP_TIMING(grayscale);

		// Find edges.
		START_TIMING(findEdges);
		IplImage *edges = cvCreateImage(cvGetSize(img), 8, 1);
		cvCanny(gray, edges, 50, 200);
		STOP_TIMING(findEdges);

		// Find lines.
		START_TIMING(findLines);
		CvSeq* lines = 0;
		cvClearMemStorage( storage );		// clear memory storage - reset free space position
		lines = cvHoughLines2( edges, storage, CV_HOUGH_PROBABILISTIC, 1, CV_PI/180, 50, 50, 10 );
		for( int i = 0; i < lines->total; i++ )
		{
			CvPoint* line = (CvPoint*)cvGetSeqElem(lines,i);
			cvLine( edges, line[0], line[1], CV_RGB(200,200,200), 3, CV_AA, 0 );
		}
		STOP_TIMING(findLines);

		// Only show the output on the 1st iteration
		if (iter == 0) {
			cvShowImage("Output", edges);
			cvWaitKey(20);
		}

		cvReleaseImage(&edges);
		cvReleaseImage(&gray);
		cvReleaseImage(&img);
	}
	STOP_TIMING(wholeCode);

	// Show the timing results
	SHOW_TIMING(wholeCode, "Whole operation");
	SHOW_TIMING(loadFile, "Load image file");
	SHOW_TIMING(grayscale, "Grayscale conversion");
	SHOW_TIMING(findEdges, "Find edges");
	SHOW_TIMING(findLines, "Find lines");

	cvReleaseMemStorage(&storage);

	return 0;
}