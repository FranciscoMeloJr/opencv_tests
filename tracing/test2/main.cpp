#include <stdio.h>


void function_a()
{
	printf("inside function_a\n");
}
int main()
{
	printf("inside main\n");
	function_a();
	return 0;
}
