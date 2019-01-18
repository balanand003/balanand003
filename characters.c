#include <stdio.h>
#include<conio.h>
void main(void)
{
char b[50];
clrscr();
scanf("%s",b);
int n=0;
for(int i=0;b[i]!='\0';i++)
{
n++;
}
printf("%d",n);
getch();
}
