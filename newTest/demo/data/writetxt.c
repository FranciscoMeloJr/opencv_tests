#include <stdio.h>
#include <stdlib.h>  /* For exit() function */
#define MAX 5
char* concat(char *s1, char *s2)
{
    char *result = malloc(strlen(s1)+strlen(s2)+1);//+1 for the zero-terminator
    //in real code you would check for errors in malloc here
    strcpy(result, s1);
    strcat(result, s2);
    return result;
}
int main()
{
   char c[1000];
   char str2[] = ".txt";
   FILE *fptr;
   int i = 0;

   for(i = 0; i < 1000 ; i++)
   {
           printf("%d",i);
	   char str1[MAX];
           //char str3[MAX+4];

           //sprintf(str1, "%d", i);
           //printf("%s",str1);
           char stringNum[20];
           //int num=100;
           sprintf(stringNum,"%d",i);
           printf("stringnum: %s\n",stringNum);

           //asprintf(&str3,"%s%s",stringNum,str2);
           //printf("%s",str3);
           char* s = concat(stringNum,str2);
 	   fptr=fopen(s,"w");
	   if(fptr==NULL)
	   {
	      printf("Error!");
	      exit(1);
	   }
	   //printf("Enter a sentence:\n");
	   //gets(c);
	   fprintf(fptr,"%d",i);
	   fclose(fptr);
   }
   return 0;
}
