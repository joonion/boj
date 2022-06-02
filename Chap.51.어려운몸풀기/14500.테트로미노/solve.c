#include <stdio.h>
#define max(x,y) (x>y) ? x : y

int move[19][3][2] = {
    {{0, 1}, {1, 0}, {0, -1}},  // rectangle
    {{0, 1}, {0, 1}, {0, 1}},   // straight - horizontal
    {{1, 0}, {1, 0}, {1, 0}},   // straight - vertical
    {{0, 1}, {-1, 0}, {0, 1}},  // skewed - right-top
    {{0, 1}, {1, 0}, {0, 1}},   // skewed - right-bottom
    {{-1, 0}, {0, 1}, {-1, 0}}, // skewed - top-right
    {{1, 0}, {0, 1}, {1, 0}},   // skewed - bottom-right
    {{0, 1}, {0, 1}, {1, -1}},  // T-shape - ㅜ
    {{0, 1}, {0, 1}, {-1, -1}}, // T-shape - ㅗ
    {{1, 0}, {1, 0}, {-1, 1}},  // T-shape - ㅏ
    {{1, 0}, {1, 0}, {-1, -1}}, // T-shape - ㅓ
    {{1, 0}, {1, 0}, {0, 1}},   // L1-shape - L
    {{-1, 0}, {0, 1}, {0, 1}},  // L2-shape - L1 + 90 deg 
    {{0, 1}, {1, 0}, {1, 0}},   // L3-shape - L2 + 90 deg
    {{0, 1}, {0, 1}, {-1, 0}},  // L4-shape - L3 + 90 deg
    {{0, 1}, {-1, 0}, {-1, 0}}, // L5-shape - L1:symmetric
    {{1, 0}, {0, 1}, {0, 1}},   // L6-shape - L5 + 90 deg
    {{-1, 0}, {-1, 0}, {0, 1}}, // L7-shape - L6 + 90 deg
    {{0, 1}, {0, 1}, {1, 0}},   // L8-shape - L7 + 90 deg
};

int main() {
    int n, m, i, j, k, s, ni, nj, opt, val;
    int A[500][500];
    scanf("%d %d", &n, &m);
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            scanf("%d", &A[i][j]);
    opt = 0;
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            for (k = 0; k < 19; k++) {
                val = A[i][j];
                ni = i; 
                nj = j;
                for (s = 0; s < 3; s++) {
                    ni = ni + move[k][s][0];
                    nj = nj + move[k][s][1];
                    if (ni < 0 || nj < 0 || ni >= n || nj >= m) {
                        val = 0;
                        break;
                    }
                    val += A[ni][nj];
                }
                opt = max(opt, val);
            }
        }
    }
    printf("%d\n", opt);
}