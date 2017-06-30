#include<stdio.h>
#include<conio.h>
void main()
{
int a=0,n=0,b;
clrscr();
printf("enter the num:");
scanf("%d",&b);
while(a<=b)
{
n+=a;
a++;
}
printf("%d",n);
getch();
}


