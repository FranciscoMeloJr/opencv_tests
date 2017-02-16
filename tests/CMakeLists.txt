cmake_minimum_required(VERSION 2.8)
project(FranciscoProject)
#find_package(OpenCV PATHS /home/frank/opencv/v3.0.0)
SET(GCC_INSTRUMENTATION_FLAGS "-pg")
set(OpenCV_DIR "/home/frank/opencv/v3.0.0/include")
set(OpenCV_INCLUDE_DIRS "/home/frank/opencv/v3.0.0/include")
set(OpenCV_LIBS "/home/frank/opencv/v3.0.0/lib" )
set(OpenCV_LIB_DIR "/home/frank/opencv/v3.0.0/lib" )

SET( CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} ${GCC_INSTRUMENTATION_FLAGS}" )

find_package( OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS} )
link_directories(${OpenCV_LIB_DIR})
add_executable(FranciscoProject opencv-test.cpp)

message(STATUS "OpenCV library status:")
message(STATUS "    version: ${OpenCV_VERSION}")

target_link_libraries(FranciscoProject ${OpenCV_LIBS} )
