#include <bits/stdc++.h>
using namespace std;

int solve(int n, vector<int> &s) {
    sort(s.begin(), s.end());
    priority_queue<int> PQ;
    for (int i = 0; i < (n + 1)/2; i++) {
        PQ.push(s[i]);
    }
    int cnt = 0;
    while (true) {
        int m = PQ.top(); PQ.pop();
        // printf("\t%d\t%d\n", cnt, m);
        if (m / 2 == 0) break;
        PQ.push(m / 2);
        cnt++;
    }
    return cnt + 1;
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n; cin >> n;
    vector<int> s(n);
    for (int i = 0; i < n; i++)
        cin >> s[i];
    // for (int i = 0; i < n; i++)
    //     printf("%d ", s[i]);
    // printf("\n");
    cout << solve(n, s);
}