#include <stdio.h>

int di[] = {0, 0, 0, 1, 1, 1, 2, 2, 2};
int dj[] = {0, 1, 2, 0, 1, 2, 0, 1, 2};

int A[2187][2187];
int a, b, c;

int check(int i, int j, int n) {
    int chk = A[i][j];
    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++)
            if (chk != A[r][c]) return 2;
    return chk;
}

int solve(int i, int j, int n) {
    int chk = check(i, j, n);
    printf("%d %d %d  %d\n", i, j, n, chk);
    if (chk == -1) a++;
    else if (chk == 0) b++;
    else if (chk == 1) c++;
    else {
        int m = n / 3;
        for (int k = 0; k < 9; k++)
            solve(i + m * di[k], j + m * dj[k], m);
    }
}

int main()
{
    int n; scanf("%d", &n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &A[i][j]);
    a = b = c = 0;
    solve(0, 0, n);
    printf("%d\n%d\n%d", a, b, c);
}