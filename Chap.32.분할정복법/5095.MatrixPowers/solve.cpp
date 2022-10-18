#include <bits/stdc++.h>
using namespace std;

typedef vector<vector<int>> matrix_t;

matrix_t mult(int n, int m, matrix_t A, matrix_t B) {
    matrix_t C(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++)
                C[i][j] += A[i][k] * B[k][j] % m;
            C[i][j] %= m;
        }
    return C;
}

matrix_t solve(int n, int m, int p, matrix_t A) {
    if (p == 1) {
        return A;
    } else if (p % 2 == 0) {
        matrix_t B = solve(n, m, p/2, A);
        return mult(n, m, B, B);
    } else {
        matrix_t B = solve(n, m, p/2, A);
        return mult(n, m, A, mult(n, m, B, B));
    }
}

int main() {
    int N, M, P;
    while (true) {
        cin >> N >> M >> P;
        if (N == 0) break;

        matrix_t A(N, vector<int>(N));
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                cin >> A[i][j];

        matrix_t B = solve(N, M, P, A);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++)
                cout << B[i][j] << " ";
            cout << endl;
        }
        cout << endl;
    }    
}