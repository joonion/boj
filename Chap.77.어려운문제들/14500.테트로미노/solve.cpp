#include <iostream>
#include <vector>
using namespace std;

#define max(x,y) (x>y) ? x : y

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

int place(matrix_t &shape, int i, int j, matrix_t &A) {
    int val = 0;
    for (int r = 0; r < shape.size(); r++)
        for (int c = 0; c < shape[0].size(); c++)
            if (shape[r][c] == 1)
                val += A[i + r][j + c];
    return val;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int n, m; cin >> n >> m;
    matrix_t A(n, vector<int>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> A[i][j];
    int opt = 0;
    for (int k = 0; k < shapes.size(); k++) {
        int maxval = 0;
        for (int i = 0; i <= n - shapes[k].size(); i++)
            for (int j = 0; j <= m - shapes[k][0].size(); j++)
                maxval = max(maxval, place(shapes[k], i, j, A));
        opt = max(opt, maxval);
    }
    cout << opt << endl;
}
