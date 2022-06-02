#include <stdio.h>
#define max(x,y) (x>y)?x:y

int main() {
    int n, m, opt, i, j, h, w;
    int A[500][500];
    scanf("%d %d", &n, &m);
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            scanf("%d", &A[i][j]);
            
    opt = 0;

    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++) {

            h = 2; w = 2;
            if (i <= n - h && j <= m - w)
                opt = max(opt, A[i][j]+A[i+1][j]+A[i][j+1]+A[i+1][j+1]);

            h = 1; w = 4;
            if (i <= n - h && j <= m - w)
                opt = max(opt, A[i][j]+A[i][j+1]+A[i][j+2]+A[i][j+3]);

            h = 4; w = 1;
            if (i <= n - h && j <= m - w)
                opt = max(opt, A[i][j]+A[i+1][j]+A[i+2][j]+A[i+3][j]);

            h = 2; w = 3;
            if (i <= n - h && j <= m - w) {
                opt = max(opt, A[i][j]+A[i][j+1]+A[i+1][j+1]+A[i+1][j+2]);
                opt = max(opt, A[i+1][j]+A[i+1][j+1]+A[i][j+1]+A[i][j+2]);
                opt = max(opt, A[i][j]+A[i][j+1]+A[i][j+2]+A[i+1][j+1]);
                opt = max(opt, A[i+1][j]+A[i+1][j+1]+A[i+1][j+2]+A[i][j+1]);
                opt = max(opt, A[i][j]+A[i+1][j]+A[i+1][j+1]+A[i+1][j+2]);
                opt = max(opt, A[i][j]+A[i][j+1]+A[i][j+2]+A[i+1][j+2]);
                opt = max(opt, A[i][j]+A[i][j+1]+A[i][j+2]+A[i+1][j]);
                opt = max(opt, A[i+1][j]+A[i+1][j+1]+A[i+1][j+2]+A[i][j+2]);
            }

            h = 3; w = 2;
            if (i <= n - h && j <= m - w) {            
                opt = max(opt, A[i][j]+A[i+1][j]+A[i+1][j+1]+A[i+2][j+1]);
                opt = max(opt, A[i][j+1]+A[i+1][j]+A[i+1][j+1]+A[i+2][j]);
                opt = max(opt, A[i][j]+A[i+1][j]+A[i+2][j]+A[i+1][j+1]);
                opt = max(opt, A[i][j+1]+A[i+1][j+1]+A[i+2][j+1]+A[i+1][j]);
                opt = max(opt, A[i][j]+A[i+1][j]+A[i+2][j]+A[i+2][j+1]);
                opt = max(opt, A[i][j]+A[i][j+1]+A[i+1][j]+A[i+2][j]);
                opt = max(opt, A[i][j+1]+A[i+1][j+1]+A[i+2][j+1]+A[i+2][j]);
                opt = max(opt, A[i][j]+A[i][j+1]+A[i+1][j+1]+A[i+2][j+1]);
            }
        }

    printf("%d", opt);
}