#!/bin/sh
echo "Script to compile the stuff:" 
rm -r CMakeCache.txt CMakeFiles/ Makefile cmake_install.cmake
rm OpenCvProject		
cmake .
make
./OpenCvProject -t
  
