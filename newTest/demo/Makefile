CXX ?= g++
GCC = gcc
FLAGS = -pg
#-finstrument-functions
CXXFLAGS += -c -Wall $(shell pkg-config --cflags) $(FLAGS) #opencv
LDFLAGS += $(-llttng-ust -ldl)

all:
	#$(CXX) -c -I. hello-tp.c
	$(GCC) -c  open.c $(CXXFLAGS)
	$(GCC) -o  open  open.o -llttng-ust -ldl

clean: ; rm -f *.o open





