#include<stdio.h>
#include<conio.h>
void main()
{
  int n;
  clrscr();
  printf("enter the num:");
  scanf("%d",&n);
  if(n>0)
     {
    printf("the number is positive %d",n);
  }
  else if(n==0)
  {
    printf("the number is zero %d",n);
  }
  else
  {
    printf("the number is negative %d",n);
  }
  getch();
}
