CXX ?= g++
GCC = gcc
FLAGS = -pg
#-finstrument-functions
CXXFLAGS += -c -Wall $(shell pkg-config --cflags) $(FLAGS) #opencv
LDFLAGS += $(-llttng-ust -ldl)

all:
	$(CXX) -c -I. hello-tp.c
	$(CXX) -c  fib_trace.cpp $(CXXFLAGS)
	$(CXX) -o  fib_trace  fib_trace.o hello-tp.o -llttng-ust -ldl

clean: ; rm -f *.o opencv





