CPP = g++

# OpenCV trunk
CPPFLAGS = -L/home/frank/opencv/v3.0.0 \
	   -I/home/frank/opencv/include

FLAGS += -pg \
-finstrument-functions

# Opencv 2.4.8
#CPPFLAGS = -L/home/krystof/libs/opencv-2.4.8/release/installed/libs \
	   -I/home/krystof/libs/opencv-2.4.8/release/installed/include

all: make_test

make_test: main_make.cpp
	$(CPP) $(CPPFLAGS) $(FLAGS) $^ -o $@
