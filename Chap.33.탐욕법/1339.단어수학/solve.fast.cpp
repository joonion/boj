#include <bits/stdc++.h>
using namespace std;

int T[26];

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        string s; cin >> s;
        for (int j = 0, k = 1; j < s.size(); j++, k *= 10)
            T[s[s.size()-1-j] - 'A'] += k;
    }
    sort(T, T+26);
    int S = 0;
    for (int i = 25; T[i]; i--)
        S += T[i] * (i - 16);
    cout << S;
}