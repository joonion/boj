#include <stdio.h>
#define MAX 100

void copyfromto(int n, int A[][MAX], int B[][MAX]) {
    int i, j;
    for (i = 0; i < n; i++)
            for (j = 0; j < n; j++)
                B[i][j] = A[i][j];
}

void mult(int n, int m, int A[][MAX], int B[][MAX], int C[][MAX]) {
    int i, j, k;
    for (i = 0; i < n; i++)
            for (j = 0; j < n; j++) {
                C[i][j] = 0;
                for (k = 0; k < n; k++)
                    C[i][j] += (A[i][k] * B[k][j]) % m;
                C[i][j] %= m;
            }
}

void solve(int n, int m, int p, int A[][MAX], int B[][MAX]) {
    int i, j;
    if (p == 1) {
        copyfromto(n, A, B);
    } else {
        int C[MAX][MAX], D[MAX][MAX];
        solve(n, m, p/2, A, C);
        mult(n, m, C, C, D);
        if (p % 2 == 0)
            copyfromto(n, D, B);
        else {
            mult(n, m, A, D, C);
            copyfromto(n, C, B);
        }
    }
}

int main()
{
    int i, j, N, M, P, A[MAX][MAX], B[MAX][MAX];
    while (1) {
        scanf("%d %d %d", &N, &M, &P);
        if (N == 0) break;
        for (i = 0; i < N; i++)
            for (j = 0; j < N; j++)
                scanf("%d", &A[i][j]);

        solve(N, M, P, A, B);

        for (i = 0; i < N; i++) {
            for (j = 0; j < N; j++)
                printf("%d ", B[i][j]);
            printf("\n");
        }
        printf("\n");
    }
}