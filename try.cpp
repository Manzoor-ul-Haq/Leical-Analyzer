#include <iostream>
#include <string.h>
using namespace std;

int a = 2;
float c = 5.0;
string name = "lexical";

int main()
{
	for(int i=0; i<5; i=i+1)
	{
		continue;
	}

	while(true)
	{
		break;
	}

	if(a == 2)
	{
		a = a + 2;
		a = a / 2;
		a = a - 0;
		a = a * 1;
		cout << a << endl;
	}
	else
	{
		cout << "hi";
	}
	return 0;
}