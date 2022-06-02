#include <stdio.h>
#define max(x,y) (x>y)?x:y

int s22[2][2] = {{1, 1}, {1, 1}};
int s14[1][4] = {{1, 1, 1, 1}};
int s41[4][1] = {{1}, {1}, {1}, {1}};
int s23[8][2][3] = {
    {{1, 1, 0}, {0, 1, 1}},
    {{0, 1, 1}, {1, 1, 0}},
    {{1, 1, 1}, {0, 1, 0}},
    {{0, 1, 0}, {1, 1, 1}},
    {{1, 1, 1}, {0, 0, 1}},
    {{0, 0, 1}, {1, 1, 1}},
    {{1, 1, 1}, {1, 0, 0}},
    {{1, 0, 0}, {1, 1, 1}}
};

int s32[8][3][2] = {
    {{1, 0}, {1, 1}, {0, 1}},
    {{0, 1}, {1, 1}, {1, 0}},
    {{1, 0}, {1, 1}, {1, 0}},
    {{0, 1}, {1, 1}, {0, 1}},
    {{1, 1}, {1, 0}, {1, 0}},
    {{1, 1}, {0, 1}, {0, 1}},
    {{1, 0}, {1, 0}, {1, 1}},
    {{0, 1}, {0, 1}, {1, 1}}
};

int main() {
    int n, m, i, j, k, r, c, h, w, opt, val;
    int A[500][500];
    scanf("%d %d", &n, &m);
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            scanf("%d", &A[i][j]);
    opt = 0;
    // s22
    h = 2; w = 2;
    for (i = 0; i <= n - h; i++)
        for (j = 0; j <= m - w; j++) {
            val = 0;
            for (r = 0; r < h; r++)
                for (c = 0; c < w; c++)
                    if (s22[r][c] == 1) val += A[i+r][j+c];
            opt = max(opt, val);
        }
    // s14
    h = 1; w = 4;
    for (i = 0; i <= n - h; i++)
        for (j = 0; j <= m - w; j++) {
            val = 0;
            for (r = 0; r < h; r++)
                for (c = 0; c < w; c++)
                    if (s14[r][c] == 1) val += A[i+r][j+c];
            opt = max(opt, val);
        }
    // s41
    h = 4; w = 1;
    for (i = 0; i <= n - h; i++)
        for (j = 0; j <= m - w; j++) {
            val = 0;
            for (r = 0; r < h; r++)
                for (c = 0; c < w; c++)
                    if (s41[r][c] == 1) val += A[i+r][j+c];
            opt = max(opt, val);
        }
    // s23
    h = 2; w = 3;
    for (k = 0; k < 8; k++)
        for (i = 0; i <= n - h; i++)
            for (j = 0; j <= m - w; j++) {
                val = 0;
                for (r = 0; r < h; r++)
                    for (c = 0; c < w; c++)
                        if (s23[k][r][c] == 1) val += A[i+r][j+c];
                opt = max(opt, val);
            }
    // s32
    h = 3; w = 2;
    for (k = 0; k < 8; k++)
        for (i = 0; i <= n - h; i++)
            for (j = 0; j <= m - w; j++) {
                val = 0;
                for (r = 0; r < h; r++)
                    for (c = 0; c < w; c++)
                        if (s32[k][r][c] == 1) val += A[i+r][j+c];
                opt = max(opt, val);
            }

    printf("%d\n", opt);
}