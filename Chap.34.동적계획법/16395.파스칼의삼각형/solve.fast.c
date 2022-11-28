#include <stdio.h>

#define min(x,y) (x<y)?x:y

int B[31];

int binom(int n, int k) {
    k = min(n, n - k);
    B[0] = 1;
    for (int i = 0; i <= n; i++)
        for (int j = min(i, k); j > 0; j--)
            B[j] += B[j-1];
    return B[k];
}

int main()
{
    int n, k; scanf("%d %d", &n, &k);
    printf("%d", binom(n-1, k-1));
}