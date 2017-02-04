#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <stdio.h>
#include<cstdlib>
#include<dirent.h>
#include <vector>
#include <string>

using namespace std;

//Function to write CVS:
void writeCSV(std::vector<string> all_strings1, std::vector<string> all_strings2){
    ofstream outfile;
    outfile.open("../results/results.csv");
    for (int i=0; i< all_strings2.size() && all_strings1.size() ; i++)
    {
      outfile << all_strings1[i] <<", "<< all_strings2[i] << endl;
    }

    outfile.close();
}
//Function to read the content of a file:
void read(string filename = "default", bool print = false){
  string line;
  std::vector<string> all_strings1;
  std::vector<string> all_strings2;
  ifstream myfile ("../results/outputfile-30.txt");
  if (myfile.is_open())
  {
    while ( getline (myfile,line) ){
      cout << line << '\n';
      all_strings1.push_back(line);
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 

  ifstream myfile2 ("../results/outputfile-31.txt");
  if (myfile2.is_open())
  {
    while ( getline (myfile2,line) ){
      cout << line << '\n';
      all_strings2.push_back(line);
    }

    if(print){
        for(int i = 0; i < all_strings2.size(); i++) {
            cout << all_strings2[i] << endl;
        }
    }

    myfile2.close();
  }

  else cout << "Unable to open file";

  writeCSV(all_strings1, all_strings2);
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
        read(filename, false);
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
