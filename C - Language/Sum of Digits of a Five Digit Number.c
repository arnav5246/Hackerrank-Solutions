#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n, sum=0,i;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    for(i=n;i!=0;i=i/10)
    {
        sum=sum+(i%10);
    }
    printf("%d",sum);
    return 0;
}
