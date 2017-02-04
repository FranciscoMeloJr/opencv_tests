#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include<stdio.h>
#include<cstdlib>
#include<dirent.h>

using namespace std;

//Function to read the content of a file:
void read(string filename = "default"){
  string line;
  ifstream myfile ("../results/outputfile-30.txt");
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

//Select command:
void execute_command(string command = "list")
{
    string filename = "../results/outputfile-30.txt";
    string path = "../results";

    cout << command;
    if(command.compare("read") == 0 ){
        read(filename);
    }
    if(command.compare("list") == 0 ){
        listFile();
    }
}

//Main:
int main( int argc, char** argv ){

    try{
        std::string str1(argv[1]);
        execute_command(str1);

    }catch(int e){

    }
    return 0;
}
