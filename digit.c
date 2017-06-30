#include<stdio.h>
#include<conio.h>
void main()
{
int n;
int count=0;
clrscr();
printf("enter the integer:");
scanf("%d",&n);
while(n!=0)
{
n=n/10;
++count;
}
printf("no of digits = %d",count);
getch();
}
