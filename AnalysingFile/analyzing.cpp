// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include<stdio.h>
#include<cstdlib>
#include<dirent.h>

using namespace std;

//Function to read the content of a file:
void read(){
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
                        cout << entry->d_name << "\n";
                }
                closedir(pDIR);
    }
}
//Main:
int main(){
    listFile();
    return 0;
}
