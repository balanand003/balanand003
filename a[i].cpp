#include <iostream>
#include<conio.h>
using namespace std;
void main() 
{
	int num;
	int i,j,k,a[num];
  clrscr();
	cout<<"enter n";
	cin>>num;
	for(i=0;i<=num;i++)
	{
		for(j=i+1;j<=num;j++)
		{
				for(k=j+1;k<=num;k++)
				{
					if(a[i]+a[j]==a[k])
					cout<<a[i]<<a[j]<<a[k];
				}
		}
	}
	getch();
}
