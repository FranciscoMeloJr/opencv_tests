cmake_minimum_required(VERSION 2.8)
project( Parser )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( Parser parser.cpp )
target_link_libraries( Parser ${OpenCV_LIBS} )
