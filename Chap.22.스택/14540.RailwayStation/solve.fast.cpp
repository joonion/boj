#include <bits/stdc++.h>
using namespace std;

bool solve(int n, vector<int> &A) {
    int stk[1001], top = 0;
    int i = 0;
    for (int x = 1; x <= n; x++) {
        stk[top++] = x;
        while (top && i<n && stk[top-1] == A[i]) {
            top--; i++;
        }
    }
    return i == n;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int n, m;
    while (1) {
        cin >> n; if (!n) break;
        while (1) {
            cin >> m; if (!m) break;
            vector<int> A(n + 1);
            A[0] = m;
            for (int i = 1; i < n; i++)
                cin >> A[i];
            cout << (solve(n, A) ? "Yes" : "No") << "\n";
        }
        cout << "\n";
    }
}