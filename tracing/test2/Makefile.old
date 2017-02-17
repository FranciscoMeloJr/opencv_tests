CXX ?= g++

FLAGS = -finstrument-functions
CXXFLAGS += -c -Wall $(shell pkg-config --cflags opencv) $(FLAGS)
LDFLAGS += $(shell pkg-config --libs --static opencv)
all: opencv_example

opencv_example: main_make.o; $(CXX) $< -o $@ $(LDFLAGS) 

%.o: %.cpp; $(CXX) $< -o $@ $(CXXFLAGS)

clean: ; rm -f main_make.o opencv_example
