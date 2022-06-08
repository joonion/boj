#include <bits/stdc++.h>
using namespace std;

const int imv[] = {-1, 0, 1, 0};
const int jmv[] = {0, 1, 0, -1};

int n, m, depth = 0;
vector<string> A;
vector<int> mark(26, 0);

void move(int d, int i, int j) {
    if (0 <= i && i < n && 0 <= j && j < m && !mark[A[i][j]-'A']) {
        depth = max(depth, d);
        for (int k = 0; k < 4; k++) {
            mark[A[i][j]-'A'] = 1;
            move(d + 1, i + imv[k], j + jmv[k]);
            mark[A[i][j]-'A'] = 0;
        }
    }
}

int main() {
    cin >> n >> m;
    A.resize(n);
    for (int i = 0; i < n; i++)
        cin >> A[i];
    move(1, 0, 0);
    cout << depth;
}
