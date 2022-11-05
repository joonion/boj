#include <stdio.h>
#include <math.h>

int main()
{
    int n; scanf("%d", &n);
    int cnt = 0, p =(int)ceil(n/3.0), q = (int)ceil(n/2.0);
    for (int c = p; c < q; c++)
        for (int b = (n-c+1)/2; b <= c; b++)
            cnt++;
    printf("%d", cnt);
}