cmake_minimum_required(VERSION 2.8)
project( DisplayProject )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( DisplayProject display.cpp )
target_link_libraries( DisplayProject ${OpenCV_LIBS} )
