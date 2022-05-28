#include <stdio.h>

#define MAX 300

int A[MAX][MAX];

int min(int a, int b) {
    return (a < b) ? a : b;
}

void rotate(int N, int M) {
    int i, j, k, r, c, n, m, t;
    // rotate from the outer cycle to the inner cycle.
    for (k = 0; k < min(N, M) / 2; k++) {
        r = k; c = k; n = N - 1 - k; m = M - 1 - k;
        t = A[r][c];
        // move top line to the left
        for (j = c; j < m; j++)
            A[r][j] = A[r][j + 1];
        // move right line to the top
        for (i = r; i < n; i++)
            A[i][m] = A[i + 1][m];
        // move bottom line to the right
        for (j = m; j > c; j--)
            A[n][j] = A[n][j - 1];
        // move left line to the bottom
        for (i = n; i > r + 1; i--)
            A[i][c] = A[i - 1][c];
        A[r + 1][c] = t;
    }
}

void solve(int N, int M, int R) {
    int i;
    for (i = 0; i < R; i++)
        rotate(N, M);
}

int main() {
    int N, M, R, i, j;
    scanf("%d %d %d", &N, &M, &R);
    for (i = 0; i < N; i++)
        for (j = 0; j < M; j++)
            scanf("%d", &A[i][j]);
    solve(N, M, R);
    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++)
            printf("%d ", A[i][j]);
        printf("\n");
    }
}