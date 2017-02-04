#!/bin/bash
# Script to compile:

echo "Analyzing"
rm -r CMakeCache.txt cmake_install.cmake Makefile CMakeFiles/ Analyzing 
cmake ../
make
clear
./Analyzing


