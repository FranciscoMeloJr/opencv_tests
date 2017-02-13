#include <stdio.h>
void do_nothing(){
  return;
}
int main(void)
{
   do_nothing();
   return printf("%s world\n", "Hello");
}

