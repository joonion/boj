#include <stdio.h>

int min_prime(int k, int p) {
    for (int i = 2; i < p; i++)
        if (k % i == 0) return 0;
    return 1;
}

int solve(int n, int p) {
    int k = p;
    for (; n > 0 && k < 1000000001; k += p)
        n -= min_prime(k, p);
    return (n == 0) ? k - p : 0;
}

int main()
{
    int n, p;
    scanf("%d %d", &n, &p);
    printf("%d", solve(n, p));
}