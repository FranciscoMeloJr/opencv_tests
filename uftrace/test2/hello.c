#include <stdio.h>
int do_nothing(){
  return printf("%s world\n", "Hello");
}
int main(void)
{
   return do_nothing();
   
}

