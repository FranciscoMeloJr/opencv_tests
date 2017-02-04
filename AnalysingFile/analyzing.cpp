#include <opencv2/opencv.hpp>
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include<stdio.h>
#include<cstdlib>
#include<dirent.h>

using namespace std;
using namespace cv;

const string commands[] = {"list", "read"};

//Function to read the content of a file:
void read(string filename = "default"){
  string line;
  ifstream myfile ("../results/output.txt");
  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
      cout << line << '\n';
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 

}
//Function to read all the files in a directory:
void listFile(){
        DIR *pDIR;
        struct dirent *entry;
        if( pDIR=opendir("../results") ){
        while(entry = readdir(pDIR)){
                        if( strcmp(entry->d_name, ".") != 0 && strcmp(entry->d_name, "..") != 0 )
                          cout << "File: "<<entry->d_name << "\n";
        }
        closedir(pDIR);
    }
}
//Keys:
const char* keys =
{
    "{help h||}"
};
//Help:
void help(){

        cout <<" Help " << endl;
        cout <<" Usage: <read> <filename.jpg>" << endl;
        cout <<" Usage: <list> <directory>" << endl;
        cout <<" All tests: -t " << endl;
        return;

}
//Select command:
void execute_command(string command = "list")
{
    string filename = "../results/output30.txt";
    string path = "../results";

    if(command.compare("read") == 0 ){
        read(filename);
    }
    if(command.compare("list") == 0 ){
        listFile();
    }
}

//Main:
int main( int argc, char** argv ){
    cv::CommandLineParser parser(argc, argv, keys);
    parser.about("OpenCv Tests v1.0.0");
    if (parser.has("help"))
    {
        help();
        return 0;
    }

    string inputCommand = NULL;
    inputCommand = parser.get<string>(0);

    try{
        execute_command(inputCommand);
    }catch(int e){

    }
    return 0;
}
