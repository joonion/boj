#include <stdio.h>
int n, i, c = 0;
int main()
{
    scanf("%d", &n);
    for (i = (n+1)/3; i < (n+1)/2; i++)
        c += (3*i-n+2)/2;
    printf("%d", c);
}