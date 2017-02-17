CXX ?= g++
GCC = gcc
FLAGS = -pg
#-finstrument-functions
CXXFLAGS += -c -Wall $(shell pkg-config --cflags opencv) $(FLAGS)
LDFLAGS += $(shell pkg-config --libs --static opencv) #-llttng-ust #-ldl

all:
	$(GCC) -c -o cyg.o cyg.c -I .
	$(CXX) -o main_make.o main_make.cpp $(CXXFLAGS)
	$(CXX) main_make.o -o opencv_example $(LDFLAGS)  #cyg.o -o opencv_example $(LDFLAGS) 

clean: ; rm -f *.o opencv_example





