#include <bits/stdc++.h>
using namespace std;

string w[3];
set<char> letters;
vector<char> chars;
map<char, int> to;
bool used[10];

int convert(string s) {
    int n = 0;
    for (int i = 0; i < s.size(); i++)
        n = n * 10 + to[s[i]];
    return n;
}

void dfs(int i) {
    if (i == letters.size()) {
        int a = convert(w[0]);
        int b = convert(w[1]);
        int c = convert(w[2]);
        if (a + b == c) {
            cout << "Yes";
            exit(0);
        }
    }
    else {
        for (int j = 0; j < 10; j++) {
            if (used[j]) continue;
            to[chars[i]] = j;
            used[j] = true;
            dfs(i + 1);
            used[j] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> w[0] >> w[1] >> w[2];
    for (char c: w[0] + w[1] + w[2])
        letters.insert(c);
    for (char c: letters)
        chars.push_back(c);
    if (letters.size() <= 10)
        dfs(0);
    cout << "No";
}
