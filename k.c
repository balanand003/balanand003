#include <stdio.h>
#include<conio.h>
void main() 
{
   int num,k,i,j,b[50],flg=0;
   scanf("%d %d",&n,&k);
   for(i=0;i<num;i++)
   {
       scanf("%d ",&b[i]);
   }
   for(i=0;i<num;i++)
   {
       for(j=i+1;j<num;j++)
       {
           if((b[i]+b[j])==k)
           {
               printf("yes..%d and  %d sums up to give %d",b[i],b[j],k);
               flg=1;
               break;
           }
       }
   }
   if(flg!=1)
   {
       printf("no");
   }
	getch();
}
