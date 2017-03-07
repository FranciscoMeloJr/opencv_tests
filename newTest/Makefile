CXX ?= g++
GCC = gcc
FLAGS = -pg
#-finstrument-functions
CXXFLAGS += -c -Wall $(shell pkg-config --cflags) $(FLAGS) #opencv
LDFLAGS += $(-llttng-ust -ldl)

all:
	$(CXX) -c -I. hello-tp.c
	$(CXX) -c  work_load_display.cpp $(CXXFLAGS)
	$(CXX) -o  program_to_load_program  work_load_display.o hello-tp.o -llttng-ust -ldl

clean: ; rm -f *.o opencv





