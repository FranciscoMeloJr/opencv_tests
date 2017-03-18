#include <stdio.h>
#include <stdlib.h>

char* concat(char *s1, char *s2)
{
    char *result = malloc(strlen(s1)+strlen(s2)+1);//+1 for the zero-terminator
    //in real code you would check for errors in malloc here
    strcpy(result, s1);
    strcat(result, s2);
    return result;
}
void handler(int signal) {
  printf("\nHouston, we have a problem:\n");
  //printf("segfault at addr=%p offset=0x%x (%f kio)\n", addr, offset, offset / 1024.0);
  exit(1);
}

int main() 
{
  int i =0;
  //char path[]="/home/frank/Documents/Artigo/1.tests/naser_tests/archives/1.txt";

  char buff[255];
  char str1[] = "data/";
  char str2[]  = ".txt";
  printf("Test open\n");    
  //signal(SIGSEGV, handler);

   for(i = 0; i<1000; i++)
	 { 	   

    char Num[5];
    sprintf(Num,"%d",i);
    printf("stringnum: %s\n",Num);
       
    char* s = concat(Num, str2);
    printf("Concat: %s",s);
    char* path = concat(str1,s);
    printf("Path: %s",path);
    
    FILE *fp;
		fp = fopen(path, "r");
		//fprintf(fp, "This is testing for fprintf...\n");
		//fputs("This is testing for fputs...%d\n",fp);
    fscanf(fp, "%s", buff);
    printf("1 : %s\n", buff );


		fclose(fp);

		}	
   

   return 0;
}
