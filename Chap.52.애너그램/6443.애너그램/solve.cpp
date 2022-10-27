#include <bits/stdc++.h>
using namespace std;

void dfs(int i, int n, string s, vector<int> &A) {
    if (i == n)
        cout << s << "\n";
    else {
        for (int j = 0; j < 26; j++) {
            if (A[j] > 0) {
                A[j]--;
                s.push_back('a' + j);
                dfs(i + 1, n, s, A);
                s.pop_back();
                A[j]++;
            }
        }
    }
}

void solve(string s) {
    vector<int> alpha(26, 0);
    for (int i = 0; i < s.size(); i++)
        alpha[s[i] - 'a']++;
    dfs(0, s.size(), "", alpha);
}

int main() {
    int n; cin >> n;
    while (n-- > 0) {
        string s; cin >> s;
        solve(s);
    }
}