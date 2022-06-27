#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<int>> matrix_t;

vector<matrix_t> shapes = {
    {{1, 1}, {1, 1}},
    {{1, 1, 1, 1}},
    {{1}, {1}, {1}, {1}},
    {{1, 1, 0}, {0, 1, 1}},
    {{0, 1, 1}, {1, 1, 0}},
    {{1, 0}, {1, 1}, {0, 1}},
    {{0, 1}, {1, 1}, {1, 0}},
    {{1, 1, 1}, {0, 1, 0}},
    {{0, 1, 0}, {1, 1, 1}},
    {{1, 0}, {1, 1}, {1, 0}},
    {{0, 1}, {1, 1}, {0, 1}},
    {{1, 1, 1}, {0, 0, 1}},
    {{0, 0, 1}, {1, 1, 1}},
    {{1, 1, 1}, {1, 0, 0}},
    {{1, 0, 0}, {1, 1, 1}},
    {{1, 1}, {1, 0}, {1, 0}},
    {{1, 1}, {0, 1}, {0, 1}},
    {{1, 0}, {1, 0}, {1, 1}},
    {{0, 1}, {0, 1}, {1, 1}}
};

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int n, m, i, j, k, r, c, w, h, opt, maxval, val;
    cin >> n >> m;
    int A[n][m];
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            cin >> A[i][j];
    opt = 0;
    for (k = 0; k < 19; k++) {
        maxval = 0;
        h = shapes[k].size();
        w = shapes[k][0].size();
        for (i = 0; i <= n - h; i++)
            for (j = 0; j <= m - w; j++) {
                val = 0;
                for (r = 0; r < h; r++)
                    for (c = 0; c < w; c++)
                        if (shapes[k][r][c])
                            val += A[i + r][j + c];
                maxval = max(maxval, val);
            }
        opt = max(opt, maxval);
    }
    cout << opt;
}
