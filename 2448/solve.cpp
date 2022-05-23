#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<char>> matrix_t;

void sierpinski(int n, matrix_t &T, int row, int col) {
    if (n == 3) {
        T[row][col] = '*';
        T[row + 1][col - 1] = T[row + 1][col + 1] = '*';
        for (int i = -2; i <= 2; i++)
            T[row + 2][col + i] = '*';
    } else {
        int m = n / 2;
        sierpinski(m, T, row, col);
        sierpinski(m, T, row + m, col - m);
        sierpinski(m, T, row + m, col + m);
    }
}

void solve(int n) {
    matrix_t T(n, vector<char>(2*n - 1, ' '));
    sierpinski(n, T, 0, n - 1);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 2*n - 1; j++)
            cout << T[i][j];
        cout << endl;
    }
}

int main() {
    int N; cin >> N;
    solve(N);
}
