#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPrime(int n)
{
   int divisor=0;
   for (divisor = 2; divisor*divisor <= n; divisor++)
      if (n % divisor==0)
         return false;
   return true;
}

int main(void)
{
   int sum=0,i=2,count=0;

   while(count<1000)
   {
      if (isPrime(i))
      {
         sum+=i;
         count++;
      }
      i++;
   }
   printf("%d",sum);

   return 0;
}
