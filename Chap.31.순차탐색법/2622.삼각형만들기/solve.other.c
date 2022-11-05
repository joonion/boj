#include <stdio.h>
#include <math.h>

int main()
{
    int n; scanf("%d", &n);
    int cnt = 0;
    for (int c = (n+1)/3; c < (n+1)/2; c++)
        for (int b = (n-c+1)/2; b <= c; b++)
            cnt++;
    printf("%d", cnt);
}