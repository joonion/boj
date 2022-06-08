#include <stdio.h>

const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};

int R, C, depth;
char A[21][21];
int path[26];

void move(int d, int i, int j) {
    int t;
    if (0 <= i && i < R && 0 <= j && j < C && !path[A[i][j] - 'A']) {
        depth = (depth < d) ? d : depth;
        for (t = 0; t < 4; t++) {
            path[A[i][j] - 'A'] = 1;
            move(d + 1, i + dx[t], j + dy[t]);
            path[A[i][j] - 'A'] = 0;
        }
    }
}

int main() {
    int i;
    scanf("%d %d", &R, &C);
    for (i = 0; i < R; i++)
        scanf("%s", A[i]);
    for (i = 0; i < 26; i++)
        path[i] = 0;
    depth = 0;
    move(1, 0, 0);
    printf("%d", depth);
}