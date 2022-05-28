#include <stdio.h>

#define MAX 5

void mult(int N, int A[][MAX], int B[][MAX], int C[][MAX]) {
    int i, j, k;
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++) {
            C[i][j] = 0;
            for (k = 0; k < N; k++)
                C[i][j] += A[i][k] * B[k][j];
        }
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            C[i][j] = C[i][j] % 1000;
}

void power(int n, int m, int A[][MAX], int C[][MAX]) {
    if (m == 1) {
        for (i = 0; i < N; i++)
            for (j = 0; j < N; j++)
                C[i][j] = A[i][j] % 1000;
    } else if (m % 2 == 1) {
        power(n, m - 1, A, C);
        mult(n, A, C, C);
    } else {
        int i;
        for (i = 0; i < m; i+=2)
            mult(P, P);
    }
}

int main() {
    int i, j, N, B, A[MAX][MAX], C[MAX][MAX];

    scanf("%d %d", &N, &B);
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            scanf("%d", &A[i][j]);

    power(N, B, A, C);

    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++)
            printf("%d ", C[i][j]);
        printf("\n");
    }
}
