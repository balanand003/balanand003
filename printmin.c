#include <stdio.h>
#include<conio.h>
void main()
{
  int array[100], min, n, i, locat = 1;
 
  printf("Enter the number of elements in array\n");
  scanf("%d", &n);
 
  printf("Enter %d integers\n", n);
 
  for (i = 0; i < n; i++)
    scanf("%d", &array[i]);
 
  min = array[0];
 
  for (i = 1; i < n; i++)
  {
    if (array[i] < min)
    {
       min  = array[i];
       locat = i+1;
    }
  }
 
  printf("Minimum element is present at location %d and it's value is %d.\n", locat, min);
  getch();
}
