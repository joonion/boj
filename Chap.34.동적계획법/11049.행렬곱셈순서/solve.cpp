#include <iostream>
#include <vector>
using namespace std;

#define INF 0x0FFFFFFF

int solve(int n, vector<int> d) {
    vector<vector<int>> D(n + 1, vector<int>(n + 1, 0));
    for (int diag = 1; diag < n; diag++)
        for (int i = 1; i < n - diag + 1; i++) {
            int j = i + diag;
            D[i][j] = INF;
            for (int k = i; k < j; k++)
                D[i][j] = min(D[i][j], D[i][k] + D[k+1][j] + d[i-1]*d[k]*d[j]);
        }
    return D[1][n];
}

int main() {
    int N; cin >> N;
    vector<int> d(N + 1);
    int n, m; cin >> n >> m;
    d[0] = n; d[1] = m;
    for (int i = 2; i <= N; i++) {
        cin >> n >> m;
        d[i] = m;
    }
    cout << solve(N, d) << endl;
}