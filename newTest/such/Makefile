CXX ?= g++
GCC = gcc
FLAGS = -pg
#-finstrument-functions
CXXFLAGS += -c -Wall $(shell pkg-config --cflags opencv) $(FLAGS)
LDFLAGS += $(-llttng-ust -ldl)

all:
	$(CXX) -c -I. hello-tp.c
	$(CXX) -c  display.cpp $(CXXFLAGS)
	$(CXX) -o opencv display.o hello-tp.o -llttng-ust -ldl -I/home/frank/opencv/v3.0.0/include -rdynamic /home/frank/opencv/v3.0.0/lib/libopencv_shape.so.3.0.0 /home/frank/opencv/v3.0.0/lib/libopencv_stitching.so.3.0.0 /home/frank/opencv/v3.0.0/lib/libopencv_superres.so.3.0.0 /home/frank/opencv/v3.0.0/lib/libopencv_videostab.so.3.0.0 /home/frank/opencv/v3.0.0/lib/libopencv_objdetect.so.3.0.0 /home/frank/opencv/v3.0.0/lib/libopencv_calib3d.so.3.0.0 /home/frank/opencv/v3.0.0/lib/libopencv_features2d.so.3.0.0 /home/frank/opencv/v3.0.0/lib/libopencv_flann.so.3.0.0 /home/frank/opencv/v3.0.0/lib/libopencv_highgui.so.3.0.0 /home/frank/opencv/v3.0.0/lib/libopencv_ml.so.3.0.0 /home/frank/opencv/v3.0.0/lib/libopencv_photo.so.3.0.0 /home/frank/opencv/v3.0.0/lib/libopencv_video.so.3.0.0 /home/frank/opencv/v3.0.0/lib/libopencv_videoio.so.3.0.0 /home/frank/opencv/v3.0.0/lib/libopencv_imgcodecs.so.3.0.0 /home/frank/opencv/v3.0.0/lib/libopencv_imgproc.so.3.0.0 /home/frank/opencv/v3.0.0/lib/libopencv_core.so.3.0.0 -Wl,-rpath,/home/frank/opencv/v3.0.0/lib

clean: ; rm -f *.o opencv





