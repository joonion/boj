#include <bits/stdc++.h>
using namespace std;

int solve(int n, priority_queue<int> &PQ) {
    int cnt = 0;
    while (true) {
        cnt++;
        int m = PQ.top(); PQ.pop();
        // printf("\t%d\t%d\n", cnt, m);
        if (m / 2 == 0) break;
        PQ.push(m / 2);
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int n; cin >> n;
    priority_queue<int> PQ;
    for (int i = 0; i < n; i++) {
        int j; cin >> j;
        if (PQ.size() <= (n - 1) / 2)
            PQ.push(j);
        else if (PQ.top() > j) {
            PQ.pop(); PQ.push(j);
        }
    }
    // cout << PQ.size() << endl;
    cout << solve(n, PQ) << endl;
}