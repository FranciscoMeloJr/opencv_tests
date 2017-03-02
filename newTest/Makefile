CXX ?= g++
GCC = gcc
FLAGS = -pg
#-finstrument-functions
CXXFLAGS += -c -Wall $(shell pkg-config --cflags opencv) $(FLAGS)
LDFLAGS += $(-llttng-ust -ldl)

all:
	$(CXX) -c -I. hello-tp.c
	$(CXX) -c  work_load_display.cpp $(CXXFLAGS)
	$(CXX) -o opencv work_load_display.o hello-tp.o -llttng-ust -ldl

clean: ; rm -f *.o opencv





