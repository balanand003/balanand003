package sample;
public class gcd 
{
public static void main( String args[] )
{
int i = 0;
int num = 0;
boolean isNeg = false;
if (str.charAt(0) == '-') 
{
isNeg = true;
i = 1;
}
while( i < str.length()) 
{
num = num*10;
num =num+ str.charAt(i++) - '0'; 
}
if (isNeg)
{
num = -num;
return num;
}
}
}
