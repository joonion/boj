#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int n, m; cin >> n >> m;
    int A[n][m];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> A[i][j];

    int opt = 0;
    int h = 2, w = 2;
    for (int i = 0; i <= n - h; i++)
        for (int j = 0; j <= m - w; j++)
            opt = max(opt, A[i][j]+A[i+1][j]+A[i][j+1]+A[i+1][j+1]);
    h = 1; w = 4;
    for (int i = 0; i <= n - h; i++)
        for (int j = 0; j <= m - w; j++)
            opt = max(opt, A[i][j]+A[i][j+1]+A[i][j+2]+A[i][j+3]);
    h = 4; w = 1;
    for (int i = 0; i <= n - h; i++)
        for (int j = 0; j <= m - w; j++)
            opt = max(opt, A[i][j]+A[i+1][j]+A[i+2][j]+A[i+3][j]);
    h = 2; w = 3;
    for (int i = 0; i <= n - h; i++)
        for (int j = 0; j <= m - w; j++) {
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
    for (int i = 0; i <= n - h; i++)
        for (int j = 0; j <= m - w; j++) {
            opt = max(opt, A[i][j]+A[i+1][j]+A[i+1][j+1]+A[i+2][j+1]);
            opt = max(opt, A[i][j+1]+A[i+1][j]+A[i+1][j+1]+A[i+2][j]);
            opt = max(opt, A[i][j]+A[i+1][j]+A[i+2][j]+A[i+1][j+1]);
            opt = max(opt, A[i][j+1]+A[i+1][j+1]+A[i+2][j+1]+A[i+1][j]);
            opt = max(opt, A[i][j]+A[i+1][j]+A[i+2][j]+A[i+2][j+1]);
            opt = max(opt, A[i][j]+A[i][j+1]+A[i+1][j]+A[i+2][j]);
            opt = max(opt, A[i][j+1]+A[i+1][j+1]+A[i+2][j+1]+A[i+2][j]);
            opt = max(opt, A[i][j]+A[i][j+1]+A[i+1][j+1]+A[i+2][j+1]);
        }

    cout << opt;
}