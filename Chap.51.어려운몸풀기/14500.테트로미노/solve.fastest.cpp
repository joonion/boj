#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int n, m; cin >> n >> m;
    int A[n][m];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> A[i][j];

    int h[] = {2, 1, 4, 2, 3};
    int w[] = {2, 4, 1, 3, 2};

    int opt = 0;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {

            if (i <= n - h[0] && j <= m - w[0])
                opt = max(opt, A[i][j]+A[i+1][j]+A[i][j+1]+A[i+1][j+1]);

            if (i <= n - h[1] && j <= m - w[1])
                opt = max(opt, A[i][j]+A[i][j+1]+A[i][j+2]+A[i][j+3]);

            if (i <= n - h[2] && j <= m - w[2])
                opt = max(opt, A[i][j]+A[i+1][j]+A[i+2][j]+A[i+3][j]);

            if (i <= n - h[3] && j <= m - w[3]) {
                opt = max(opt, A[i][j]+A[i][j+1]+A[i+1][j+1]+A[i+1][j+2]);
                opt = max(opt, A[i+1][j]+A[i+1][j+1]+A[i][j+1]+A[i][j+2]);
                opt = max(opt, A[i][j]+A[i][j+1]+A[i][j+2]+A[i+1][j+1]);
                opt = max(opt, A[i+1][j]+A[i+1][j+1]+A[i+1][j+2]+A[i][j+1]);
                opt = max(opt, A[i][j]+A[i+1][j]+A[i+1][j+1]+A[i+1][j+2]);
                opt = max(opt, A[i][j]+A[i][j+1]+A[i][j+2]+A[i+1][j+2]);
                opt = max(opt, A[i][j]+A[i][j+1]+A[i][j+2]+A[i+1][j]);
                opt = max(opt, A[i+1][j]+A[i+1][j+1]+A[i+1][j+2]+A[i][j+2]);
            }

            if (i <= n - h[4] && j <= m - w[4]) {
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

    cout << opt;
}