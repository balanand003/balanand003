#include <stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<conio.h>
void main()
{
char str[30];
int i=0,count=0;
clrscr();
printf("enter the string");
scanf("%s",&str);
while(str[i]!='\0')
{
if(!(isdigit(str[i]))&&!(isalnum(str[i])))
{
++count;
}
++i;
}
printf("no of special characters is %d ",count);
getch();
}
