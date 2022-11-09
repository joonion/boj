#include <stdio.h>

int solve(int n, int A[]) {
    int i, j = 0, stk[1001], top = 0;
    for (i = 1; i <= n; i++) {
        stk[top++] = i;
        while (top && j < n && stk[top-1] == A[j]) {
            top--; j++;
        }
    }
    return j == n;
}

int main()
{
    int i, n, m, A[1001];
    while (1) {
        scanf("%d", &n);
        if (!n) break;
        while (1) {
            scanf("%d", &m);
            if (!m) break;
            A[0] = m;
            for (i = 1; i < n; i++)
                scanf("%d", &A[i]);
            printf("%s\n", (solve(n, A) ? "Yes" : "No"));
        }
        printf("\n");
    }
}