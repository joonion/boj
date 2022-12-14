#include <stdio.h>

int a[1000][5], b[1000];

int main()
{
    int i, j, k, n, maxi = 0;

    scanf("%d", &n);
    for (i = 0; i < n; i++)
        scanf("%d %d %d %d %d", &a[i][0], &a[i][1], &a[i][2], &a[i][3], &a[i][4]);

    for (i = 0; i < n; i++) {
        for (j = i + 1; j < n; j++)
            if (a[i][0] == a[j][0] || a[i][1] == a[j][1] || a[i][2] == a[j][2] || a[i][3] == a[j][3] || a[i][4] == a[j][4]) {
                b[i]++; b[j]++;
            }
    }
    for (i = 1; i < n; i++)
        if (b[i] > b[maxi]) maxi = i;
    printf("%d", maxi + 1);
}