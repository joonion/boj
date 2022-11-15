#include <bits/stdc++.h>
using namespace std;

map<char, int> T = {
    {'M',1000}, {'D',500}, {'C',100}, {'L',50}, {'X',10}, {'V',5}, {'I',1}
};

int largest(vector<char> &roman) {
    int maxn = 0;
    for (int i = 0; i < roman.size(); i++) {
        maxn = max(maxn, maxn + T)

    }
    return maxn;    
}

int solve(string s) {
    vector<char> v;
    for (int i = 0; i < s.size(); i++) {
        if (T.find(toupper(s[i])) != T.end())
            v.push_back(toupper(s[i]));
    }
    return v.size() ? largest(v) : 0;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    string s;
    getline(cin, s);
    int n = stoi(s);
    while (n--) {
        getline(cin, s);
        cout << solve(s) << "\n";
    }
}