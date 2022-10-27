#include <bits/stdc++.h>
using namespace std;

void swap(int &x, int &y) {
    int t = x; x = y; y = t;
}

void solve(int n, int k, vector<int> &A) {
    int cnt = 0;
    for (int last = n; last >= 2; last--)
        for (int i = 1; i <= last - 1; i++)
            if (A[i] > A[i+1]) {
                swap(A[i], A[i+1]);
                if (++cnt == k) {
                    cout << A[i] << " " << A[i+1] << endl;
                    return;
                }
            }
    cout << -1 << endl;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int N, K; cin >> N >> K;
    vector<int> A(N + 1);
    for (int i = 1; i <= N; i++)
        cin >> A[i];
    solve(N, K, A);
}