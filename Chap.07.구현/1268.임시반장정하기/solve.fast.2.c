#include <stdio.h>

int main()
{
    int i, j, k, n;
    int a[5000], b[1000]={0};
    scanf("%d", &n);
    for (i = 0; i < n*5; i++)
        scanf("%d", &a[i]);

    for (i = 0; i < n; i++) {
        for (j = i + 1; j < n; j++)
            for (k = 0; k < 5; k++)
                if (a[i*5+k]==a[j*5+k]) {
                    b[i]++; b[j]++; break;
                }
    }
    int m = 0;
    for (i = 1; i < n; i++)
        if (b[i] > b[m]) m = i;
    printf("%d", m + 1);
}