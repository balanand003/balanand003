#include <stdio.h>
#include<conio.h>
void main()
{
int n;
reverseNumber=0;
rem;
printf("Enter an integer: ");
scanf("%d", &n);
while(n != 0)
{
rem = n%10;
reverseNumber = reversedNumber*10 + rem;
n /= 10;
}
printf("Reversed Number = %d", reversedNumber);
getch();
}
