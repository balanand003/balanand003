#include <stdio.h>
#include<conio.h>
void main()
{
int min,rem,hr;
scanf("%d",&min);
hr=min/60;
rem=min-(60*hr);
printf("%d:%d",hr,rem);
getch();
}
