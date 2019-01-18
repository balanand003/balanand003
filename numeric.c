#include <stdio.h>
#include<conio.h>
#include<math.h>
void main()
{
int a,b,lcm,gcd;
clrscr();
scanf("%d %d",&a,&b);
int i=2;
while(i<=a&&i<=b)
{
if(a%i==0 && b%i==0)  
{
gcd=i;
}i++;
}
lcm=(a*b)/gcd;
printf("%d",lcm);
getch();
}
