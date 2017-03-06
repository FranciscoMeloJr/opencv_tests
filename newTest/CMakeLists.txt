SET(GCC_COVERAGE_COMPILE_FLAGS "-llttng-ust -ldl")
SET( CMAKE_CXX_FLAGS  "${GCC_COVERAGE_COMPILE_FLAGS}" )

cmake_minimum_required(VERSION 2.8)
project( OpenCvDisplay )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
#add_executable(hello-tp hello-tp.o)
add_executable( OpenCvProject display.cpp)

target_link_libraries( OpenCvProject ${OpenCV_LIBS} )
