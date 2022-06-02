#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<int>> matrix_t;

vector<matrix_t> shapes = {
    {{1, 1}, {1, 1}},         // rectangle
    {{1, 1, 1, 1}},           // straight
    {{1, 1, 1}, {0, 1, 0}},   // T-shape
    {{1, 1, 0}, {0, 1, 1}},   // skewed 1: right-bottom
    {{0, 1, 1}, {1, 1, 0}},   // skewed 2: right-top
    {{1, 0}, {1, 0}, {1, 1}}, // L-type 1: L-shape
    {{0, 1}, {0, 1}, {1, 1}}, // L-type 2: L-flipped
};

matrix_t rotate(matrix_t &s) {
    int h = s[0].size(), w = s.size();
    matrix_t shape(h, vector<int>(w));
    for (int i = 0; i < h; i++)
        for (int j = 0; j < w; j++)
            shape[i][j] = s[w - 1 - j][i];
    return shape;
}

void shape(int k, int &h, int &w, matrix_t &s) {
    switch (k) {
        case 0: s = shapes[0]; break;
        case 1: s = shapes[1]; break;
        case 3: s = shapes[2]; break;
        case 7: s = shapes[3]; break;
        case 9: s = shapes[4]; break;
        case 11: s = shapes[5]; break;
        case 15: s = shapes[6]; break;
        default: s = rotate(s);
    }
    h = s.size(); w = s[0].size();
}

int value(int i, int j, int h, int w, matrix_t &s, matrix_t &A) {
    int val = 0;
    for (int r = 0; r < h; r++)
        for (int c = 0; c < w; c++)
            if (s[r][c] == 1)
                val += A[i + r][j + c];
    return val;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int n, m; cin >> n >> m;
    matrix_t A(n, vector<int>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> A[i][j];
    int opt = 0;
    matrix_t s; int h, w;
    for (int k = 0; k < 19; k++) {
        shape(k, h, w, s);
        for (int i = 0; i <= n - h; i++)
            for (int j = 0; j <= m - w; j++)
                opt = max(opt, value(i, j, h, w, s, A));
    }
    cout << opt << "\n";
}