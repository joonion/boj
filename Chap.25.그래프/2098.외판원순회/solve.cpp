#include <bits/stdc++.h>
using namespace std;

int INF = 0xFFFFFFF;

int n;
vector<vector<int>> W, D;

inline int minimum(int i, int A) {
    int minV = INF;
    for (int j = 2; j <= n; j++) {
        if (!(A & (1 << (j - 2)))) continue;
        minV = min(minV, W[i][j] + D[j][A & ~(1 << (j - 2))]);
    }
    return minV;
}

inline int solve() {
    int subsetsize = 1 << (n - 1);
    for (int i = 2; i <= n; i++)
        D[i][0] = W[i][1];
    for (int k = 1; k <= n - 2; k++)
        for (int A = 0; A < subsetsize; A++) {
            if (__builtin_popcount(A) != k) continue;
            for (int i = 2; i <= n; i++) {
                if (A & (1 << (i - 2))) continue;
                D[i][A] = minimum(i, A);
            }
        }
    return minimum(1, subsetsize - 1);
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n;
    W.resize(n + 1, vector<int>(n + 1, INF));
    D.resize(n + 1, vector<int>(1 << (n - 1), 0));
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++) {
            cin >> W[i][j];
            W[i][j] = W[i][j] ? W[i][j] : INF;
        }
    cout << solve();
}
