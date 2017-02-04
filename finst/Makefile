CPP = g++

# OpenCV trunk
CPPFLAGS = -L/home/frank/opencv/v3.0.0 \
	   -I/home/frank/opencv/include

FLAGS += -finstrument-functions

all: make_test

make_test: main_make.cpp
	$(CPP) $(CPPFLAGS) $(FLAGS) $^ -o $@
